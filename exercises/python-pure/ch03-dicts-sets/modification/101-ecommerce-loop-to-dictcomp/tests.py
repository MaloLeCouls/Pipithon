import ast
import inspect

from solution_user import stock_index

P = [{"sku": "A", "stock": 3}, {"sku": "B", "stock": 0}]


def test_behavior_preserved():
    assert stock_index(P) == {"A": 3, "B": 0}


def test_empty():
    assert stock_index([]) == {}


def test_uses_dict_comprehension():
    tree = ast.parse(inspect.getsource(stock_index))
    assert any(isinstance(n, ast.DictComp) for n in ast.walk(tree)), \
        "utilise une dict comprehension"


def test_no_for_loop():
    tree = ast.parse(inspect.getsource(stock_index))
    assert not any(isinstance(n, ast.For) for n in ast.walk(tree)), \
        "supprime la boucle for"


def test_duplicate_sku_last_wins():
    # edge : sémantique dict inchangée
    assert stock_index([{"sku": "X", "stock": 1}, {"sku": "X", "stock": 9}]) == {"X": 9}
