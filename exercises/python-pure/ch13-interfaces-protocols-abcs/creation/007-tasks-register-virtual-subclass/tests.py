import pytest

from solution_user import MemoryTask, RedisTask, Storable, register_redis


def test_memory_task_is_storable_by_inheritance():
    assert isinstance(MemoryTask(), Storable)


def test_redis_task_not_storable_before_register():
    # Avant register, RedisTask n'a aucun lien avec Storable.
    assert not isinstance(RedisTask(), Storable)


def test_redis_task_becomes_storable_after_register():
    register_redis()
    assert isinstance(RedisTask(), Storable)
    assert issubclass(RedisTask, Storable)


def test_redis_task_mro_does_not_contain_storable():
    """register() ne touche PAS le MRO — c'est un virtual subclass."""
    register_redis()
    assert Storable not in RedisTask.__mro__


def test_memory_task_save_works():
    m = MemoryTask()
    m.save()
    assert m.saved is True


def test_storable_still_abstract():
    with pytest.raises(TypeError):
        Storable()  # type: ignore[abstract]
