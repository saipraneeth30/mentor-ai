from abc import ABC, abstractmethod


class StudentRepository(ABC):
    """
    Contract for Student Repository.

    The Database Team will implement this interface.
    Business Services should depend only on this contract.
    """

    @abstractmethod
    def create_student(self, student):
        pass

    @abstractmethod
    def get_student_by_id(self, student_id: int):
        pass

    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def update_student(self, student_id: int, student):
        pass

    @abstractmethod
    def delete_student(self, student_id: int):
        pass