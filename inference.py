import os
from env import BugTriageEnv
from baseline import simple_agent

# Env variables
API_BASE_URL = os.getenv("API_BASE_URL", "dummy")
MODEL_NAME = os.getenv("MODEL_NAME", "bug-triage")
HF_TOKEN = os.getenv("HF_TOKEN")

env = BugTriageEnv()

def run_inference(issue_title, issue_desc, files, code):
    print("START")

    obs = {
        "issue_title": issue_title,
        "issue_description": issue_desc,
        "files_changed": [f.strip() for f in files.split(",")],
        "code_diff": code,
    }

    print("STEP: Running agent")

    action = simple_agent(obs)

    print("STEP: Preparing output")

    result = {
        "severity": action["severity"],
        "component": action["component"],
        "fix": action["fix_suggestion"]
    }

    print("END")

    return result