import pytest

from solution_user import GPU, OutOfMemoryError, TryAllocate


def test_normal_path_status_free():
    g = GPU("g0")
    with TryAllocate(g) as got:
        assert got is g
        assert g.status == "in_use"
    assert g.status == "free"


def test_oom_is_swallowed_and_marks_failed():
    g = GPU("g0")
    # Le with NE doit PAS lever — l'exception est avalée par __exit__.
    with TryAllocate(g):
        raise OutOfMemoryError("vram full")
    assert g.status == "failed"


def test_other_exception_propagates_and_status_free():
    g = GPU("g0")
    with pytest.raises(RuntimeError):
        with TryAllocate(g):
            raise RuntimeError("bug")
    assert g.status == "free"


def test_value_error_propagates():
    g = GPU("g0")
    with pytest.raises(ValueError):
        with TryAllocate(g):
            raise ValueError("bad config")
    assert g.status == "free"


def test_oom_subclass_also_swallowed():
    class HardOOM(OutOfMemoryError):
        pass

    g = GPU("g0")
    with TryAllocate(g):
        raise HardOOM("hard oom")
    assert g.status == "failed"
