import solution_user
from solution_user import CLOCK_LOG, clock, make_averager


def setup_function():
    CLOCK_LOG.clear()
    solution_user._TICK = 0


def test_clock_basic():
    @clock("{name}:{elapsed}={result}")
    def double(n):
        return n * 2
    assert double(3) == 6
    assert CLOCK_LOG == ["double:1=6"]


def test_clock_preserves_metadata():
    @clock("{name}")
    def documented():
        """A doc."""
        return None
    assert documented.__name__ == "documented"
    assert documented.__doc__ == "A doc."


def test_make_averager_running_mean():
    avg = make_averager()
    assert avg(10) == 10.0
    assert avg(20) == 15.0
    assert avg(30) == 20.0


def test_combo_clocked_averager():
    @clock("avg:{result:.1f}")
    def avg_one(value, _avg=make_averager()):
        return _avg(value)
    avg_one(10)
    avg_one(20)
    avg_one(30)
    assert CLOCK_LOG == ["avg:10.0", "avg:15.0", "avg:20.0"]


def test_clock_returns_value_unchanged():
    @clock("ignored")
    def identity(x):
        return x
    assert identity({"k": 1}) == {"k": 1}
