import ast
import inspect

from solution_user import discounted_skus

PRODUCTS = [
    {"sku": "A", "discount": 10},
    {"sku": "B", "discount": 0},
    {"sku": "C", "discount": 5},
]


def test_behavior_preserved():
    assert discounted_skus(PRODUCTS) == ["A", "C"]


def test_no_discount_returns_empty():
    assert discounted_skus([{"sku": "X", "discount": 0}]) == []


def test_uses_list_comprehension():
    tree = ast.parse(inspect.getsource(discounted_skus))
    assert any(isinstance(n, ast.ListComp) for n in ast.walk(tree)), \
        "utilise une list comprehension"


def test_no_explicit_for_loop():
    tree = ast.parse(inspect.getsource(discounted_skus))
    assert not any(isinstance(n, ast.For) for n in ast.walk(tree)), \
        "supprime la boucle for explicite"


def test_empty_input():
    # edge : entrée vide -> sortie vide, sans erreur
    assert discounted_skus([]) == []
