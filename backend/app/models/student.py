import uuid
from typing import List, Optional

class Student:
    def __init__(
        self,
        student_id: str = None,
        first_name: str = "",
        last_name: str = "",
        email: str = "",
        photo_url: Optional[str] = None,
        enrolled_courses: Optional[List[str]] = None
    ):
        self.student_id = student_id or str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.photo_url = photo_url
        self.enrolled_courses = enrolled_courses or []  # pre-populated externally

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "photo_url": self.photo_url,
            "enrolled_courses": self.enrolled_courses,
        }

    def register_photo(self, photo_url: str) -> str:
        self.photo_url = photo_url
        return self.photo_url

    def view_registered_courses(self) -> List[str]:
        """Return the list of courses the student is already registered in."""
        return self.enrolled_courses

    def check_attendance(self, course_id: str):
        return f"Attendance records for {self.first_name} in {course_id} (dummy data)"
