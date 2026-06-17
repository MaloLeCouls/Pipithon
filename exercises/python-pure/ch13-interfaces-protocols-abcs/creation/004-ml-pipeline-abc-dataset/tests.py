import pytest

from solution_user import Dataset, RangeDataset


def test_cannot_instantiate_abstract_dataset():
    with pytest.raises(TypeError):
        Dataset()  # type: ignore[abstract]


def test_range_dataset_len():
    assert len(RangeDataset(5)) == 5


def test_range_dataset_getitem():
    ds = RangeDataset(3)
    assert ds[0] == 0
    assert ds[1] == 2
    assert ds[2] == 4


def test_summary_uses_template_method():
    assert RangeDataset(7).summary() == "Dataset(n=7)"


def test_range_dataset_is_dataset_subclass():
    assert issubclass(RangeDataset, Dataset)


def test_dataset_has_abstractmethods():
    # Vérifie qu'au moins une méthode est marquée abstraite.
    assert Dataset.__abstractmethods__, "Dataset doit avoir des @abstractmethod."
