import inspect

from solution_user import TaskRecord, process


def test_behavior_format():
    t = {"title": "Ship", "priority": 2, "done": False}
    assert process(t) == "Ship (P2)"


def test_form_taskrecord_declared():
    assert "title" in TaskRecord.__annotations__
    assert "priority" in TaskRecord.__annotations__
    assert "done" in TaskRecord.__annotations__


def test_form_process_typed_as_taskrecord():
    sig = inspect.signature(process)
    ann = sig.parameters["task"].annotation
    assert ann is TaskRecord or ann == "TaskRecord", \
        f"`task` doit être annoté TaskRecord, obtenu {ann}."


def test_form_no_any_in_signature():
    sig = inspect.signature(process)
    for p in sig.parameters.values():
        assert "Any" not in str(p.annotation)
