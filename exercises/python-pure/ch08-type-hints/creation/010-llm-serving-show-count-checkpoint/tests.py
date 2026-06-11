import inspect

from solution_user import show_count


def test_one_singular():
    assert show_count(1, "token") == "1 token"


def test_zero_default_plural():
    assert show_count(0, "token") == "0 tokens"


def test_many_default_plural():
    assert show_count(3, "token") == "3 tokens"


def test_explicit_plural():
    assert show_count(5, "mouse", "mice") == "5 mice"


def test_explicit_plural_one_still_singular():
    # 1 -> singular peu importe le plural fourni.
    assert show_count(1, "mouse", "mice") == "1 mouse"


def test_signature_fully_annotated():
    sig = inspect.signature(show_count)
    for name, p in sig.parameters.items():
        assert p.annotation is not inspect.Parameter.empty, f"annotate `{name}`"
    assert sig.return_annotation is not inspect.Signature.empty


def test_param_types_correct():
    sig = inspect.signature(show_count)
    assert sig.parameters["count"].annotation in (int, "int")
    assert sig.parameters["singular"].annotation in (str, "str")
    assert sig.parameters["plural"].annotation in (str, "str")
