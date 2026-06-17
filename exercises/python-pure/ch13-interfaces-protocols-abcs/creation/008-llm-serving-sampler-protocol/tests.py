from pymistral import GenerationConfig, Logits
from pymistral.sampling import Sampler

from solution_user import CountingSampler


def test_satisfies_sampler_protocol():
    s = CountingSampler()
    assert isinstance(s, Sampler), \
        "CountingSampler doit satisfaire le Protocol Sampler (runtime_checkable)."


def test_call_returns_argmax():
    s = CountingSampler()
    out = s(Logits([0.1, 0.9, 0.2]), GenerationConfig())
    assert out == 1


def test_call_increments_counter():
    s = CountingSampler()
    assert s.calls == 0
    s(Logits([0.5, 0.5]), GenerationConfig())
    s(Logits([0.5, 0.5]), GenerationConfig())
    assert s.calls == 2


def test_empty_logits_returns_fallback():
    s = CountingSampler(fallback=7)
    out = s(Logits([]), GenerationConfig())
    assert out == 7


def test_no_inheritance_from_sampler():
    """Sampler est un Protocol — pas dans le MRO de CountingSampler."""
    assert Sampler not in CountingSampler.__mro__
