from solution_user import TIMINGS, ping


def setup_function():
    TIMINGS.clear()


def test_ping_returns_pong():
    assert ping() == "pong"


def test_timings_recorded():
    ping()
    assert TIMINGS == [("latency", "pong")]


def test_multiple_calls_accumulate():
    ping()
    ping()
    assert TIMINGS == [("latency", "pong"), ("latency", "pong")]
