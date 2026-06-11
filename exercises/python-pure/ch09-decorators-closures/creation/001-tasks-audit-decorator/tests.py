from solution_user import AUDIT_LOG, audit


def setup_function():
    AUDIT_LOG.clear()


@audit
def assign(task: str) -> str:
    return f"assigned:{task}"


@audit
def close(task: str) -> str:
    return f"closed:{task}"


def test_call_logged():
    assign("X1")
    assert AUDIT_LOG == ["assign"]


def test_return_value_preserved():
    assert assign("Y") == "assigned:Y"


def test_multiple_calls_accumulate():
    assign("a")
    close("b")
    assign("c")
    assert AUDIT_LOG == ["assign", "close", "assign"]


def test_decorator_is_a_function():
    # audit doit être appelable (c'est une fonction).
    assert callable(audit)


def test_decorated_function_remains_callable():
    @audit
    def noop() -> int:
        return 42
    assert noop() == 42
