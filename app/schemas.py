from pydantic import BaseModel
from typing import List, Optional

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    age: int
    weight: int
    height: int
    activity_ids: Optional[List[str]]
    health_metric_ids: Optional[List[str]]
