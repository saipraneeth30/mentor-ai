from backend.schemas.student import StudentRegistration


class StudentService:

    @staticmethod
    def register_student(student: StudentRegistration):

        return {
            "success": True,
            "message": "Student Registered Successfully",
            "student": student.model_dump()
        }