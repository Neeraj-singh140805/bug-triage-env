def simple_agent(observation):
    text = (observation["issue_title"] + " " + observation["issue_description"]).lower()
    files = [f.lower() for f in observation["files_changed"]]
    files_text = " ".join(files)
    diff = observation["code_diff"].lower()

    # ── Severity ──────────────────────────────────────────────
    if any(k in text for k in ["crash", "fail", "injection", "null", "infinite", "memory", "leak", "always", "vulnerability"]):
        severity = "HIGH"
    elif any(k in text for k in ["timeout", "slow", "session", "broken", "mismatch"]):
        severity = "MEDIUM"
    else:
        severity = "LOW"

    # ── Component ─────────────────────────────────────────────
    if any(k in files_text for k in ["css", "html", "jsx", "navbar", "profile", "footer", "index"]):
        component = "UI"
    elif any(k in files_text for k in ["db", "sql", "database"]):
        component = "DATABASE"
    elif any(k in files_text for k in ["api", "login", "auth", "session"]):
        component = "BACKEND"
    else:
        component = "BACKEND"

    # ── Fix Suggestion ────────────────────────────────────────
    if "injection" in text or "sql" in files_text:
        fix = "Use parameterized queries to prevent SQL injection"
    elif "null" in text or "none" in diff:
        fix = "Add null check before accessing length or property"
    elif "infinite" in text or "while" in diff:
        fix = "Add proper loop exit condition"
    elif "memory" in text or "leak" in text:
        fix = "Clear unused objects or use proper memory management"
    elif "=" in diff and "==" not in diff and any(k in files_text for k in [".js", ".py", ".ts"]):
        fix = "Use == instead of = for comparison"
    elif "timeout" in text or "session" in text:
        fix = "Increase timeout or session duration"
    elif "color" in text or "css" in files_text:
        fix = "Update color to match design specification"
    elif "slow" in text or "performance" in text:
        fix = "Optimize API calls and reduce redundant requests"
    elif "login" in text or "auth" in files_text:
        fix = "Check authentication logic and password validation"
    elif "typo" in text or "spelling" in text:
        fix = "Correct the spelling error in the text"
    elif "align" in text or "margin" in diff:
        fix = "Fix margin or padding for correct alignment"
    elif "overflow" in text:
        fix = "Use responsive width instead of fixed width"
    elif "link" in text or "href" in diff:
        fix = "Fix the route path in the navigation link"
    else:
        fix = "Review the code and fix the identified issue"

    return {
        "severity": severity,
        "component": component,
        "fix_suggestion": fix
    }
if __name__ == "__main__":
    from env import BugTriageEnv

    env = BugTriageEnv()

    total_reward = 0
    n = len(env.dataset)

    print("Running evaluation on full dataset (15 tasks)...\n")

    for i, task in enumerate(env.dataset):
        env.current_task = task

        obs = {
            "issue_title": task["issue_title"],
            "issue_description": task["issue_description"],
            "files_changed": task["files_changed"],
            "code_diff": task["code_diff"],
        }

        action = simple_agent(obs)
        _, reward, _, info = env.step(action)

        print(f"Sample {i+1}: Reward = {reward:.2f}")
        total_reward += reward
    avg_reward = total_reward / n

    print("\n====================")
    print(f"Average Reward: {avg_reward:.2f}")
    print("====================")