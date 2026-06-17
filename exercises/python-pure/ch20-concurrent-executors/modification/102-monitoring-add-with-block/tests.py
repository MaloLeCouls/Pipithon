import ast
import inspect

from solution_user import sample_all


def test_behavior_basic():
    assert sample_all(["cpu", "mem", "disk"]) == [3, 3, 4]


def test_behavior_empty():
    assert sample_all([]) == []


def test_form_uses_with_block():
    src = inspect.getsource(sample_all)
    tree = ast.parse(src)
    assert any(isinstance(n, ast.With) for n in ast.walk(tree)), \
        "Utilise `with ThreadPoolExecutor(...) as ex:`."


def test_form_no_explicit_shutdown_outside_with():
    """Plus besoin d'un `shutdown` manuel quand on a un `with`."""
    src = inspect.getsource(sample_all)
    tree = ast.parse(src)
    # Détecte ex.shutdown(...) qui ne serait pas dans un With block.
    # Simplification : on accepte aussi pas de shutdown du tout.
    n_shutdown = sum(
        1 for n in ast.walk(tree)
        if isinstance(n, ast.Attribute) and n.attr == "shutdown"
    )
    assert n_shutdown <= 0, "Pas besoin de shutdown manuel — le `with` s'en charge."
