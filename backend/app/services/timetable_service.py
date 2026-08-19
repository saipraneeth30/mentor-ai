from app.repositories.interfaces.timetable_repository import TimetableRepository
from app.agents.timetable_agent import TimetableAgent
from app.validators.timetable_validator import TimetableValidator
from app.utils.logger import get_logger
from app.exceptions.timetable_exceptions import TimetableNotFoundException

logger = get_logger(__name__)


class TimetableService:
    """
    Business Service for Timetable operations.

    Responsibilities:
    - Validate timetable requests
    - Generate study schedules
    - Delegate persistence to the Repository
    """

    def __init__(
        self,
        timetable_repository: TimetableRepository
    ):
        self.timetable_repository = timetable_repository
        self.agent = TimetableAgent()

    def generate_weekly_schedule(
        self,
        subjects,
        profile,
        study_hours
    ):

        logger.info("Generating weekly timetable")

        if not subjects:
            raise TimetableNotFoundException()

        for subject in subjects:
            TimetableValidator.validate_difficulty(
                subject.difficulty
            )

        schedule = self.agent.generate_weekly_schedule(
            subjects,
            profile,
            study_hours
        )

        return schedule

    def save_schedule(
        self,
        student_id,
        schedule
    ):

        logger.info(
            f"Saving timetable for student {student_id}"
        )

        return self.timetable_repository.save_timetable(
            student_id,
            schedule
        )

    def get_schedule(
        self,
        student_id
    ):

        logger.info(
            f"Fetching timetable for student {student_id}"
        )

        return self.timetable_repository.get_timetable(
            student_id
        )

    def complete_session(
        self,
        timetable_id
    ):

        logger.info(
            f"Completing timetable session {timetable_id}"
        )

        return self.timetable_repository.mark_completed(
            timetable_id
        )