import pytest

from analytics.calculators.velocity import calculate_velocity


def test_velocity_normal():
    assert calculate_velocity(80, 10) == 8.0


def test_velocity_full_progress():
    assert calculate_velocity(100, 10) == 10.0


def test_velocity_zero_progress():
    assert calculate_velocity(0, 10) == 0.0


def test_velocity_decimal():
    assert calculate_velocity(75, 8) == 9.38


def test_negative_progress():
    with pytest.raises(ValueError):
        calculate_velocity(-10, 10)


def test_zero_time():
    with pytest.raises(ValueError):
        calculate_velocity(80, 0)


def test_negative_time():
    with pytest.raises(ValueError):
        calculate_velocity(80, -5)