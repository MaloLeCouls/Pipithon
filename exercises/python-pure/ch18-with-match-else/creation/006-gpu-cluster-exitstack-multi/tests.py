import pytest

from solution_user import GPU, allocate_all


def test_all_in_use_inside_block():
    gpus = [GPU(f"g{i}") for i in range(3)]
    with allocate_all(gpus) as locked:
        assert all(g.status == "in_use" for g in locked)
        assert len(locked) == 3


def test_all_free_after_block():
    gpus = [GPU(f"g{i}") for i in range(3)]
    with allocate_all(gpus):
        pass
    assert all(g.status == "free" for g in gpus)


def test_yields_locked_list():
    gpus = [GPU("g0"), GPU("g1")]
    with allocate_all(gpus) as locked:
        assert [g.gpu_id for g in locked] == ["g0", "g1"]


def test_all_free_after_exception():
    gpus = [GPU(f"g{i}") for i in range(4)]
    with pytest.raises(RuntimeError):
        with allocate_all(gpus):
            raise RuntimeError("oom")
    assert all(g.status == "free" for g in gpus)


def test_empty_list_works():
    with allocate_all([]) as locked:
        assert locked == []
