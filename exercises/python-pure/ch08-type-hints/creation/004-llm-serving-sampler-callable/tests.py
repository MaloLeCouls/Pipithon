import inspect

from pymistral import GenerationConfig, Logits, greedy_sampler, top_k_sampler
from solution_user import sample_next


def test_with_greedy_sampler_returns_argmax():
    logits = Logits([0.1, 0.9, 0.5])
    cfg = GenerationConfig()
    assert sample_next(logits, cfg, greedy_sampler) == 1


def test_with_top_k_sampler_returns_in_topk():
    logits = Logits([5.0, 4.0, -10.0])
    cfg = GenerationConfig(top_k=2, seed=42)
    out = sample_next(logits, cfg, top_k_sampler)
    assert out in (0, 1)


def test_works_with_custom_callable():
    # un lambda satisfait le Protocol Sampler par structure.
    logits = Logits([1.0, 2.0])
    cfg = GenerationConfig()
    assert sample_next(logits, cfg, lambda lg, c, rng=None: 0) == 0


def test_signature_fully_annotated():
    sig = inspect.signature(sample_next)
    for name, p in sig.parameters.items():
        assert p.annotation is not inspect.Parameter.empty, f"annotate `{name}`"
    assert sig.return_annotation is not inspect.Signature.empty


def test_return_type_is_int():
    sig = inspect.signature(sample_next)
    ret = sig.return_annotation
    assert ret is int or str(ret) == "int"
