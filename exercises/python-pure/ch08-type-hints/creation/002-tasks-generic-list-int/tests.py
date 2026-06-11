import inspect

from solution_user import count_urgent


def test_counts_priority_one():
    assert count_urgent([1, 2, 3, 1, 1]) == 3


def test_no_urgent():
    assert count_urgent([2, 3, 4]) == 0


def test_empty_list():
    assert count_urgent([]) == 0


def test_param_annotated_with_list_int():
    sig = inspect.signature(count_urgent)
    ann = sig.parameters["priorities"].annotation
    # accepte `list[int]` ou la chaine équivalente sous from __future__ import annotations
    # Sous `from __future__ import annotations`, l'annotation arrive comme str.
    assert ann == list[int] or str(ann) == "list[int]", f"annotation = {ann}"


def test_return_annotated_int():
    sig = inspect.signature(count_urgent)
    ret = sig.return_annotation
    assert ret is int or str(ret) == "int"
