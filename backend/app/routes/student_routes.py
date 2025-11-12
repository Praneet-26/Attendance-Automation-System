from fastapi import APIRouter, Form, UploadFile, File
import boto3, uuid

from backend.app.models.student import Student
from backend.app.schemas.student_schema import StudentResponse

router = APIRouter()

# Temporary in-memory store (replace later with DynamoDB)
students_db = {}

# # S3 client (for storing profile photos)
# s3 = boto3.client("s3", region_name="us-east-1")
# BUCKET_NAME = "attendance-student-photos"   # replace with your bucket

# Register student (with optional photo upload)
# @router.post("/register", response_model=StudentResponse)
# async def register_student(
#     first_name: str = Form(...),
#     last_name: str = Form(...),
#     email: str = Form(...),
#     photo: UploadFile = File(None)
# ):
#     student = Student(first_name=first_name, last_name=last_name, email=email)

#     # Upload photo to S3 if provided
#     if photo:
#         file_extension = photo.filename.split(".")[-1]
#         s3_key = f"students/{student.student_id}/{uuid.uuid4()}.{file_extension}"
#         s3.upload_fileobj(photo.file, BUCKET_NAME, s3_key)
#         student.photo_url = f"s3://{BUCKET_NAME}/{s3_key}"

#     students_db[student.student_id] = student.to_dict()
#     return student.to_dict()

# Get student details
@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: str):
    student = students_db.get(student_id)
    if not student:
        return {"error": "Student not found"}
    return student

# View courses the student is registered in
@router.get("/{student_id}/courses", response_model=list[str])
async def get_registered_courses(student_id: str):
    student = students_db.get(student_id)
    if not student:
        return {"error": "Student not found"}
    return student["enrolled_courses"]

# Check attendance for a student in a course
@router.get("/{student_id}/attendance/{course_id}")
async def check_attendance(student_id: str, course_id: str):
    student = students_db.get(student_id)
    if not student:
        return {"error": "Student not found"}
    # later: query DynamoDB Attendance table
    return {
        "student_id": student_id,
        "course_id": course_id,
        "attendance": "75% (dummy data)"
    }
