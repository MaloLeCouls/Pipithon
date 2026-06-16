import pytest

from pymistral import Token
from solution_user import make_token_counter


def test_first_send_does_not_raise():
    coro = make_token_counter()
    # Sans amorçage, ce send() lève TypeError ("can't send non-None value
    # to a just-started generator").
    count = coro.send(Token(id=0, text="a"))
    assert count == 1


def test_running_count():
    coro = make_token_counter()
    assert coro.send(Token(id=1, text="b")) == 1
    assert coro.send(Token(id=2, text="c")) == 2
    assert coro.send(Token(id=3, text="d")) == 3


def test_close_silent():
    coro = make_token_counter()
    coro.send(Token(id=0, text="a"))
    coro.close()
    with pytest.raises(StopIteration):
        coro.send(Token(id=1, text="b"))


def test_instances_independent():
    a = make_token_counter()
    b = make_token_counter()
    a.send(Token(id=0, text="x"))
    a.send(Token(id=1, text="y"))
    assert b.send(Token(id=2, text="z")) == 1


def test_close_immediately_after_priming():
    # Edge case : on ferme une coroutine déjà prête, sans aucun send.
    coro = make_token_counter()
    coro.close()  # ne doit pas lever
