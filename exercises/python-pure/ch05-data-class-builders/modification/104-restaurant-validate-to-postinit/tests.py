import pytest

from solution_user import Dish


def test_valid_dish_ok():
    d = Dish("Pizza", 12.0)
    assert d.name == "Pizza"
    assert d.price == 12.0


def test_zero_price_rejected_at_construction():
    with pytest.raises(ValueError):
        Dish("Eau", 0.0)


def test_negative_price_rejected_at_construction():
    with pytest.raises(ValueError):
        Dish("Bug", -1.0)


def test_validation_is_automatic_no_external_call():
    # Aucun import de validate_dish : la validation est portée par la classe.
    import solution_user

    assert not hasattr(solution_user, "validate_dish")


def test_is_a_dataclass():
    assert "__dataclass_fields__" in vars(Dish)
