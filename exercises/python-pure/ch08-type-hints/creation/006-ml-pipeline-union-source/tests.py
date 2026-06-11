import inspect

from solution_user import byte_size


def test_bytes_path():
    assert byte_size(b"hello") == 5


def test_str_path_ascii():
    assert byte_size("hello") == 5


def test_str_path_utf8_multi_byte():
    # 'é' = 2 bytes en UTF-8.
    assert byte_size("café") == 5


def test_param_annotated_union():
    sig = inspect.signature(byte_size)
    ann = str(sig.parameters["source"].annotation)
    assert "str" in ann and "bytes" in ann, f"annotation = {ann}"


def test_return_annotated_int():
    sig = inspect.signature(byte_size)
    ret = sig.return_annotation
    assert ret is int or str(ret) == "int"
