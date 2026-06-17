from dataclasses import dataclass

from solution_user import Probe, sample


class CPUProbe:
    def read(self) -> float:
        return 42.5


@dataclass
class MemoryProbe:
    base: float

    def read(self) -> float:
        return self.base + 1.0


def test_sample_works_with_class_implementing_read():
    assert sample(CPUProbe()) == 42.5


def test_sample_works_with_dataclass():
    assert sample(MemoryProbe(base=10.0)) == 11.0


def test_no_inheritance_required():
    """Aucune classe du test n'hérite de `Probe` — c'est la moitié du test."""
    assert Probe not in CPUProbe.__mro__
    # Le vrai test : ça marche, sans avoir hérité.
    assert sample(CPUProbe()) is not None


def test_probe_has_read_method_signature():
    # On vérifie que la signature attendue est bien `read(self) -> float`
    assert hasattr(Probe, "read")


def test_anonymous_object_satisfies_protocol():
    class _Anon:
        def read(self) -> float:
            return -3.14

    assert sample(_Anon()) == -3.14
