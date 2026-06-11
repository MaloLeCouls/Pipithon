from solution_user import TRACES, trace


def setup_function():
    TRACES.clear()


def test_unary_still_works():
    @trace
    def unary(x):
        return x * 2
    assert unary(3) == 6
    assert TRACES == ["unary"]


def test_kwargs_supported():
    @trace
    def assign(task: str, priority: int = 0):
        return f"{task}:p{priority}"
    out = assign("X", priority=1)
    assert out == "X:p1"


def test_multiple_args_supported():
    @trace
    def join(a, b, c):
        return (a, b, c)
    assert join(1, 2, 3) == (1, 2, 3)


def test_zero_args_supported():
    @trace
    def constant():
        return 42
    assert constant() == 42
