import ast
import inspect

from solution_user import top_orders


def test_behaviour_sort_descending():
    orders = [{"id": "a", "total": 30}, {"id": "b", "total": 100}, {"id": "c", "total": 50}]
    assert [o["id"] for o in top_orders(orders)] == ["b", "c", "a"]


def test_no_lambda_in_source():
    src = inspect.getsource(top_orders)
    tree = ast.parse(src)
    for node in ast.walk(tree):
        assert not isinstance(node, ast.Lambda), "remplace le lambda par operator.itemgetter"


def test_imports_itemgetter():
    src = inspect.getsource(top_orders)
    # importé soit dans la fn, soit en module — on est tolérant.
    import solution_user
    assert "itemgetter" in (src + inspect.getsource(solution_user))


def test_does_not_mutate_input():
    orders = [{"id": "a", "total": 1}]
    top_orders(orders)
    assert orders == [{"id": "a", "total": 1}]


def test_empty_input():
    assert top_orders([]) == []
