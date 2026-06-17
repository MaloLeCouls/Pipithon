from solution_user import sum_typed


def test_sum_ints():
    result = sum_typed([1, 2, 3])
    assert result == 6


def test_sum_floats():
    result = sum_typed([1.5, 2.5])
    assert result == 4.0


def test_sum_negatives():
    assert sum_typed([-1, -2, -3]) == -6


def test_sum_empty_int():
    # Edge case : empty -> 0 (int builtin behavior)
    assert sum_typed([]) == 0


def test_sum_single_float():
    assert sum_typed([3.14]) == 3.14
