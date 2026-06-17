from solution_user import TokenizerABC


class HasTokenize:
    def tokenize(self, text: str) -> list[str]:
        return text.split()


class NoTokenize:
    def encode(self, text: str) -> list[int]:
        return list(text.encode())


class InheritsTokenize(HasTokenize):
    pass


def test_class_with_tokenize_is_recognized():
    assert isinstance(HasTokenize(), TokenizerABC)


def test_class_without_tokenize_not_recognized():
    assert not isinstance(NoTokenize(), TokenizerABC)


def test_subclass_inherits_recognition():
    assert isinstance(InheritsTokenize(), TokenizerABC)


def test_issubclass_works():
    assert issubclass(HasTokenize, TokenizerABC)
    assert not issubclass(NoTokenize, TokenizerABC)


def test_no_explicit_inheritance():
    """HasTokenize n'a PAS TokenizerABC dans son MRO."""
    assert TokenizerABC not in HasTokenize.__mro__


def test_builtins_are_rejected():
    assert not isinstance(42, TokenizerABC)
    assert not isinstance("hi", TokenizerABC)
