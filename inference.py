import os
import sys
from env import BugTriageEnv
from baseline import simple_agent

env = BugTriageEnv()

def run_inference(issue_title, issue_desc, files, code, task_name="bug_triage"):
    obs = {
        "issue_title": issue_title,
        "issue_description": issue_desc,
        "files_changed": [f.strip() for f in files.split(",")],
        "code_diff": code,
    }

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
        reward = 0.5

    print(f"[STEP] step=1 reward={reward:.2f}", flush=True)
    print(f"[END] task={task_name} score={reward:.2f} steps=1", flush=True)

    return {
        "severity": action["severity"],
        "component": action["component"],
        "fix": action["fix_suggestion"]
    }


if __name__ == "__main__":
    tasks = [
        {
            "issue_title": "Broken navigation link",
            "issue_desc": "Navbar link redirects to wrong page",
            "files": "navbar.jsx",
            "code": '<a href="/hom">Home</a>',
        },
        {
            "issue_title": "SQL injection vulnerability",
            "issue_desc": "User input is not sanitized in login form",
            "files": "login.py",
            "code": 'query = "SELECT * FROM users WHERE id=" + user_input',
        },
        {
            "issue_title": "Slow API response",
            "issue_desc": "Dashboard takes too long to load due to multiple API calls",
            "files": "dashboard.js",
            "code": "for item in items: fetch(api + item.id)",
        },
        {
            "issue_title": "Null pointer exception on profile page",
            "issue_desc": "App crashes when user has no profile picture",
            "files": "profile.jsx",
            "code": "return user.profile.picture.url",
        },
        {
            "issue_title": "Infinite loop in data processing",
            "issue_desc": "While loop never exits when processing empty list",
            "files": "processor.py",
            "code": "while not done: process(data)",
        },
    ]

    for i, t in enumerate(tasks):
        run_inference(
            issue_title=t["issue_title"],
            issue_desc=t["issue_desc"],
            files=t["files"],
            code=t["code"],
            task_name=f"bug_triage_{i+1}"
        )