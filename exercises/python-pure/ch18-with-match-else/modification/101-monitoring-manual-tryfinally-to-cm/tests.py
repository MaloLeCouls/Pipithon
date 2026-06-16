import ast
import inspect

import pytest

from solution_user import Probe, traced_run, tracing_window


def test_behavior_probe_active_during():
    probe = Probe()
    seen: list[bool] = []

    def work():
        seen.append(probe.active)

    traced_run(probe, work)
    assert seen == [True]
    assert probe.active is False


def test_behavior_probe_off_after_exception():
    probe = Probe()

    def work():
        raise RuntimeError("oops")

    with pytest.raises(RuntimeError):
        traced_run(probe, work)
    assert probe.active is False


def test_behavior_tracing_window_usable_standalone():
    probe = Probe()
    with tracing_window(probe):
        assert probe.active is True
    assert probe.active is False


def test_form_traced_run_uses_with():
    tree = ast.parse(inspect.getsource(traced_run))
    has_with = any(isinstance(n, ast.With) for n in ast.walk(tree))
    has_tryfinally = any(
        isinstance(n, ast.Try) and n.finalbody for n in ast.walk(tree)
    )
    assert has_with, "`traced_run` doit utiliser `with tracing_window(...)`."
    assert not has_tryfinally, "Plus de try/finally dans `traced_run` — extrait dans le CM."


def test_form_tracing_window_is_contextmanager():
    # Détection robuste : un @contextmanager produit un objet ayant
    # `__enter__`/`__exit__` quand appelé.
    probe = Probe()
    cm = tracing_window(probe)
    assert hasattr(cm, "__enter__")
    assert hasattr(cm, "__exit__")
