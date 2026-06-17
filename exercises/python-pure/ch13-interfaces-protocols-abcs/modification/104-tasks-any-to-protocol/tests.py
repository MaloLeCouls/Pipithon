import inspect
from typing import Any

from solution_user import Completable, finish_task


class GymBooking:
    def complete(self) -> str:
        return "done"


def test_behavior_returns_completed_string():
    assert finish_task(GymBooking()) == "done"


def test_completable_is_protocol():
    # On vérifie que c'est bien un Protocol via mro
    from typing import Protocol
    assert Protocol in Completable.__mro__


def test_completable_declares_complete_method():
    assert "complete" in dir(Completable)


def test_form_signature_typed_as_completable():
    sig = inspect.signature(finish_task)
    p = sig.parameters["task"]
    # L'annotation est stringifiée à cause de `from __future__ import annotations`.
    ann = p.annotation
    assert ann is Completable or ann == "Completable", \
        f"`task` doit être annoté `Completable`, pas `{ann}`."
    # Surtout, plus d'`Any`
    assert ann is not Any, "Plus d'`Any` sur task."
