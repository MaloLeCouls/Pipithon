import ast
import inspect

from solution_user import report


def test_behavior_completion_order():
    # Le job 2 (delay 0.005) finit en premier
    jobs = [(0, 0.05), (1, 0.03), (2, 0.005)]
    result = report(jobs)
    assert result[0][0] == 2


def test_behavior_all_jobs_present():
    jobs = [(0, 0.01), (1, 0.02), (2, 0.005), (3, 0.0), (4, 0.015)]
    result = report(jobs)
    assert sorted(r[0] for r in result) == [0, 1, 2, 3, 4]


def test_behavior_empty():
    assert report([]) == []


def test_form_uses_as_completed():
    src = inspect.getsource(report)
    tree = ast.parse(src)
    has = any(
        isinstance(n, ast.Name) and n.id == "as_completed" for n in ast.walk(tree)
    )
    assert has, "Utilise `as_completed`."
