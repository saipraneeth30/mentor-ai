from app.services.timetable_service import TimetableService
from tests.mocks import MockTimetableRepository


class MockSubject:

    def __init__(self, subject_name, difficulty):
        self.subject_name = subject_name
        self.difficulty = difficulty


class MockProfile:

    def __init__(self):
        self.goal = "Placement"
        self.weak_subjects = "DBMS,AI"
        self.preferred_study_time = "Morning"


def test_generate_weekly_schedule():

    repository = MockTimetableRepository()

    service = TimetableService(repository)

    subjects = [
        MockSubject("Python", "Easy"),
        MockSubject("DBMS", "Hard"),
        MockSubject("AI", "Medium")
    ]

    profile = MockProfile()

    schedule = service.generate_weekly_schedule(
        subjects,
        profile,
        6
    )

    assert schedule is not None
    assert isinstance(schedule, dict)
    assert "Monday" in schedule