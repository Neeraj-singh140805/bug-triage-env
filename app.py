import gradio as gr
import sys
import os
import time

sys.path.append(os.path.dirname(__file__))

from env import BugTriageEnv
from baseline import simple_agent

env = BugTriageEnv()


def run(issue_title, issue_desc, files, code):
    time.sleep(1)

    obs = {
        "issue_title": issue_title,
        "issue_description": issue_desc,
        "files_changed": files.split(","),
        "code_diff": code,
    }

    env.current_task = {
        **obs,
        "ground_truth": {"severity": "LOW", "component": "UI", "fix": ""}
    }

    action = simple_agent(obs)
    _, reward, _, _ = env.step(action)

    return (
        f"📝 **Title:** {obs['issue_title']}\n\n"
        f"📄 **Description:** {obs['issue_description']}\n\n"
        f"📂 **Files:** {files}\n\n"
        f"💻 **Code:**\n{obs['code_diff']}",

        f"⚠ **Severity:** {action['severity']}\n"
        f"🧩 **Component:** {action['component']}\n"
        f"🛠 **Fix Suggestion:** {action['fix_suggestion']}",

        f"🏆 **Reward Score:** {reward:.2f}\n\n"
        f"📈 Performance: {'Excellent' if reward > 0.8 else 'Good' if reward > 0.5 else 'Needs Improvement'}"
    )


with gr.Blocks(theme=gr.themes.Base(primary_hue="violet")) as demo:

    # 🔥 HERO
    gr.Markdown("""
    # 🚀 Bug Triage AI  
    ### ⚡ Smart debugging powered by AI  
    Identify bugs → classify severity → suggest fixes instantly  
    ---
    """)

    # 🧾 INPUT SECTION (NEW 🔥)
    gr.Markdown("### 🧾 Enter Bug Details")

    with gr.Row():
        title_input = gr.Textbox(
            label="Bug Title",
            value="Broken navigation link"
        )

    with gr.Row():
        desc_input = gr.Textbox(
            label="Bug Description",
            value="Navbar link redirects to wrong page",
            lines=2
        )

    with gr.Row():
        files_input = gr.Textbox(
            label="Files Changed (comma separated)",
            value="navbar.jsx"
        )

    with gr.Row():
        code_input = gr.Textbox(
            label="Code Diff",
            value='<a href="/hom">Home</a>',
            lines=3
        )

    # 🔘 BUTTON (better visibility)
    with gr.Row():
        btn = gr.Button("🚀 Analyze Bug", variant="primary")

    # 📦 OUTPUT SECTION
    with gr.Row():
        obs_box = gr.Markdown()
        action_box = gr.Markdown()
        reward_box = gr.Markdown()

    # ⚙️ ACTION
    btn.click(
        run,
        inputs=[title_input, desc_input, files_input, code_input],
        outputs=[obs_box, action_box, reward_box],
        show_progress=True
    )

    # 💎 FOOTER
    gr.Markdown("---")
    gr.Markdown("💡 Built with ❤️ for intelligent bug triage systems")


demo.launch()