from app.services.student_service import StudentService
from tests.mocks import MockStudentRepository


def test_get_student():

    repository = MockStudentRepository()

    service = StudentService(repository)

    student = service.get_student(1)

    assert student["id"] == 1
    assert student["name"] == "Anupama"