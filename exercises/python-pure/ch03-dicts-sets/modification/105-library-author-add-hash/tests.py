import ast
import inspect

from solution_user import Author, distinct


def test_distinct_behavior_and_order():
    authors = [
        Author("Frank", "Herbert"),
        Author("William", "Gibson"),
        Author("Frank", "Herbert"),
    ]
    assert distinct(authors) == [
        Author("Frank", "Herbert"),
        Author("William", "Gibson"),
    ]


def test_author_is_hashable():
    hash(Author("Frank", "Herbert"))  # ne doit pas lever TypeError


def test_hash_consistent_with_eq():
    a, b = Author("Frank", "Herbert"), Author("Frank", "Herbert")
    assert a == b
    assert hash(a) == hash(b)


def test_author_usable_in_set():
    s = {Author("A", "B"), Author("A", "B"), Author("C", "D")}
    assert len(s) == 2


def test_distinct_uses_a_set():
    tree = ast.parse(inspect.getsource(distinct))
    uses_set = any(
        (isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "set")
        or isinstance(n, ast.SetComp)
        for n in ast.walk(tree)
    )
    assert uses_set, "déduplique via un set (pas un `in` sur liste en O(n^2))"


def test_empty():
    # edge
    assert distinct([]) == []
