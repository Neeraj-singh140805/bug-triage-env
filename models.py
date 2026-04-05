from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    issue_title: str
    issue_description: str
    files_changed: List[str]
    code_diff: str


class Action(BaseModel):
    severity: str  # LOW / MEDIUM / HIGH
    component: str  # UI / BACKEND / DATABASE / API
    fix_suggestion: str


class Reward(BaseModel):
    score: float  # between 0 and 1