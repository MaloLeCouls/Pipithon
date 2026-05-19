---
chapter: 11
title: "A Pythonic Object"
fluent_python_pages: "363-396"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [1, 6]
---

## Concepts clés (à drill)
- `__repr__` vs `__str__` ; `classmethod` vs `staticmethod`
- `__format__` + mini-langage de format (`format(obj, '.3f')`, f-strings)
- Rendre une classe **hashable** : `__hash__` + `__eq__` cohérents, attributs read-only
- Attributs « privés » : `_x` (convention) vs `__x` (name mangling)
- `__slots__` : économie mémoire, restrictions (pas de `__dict__`, héritage)
- Class attribute vs instance attribute (override par instance)

## Pièges classiques
- `__hash__` redéfini sans `__eq__` (ou inverse) → set/dict cassés
- Objet hashable mais mutable → corruption de set/dict après mutation
- `__slots__` mais on assigne un attribut non déclaré → `AttributeError`
- `__slots__` non répété en sous-classe → `__dict__` réapparaît
- Mutable class attribute partagé (ex. `tags = []` au niveau classe)
- `classmethod` utilisé là où `staticmethod` suffit (ou inverse)

## Thèmes recommandés
`furniture`, `library`, `ecommerce`, `tasks` (objets-valeur hashables : clé de
set/dict). Varier le thème pour drilller `__hash__` (cf. `pedagogy.md` §3).

## Référence « checkpoint » niveau 5
Reproduire **`Vector2d`** complet : `__repr__`/`__str__`, `__eq__`/`__hash__`,
`__abs__`/`__bool__`, `__format__`, `classmethod frombytes`, `__slots__` — cf.
`fluentpython/example-code-2e` dossier `11-pythonic-obj`.

## Lien PyMistral
`pymistral_link: null`. Thèmes ML *fake* autorisés (chap. ≥ 8) ; objets
hashables = lecture courante de PRs vLLM/transformers (`mapping-mistral.md` C1).
