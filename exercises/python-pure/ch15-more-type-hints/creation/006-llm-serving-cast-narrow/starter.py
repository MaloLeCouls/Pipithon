"""Une fn reçoit un `dict[str, object]` (JSON parsé). Tu sais (par
contrat avec l'API) que `result["count"]` est un `int`. Mais mypy
voit `object` et refuse les opérations entières.

`cast` te permet de dire « je promets que c'est un int ». À runtime,
c'est invisible — pas de check.

Contrat :

- `parse_count(blob: dict[str, object]) -> int` :
  utilise `cast(int, blob["count"])` puis renvoie-le.

⚠️ `cast` ne convertit PAS — il informe mypy. Si tu passes un dict avec
`count="42"` (str), le test va planter à l'usage (la fn renvoie une str
même si elle est typée int).
"""
from __future__ import annotations

from typing import cast


def parse_count(blob: dict[str, object]) -> int:
    raise NotImplementedError("À implémenter")
