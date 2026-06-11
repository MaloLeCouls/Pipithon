import gc
import weakref

from solution_user import TokenCounter


def test_basic_correctness():
    tc = TokenCounter()
    assert tc.count_chars("abc") == 3


def test_two_instances_consistent():
    a = TokenCounter()
    b = TokenCounter()
    assert a.count_chars("hello") == 5
    assert b.count_chars("hello") == 5


def test_instance_is_releasable():
    # Le coeur du fix : une fois la dernière référence forte tombée,
    # l'instance doit pouvoir être collectée.
    tc = TokenCounter()
    ref = weakref.ref(tc)
    tc.count_chars("abc")  # déclenche le cache
    del tc
    gc.collect()
    assert ref() is None, "l'instance ne devrait plus être référencée par le cache"
