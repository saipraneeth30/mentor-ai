from abc import ABC, abstractmethod


class ProfileRepository(ABC):

    @abstractmethod
    def create_profile(self, profile):
        pass

    @abstractmethod
    def get_profile(self, student_id: int):
        pass

    @abstractmethod
    def update_profile(self, student_id: int, profile):
        pass