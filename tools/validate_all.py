"""Valide TOUS les exercices du repo (CI / pre-commit).

A lancer avant tout commit touchant exercises/ (CLAUDE.md S6) :
    python tools/validate_all.py
    python tools/validate_all.py exercises/python-pure/ch01-data-model  # sous-arbre

Un exercice = un dossier contenant meta.yaml. Code 0 si tous OK, 1 sinon.
"""

from __future__ import annotations

import sys
from pathlib import Path

from validate_exercise import validate_exercise

REPO = Path(__file__).resolve().parent.parent


def find_exercises(root: Path) -> list[Path]:
    return sorted(p.parent for p in root.rglob("meta.yaml"))


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else REPO / "exercises"
    if not root.exists():
        print(f"[FAIL] {root} introuvable")
        return 1

    exos = find_exercises(root)
    if not exos:
        print(f"Aucun exercice (meta.yaml) sous {root} - rien a valider.")
        return 0

    total = len(exos)
    print(f"Validation de {total} exercice(s)...", flush=True)
    failed = 0
    for i, exo in enumerate(exos, 1):
        rel = exo.relative_to(REPO).as_posix()
        print(f"  [{i}/{total}] {rel} ... ", end="", flush=True)
        errors = validate_exercise(exo)
        if errors:
            failed += 1
            print("FAIL", flush=True)
            for e in errors:
                print(f"      - {e}", flush=True)
        else:
            print("OK", flush=True)

    print(f"\n{total - failed}/{total} OK"
          + (f" - {failed} ECHEC(S)" if failed else " - tout vert."), flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main(sys.argv))
