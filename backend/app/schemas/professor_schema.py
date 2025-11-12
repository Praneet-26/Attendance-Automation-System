from pydantic import BaseModel
from typing import List, Optional

# Input when creating/registering a professor
class ProfessorCreate(BaseModel):
    first_name: str
    last_name: str
    email: str

# Response schema for returning professor info
class ProfessorResponse(BaseModel):
    professor_id: str
    first_name: str
    last_name: str
    email: str
    courses: Optional[List[str]] = []
