from solution_user import apply_discount, flat_5, half_off


def test_half_off_basic():
    assert half_off(100) == 50


def test_flat_5_basic():
    assert flat_5(20) == 15


def test_flat_5_clamps_at_zero():
    assert flat_5(3) == 0


def test_apply_discount_delegates():
    assert apply_discount(100, half_off) == 50
    assert apply_discount(20, flat_5) == 15


def test_apply_discount_accepts_lambda():
    # un lambda est une fonction : il doit marcher pareil.
    assert apply_discount(100, lambda p: p * 0.9) == 90
