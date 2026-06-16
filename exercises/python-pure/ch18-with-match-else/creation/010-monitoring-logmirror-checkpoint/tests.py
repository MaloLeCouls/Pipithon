import pytest

from solution_user import LogMirror, log_mirror


def test_class_form_yields_label():
    with LogMirror() as label:
        assert label == "MIRROR"


def test_class_form_reverses_print(capsys):
    with LogMirror():
        print("hello", end="")
    out = capsys.readouterr().out
    assert out == "olleh"


def test_class_form_restores_stdout_after(capsys):
    with LogMirror():
        pass
    print("normal", end="")
    out = capsys.readouterr().out
    assert out == "normal"


def test_class_form_restores_stdout_after_exception(capsys):
    with pytest.raises(RuntimeError):
        with LogMirror():
            raise RuntimeError("boom")
    print("after", end="")
    out = capsys.readouterr().out
    assert out == "after"


def test_class_form_swallows_zero_division(capsys):
    # Pas de raise observé côté appelant.
    with LogMirror():
        _ = 1 / 0
    out = capsys.readouterr().out
    assert out == "RECOVERED"


def test_gen_form_yields_label():
    with log_mirror() as label:
        assert label == "MIRROR"


def test_gen_form_reverses_print(capsys):
    with log_mirror():
        print("world", end="")
    out = capsys.readouterr().out
    assert out == "dlrow"


def test_gen_form_swallows_zero_division(capsys):
    with log_mirror():
        _ = 1 / 0
    out = capsys.readouterr().out
    assert out == "RECOVERED"


def test_gen_form_restores_after_other_exception(capsys):
    with pytest.raises(RuntimeError):
        with log_mirror():
            raise RuntimeError("boom")
    print("ok", end="")
    out = capsys.readouterr().out
    assert out == "ok"
