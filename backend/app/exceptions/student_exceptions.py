from app.exceptions.base_exception import BusinessException


class StudentNotFoundException(BusinessException):

    def __init__(self):
        super().__init__("Student not found")


class StudentAlreadyExistsException(BusinessException):

    def __init__(self):
        super().__init__("Student already exists")