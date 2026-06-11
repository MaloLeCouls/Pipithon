from solution_user import PercentageDiscount


def test_basic_discount():
    d = PercentageDiscount(0.2)
    assert d(100) == 80.0


def test_zero_rate_returns_full_price():
    d = PercentageDiscount(0.0)
    assert d(50) == 50.0


def test_full_rate_returns_zero():
    d = PercentageDiscount(1.0)
    assert d(75) == 0.0


def test_instance_is_callable():
    d = PercentageDiscount(0.1)
    assert callable(d)


def test_two_instances_independent():
    a = PercentageDiscount(0.1)
    b = PercentageDiscount(0.5)
    assert a(100) == 90.0
    assert b(100) == 50.0


def test_usable_as_higher_order_argument():
    # une instance doit être utilisable partout où une fonction est attendue.
    d = PercentageDiscount(0.25)
    out = [d(p) for p in [100, 200, 400]]
    assert out == [75.0, 150.0, 300.0]
