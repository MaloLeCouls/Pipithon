from solution_user import normalize


def test_normalize_int():
    assert normalize(5) == 5.0


def test_normalize_list():
    assert normalize([1, 2, 3]) == [1.0, 2.0, 3.0]


def test_normalize_zero():
    assert normalize(0) == 0.0


def test_normalize_empty_list():
    assert normalize([]) == []
