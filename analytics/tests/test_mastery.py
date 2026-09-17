import pytest

from analytics.calculators.mastery import calculate_mastery


def test_mastery_normal():
    assert calculate_mastery(80, 60) == 70.0


def test_mastery_full():
    assert calculate_mastery(100, 100) == 100.0


def test_mastery_zero():
    assert calculate_mastery(0, 0) == 0.0


def test_assessment_score_above_100():
    with pytest.raises(ValueError):
        calculate_mastery(101, 80)


def test_practice_score_above_100():
    with pytest.raises(ValueError):
        calculate_mastery(80, 101)


def test_negative_assessment_score():
    with pytest.raises(ValueError):
        calculate_mastery(-1, 80)


def test_negative_practice_score():
    with pytest.raises(ValueError):
        calculate_mastery(80, -1)