import random
from dataset import DATASET


def compute_fix_score(predicted, actual):
    pred_words = set(predicted.lower().split())
    actual_words = set(actual.lower().split())

    if len(pred_words) == 0 or len(actual_words) == 0:
        return 0

    overlap = pred_words.intersection(actual_words)

    precision = len(overlap) / len(pred_words)
    recall = len(overlap) / len(actual_words)

    if precision + recall == 0:
        return 0

    f1 = 2 * (precision * recall) / (precision + recall)
    return f1


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

    def step(self, action):
        gt = self.current_task["ground_truth"]   # ← was missing

        severity_correct = action["severity"] == gt["severity"]     # ← was missing
        component_correct = action["component"] == gt["component"]  # ← was missing
        fix_score = compute_fix_score(action["fix_suggestion"], gt["fix"])  # ← use the function!

        score = 0   # ← must come BEFORE any score +=
        if severity_correct:
            score += 0.4
        if component_correct:
            score += 0.3
        score += fix_score * 0.3   # ← partial fix credit

        done = True
        return None, score, done, {"ground_truth": gt}

    def state(self):
        return self.current_task