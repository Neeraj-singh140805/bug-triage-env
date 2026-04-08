from env import BugTriageEnv
from baseline import simple_agent

env = BugTriageEnv()

total_reward = 0
n = len(env.dataset)

for i in range(n):
    obs = env.reset()
    action = simple_agent(obs)

    _, reward, _, info = env.step(action)

    print(f"Sample {i+1}: Reward = {reward:.2f}")
    total_reward += reward

avg_reward = total_reward / n

print("\n====================")
print(f"Average Reward: {avg_reward:.2f}")
print("====================")