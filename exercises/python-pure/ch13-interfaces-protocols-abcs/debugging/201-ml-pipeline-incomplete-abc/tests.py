from solution_user import WordTokenizer


def test_can_instantiate():
    # Avec le starter, ceci lève TypeError : abstract method `decode` not overridden.
    WordTokenizer()


def test_encode_returns_word_lengths():
    assert WordTokenizer().encode("hello world") == [5, 5]


def test_decode_returns_string():
    out = WordTokenizer().decode([3, 5])
    assert isinstance(out, str)


def test_encode_then_decode_preserves_lengths():
    t = WordTokenizer()
    ids = t.encode("hi everyone")
    decoded = t.decode(ids)
    assert len(decoded.split()) == len(ids)
