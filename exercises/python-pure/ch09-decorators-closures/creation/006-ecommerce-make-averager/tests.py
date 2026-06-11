from solution_user import make_averager


def test_first_value():
    avg = make_averager()
    assert avg(10) == 10.0


def test_running_average():
    avg = make_averager()
    avg(10)
    avg(20)
    assert avg(30) == 20.0


def test_independent_averagers():
    a = make_averager()
    b = make_averager()
    a(100)
    b(0)
    assert a(50) == 75.0
    assert b(100) == 50.0


def test_returns_float():
    avg = make_averager()
    out = avg(1)
    assert isinstance(out, float)
