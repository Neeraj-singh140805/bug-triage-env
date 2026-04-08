import gradio as gr
import sys
import os
import time
import html

sys.path.append(os.path.dirname(__file__))

from env import BugTriageEnv
from baseline import simple_agent

env = BugTriageEnv()

# 🎨 Custom CSS
custom_css = """
body {
    background: linear-gradient(135deg, #0f0f1a, #1a1a2e);
}
.gradio-container {
    max-width: 1100px;
    margin: auto;
}
button {
    border-radius: 12px !important;
    font-weight: bold;
    box-shadow: 0px 0px 20px rgba(124, 58, 237, 0.6);
}
button:hover {
    transform: scale(1.03);
    transition: 0.2s;
}
textarea, input {
    border-radius: 10px !important;
}
"""


def run(issue_title, issue_desc, files, code,
        exp_severity, exp_component, exp_fix):

    time.sleep(0.6)

    obs = {
        "issue_title": issue_title,
        "issue_description": issue_desc,
        "files_changed": [f.strip() for f in files.split(",")],
        "code_diff": code,
    }

    action = simple_agent(obs)
    env.current_task = {
        **obs,
        "ground_truth": {
            "severity": exp_severity,
            "component": exp_component,
            "fix": exp_fix if exp_fix else "fix the issue"
        }
    }

    try:
        _, reward, _, _ = env.step(action)
    except Exception as e:
        return "❌ Error", str(e), "Fix env issue"
    reason = []

    if action["severity"] == "HIGH":
        reason.append("Critical keywords detected (crash/security issue)")
    elif action["severity"] == "MEDIUM":
        reason.append("Moderate issue like performance or broken feature")
    else:
        reason.append("Minor issue with low impact")

    if action["component"] == "UI":
        reason.append("File indicates frontend/UI issue")
    elif action["component"] == "DATABASE":
        reason.append("Database-related file detected")
    else:
        reason.append("Backend logic involved")

    reason.append("Rule-based agent matched patterns from bug description and file context")
    reason_text = "\n".join([f"- {r}" for r in reason])

    # 🎯 Score styling
    color = "🟢" if reward > 0.8 else "🟡" if reward > 0.5 else "🔴"

    confidence = (
        "High Confidence" if reward > 0.8
        else "Medium Confidence" if reward > 0.5
        else "Low Confidence"
    )

    safe_code = html.escape(obs["code_diff"])

    return (
        f"""### 📥 Bug Details
📝 **Title:** {obs['issue_title']}  
📄 **Description:** {obs['issue_description']}  
📂 **Files:** {files}  
💻 **Code**
<pre style="background:#0d1117;padding:14px;border-radius:10px;
border:1px solid #30363d;overflow-x:auto;">
<code>{safe_code}</code>
</pre>
""",

        f"""### 🤖 AI Decision Engine
⚠ **Severity:** `{action['severity']}`  
🧩 **Component:** `{action['component']}`  
🛠 **Fix Suggestion:**  
{action['fix_suggestion']}
📌 **Why this decision?**
{reason_text}
""",

        f"""### 📊 Score
🏆 **Reward:** {color} `{reward:.2f}`  
📌 **Breakdown:**
- Severity Match: {'✅' if action['severity'] == exp_severity else '❌'}
- Component Match: {'✅' if action['component'] == exp_component else '❌'}
📈 **Performance:**  
{'🔥 Excellent' if reward > 0.8 else '⚡ Good' if reward > 0.5 else '❌ Needs Review'}
🎯 **Confidence:** {confidence}
"""
    )


# ✅ UI
with gr.Blocks(theme=gr.themes.Base(primary_hue="violet"), css=custom_css) as demo:

    gr.Markdown("""
# 🚀 Bug Triage AI  
### ⚡ AI-powered debugging assistant for developers  
💡 Paste a bug → get instant triage + fix suggestions  
---
""")

    gr.Markdown("### 🧾 Enter Bug Details")

    title_input = gr.Textbox(label="Bug Title", value="Broken navigation link")
    desc_input = gr.Textbox(label="Bug Description", value="Navbar link redirects to wrong page", lines=2)
    files_input = gr.Textbox(label="Files Changed (comma separated)", value="navbar.jsx")
    code_input = gr.Textbox(label="Code Diff", value='<a href="/hom">Home</a>', lines=3)

    gr.Markdown("### 🎯 Expected Answer (for scoring)")

    with gr.Row():
        expected_severity = gr.Dropdown(
            choices=["LOW", "MEDIUM", "HIGH"],
            label="Expected Severity",
            value="LOW"
        )
        expected_component = gr.Dropdown(
            choices=["UI", "BACKEND", "DATABASE", "API"],
            label="Expected Component",
            value="UI"
        )

    expected_fix = gr.Textbox(
        label="Expected Fix (optional)",
        value="",
        placeholder="e.g. Use parameterized queries"
    )

    btn = gr.Button("🚀 Analyze Bug", variant="primary")

    gr.Examples(
        examples=[
            ["App crashes on login", "App crashes when user logs in", "login.js", "if(user = null)"],
            ["Slow API response", "API takes 10 seconds", "api.py", "time.sleep(10)"]
        ],
        inputs=[title_input, desc_input, files_input, code_input]
    )

    with gr.Row():
        obs_box = gr.Markdown()
        action_box = gr.Markdown()
        reward_box = gr.Markdown()

    btn.click(
        run,
        inputs=[
            title_input, desc_input, files_input, code_input,
            expected_severity, expected_component, expected_fix
        ],
        outputs=[obs_box, action_box, reward_box],
        show_progress="full"
    )

    gr.Markdown("⚠️ Scoring is based on expected answers provided by the user.")
    gr.Markdown("---")
    gr.Markdown("💡 Built with ❤️ for intelligent bug triage systems")


demo.launch(server_name="0.0.0.0", server_port=7860)