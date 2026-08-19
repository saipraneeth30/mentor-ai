from app.services.attendance_service import AttendanceService
from tests.mocks import MockAttendanceRepository


def test_get_attendance_percentage():

    repository = MockAttendanceRepository()

    service = AttendanceService(repository)

    percentage = service.get_attendance_percentage(1)

    assert percentage == 92