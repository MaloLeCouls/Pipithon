from solution_user import make_counter


def test_first_call_returns_one():
    c = make_counter()
    assert c() == 1


def test_successive_increments():
    c = make_counter()
    assert [c(), c(), c()] == [1, 2, 3]


def test_independent_counters():
    a = make_counter()
    b = make_counter()
    a()
    assert b() == 1


def test_custom_start():
    c = make_counter(10)
    assert c() == 11
