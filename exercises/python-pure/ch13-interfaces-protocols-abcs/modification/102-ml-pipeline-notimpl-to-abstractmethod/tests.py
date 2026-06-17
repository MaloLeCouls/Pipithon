import pytest

from solution_user import BaseTokenizer, CompleteTokenizer, IncompleteTokenizer


def test_complete_tokenizer_encodes():
    assert CompleteTokenizer().encode("ab") == [97, 98]


def test_complete_tokenizer_decodes():
    assert CompleteTokenizer().decode([97, 98]) == "ab"


def test_incomplete_tokenizer_cannot_instantiate():
    """Avec abstractmethod, l'instanciation d'une sous-classe incomplète lève TypeError."""
    with pytest.raises(TypeError):
        IncompleteTokenizer()  # type: ignore[abstract]


def test_base_tokenizer_is_abstract():
    with pytest.raises(TypeError):
        BaseTokenizer()  # type: ignore[abstract]


def test_form_base_tokenizer_uses_abc():
    import abc as abc_mod
    assert issubclass(BaseTokenizer, abc_mod.ABC) or isinstance(
        BaseTokenizer, abc_mod.ABCMeta
    )


def test_form_has_abstractmethods():
    assert BaseTokenizer.__abstractmethods__, \
        "BaseTokenizer doit déclarer des @abstractmethod."
