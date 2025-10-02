from fastapi import APIRouter, Form, UploadFile
from backend.app.models.professor import Professor
from backend.app.schemas.professor_schema import ProfessorResponse

router = APIRouter()

# Temporary in-memory "database"
professors_db = {}



# s3 = boto3.client("s3", region_name="us-east-1") 
# BUCKET_NAME = "attendance-class-photos" 

@router.post("/register", response_model=ProfessorResponse)
async def register_professor(first_name: str = Form(...), last_name: str = Form(...), email: str = Form(...)):
    """Register a new professor"""
    professor = Professor(first_name=first_name, last_name=last_name, email=email)
    professors_db[professor.professor_id] = professor.to_dict()
    return professor.to_dict()

@router.get("/{professor_id}", response_model=ProfessorResponse)
async def get_professor(professor_id: str):
    """Fetch a professor by ID"""
    return professors_db.get(professor_id)


@router.post("/{professor_id}/capture_class_photo")
async def capture_class_photo(professor_id: str, course_id: str = Form(...), photo: UploadFile = None):
    """Professor captures a class photo (later triggers S3 + Lambda)."""
    professor = professors_db.get(professor_id)
    if not professor:
        return {"error": "Professor not found"}

    return {
        "message": f"Photo for course {course_id} captured by Professor {professor_id}",
        "photo": photo.filename if photo else None
    }

@router.get("/{professor_id}/view_attendance/{course_id}")
async def view_attendance(professor_id: str, course_id: str):
    """Professor views attendance (dummy for now)."""
    professor = professors_db.get(professor_id)
    if not professor:
        return {"error": "Professor not found"}
    return {"course_id": course_id, "attendance": ["student1", "student2"]}


# @router.post("/{professor_id}/capture_class_photo")
# async def capture_class_photo(professor_id: str, course_id: str = Form(...), photo: UploadFile = File(...)):
#     professor = professors_db.get(professor_id)
#     if not professor:
#         return {"error": "Professor not found"}

#     # Generate unique S3 key
#     file_extension = photo.filename.split(".")[-1]
#     s3_key = f"class_photos/{course_id}/{professor_id}/{uuid.uuid4()}.{file_extension}"

#     # Upload file to S3
#     s3.upload_fileobj(photo.file, BUCKET_NAME, s3_key)

#     return {
#         "message": f"Photo uploaded successfully. Lambda will be triggered by S3.",
#         "s3_key": s3_key,
#         "bucket": BUCKET_NAME
#     }
