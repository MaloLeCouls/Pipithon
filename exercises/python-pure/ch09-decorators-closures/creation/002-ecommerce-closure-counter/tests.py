from solution_user import make_counter


def test_first_call_returns_one():
    c = make_counter()
    assert c() == 1


def test_successive_calls_increment():
    c = make_counter()
    assert [c(), c(), c()] == [1, 2, 3]


def test_independent_counters():
    a = make_counter()
    b = make_counter()
    a()
    a()
    assert a() == 3
    assert b() == 1


def test_custom_start():
    c = make_counter(100)
    assert c() == 101
    assert c() == 102
