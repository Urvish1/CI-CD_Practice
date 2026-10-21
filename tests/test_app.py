
import pytest

from app import add_numbers, greet_user, calculate_discount


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_greet_user():
    assert greet_user("Urvish") == "Hello, Urvish!"


def test_calculate_discount():
    assert calculate_discount(1000, 10) == 900


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(1000, 150)
