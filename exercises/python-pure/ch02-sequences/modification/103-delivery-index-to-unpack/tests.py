import ast
import inspect

from solution_user import routing_label


def test_express():
    assert routing_label(("A1", 2.0, "Z3", True)) == "A1 [EXPRESS Z3] 2.0kg"


def test_standard():
    assert routing_label(("B2", 5.5, "Z1", False)) == "B2 [Z1] 5.5kg"


def test_no_indexing_of_rec():
    tree = ast.parse(inspect.getsource(routing_label))
    indexed = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.Subscript)
        and isinstance(n.value, ast.Name)
        and n.value.id == "rec"
    ]
    assert not indexed, "déballe rec par unpacking, pas d'accès rec[i]"


def test_uses_unpacking_assignment():
    tree = ast.parse(inspect.getsource(routing_label))
    tuple_targets = [
        t for n in ast.walk(tree) if isinstance(n, ast.Assign)
        for t in n.targets if isinstance(t, ast.Tuple)
    ]
    assert tuple_targets, "utilise un unpacking (a, b, c, d = rec)"


def test_integer_weight_edge():
    # edge : poids entier rendu tel quel
    assert routing_label(("C3", 7, "Z9", True)) == "C3 [EXPRESS Z9] 7kg"
