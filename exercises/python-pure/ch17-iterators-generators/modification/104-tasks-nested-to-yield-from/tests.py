import ast
import inspect

from solution_user import Task, all_tasks


def test_behavior_concatenates_in_order():
    s1 = [Task("A1"), Task("A2")]
    s2 = [Task("B1")]
    ids = [t.task_id for t in all_tasks(s1, s2)]
    assert ids == ["A1", "A2", "B1"]


def test_behavior_no_args():
    assert list(all_tasks()) == []


def test_behavior_accepts_generators():
    def gen():
        yield Task("G1")
        yield Task("G2")

    ids = [t.task_id for t in all_tasks(gen(), [Task("L1")])]
    assert ids == ["G1", "G2", "L1"]


def test_form_uses_yield_from():
    tree = ast.parse(inspect.getsource(all_tasks))
    assert any(isinstance(n, ast.YieldFrom) for n in ast.walk(tree)), \
        "Utilise `yield from sprint` à la place de la boucle interne."


def test_form_no_inner_for_with_plain_yield():
    # Détecter un `for` IMBRIQUÉ qui contient un Yield simple : c'est ce
    # qu'on veut éliminer. Un seul `for` (externe) reste autorisé.
    tree = ast.parse(inspect.getsource(all_tasks))
    fors = [n for n in ast.walk(tree) if isinstance(n, ast.For)]
    assert len(fors) <= 1, "Une seule boucle for (externe) — l'interne devient `yield from`."
