from app.services.dashboard_service import DashboardService


def test_dashboard_summary():

    service = DashboardService()

    summary = service.get_dashboard_summary(
        student_name="Anupama",
        attendance_percentage=90,
        progress_percentage=80,
        recommendation_count=3
    )

    assert summary["student"] == "Anupama"
    assert summary["attendance_percentage"] == 90
    assert summary["progress_percentage"] == 80
    assert summary["recommendations"] == 3
    assert summary["productivity_score"] == 85