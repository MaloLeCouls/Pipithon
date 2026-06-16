import ast
import inspect

from solution_user import status_label


def test_behavior_all_known():
    assert status_label("todo") == "À faire"
    assert status_label("doing") == "En cours"
    assert status_label("review") == "En revue"
    assert status_label("done") == "Terminé"
    assert status_label("blocked") == "Bloqué"


def test_behavior_unknown_default():
    assert status_label("xxx") == "Inconnu"
    assert status_label("") == "Inconnu"


def test_form_uses_match():
    tree = ast.parse(inspect.getsource(status_label))
    has_match = any(isinstance(n, ast.Match) for n in ast.walk(tree))
    assert has_match, "Utilise un `match status:` à la place des if/elif."


def test_form_no_if_elif_left():
    tree = ast.parse(inspect.getsource(status_label))
    has_if = any(isinstance(n, ast.If) for n in ast.walk(tree))
    assert not has_if, "Supprime tous les `if`/`elif` — un seul `match` suffit."
