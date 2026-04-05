def simple_agent(observation):
    text = (observation["issue_title"] + " " + observation["issue_description"]).lower()
    files = str(observation["files_changed"]).lower()

    # Severity
    if "timeout" in text:
        severity = "MEDIUM"
    elif "crash" in text or "fail" in text:
        severity = "HIGH"
    elif "slow" in text:
        severity = "MEDIUM"
    else:
        severity = "LOW"
    

    # Component
    if "css" in files or "html" in files:
        component = "UI"
    elif "db" in files or "sql" in files:
        component = "DATABASE"
    elif "api" in files:
        component = "API"
    else:
        component = "BACKEND"


    # Fix suggestion (IMPROVED)
    if "timeout" in text:
        fix = "Increase timeout value"
    elif "color" in text or "css" in files:
        fix = "Fix CSS styling or update color"
    elif "login" in text or "auth" in files:
        fix = "Check authentication logic and password validation"
    elif "slow" in text:
        fix = "Optimize API calls or improve performance"
    elif "error" in text or "fail" in text:
        fix = "Debug the failing logic and correct the condition"
    else:
        fix = "Fix the issue in the code"

    return {
        "severity": severity,
        "component": component,
        "fix_suggestion": fix,
        "confidence": 0.8
    }