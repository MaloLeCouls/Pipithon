import pytest

from solution_user import AlertSilencer, Dashboard


def test_silenced_inside_block():
    d = Dashboard(silenced=False)
    with AlertSilencer(d):
        assert d.silenced is True


def test_restored_after_block_from_false():
    d = Dashboard(silenced=False)
    with AlertSilencer(d):
        pass
    assert d.silenced is False


def test_restored_after_block_from_true():
    d = Dashboard(silenced=True)
    with AlertSilencer(d):
        assert d.silenced is True
    assert d.silenced is True  # on restore l'ancien True


def test_restored_after_exception():
    d = Dashboard(silenced=False)
    with pytest.raises(RuntimeError):
        with AlertSilencer(d):
            raise RuntimeError("boom")
    assert d.silenced is False


def test_enter_returns_dashboard():
    d = Dashboard()
    with AlertSilencer(d) as got:
        assert got is d
