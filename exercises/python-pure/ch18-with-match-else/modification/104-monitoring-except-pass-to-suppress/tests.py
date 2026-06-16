import ast
import inspect

from solution_user import Dashboard, silence_alerts


def make_dashboard() -> Dashboard:
    d = Dashboard()
    d.enable("cpu")
    d.enable("mem")
    return d


def test_behavior_disables_existing():
    d = make_dashboard()
    silence_alerts(d, ["cpu"])
    assert d.is_enabled("cpu") is False
    assert d.is_enabled("mem") is True


def test_behavior_ignores_missing():
    d = make_dashboard()
    silence_alerts(d, ["missing-a", "missing-b"])
    # Aucune exception, aucun état changé.
    assert d.is_enabled("cpu") is True
    assert d.is_enabled("mem") is True


def test_behavior_mix():
    d = make_dashboard()
    silence_alerts(d, ["cpu", "missing", "mem"])
    assert d.is_enabled("cpu") is False
    assert d.is_enabled("mem") is False


def test_form_uses_suppress():
    src = inspect.getsource(silence_alerts)
    assert "suppress" in src, "Utilise `contextlib.suppress`."


def test_form_no_try_except_left():
    tree = ast.parse(inspect.getsource(silence_alerts))
    has_try = any(isinstance(n, ast.Try) for n in ast.walk(tree))
    assert not has_try, "Plus de `try/except` dans `silence_alerts` — `suppress` suffit."
