from pymistral import GenerationConfig, Logits, greedy_sampler
from solution_user import SAMPLE_LOG, log_sampler


def setup_function():
    SAMPLE_LOG.clear()


def test_wrap_greedy_returns_argmax():
    wrapped = log_sampler(greedy_sampler)
    out = wrapped(Logits([0.1, 0.9, 0.5]), GenerationConfig())
    assert out == 1


def test_log_records_token_and_vocab_size():
    wrapped = log_sampler(greedy_sampler)
    wrapped(Logits([0.1, 0.9, 0.5, 0.2]), GenerationConfig())
    assert SAMPLE_LOG == [(1, 4)]


def test_multiple_calls_accumulate():
    wrapped = log_sampler(greedy_sampler)
    wrapped(Logits([0.0, 1.0]), GenerationConfig())
    wrapped(Logits([1.0, 0.0, 0.5]), GenerationConfig())
    assert SAMPLE_LOG == [(1, 2), (0, 3)]


def test_works_with_arbitrary_sampler():
    @log_sampler
    def custom(logits, cfg, rng=None):
        return 0
    custom(Logits([1.0, 2.0]), GenerationConfig())
    assert SAMPLE_LOG == [(0, 2)]
