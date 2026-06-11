import inspect

from solution_user import apply_discount


def test_basic_behavior():
    assert apply_discount(100, 0.2) == 80.0


def test_zero_rate():
    assert apply_discount(50, 0) == 50.0


def test_signature_fully_annotated():
    sig = inspect.signature(apply_discount)
    for name, p in sig.parameters.items():
        assert p.annotation is not inspect.Parameter.empty, f"annotate `{name}`"
    assert sig.return_annotation is not inspect.Signature.empty, "annotate le retour"


def test_param_types_are_float():
    sig = inspect.signature(apply_discount)
    # sous `from __future__ import annotations`, l'annotation arrive en str.
    assert sig.parameters["price"].annotation in (float, "float")
    assert sig.parameters["rate"].annotation in (float, "float")


def test_return_type_is_float():
    sig = inspect.signature(apply_discount)
    assert sig.return_annotation in (float, "float")
