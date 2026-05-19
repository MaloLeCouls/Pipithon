from solution_user import read_header

BOM = b"\xef\xbb\xbf"


def test_with_bom():
    assert read_header(BOM + b"title,author") == "title,author"


def test_without_bom():
    assert read_header(b"title,author") == "title,author"


def test_no_feff_in_result():
    assert "﻿" not in read_header(BOM + b"isbn")


def test_accented_after_bom():
    assert read_header(BOM + "Préface".encode("utf-8")) == "Préface"


def test_empty_with_bom_only():
    # edge : juste un BOM -> chaîne vide
    assert read_header(BOM) == ""
