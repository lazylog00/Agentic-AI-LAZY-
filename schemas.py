from pydantic import BaseModel
from typing import List, Any

class Action(BaseModel):
    action: str
    a: float
    b: float

class Response(BaseModel):
    ans: str
    steps: List[str]
    intermediate_results: List[Any] = []