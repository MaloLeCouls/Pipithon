import gc

from solution_user import Book, build_index


def test_index_contains_all_books_initially():
    books = [Book("978-1", "A"), Book("978-2", "B")]
    idx = build_index(books)
    assert idx["978-1"] is books[0]
    assert idx["978-2"] is books[1]


def test_index_lookup_returns_same_object():
    books = [Book("978-1", "A")]
    idx = build_index(books)
    assert idx["978-1"].title == "A"


def test_index_shrinks_when_books_released():
    books = [Book("978-1", "A"), Book("978-2", "B")]
    idx = build_index(books)
    assert len(idx) == 2
    books.clear()
    gc.collect()
    assert len(idx) == 0


def test_partial_release():
    keep = Book("978-keep", "X")
    drop = Book("978-drop", "Y")
    idx = build_index([keep, drop])
    del drop
    gc.collect()
    assert "978-keep" in idx
    assert "978-drop" not in idx


def test_returns_a_weakref_dict():
    import weakref
    assert isinstance(build_index([]), weakref.WeakValueDictionary)
