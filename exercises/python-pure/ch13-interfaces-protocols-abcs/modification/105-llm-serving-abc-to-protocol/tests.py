from typing import Protocol

from solution_user import GreedyImpl, Sampler, pick


def test_behavior_greedy_picks_argmax():
    assert pick(GreedyImpl(), [0.1, 0.9, 0.2]) == 1


def test_behavior_works_on_single_element():
    assert pick(GreedyImpl(), [0.5]) == 0


def test_form_sampler_is_protocol():
    assert Protocol in Sampler.__mro__, \
        "`Sampler` doit être un Protocol, pas une ABC."


def test_form_greedy_does_not_inherit_sampler():
    assert Sampler not in GreedyImpl.__mro__, \
        "`GreedyImpl` ne doit PLUS hériter de Sampler — Protocol est structurel."


def test_behavior_anonymous_class_works():
    """N'importe quelle classe avec `sample(...)` doit marcher au runtime."""

    class Anon:
        def sample(self, scores: list[float]) -> int:
            return 0

    assert pick(Anon(), [0.0, 1.0]) == 0
