import gradio as gr
import sys
import os
import time

sys.path.append(os.path.dirname(__file__))

from env import BugTriageEnv
from baseline import simple_agent

env = BugTriageEnv()

def run():
    time.sleep(1)  # makes it feel like AI is thinking

    obs = env.reset()
    action = simple_agent(obs)
    _, reward, _, _ = env.step(action)

    return (
        f"📝 **Title:** {obs['issue_title']}\n\n"
        f"📄 **Description:** {obs['issue_description']}\n\n"
        f"📂 **Files:** {', '.join(obs['files_changed'])}\n\n"
        f"💻 **Code:**\n{obs['code_diff']}",

        f"⚠ **Severity:** {action['severity']}\n"
        f"🧩 **Component:** {action['component']}\n"
        f"🛠 **Fix Suggestion:** {action['fix_suggestion']}",

        f"🏆 **Reward Score:** {reward:.2f}\n\n📈 Performance: {'Excellent' if reward > 0.8 else 'Good' if reward > 0.5 else 'Needs Improvement'}"
    )

with gr.Blocks(theme=gr.themes.Base(primary_hue="violet")) as demo:

    # 🔥 Hero Section
    gr.Markdown("""
    # 🚀 Bug Triage AI  
    ### ⚡ Smart debugging powered by AI  
    Identify bugs → classify severity → suggest fixes instantly  
    ---
    """)

    # 🔘 Button
    with gr.Row():
        btn = gr.Button("🚀 Analyze Bug Instantly", variant="primary", scale=2)

    # 📦 Output Sections
    with gr.Row():
        obs_box = gr.Textbox(label="📥 Bug Details", lines=10)
        action_box = gr.Textbox(label="🤖 AI Analysis", lines=10)
        reward_box = gr.Textbox(label="📊 Confidence Score", lines=2)

    # ⚙️ Action
    btn.click(run, outputs=[obs_box, action_box, reward_box], show_progress=True)

    # 💎 Footer
    gr.Markdown("---")
    gr.Markdown("💡 Built with ❤️ for intelligent bug triage systems")

demo.launch()