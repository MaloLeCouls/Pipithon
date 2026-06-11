import pytest

from solution_user import retry


def test_succeeds_first_try():
    calls = [0]
    @retry(max_attempts=3)
    def ok():
        calls[0] += 1
        return "fine"
    assert ok() == "fine"
    assert calls[0] == 1


def test_recovers_after_two_failures():
    calls = [0]
    @retry(max_attempts=3)
    def flaky():
        calls[0] += 1
        if calls[0] < 3:
            raise RuntimeError("boom")
        return "ok"
    assert flaky() == "ok"
    assert calls[0] == 3


def test_raises_last_exception_after_all_fail():
    calls = [0]
    @retry(max_attempts=2)
    def always_fails():
        calls[0] += 1
        raise ValueError(f"attempt {calls[0]}")
    with pytest.raises(ValueError, match="attempt 2"):
        always_fails()
    assert calls[0] == 2


def test_passes_args_through():
    @retry(max_attempts=1)
    def echo(*args, **kwargs):
        return (args, kwargs)
    assert echo(1, 2, x=3) == ((1, 2), {"x": 3})
