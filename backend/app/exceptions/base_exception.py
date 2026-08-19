class BusinessException(Exception):
    """
    Base class for all business exceptions.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)