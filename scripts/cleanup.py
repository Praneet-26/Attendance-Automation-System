professors_db = {}
students_db = {}

def cleanup():
    professors_db.clear()
    students_db.clear()
    print("All test data cleared")

if __name__ == "__main__":
    cleanup()