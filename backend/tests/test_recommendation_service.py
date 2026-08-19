from app.services.recommendation_service import RecommendationService


class MockProfile:

    def __init__(self):

        self.goal = "Placement"

        self.weak_subjects = "DBMS,AI"


def test_generate_recommendations():

    service = RecommendationService()

    profile = MockProfile()

    recommendations = service.generate_recommendations(
        profile,
        attendance_percentage=70,
        progress_percentage=40
    )

    assert len(recommendations) > 0

    assert "Improve your attendance." in recommendations

    assert "Complete more timetable tasks." in recommendations