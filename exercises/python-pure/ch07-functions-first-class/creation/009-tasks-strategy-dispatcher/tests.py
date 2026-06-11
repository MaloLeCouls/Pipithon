import pytest

from solution_user import make_dispatcher


def test_dispatches_to_named_strategy():
    strategies = {
        "triage": lambda t: f"triage:{t['title']}",
        "close": lambda t: f"close:{t['title']}",
    }
    dispatch = make_dispatcher(strategies)
    assert dispatch("triage", {"title": "bug"}) == "triage:bug"
    assert dispatch("close", {"title": "feat"}) == "close:feat"


def test_unknown_strategy_raises_keyerror():
    dispatch = make_dispatcher({"triage": lambda t: "x"})
    with pytest.raises(KeyError):
        dispatch("unknown", {"title": "y"})


def test_empty_registry():
    dispatch = make_dispatcher({})
    with pytest.raises(KeyError):
        dispatch("anything", {})


def test_adding_to_registry_affects_dispatcher():
    # closure sur le dict d'origine : muter le dict après création est visible.
    strategies: dict = {"a": lambda t: "A"}
    dispatch = make_dispatcher(strategies)
    strategies["b"] = lambda t: "B"
    assert dispatch("b", {}) == "B"


def test_callable_class_works_as_strategy():
    # toute callable doit marcher, pas seulement les def/lambda.
    class Const:
        def __call__(self, t: dict) -> str:
            return "K"
    dispatch = make_dispatcher({"const": Const()})
    assert dispatch("const", {}) == "K"
