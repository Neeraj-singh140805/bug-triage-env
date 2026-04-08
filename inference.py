import os
from flask import Flask, request, jsonify
from env import BugTriageEnv
from baseline import simple_agent

app = Flask(__name__)

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
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


@app.route("/reset", methods=["POST"])
def reset():
    """Reset the environment — required by OpenEnv checker."""
    env.reset()
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    """Run inference on a bug triage request."""
    data = request.get_json()

    result = run_inference(
        issue_title=data.get("issue_title", ""),
        issue_desc=data.get("issue_description", ""),
        files=data.get("files_changed", ""),
        code=data.get("code_diff", ""),
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)