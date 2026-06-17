from solution_user import Cost


def test_format_default():
    assert format(Cost(1.5)) == "1.5€"


def test_format_with_spec():
    # Le starter EXPLOSE ici avec RecursionError.
    assert format(Cost(1.5), ".2f") == "1.50€"


def test_f_string_basic():
    c = Cost(2.75)
    assert f"{c}" == "2.75€"


def test_f_string_with_spec():
    c = Cost(0.123456)
    assert f"{c:.3f}" == "0.123€"
