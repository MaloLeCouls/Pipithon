import pytest

from solution_user import GPU, GPULock


def test_normal_path_still_works():
    g = GPU("g0")
    with GPULock(g) as got:
        assert got is g
        assert g.status == "in_use"
    assert g.status == "free"


def test_runtime_error_propagates():
    g = GPU("g0")
    with pytest.raises(RuntimeError):
        with GPULock(g):
            raise RuntimeError("scheduler bug")


def test_value_error_propagates():
    g = GPU("g0")
    with pytest.raises(ValueError):
        with GPULock(g):
            raise ValueError("bad config")


def test_status_free_after_exception():
    g = GPU("g0")
    with pytest.raises(RuntimeError):
        with GPULock(g):
            raise RuntimeError("crash")
    assert g.status == "free"


def test_exit_returns_falsy():
    # Edge case : on ré-affirme la sémantique. __exit__(None, None, None)
    # doit retourner None ou False — jamais True quand il n'y a pas
    # d'exception (sinon comportement asymétrique).
    g = GPU("g0")
    lock = GPULock(g)
    lock.__enter__()
    result = lock.__exit__(None, None, None)
    assert not result
