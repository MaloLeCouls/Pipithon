from solution_user import instrument


@instrument
def ping() -> str:
    """Renvoie 'pong'."""
    return "pong"


def test_call_increments_counter():
    ping.__calls__ = 0
    ping()
    ping()
    assert ping.__calls__ == 2


def test_return_value_preserved():
    assert ping() == "pong"


def test_name_preserved():
    assert ping.__name__ == "ping"


def test_doc_preserved():
    assert ping.__doc__ == "Renvoie 'pong'."


def test_initial_counter_is_zero():
    @instrument
    def freshly_decorated() -> None:
        pass
    assert freshly_decorated.__calls__ == 0
