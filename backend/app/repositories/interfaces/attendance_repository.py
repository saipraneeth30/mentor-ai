from abc import ABC, abstractmethod


class AttendanceRepository(ABC):

    @abstractmethod
    def mark_attendance(self, attendance):
        pass

    @abstractmethod
    def get_attendance(self, student_id: int):
        pass

    @abstractmethod
    def get_attendance_percentage(self, student_id: int):
        pass