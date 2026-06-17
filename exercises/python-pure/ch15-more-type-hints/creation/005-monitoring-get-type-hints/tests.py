from solution_user import param_types, record_metric


def test_returns_dict_of_types():
    hints = param_types(record_metric)
    assert hints == {"name": str, "value": float}


def test_return_key_removed():
    hints = param_types(record_metric)
    assert "return" not in hints


def test_resolves_stringified_annotations():
    """`from __future__ import annotations` rend les annotations str ;
    `get_type_hints` les résout en VRAI types."""
    hints = param_types(record_metric)
    for v in hints.values():
        assert isinstance(v, type), f"Attendait un type, obtenu {type(v).__name__}"


def test_works_on_anonymous_fn():
    def probe(value: int) -> float:
        return float(value)

    assert param_types(probe) == {"value": int}


def test_empty_signature():
    def noop() -> None:
        return None

    assert param_types(noop) == {}
