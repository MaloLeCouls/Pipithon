from solution_user import format_alert


def test_with_unit_provided():
    result = format_alert({"name": "cpu", "value": 0.7, "unit": "%"})
    assert result == "cpu=0.7%"


def test_without_unit_default_ms():
    # Le starter EXPLOSE avec KeyError ici.
    result = format_alert({"name": "lat", "value": 100.0})
    assert result == "lat=100.0ms"


def test_value_zero():
    result = format_alert({"name": "x", "value": 0.0, "unit": "s"})
    assert "0.0" in result
    assert result.endswith("s")
