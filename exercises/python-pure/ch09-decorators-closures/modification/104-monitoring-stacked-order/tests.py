from solution_user import AUDIT, square


def setup_function():
    AUDIT.clear()
    square.cache_clear()


def test_first_call_audited():
    square(2)
    assert AUDIT == ["square"]


def test_cached_call_not_audited():
    # Le coeur du refactor : un hit ne traverse plus audit.
    square(2)
    square(2)
    square(2)
    assert AUDIT == ["square"]


def test_distinct_inputs_each_audited_once():
    square(2)
    square(3)
    square(2)
    assert AUDIT == ["square", "square"]


def test_correctness():
    assert square(5) == 25
