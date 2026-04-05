DATASET = [

# ========================
# 🟢 EASY TASKS (Severity)
# ========================

{
    "difficulty": "easy",
    "issue_title": "Typo in homepage title",
    "issue_description": "Homepage shows 'Welcom' instead of 'Welcome'",
    "files_changed": ["index.html"],
    "code_diff": "<h1>Welcom</h1>",
    "ground_truth": {
        "severity": "LOW",
        "component": "UI",
        "fix": "Correct spelling to 'Welcome'"
    }
},

{
    "difficulty": "easy",
    "issue_title": "Button color mismatch",
    "issue_description": "Submit button color is different from design",
    "files_changed": ["styles.css"],
    "code_diff": ".btn { color: red; }",
    "ground_truth": {
        "severity": "LOW",
        "component": "UI",
        "fix": "Update color to match design"
    }
},

{
    "difficulty": "easy",
    "issue_title": "Console warning on load",
    "issue_description": "Minor console warning appears on page load",
    "files_changed": ["app.js"],
    "code_diff": "console.warn('deprecated')",
    "ground_truth": {
        "severity": "LOW",
        "component": "UI",
        "fix": "Remove deprecated warning"
    }
},

{
    "difficulty": "easy",
    "issue_title": "Image not aligned",
    "issue_description": "Profile image is slightly misaligned",
    "files_changed": ["profile.css"],
    "code_diff": "margin-left: 3px;",
    "ground_truth": {
        "severity": "LOW",
        "component": "UI",
        "fix": "Fix margin alignment"
    }
},

{
    "difficulty": "easy",
    "issue_title": "Footer text overflow",
    "issue_description": "Footer text overflows on small screens",
    "files_changed": ["footer.css"],
    "code_diff": "width: 500px;",
    "ground_truth": {
        "severity": "LOW",
        "component": "UI",
        "fix": "Use responsive width"
    }
},

# ========================
# 🟡 MEDIUM TASKS (Component)
# ========================

{
    "difficulty": "medium",
    "issue_title": "Login API failing",
    "issue_description": "Users cannot login due to API error",
    "files_changed": ["auth.js", "api/login.js"],
    "code_diff": "fetch('/login') → 500 error",
    "ground_truth": {
        "severity": "HIGH",
        "component": "BACKEND",
        "fix": "Fix API endpoint or server error"
    }
},

{
    "difficulty": "medium",
    "issue_title": "Data not saving",
    "issue_description": "User data not stored after form submission",
    "files_changed": ["db.js"],
    "code_diff": "db.save() not called",
    "ground_truth": {
        "severity": "HIGH",
        "component": "DATABASE",
        "fix": "Ensure save function is called"
    }
},

{
    "difficulty": "medium",
    "issue_title": "Slow dashboard load",
    "issue_description": "Dashboard takes too long to load",
    "files_changed": ["dashboard.js"],
    "code_diff": "multiple API calls",
    "ground_truth": {
        "severity": "MEDIUM",
        "component": "BACKEND",
        "fix": "Optimize API calls"
    }
},

{
    "difficulty": "medium",
    "issue_title": "Broken navigation link",
    "issue_description": "Navbar link redirects to wrong page",
    "files_changed": ["navbar.jsx"],
    "code_diff": "<a href='/hom'>Home</a>",
    "ground_truth": {
        "severity": "MEDIUM",
        "component": "UI",
        "fix": "Fix route path"
    }
},

{
    "difficulty": "medium",
    "issue_title": "Session timeout issue",
    "issue_description": "User session expires too quickly",
    "files_changed": ["session.js"],
    "code_diff": "timeout = 5 seconds",
    "ground_truth": {
        "severity": "MEDIUM",
        "component": "BACKEND",
        "fix": "Increase session timeout"
    }
},

# ========================
# 🔴 HARD TASKS (Fix Suggestion)
# ========================

{
    "difficulty": "hard",
    "issue_title": "Login always fails",
    "issue_description": "Password check not working",
    "files_changed": ["auth.js"],
    "code_diff": "if(password = input_password)",
    "ground_truth": {
        "severity": "HIGH",
        "component": "BACKEND",
        "fix": "Use == instead of ="
    }
},

{
    "difficulty": "hard",
    "issue_title": "App crashes on null input",
    "issue_description": "App crashes when input is empty",
    "files_changed": ["form.js"],
    "code_diff": "user.name.length",
    "ground_truth": {
        "severity": "HIGH",
        "component": "BACKEND",
        "fix": "Add null check before accessing length"
    }
},

{
    "difficulty": "hard",
    "issue_title": "Infinite loop in processing",
    "issue_description": "System hangs due to loop",
    "files_changed": ["process.py"],
    "code_diff": "while(true):",
    "ground_truth": {
        "severity": "HIGH",
        "component": "BACKEND",
        "fix": "Add proper loop exit condition"
    }
},

{
    "difficulty": "hard",
    "issue_title": "SQL injection vulnerability",
    "issue_description": "User input directly used in query",
    "files_changed": ["db.sql"],
    "code_diff": "SELECT * FROM users WHERE name = '" + "user_input" + "'",
    "ground_truth": {
        "severity": "HIGH",
        "component": "DATABASE",
        "fix": "Use parameterized queries"
    }
},

{
    "difficulty": "hard",
    "issue_title": "Memory leak issue",
    "issue_description": "App memory increases over time",
    "files_changed": ["cache.js"],
    "code_diff": "objects stored but never cleared",
    "ground_truth": {
        "severity": "HIGH",
        "component": "BACKEND",
        "fix": "Clear unused objects or use proper memory management"
    }
},

]