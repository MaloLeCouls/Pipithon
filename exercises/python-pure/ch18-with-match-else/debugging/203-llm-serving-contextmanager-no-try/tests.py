import pytest

from solution_user import Session, inference_window


def test_normal_path_idle_after():
    s = Session("s1")
    with inference_window(s) as got:
        assert got is s
        assert s.state == "active"
    assert s.state == "idle"


def test_idle_after_runtime_error():
    s = Session("s1")
    with pytest.raises(RuntimeError):
        with inference_window(s):
            raise RuntimeError("bad logits")
    assert s.state == "idle"  # AVANT le fix, restait "active"


def test_idle_after_value_error():
    s = Session("s1")
    with pytest.raises(ValueError):
        with inference_window(s):
            raise ValueError("oops")
    assert s.state == "idle"


def test_exception_still_propagates():
    s = Session("s1")
    with pytest.raises(RuntimeError):
        with inference_window(s):
            raise RuntimeError("must propagate")


def test_yields_session():
    s = Session("s1")
    with inference_window(s) as got:
        assert got is s
