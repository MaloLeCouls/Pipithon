import ast
import inspect

from solution_user import late_fees_total

LOANS = [
    {"fine": 2.0, "late": True},
    {"fine": 5.0, "late": False},
    {"fine": 1.5, "late": True},
]


def test_behavior_preserved():
    assert late_fees_total(LOANS) == 3.5


def test_no_late_loans():
    assert late_fees_total([{"fine": 9.0, "late": False}]) == 0


def test_no_list_comprehension():
    tree = ast.parse(inspect.getsource(late_fees_total))
    assert not any(isinstance(n, ast.ListComp) for n in ast.walk(tree)), \
        "retire la list comprehension : passe une generator expression"


def test_uses_generator_expression():
    tree = ast.parse(inspect.getsource(late_fees_total))
    assert any(isinstance(n, ast.GeneratorExp) for n in ast.walk(tree)), \
        "utilise une generator expression dans sum()"


def test_empty():
    # edge : aucun prêt -> 0
    assert late_fees_total([]) == 0
