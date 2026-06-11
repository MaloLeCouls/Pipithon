"""Valide un exercice du dojo pipithon.

Contrat (cf. docs/exercise-format.md §8, INIT_PROMPT.md §6) :

1. meta.yaml parse et est conforme au schema.
2. solution.py chargee comme module `solution_user` -> pytest 100% vert.
3. starter.py chargee comme `solution_user` -> pytest DOIT echouer
   (creation/debugging : pas de solution dans le starter / bug present ;
    modification : les tests de forme ast/mypy echouent).

Usage :
    python tools/validate_exercise.py exercises/python-pure/ch01-data-model/creation/001-...
Sortie : code 0 si OK, 1 sinon. Messages explicites.

Note : la doc mentionne `uv run python ...` ; `python ...` direct fonctionne
aussi (uv n'est qu'un wrapper d'environnement).
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

THEME_SLUGS = {
    # concrets (chap. 1-7+)
    "furniture", "delivery", "ecommerce", "gym", "library",
    "restaurant", "clinic", "payroll", "streaming", "tasks",
    # ML fake (chap. 8+)
    "llm-serving", "ml-pipeline", "monitoring", "gpu-cluster",
}
TYPES = {"creation", "modification", "debugging"}
COUNTER_RANGE = {
    "creation": (1, 99),
    "modification": (101, 199),
    "debugging": (201, 299),
}
ID_RE = re.compile(r"^ch(\d{2})-(\d{3})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
REQUIRED = [
    "id", "chapter", "chapter_slug", "type", "difficulty",
    "estimated_minutes", "concepts", "theme", "title",
    "short_description", "hints", "reference_book", "pymistral_link", "tags",
]


def _fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def validate_meta(meta: dict, exo_dir: Path, errors: list[str]) -> None:
    for key in REQUIRED:
        if key not in meta:
            _fail(errors, f"meta.yaml: champ obligatoire manquant `{key}`")
    if errors:
        return

    m = ID_RE.match(str(meta["id"]))
    if not m:
        _fail(errors, f"meta.yaml: `id` invalide ({meta['id']!r}) "
                      f"-> attendu chNN-CCC-slug")
        return
    id_chap, id_counter, id_slug = int(m.group(1)), int(m.group(2)), m.group(3)

    if not isinstance(meta["chapter"], int) or not 1 <= meta["chapter"] <= 24:
        _fail(errors, "meta.yaml: `chapter` doit etre un int 1-24")
    if meta["chapter"] != id_chap:
        _fail(errors, f"meta.yaml: `chapter` ({meta['chapter']}) != prefixe id ({id_chap})")

    if meta["type"] not in TYPES:
        _fail(errors, f"meta.yaml: `type` doit etre dans {sorted(TYPES)}")
    else:
        lo, hi = COUNTER_RANGE[meta["type"]]
        if not lo <= id_counter <= hi:
            _fail(errors, f"meta.yaml: compteur {id_counter:03d} hors range "
                          f"{meta['type']} ({lo}-{hi})")

    if not isinstance(meta["difficulty"], int) or not 1 <= meta["difficulty"] <= 5:
        _fail(errors, "meta.yaml: `difficulty` doit etre un int 1-5")
    if not isinstance(meta["estimated_minutes"], int) or meta["estimated_minutes"] <= 0:
        _fail(errors, "meta.yaml: `estimated_minutes` doit etre un int > 0")

    if not isinstance(meta["concepts"], list) or not meta["concepts"]:
        _fail(errors, "meta.yaml: `concepts` doit etre une liste non vide")
    if meta["theme"] not in THEME_SLUGS:
        _fail(errors, f"meta.yaml: `theme` ({meta['theme']!r}) inconnu "
                      f"(cf. docs/themes.md)")

    hints = meta["hints"]
    if not isinstance(hints, list) or not 1 <= len(hints) <= 3:
        _fail(errors, "meta.yaml: `hints` doit etre une liste de 1 a 3 elements")

    pml = meta["pymistral_link"]
    if pml is not None and not isinstance(pml, str):
        _fail(errors, "meta.yaml: `pymistral_link` doit etre null ou une "
                      "string (dotted-path, ex. 'pymistral.sampling') - "
                      "cf. docs/context/pymistral-link.md")

    if not isinstance(meta["tags"], list) or not meta["tags"]:
        _fail(errors, "meta.yaml: `tags` doit etre une liste non vide")

    # Coherence id <-> arborescence
    folder = exo_dir.name
    if folder != f"{id_counter:03d}-{id_slug}":
        _fail(errors, f"dossier `{folder}` != `{id_counter:03d}-{id_slug}` (id)")
    if exo_dir.parent.name != meta["type"]:
        _fail(errors, f"dossier type `{exo_dir.parent.name}` != meta.type "
                      f"`{meta['type']}`")
    ch_dir = exo_dir.parent.parent.name
    if not ch_dir.startswith(f"ch{id_chap:02d}-"):
        _fail(errors, f"dossier chapitre `{ch_dir}` incoherent avec id")
    if ch_dir != f"ch{id_chap:02d}-{meta['chapter_slug']}":
        _fail(errors, f"dossier chapitre `{ch_dir}` != "
                      f"`ch{id_chap:02d}-{meta['chapter_slug']}`")


RUN_TIMEOUT_S = 20  # un starter buggé peut boucler (itération via __getitem__) :
                    # le timeout le traite comme "echoue", ce qui est l'attendu.

# Racine du framework pymistral (paquet Python pur, fil rouge ch1-21).
# Copié dans le tmpdir pour que `from pymistral import ...` marche dans les
# tests, sans installer le paquet.
_REPO_ROOT = Path(__file__).resolve().parent.parent
_PYMISTRAL_PKG = _REPO_ROOT / "exercises" / "_pymistral" / "pymistral"


def run_pytest(exo_dir: Path, impl: str) -> tuple[bool, str]:
    """Lance tests.py avec `impl` (solution.py|starter.py) monte comme
    module solution_user. Retourne (tests_passent, sortie).

    Un dépassement de RUN_TIMEOUT_S => (False, ...) : un code qui ne
    termine pas N'EST PAS un code qui passe les tests."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        shutil.copy(exo_dir / "tests.py", tmp_path / "tests.py")
        shutil.copy(exo_dir / impl, tmp_path / "solution_user.py")
        if _PYMISTRAL_PKG.is_dir():
            shutil.copytree(_PYMISTRAL_PKG, tmp_path / "pymistral")
        try:
            proc = subprocess.run(
                [sys.executable, "-m", "pytest", "tests.py", "-q",
                 "-p", "no:cacheprovider"],
                cwd=tmp_path, capture_output=True, text=True,
                timeout=RUN_TIMEOUT_S,
            )
        except subprocess.TimeoutExpired:
            return False, (f"TIMEOUT > {RUN_TIMEOUT_S}s en chargeant {impl} "
                           f"(boucle infinie probable : __getitem__ qui ne "
                           f"lève jamais IndexError ?).")
        return proc.returncode == 0, proc.stdout + proc.stderr


def validate_exercise(exo_dir: Path) -> list[str]:
    errors: list[str] = []
    for fname in ("meta.yaml", "starter.py", "solution.py", "tests.py"):
        if not (exo_dir / fname).is_file():
            _fail(errors, f"fichier manquant : {fname}")
    if errors:
        return errors

    try:
        meta = yaml.safe_load((exo_dir / "meta.yaml").read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"meta.yaml: YAML invalide : {e}"]
    if not isinstance(meta, dict):
        return ["meta.yaml: racine doit etre un mapping"]

    validate_meta(meta, exo_dir, errors)
    if errors:
        return errors

    sol_ok, sol_out = run_pytest(exo_dir, "solution.py")
    if not sol_ok:
        _fail(errors, "solution.py NE PASSE PAS pytest (exo bugue) :\n"
                      + _tail(sol_out))

    start_ok, start_out = run_pytest(exo_dir, "starter.py")
    if start_ok:
        _fail(errors, f"starter.py PASSE pytest alors que type="
                      f"{meta['type']} -> le starter contient deja la "
                      f"solution / aucun bug / refactor deja fait :\n"
                      + _tail(start_out))
    return errors


def _tail(text: str, n: int = 25) -> str:
    lines = text.strip().splitlines()
    return "\n".join("  | " + ln for ln in lines[-n:])


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python tools/validate_exercise.py <dossier-exo>")
        return 2
    exo_dir = Path(argv[1]).resolve()
    if not exo_dir.is_dir():
        print(f"[FAIL] {exo_dir} : pas un dossier")
        return 1
    errors = validate_exercise(exo_dir)
    rel = exo_dir.name
    if errors:
        print(f"[FAIL] {rel}")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"[OK]   {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
