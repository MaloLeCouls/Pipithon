import inspect

from pymistral import GenerationConfig, Logits
from solution_user import top_token_per_batch


def _argmax_scorer(logits: Logits, _cfg: GenerationConfig) -> int:
    return logits.argmax()


def test_returns_one_int_per_logits_in_batch():
    batch = [Logits([1.0, 2.0, 0.5]), Logits([5.0, 1.0])]
    assert top_token_per_batch(batch, _argmax_scorer) == [1, 0]


def test_accepts_generator():
    gen = (Logits([0.1, 0.9]) for _ in range(3))
    assert top_token_per_batch(gen, _argmax_scorer) == [1, 1, 1]


def test_empty_batch():
    assert top_token_per_batch([], _argmax_scorer) == []


def test_signature_uses_callable():
    src = inspect.getsource(top_token_per_batch)
    assert "Callable" in src, "annote `scorer` avec Callable[[...], ...]"


def test_signature_fully_annotated():
    sig = inspect.signature(top_token_per_batch)
    for name, p in sig.parameters.items():
        assert p.annotation is not inspect.Parameter.empty, f"annotate `{name}`"
    assert sig.return_annotation is not inspect.Signature.empty
