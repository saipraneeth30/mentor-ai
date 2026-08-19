from app.exceptions.base_exception import BusinessException


class ProfileNotFoundException(BusinessException):

    def __init__(self):
        super().__init__("Student profile not found")


class ProfileAlreadyExistsException(BusinessException):

    def __init__(self):
        super().__init__("Student profile already exists")