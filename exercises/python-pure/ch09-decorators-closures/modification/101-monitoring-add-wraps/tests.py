from solution_user import instrument


@instrument
def ping() -> str:
    """ping doc."""
    return "pong"


def test_returns_pong():
    assert ping() == "pong"


def test_call_counter_works():
    ping.__calls__ = 0
    ping()
    ping()
    assert ping.__calls__ == 2


def test_name_is_preserved_not_wrapper():
    # Le coeur du refactor.
    assert ping.__name__ == "ping"


def test_doc_is_preserved():
    assert ping.__doc__ == "ping doc."
