from env import BugTriageEnv

env = BugTriageEnv()

obs = env.reset()
print("OBS:", obs)

action = {
    "severity": "HIGH",
    "component": "BACKEND",
    "fix_suggestion": "Use == instead of ="
}

obs, reward, done, info = env.step(action)

print("Reward:", reward)
print("Ground Truth:", info)