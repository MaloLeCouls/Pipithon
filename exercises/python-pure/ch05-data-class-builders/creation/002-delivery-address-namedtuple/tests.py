import pytest

from solution_user import Address


def test_named_access():
    a = Address("1 rue X", "Paris", "75001")
    assert a.street == "1 rue X"
    assert a.city == "Paris"
    assert a.zip_code == "75001"


def test_is_immutable():
    a = Address("s", "c", "z")
    with pytest.raises(AttributeError):
        a.city = "Lyon"


def test_is_tuple():
    a = Address("s", "c", "z")
    assert tuple(a) == ("s", "c", "z")
    assert a[1] == "c"


def test_unpacking():
    street, city, zip_code = Address("s", "c", "z")
    assert (street, city, zip_code) == ("s", "c", "z")


def test_equality_and_hash():
    # edge : deux adresses égales -> hashables et égales (clé de dict ok)
    a, b = Address("s", "c", "z"), Address("s", "c", "z")
    assert a == b
    assert {a: 1}[b] == 1
