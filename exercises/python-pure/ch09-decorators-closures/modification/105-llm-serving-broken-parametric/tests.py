from pymistral import GenerationConfig, Logits
from solution_user import TAGGED, tag


def setup_function():
    TAGGED.clear()


def test_basic_parametric():
    @tag("greedy")
    def custom(logits, cfg, rng=None):
        return logits.argmax()
    custom(Logits([0.1, 0.9, 0.5]), GenerationConfig())
    assert TAGGED == [("greedy", 1)]


def test_distinct_labels():
    @tag("A")
    def f1(): return 1
    @tag("B")
    def f2(): return 2
    f1()
    f2()
    f1()
    assert TAGGED == [("A", 1), ("B", 2), ("A", 1)]


def test_factory_is_callable_alone():
    # tag(label) seul DOIT renvoyer un décorateur.
    d = tag("test")
    assert callable(d)
