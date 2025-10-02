from ..backend.app.models.professor import Professor
from ..backend.app.models.student import Student

professors_db = {}
students_db = {}

def seed_data():
    prof1 = Professor(first_name="Kal", last_name="Rabb", email="kal.rabb@example.com")
    prof2 = Professor(first_name="Yu", last_name="Zhu", email="Yu.Zhu@example.com")
    professors_db[prof1.professor_id] = prof1.to_dict()
    professors_db[prof2.professor_id] = prof2.to_dict()

    stu1 = Student(first_name="Praneet", last_name="Naik", email="pnaik@example.com")
    stu2 = Student(first_name="Shreya", last_name="Pandey", email="spandey@example.com")
    students_db[stu1.student_id] = stu1.to_dict()
    students_db[stu2.student_id] = stu2.to_dict()

    print("Seed data loaded")

if __name__ == "__main__":
    seed_data()