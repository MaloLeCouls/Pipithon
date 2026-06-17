from solution_user import SamplingConfig, is_greedy


def test_greedy_when_temp_zero_no_filters():
    cfg: SamplingConfig = {"temperature": 0.0}
    assert is_greedy(cfg) is True


def test_not_greedy_when_top_k_set():
    cfg: SamplingConfig = {"temperature": 0.0, "top_k": 50}
    assert is_greedy(cfg) is False


def test_not_greedy_when_top_p_set():
    cfg: SamplingConfig = {"temperature": 0.0, "top_p": 0.9}
    assert is_greedy(cfg) is False


def test_not_greedy_when_temp_nonzero():
    cfg: SamplingConfig = {"temperature": 0.7}
    assert is_greedy(cfg) is False


def test_optional_keys_not_required_at_runtime():
    """Le TypedDict accepte les seeds optionnels manquants à runtime."""
    cfg: SamplingConfig = {"temperature": 1.0, "seed": 42}
    assert "seed" in cfg


def test_typed_dict_has_temperature():
    assert "temperature" in SamplingConfig.__annotations__
