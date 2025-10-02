from pydantic import BaseModel
from typing import List, Optional

# Input schema (used when creating/registering student)
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str

# Output schema (general student info)
class StudentResponse(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: str
    photo_url: Optional[str] = None
    enrolled_courses: Optional[List[str]] = []
