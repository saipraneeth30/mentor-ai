class MockStudentRepository:

    def create_student(self, student):
        return student

    def get_student_by_id(self, student_id):
        return {
            "id": student_id,
            "name": "Anupama"
        }

    def get_all_students(self):
        return [
            {
                "id": 1,
                "name": "Anupama"
            }
        ]

    def update_student(self, student_id, student):
        return student

    def delete_student(self, student_id):
        return True

class MockTimetableRepository:

    def save_timetable(self, student_id, schedule):
        return {
            "student_id": student_id,
            "schedule": schedule
        }

    def get_timetable(self, student_id):
        return [
            {
                "subject": "Python",
                "duration": "2 Hours"
            }
        ]

    def mark_completed(self, timetable_id):
        return {
            "id": timetable_id,
            "completed": True
        }

    def delete_student_timetable(self, student_id):
        return True

class MockAttendanceRepository:

    def mark_attendance(self, attendance):
        return attendance

    def get_attendance(self, student_id):
        return {
            "student_id": student_id,
            "attendance": 92
        }

    def get_attendance_percentage(self, student_id):
        return 92