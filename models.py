from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    issue_title: str
    issue_description: str
    files_changed: List[str]
    code_diff: str


class Action(BaseModel):
    severity: str
    component: str 
    fix_suggestion: str


class Reward(BaseModel):
    score: float