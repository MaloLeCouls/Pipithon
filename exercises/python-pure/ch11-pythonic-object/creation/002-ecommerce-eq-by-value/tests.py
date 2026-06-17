from solution_user import Coupon


def test_equal_codes_and_rates_are_equal():
    assert Coupon("SUMMER", 0.1) == Coupon("SUMMER", 0.1)


def test_different_codes_not_equal():
    assert Coupon("A", 0.1) != Coupon("B", 0.1)


def test_different_rates_not_equal():
    assert Coupon("A", 0.1) != Coupon("A", 0.2)


def test_not_equal_to_unrelated_type():
    assert Coupon("X", 0.0) != "X"
    assert Coupon("X", 0.0) != 42


def test_comparison_with_unrelated_returns_notimplemented():
    """Vérifie qu'on renvoie bien NotImplemented (pas juste False)."""
    c = Coupon("X", 0.0)
    assert c.__eq__("hello") is NotImplemented
