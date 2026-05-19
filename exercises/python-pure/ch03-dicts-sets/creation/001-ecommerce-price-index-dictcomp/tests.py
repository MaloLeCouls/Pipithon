import ast
import inspect

from solution_user import price_index

PRODUCTS = [
    {"sku": "A1", "price": 9.9},
    {"sku": "B2", "price": 19.0},
]


def test_basic_index():
    assert price_index(PRODUCTS) == {"A1": 9.9, "B2": 19.0}


def test_empty():
    assert price_index([]) == {}


def test_uses_dict_comprehension():
    tree = ast.parse(inspect.getsource(price_index))
    assert any(isinstance(n, ast.DictComp) for n in ast.walk(tree)), \
        "utilise une dict comprehension"
    assert not any(isinstance(n, ast.For) for n in ast.walk(tree)), \
        "pas de boucle for explicite"


def test_duplicate_sku_last_wins():
    # edge : sémantique dict — le dernier prix écrase
    dup = [{"sku": "X", "price": 1.0}, {"sku": "X", "price": 2.0}]
    assert price_index(dup) == {"X": 2.0}
