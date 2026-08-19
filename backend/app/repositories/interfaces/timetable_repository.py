from abc import ABC, abstractmethod


class TimetableRepository(ABC):

    @abstractmethod
    def save_timetable(self, timetable):
        pass

    @abstractmethod
    def get_timetable(self, student_id: int):
        pass

    @abstractmethod
    def mark_completed(self, timetable_id: int):
        pass

    @abstractmethod
    def delete_student_timetable(self, student_id: int):
        pass