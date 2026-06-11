import inspect

from solution_user import display_eta


def test_eta_string_returned_verbatim():
    assert display_eta("2026-06-12T10:00") == "2026-06-12T10:00"


def test_none_returns_pending():
    assert display_eta(None) == "pending"


def test_param_annotated_with_optional():
    sig = inspect.signature(display_eta)
    ann = str(sig.parameters["eta"].annotation)
    # str | None ou Optional[str], les deux acceptables.
    assert "None" in ann, f"l'annotation doit mentionner None : {ann}"


def test_return_annotated_str():
    sig = inspect.signature(display_eta)
    ret = sig.return_annotation
    assert ret is str or str(ret) == "str"
