import pytest

from analytics.calculators.progress import calculate_progress


def test_progress_normal():
    assert calculate_progress(8, 10) == 80.0


def test_progress_full():
    assert calculate_progress(10, 10) == 100.0


def test_progress_zero():
    assert calculate_progress(0, 10) == 0.0


def test_progress_greater_than_total():
    with pytest.raises(ValueError):
        calculate_progress(11, 10)


def test_progress_negative():
    with pytest.raises(ValueError):
        calculate_progress(-1, 10)


def test_progress_zero_total():
    with pytest.raises(ValueError):
        calculate_progress(5, 0)