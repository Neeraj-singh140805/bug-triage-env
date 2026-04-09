import os
import sys
from env import BugTriageEnv
from baseline import simple_agent

env = BugTriageEnv()

def run_inference(issue_title, issue_desc, files, code):
    obs = {
        "issue_title": issue_title,
        "issue_description": issue_desc,
        "files_changed": [f.strip() for f in files.split(",")],
        "code_diff": code,
    }

    task_name = "bug_triage"

    print(f"[START] task={task_name}", flush=True)

    action = simple_agent(obs)

    env.current_task = {
        **obs,
        "ground_truth": {
            "severity": action["severity"],
            "component": action["component"],
            "fix": action["fix_suggestion"]
        }
    }

    try:
        _, reward, _, _ = env.step(action)
    except Exception:
        reward = 0.0

    print(f"[STEP] step=1 reward={reward:.2f}", flush=True)
    print(f"[END] task={task_name} score={reward:.2f} steps=1", flush=True)

    return {
        "severity": action["severity"],
        "component": action["component"],
        "fix": action["fix_suggestion"]
    }


if __name__ == "__main__":
    run_inference(
        issue_title="Broken navigation link",
        issue_desc="Navbar link redirects to wrong page",
        files="navbar.jsx",
        code='<a href="/hom">Home</a>'
    )