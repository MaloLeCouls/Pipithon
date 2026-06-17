from solution_user import Dataset


def test_from_csv_basic():
    ds = Dataset.from_csv("1,2,3")
    assert ds.samples == [1, 2, 3]


def test_from_csv_polymorphic():
    class TaggedDataset(Dataset):
        pass

    td = TaggedDataset.from_csv("4,5")
    assert type(td) is TaggedDataset
    assert td.samples == [4, 5]


def test_is_valid_line_true():
    assert Dataset.is_valid_line("1,2,3") is True


def test_is_valid_line_false_for_empty():
    assert Dataset.is_valid_line("") is False


def test_is_valid_line_false_for_garbage():
    assert Dataset.is_valid_line("1,abc,3") is False


def test_is_valid_line_callable_without_instance():
    # staticmethod : on l'appelle sur la classe directement, pas besoin
    # d'instancier ni de passer un `cls` implicite.
    assert Dataset.is_valid_line("7") is True


def test_from_csv_is_classmethod():
    import inspect
    # bound method on the class -> classmethod
    assert inspect.ismethod(Dataset.from_csv)


def test_is_valid_line_is_staticmethod():
    # une staticmethod n'est PAS bound à la classe -> ce n'est pas une method.
    import inspect
    assert not inspect.ismethod(Dataset.is_valid_line)
    assert inspect.isfunction(Dataset.is_valid_line)
