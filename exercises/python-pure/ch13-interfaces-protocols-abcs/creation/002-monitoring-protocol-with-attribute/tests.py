from dataclasses import dataclass
from typing import NamedTuple

from solution_user import Named, label


@dataclass
class CPUMetric:
    name: str
    value: float


class MemMetric(NamedTuple):
    name: str
    used_mb: int


def test_label_dataclass():
    assert label(CPUMetric(name="cpu_user", value=0.7)) == "metric:cpu_user"


def test_label_namedtuple():
    assert label(MemMetric(name="mem_rss", used_mb=512)) == "metric:mem_rss"


def test_label_plain_class():
    class Custom:
        def __init__(self, name: str) -> None:
            self.name = name

    assert label(Custom("io_wait")) == "metric:io_wait"


def test_named_declares_name_annotation():
    # Vérifie que `Named` annote bien `name: str` dans son corps.
    # (avec `from __future__ import annotations`, l'annotation est stringifiée)
    assert "name" in Named.__annotations__
    ann = Named.__annotations__["name"]
    assert ann is str or ann == "str"
