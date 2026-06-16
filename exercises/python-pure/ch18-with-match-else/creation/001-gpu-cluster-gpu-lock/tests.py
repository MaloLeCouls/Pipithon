import pytest

from solution_user import GPU, GPULock


def test_status_in_use_inside_block():
    gpu = GPU("g0")
    with GPULock(gpu) as g:
        assert g.status == "in_use"


def test_status_free_after_block():
    gpu = GPU("g0")
    with GPULock(gpu):
        pass
    assert gpu.status == "free"


def test_enter_returns_the_gpu():
    gpu = GPU("g0")
    with GPULock(gpu) as g:
        assert g is gpu


def test_status_free_after_exception():
    gpu = GPU("g0")
    with pytest.raises(RuntimeError):
        with GPULock(gpu):
            raise RuntimeError("boom")
    assert gpu.status == "free"


def test_exception_is_not_swallowed():
    gpu = GPU("g0")
    with pytest.raises(ValueError):
        with GPULock(gpu):
            raise ValueError("oops")
