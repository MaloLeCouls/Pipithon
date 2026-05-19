from solution_user import expensive_prices


def test_basic_filter():
    assert expensive_prices([10, 50, 99, 5], 20) == [50, 99]


def test_order_preserved():
    assert expensive_prices([100, 10, 80], 15) == [100, 80]


def test_strict_threshold():
    assert expensive_prices([20, 21], 20) == [21]


def test_empty_input():
    assert expensive_prices([], 10) == []


def test_input_not_mutated():
    # edge : fonction pure, l'entrée reste intacte
    src = [10, 50]
    expensive_prices(src, 20)
    assert src == [10, 50]
