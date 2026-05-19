import ast
import inspect

from solution_user import decode_feed

BOM = b"\xef\xbb\xbf"


def test_with_bom():
    assert decode_feed(BOM + b"hello") == "hello"


def test_without_bom():
    assert decode_feed(b"hello") == "hello"


def test_accented():
    assert decode_feed(BOM + "Préface".encode("utf-8")) == "Préface"


def test_uses_utf8_sig():
    tree = ast.parse(inspect.getsource(decode_feed))
    consts = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant)]
    assert "utf-8-sig" in consts, "décode avec le codec utf-8-sig"


def test_empty_and_bom_only():
    # edge
    assert decode_feed(b"") == ""
    assert decode_feed(BOM) == ""
