import pytest

from solution_user import Dish


def test_valid_dish():
    d = Dish("Soupe", 7.5)
    assert d.name == "Soupe"
    assert d.price == 7.5


def test_zero_price_rejected():
    with pytest.raises(ValueError, match="price"):
        Dish("Soupe", 0)


def test_negative_price_rejected():
    with pytest.raises(ValueError, match="price"):
        Dish("Soupe", -3.0)


def test_empty_name_rejected():
    with pytest.raises(ValueError, match="name"):
        Dish("", 5.0)


def test_whitespace_name_rejected():
    # edge : un nom d'espaces est aussi vide
    with pytest.raises(ValueError, match="name"):
        Dish("   ", 5.0)
