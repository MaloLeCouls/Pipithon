import pytest

from solution_user import LineItem


def test_behavior_basic():
    li = LineItem("SKU-1", 3, 9.99)
    assert li.sku == "SKU-1"
    assert li.quantity == 3
    assert li.unit_price == 9.99


def test_behavior_subtotal():
    assert LineItem("X", 2, 5.0).subtotal() == 10.0


def test_form_slots_declared():
    assert hasattr(LineItem, "__slots__")
    assert set(LineItem.__slots__) == {"sku", "quantity", "unit_price"}


def test_form_no_dict():
    li = LineItem("X", 1, 1.0)
    assert not hasattr(li, "__dict__"), \
        "__slots__ doit supprimer __dict__."


def test_form_extra_attr_raises():
    li = LineItem("X", 1, 1.0)
    with pytest.raises(AttributeError):
        li.discount = 0.1  # type: ignore[attr-defined]
