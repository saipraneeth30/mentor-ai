from app.exceptions.base_exception import BusinessException


class AttendanceNotFoundException(BusinessException):

    def __init__(self):
        super().__init__("Attendance record not found")