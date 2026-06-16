import pytest

import solution_user
from solution_user import GPU, gpu_lock


def test_behavior_in_use_inside():
    g = GPU("g0")
    with gpu_lock(g) as got:
        assert got is g
        assert g.status == "in_use"
    assert g.status == "free"


def test_behavior_free_after_exception():
    g = GPU("g0")
    with pytest.raises(RuntimeError):
        with gpu_lock(g):
            raise RuntimeError("boom")
    assert g.status == "free"


def test_form_class_removed():
    assert not hasattr(solution_user, "GPULockCM"), \
        "Supprime la classe GPULockCM — le décorateur suffit."


def test_form_gpu_lock_is_contextmanager():
    g = GPU("g0")
    cm = gpu_lock(g)
    assert hasattr(cm, "__enter__")
    assert hasattr(cm, "__exit__")
