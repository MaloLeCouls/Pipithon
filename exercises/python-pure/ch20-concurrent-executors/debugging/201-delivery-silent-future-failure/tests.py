import pytest

from solution_user import dispatch


def test_all_ok_returns_message():
    assert dispatch(["TRK-1", "TRK-2"]) == "all dispatched"


def test_error_propagates():
    """Le starter renvoie 'all dispatched' au lieu de propager."""
    with pytest.raises(PermissionError):
        dispatch(["TRK-1", "FORBIDDEN", "TRK-2"])


def test_first_failure_raises():
    with pytest.raises(PermissionError):
        dispatch(["FORBIDDEN"])


def test_empty_ok():
    assert dispatch([]) == "all dispatched"
