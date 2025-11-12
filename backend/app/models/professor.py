import uuid
from typing import List

class Professor:
    def __init__(self, professor_id: str = None, first_name: str = "", last_name: str = "", email: str = "", courses: List[str] = None):
        self.professor_id = professor_id or str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.courses = courses or []

    def to_dict(self) -> dict:
        return {
            "professor_id": self.professor_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "courses": self.courses
        }

    def capture_class_photo(self, course_id: str, photo_key: str):
        return f"Class photo for course {course_id} uploaded at {photo_key}"

    def view_attendance(self, course_id: str):
        return f"Attendance records for course {course_id}"
