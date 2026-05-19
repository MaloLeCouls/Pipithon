---
chapter: 4
title: "Unicode Text versus Bytes"
fluent_python_pages: "111-156"   # approx, éd. 2 O'Reilly 2022
tier: A
status: active
prereqs: [2]
---

## Concepts clés (à drill)
- `str` vs `bytes` vs `bytearray` ; `.encode()` / `.decode()`
- Encodages : UTF-8, UTF-16, latin-1, ASCII ; `errors=` (`replace`, `ignore`, `xmlcharrefreplace`)
- `UnicodeEncodeError` / `UnicodeDecodeError` : lire et corriger
- BOM (byte order mark) et son piège en UTF-16
- `unicodedata` : normalisation NFC/NFD/NFKC/NFKD, case folding
- Égalité canonique (comparer deux str équivalentes Unicode)
- Dual-mode API : fonction qui accepte `str` ou `bytes`

## Pièges classiques
- Comparer deux str « identiques à l'œil » non normalisées → `False`
- Décoder des bytes avec le mauvais codec (UTF-8 vs latin-1) sans erreur visible
- `len()` sur un str avec caractères combinants ≠ ce qu'on croit
- `.upper()` pour comparaison insensible à la casse au lieu de `.casefold()`
- Slicing de `bytes` retourne `int` (un seul) vs `bytes` (tranche)

## Thèmes recommandés
`library` (titres/auteurs multilingues), `clinic`, `streaming` (titres),
`tasks`. Pertinent pour la tokenisation (culture ML), **sans jargon ML** (chap. < 8).

## Référence « checkpoint » niveau 5
Reproduire **`nfc_equal` / `fold_equal`** (comparaison Unicode robuste : NFC +
casefold) — cf. `fluentpython/example-code-2e` dossier `04-text-byte`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Note : la normalisation Unicode est
un prérequis culturel de la tokenisation — exploité plus tard (thème
`ml-pipeline`, chap. ≥ 8).
