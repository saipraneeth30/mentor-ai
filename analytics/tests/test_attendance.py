import pytest

from analytics.calculators.attendance import calculate_attendance


def test_attendance_normal():
    assert calculate_attendance(8, 10) == 80.0


def test_attendance_full():
    assert calculate_attendance(10, 10) == 100.0


def test_attendance_zero():
    assert calculate_attendance(0, 10) == 0.0


def test_attendance_greater_than_total():
    with pytest.raises(ValueError):
        calculate_attendance(11, 10)


def test_attendance_negative():
    with pytest.raises(ValueError):
        calculate_attendance(-1, 10)


def test_attendance_zero_total():
    with pytest.raises(ValueError):
        calculate_attendance(5, 0)