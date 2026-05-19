---
chapter: 6
title: "Object References, Mutability, and Recycling"
fluent_python_pages: "187-220"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [1]
---

## Concepts clés (à drill)
- Variables = labels, pas des boîtes ; sémantique d'affectation
- `is` (identité) vs `==` (égalité) ; `id()`
- Tuple « relativement » immutable (contenu mutable possible)
- `copy.copy` (superficielle) vs `copy.deepcopy` (profonde)
- Aliasing et ses pièges ; passage de paramètres par référence d'objet
- Mutable default argument (le piège canonique)
- GC : reference counting, cycles, `del` (≠ free immédiat)
- `weakref`, `WeakValueDictionary` / `WeakKeyDictionary`
- Interning de petits ints / strings (pourquoi `is` « marche » parfois)

## Pièges classiques
- `def f(x, acc=[])` : `acc` partagé entre appels (mutable default)
- Modifier une liste passée en argument → effet de bord chez l'appelant
- `copy.copy` d'un objet à attributs mutables → partage des sous-objets
- `a is b` vrai par hasard (interning) → croire que `is` teste l'égalité
- `t = (1, [2]); t[1] += [3]` → mute **et** lève `TypeError` (état partiel modifié)

## Thèmes recommandés
`delivery` (routes partagées), `tasks` (assignees), `gym` (bookings),
`furniture` (catalogues copiés).

## Référence « checkpoint » niveau 5
Reproduire **`HauntedBus` / `Bus` + deepcopy** : démontrer mutable default et
copie superficielle vs profonde sur une flotte — cf.
`fluentpython/example-code-2e` dossier `06-obj-ref`.

## Lien PyMistral
Aucun (chap. < 8). `pymistral_link: null`. Thèmes concrets uniquement.
