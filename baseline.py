from env import BugTriageEnv

def simple_agent(observation):
    text = (observation["issue_title"] + " " + observation["issue_description"]).lower()

    # Improved rules
    if "timeout" in text:
        severity = "MEDIUM"
    elif "crash" in text or "fail" in text:
        severity = "HIGH"
    elif "slow" in text:
        severity = "MEDIUM"
    else:
        severity = "LOW"
    files = str(observation["files_changed"]).lower()

    if "css" in files or "html" in files:
        component = "UI"
    elif "db" in files or "sql" in files:
        component = "DATABASE"
    elif "api" in files:
        component = "API"
    else:
        component = "BACKEND"
    fix = "Check code and fix the issue"

    return {
        "severity": severity,
        "component": component,
        "fix_suggestion": fix,
        "confidence": 0.8
    }


if __name__ == "__main__":
    env = BugTriageEnv()

    obs = env.reset()
    print("OBS:", obs)

    action = simple_agent(obs)

    obs, reward, done, info = env.step(action)

    print("ACTION:", action)
    print("REWARD:", reward)
    print("DETAILS:", info)