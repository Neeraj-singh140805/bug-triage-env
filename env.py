import random
from models import Observation, Action, Reward
from dataset import DATASET
def compute_fix_score(predicted, actual):
    pred_words = set(predicted.lower().split())
    actual_words = set(actual.lower().split())

    overlap = pred_words.intersection(actual_words)

    if len(actual_words) == 0:
        return 0

    return len(overlap) / len(actual_words)
class BugTriageEnv:

    def __init__(self):
        self.dataset = DATASET
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(self.dataset)

        observation = {
            "issue_title": self.current_task["issue_title"],
            "issue_description": self.current_task["issue_description"],
            "files_changed": self.current_task["files_changed"],
            "code_diff": self.current_task["code_diff"],
        }

        return observation

    def step(self, action: Action):
        gt = self.current_task["ground_truth"]

        # Compare with ground truth (simple for now)
        severity_correct = action["severity"] == gt["severity"]
        component_correct = action["component"] == gt["component"]
        fix_score = compute_fix_score(action["fix_suggestion"], gt["fix"])

        # Temporary scoring
        score = 0
        if severity_correct:
            score += 0.4
        if component_correct:
            score += 0.3
        if fix_score:
            score += 0.3

        done = True

        return self.reset(), score, done, {"ground_truth": gt}

    def state(self):
        return self.current_task