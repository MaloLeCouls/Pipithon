import pytest

from pymistral import GenerationConfig
from solution_user import validate_temperature


@validate_temperature
def infer(prompt: str, config: GenerationConfig) -> str:
    return f"infer:{prompt}:t={config.temperature}"


def test_accepts_valid_temperature_positional():
    cfg = GenerationConfig(temperature=0.7)
    assert infer("hello", cfg) == "infer:hello:t=0.7"


def test_accepts_valid_temperature_keyword():
    cfg = GenerationConfig(temperature=1.0)
    assert infer("hi", config=cfg).startswith("infer:hi")


def test_rejects_low_temperature():
    cfg = GenerationConfig(temperature=0.1)
    with pytest.raises(ValueError, match="temperature too low"):
        infer("x", cfg)


def test_does_not_call_fn_when_invalid():
    seen = []
    @validate_temperature
    def f(prompt: str, config: GenerationConfig) -> None:
        seen.append(prompt)
    cfg = GenerationConfig(temperature=0.2)
    with pytest.raises(ValueError):
        f("never", cfg)
    assert seen == []
