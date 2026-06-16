import math

import pytest

from solution_user import make_logprob_accumulator


def test_first_send_works_without_explicit_priming():
    coro = make_logprob_accumulator()
    # Si l'amorçage est oublié, ce send() lève TypeError ("can't send non-None
    # value to a just-started generator").
    avg = coro.send(-1.0)
    assert math.isclose(avg, -1.0)


def test_running_average():
    coro = make_logprob_accumulator()
    assert math.isclose(coro.send(-2.0), -2.0)
    assert math.isclose(coro.send(-4.0), -3.0)
    assert math.isclose(coro.send(0.0), -2.0)


def test_close_does_not_raise():
    coro = make_logprob_accumulator()
    coro.send(-1.0)
    coro.close()  # doit être silencieux
    # Après close, send lève StopIteration.
    with pytest.raises(StopIteration):
        coro.send(0.0)


def test_independent_instances():
    a = make_logprob_accumulator()
    b = make_logprob_accumulator()
    a.send(-3.0)
    a.send(-5.0)
    # b n'est pas affecté par a.
    assert math.isclose(b.send(-1.0), -1.0)


def test_close_after_no_input():
    coro = make_logprob_accumulator()
    coro.close()  # fermeture immédiate, sans aucun send
    # Pas d'exception attendue.
