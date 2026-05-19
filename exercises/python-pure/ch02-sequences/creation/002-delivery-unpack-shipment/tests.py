import ast
import inspect

from solution_user import describe


def test_basic_format():
    assert describe(("ABC123", 2.5, "10:00")) == "ABC123 -> 2.5kg, ETA 10:00"


def test_other_values():
    assert describe(("Z9", 0.3, "23:45")) == "Z9 -> 0.3kg, ETA 23:45"


def test_uses_unpacking_not_indexing():
    # on veut l'idiome unpacking, pas shipment[0]/[1]/[2]
    # (on ne flague que l'indexation de `shipment`, pas l'annotation tuple[...])
    tree = ast.parse(inspect.getsource(describe))
    indexed_shipment = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.Subscript)
        and isinstance(n.value, ast.Name)
        and n.value.id == "shipment"
    ]
    assert not indexed_shipment, "déballe le tuple, n'indexe pas shipment[i]"


def test_integer_weight():
    # edge : poids entier formaté tel quel
    assert describe(("P1", 5, "08:00")) == "P1 -> 5kg, ETA 08:00"
