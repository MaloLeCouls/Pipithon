import inspect

from solution_user import first_or_default


def test_first_of_non_empty_list_of_str():
    assert first_or_default(["a", "b", "c"], "x") == "a"


def test_default_returned_for_empty():
    assert first_or_default([], 42) == 42


def test_works_with_int_list():
    assert first_or_default([10, 20], 0) == 10


def test_works_with_generator():
    assert first_or_default((x for x in [1, 2]), 0) == 1


def test_uses_typevar():
    import solution_user
    src = inspect.getsource(solution_user)
    assert "TypeVar" in src, "utilise typing.TypeVar pour annoter génériquement"


def test_signature_fully_annotated():
    sig = inspect.signature(first_or_default)
    for name, p in sig.parameters.items():
        assert p.annotation is not inspect.Parameter.empty, f"annotate `{name}`"
    assert sig.return_annotation is not inspect.Signature.empty
