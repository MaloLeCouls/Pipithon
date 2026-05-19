from solution_user import decode_label


def test_ascii():
    assert decode_label(b"BOX-1") == "BOX-1"


def test_accented_latin1_no_crash():
    # 'é' en latin-1 = octet 0xE9
    assert decode_label(b"Caf\xe9") == "Café"


def test_other_latin1_chars():
    assert decode_label(b"Z\xfcrich") == "Zürich"


def test_returns_str():
    assert isinstance(decode_label(b"\xe9"), str)


def test_empty_edge():
    assert decode_label(b"") == ""
