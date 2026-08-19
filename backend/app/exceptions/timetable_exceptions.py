from app.exceptions.base_exception import BusinessException


class TimetableNotFoundException(BusinessException):

    def __init__(self):
        super().__init__("Timetable not found")