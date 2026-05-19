---
chapter: 17
title: "Iterators, Generators, and Classic Coroutines"
fluent_python_pages: "587-636"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [2, 7]
---

## Concepts clés (à drill)
- Protocole d'itération : `__iter__`, `__next__`, `StopIteration`
- Iterator vs iterable (un iterator est son propre iterable)
- Générateurs (`yield`) vs iterator écrit à la main
- Generator expressions ; lazy evaluation, pipelines
- `itertools` : `count`, `cycle`, `chain`, `groupby`, `tee`, `accumulate`,
  `compress`, `dropwhile`, `takewhile`, `combinations`, `product`
- `yield from` (délégation à un sous-générateur)
- Coroutines classiques `yield` : `send()`, `throw()`, `close()`

## Pièges classiques
- Classe avec `__next__` mais `__iter__` qui ne retourne pas `self` → non réitérable
- Réutiliser un générateur déjà épuisé (silencieusement vide)
- `tee` puis consommer une branche entièrement → l'autre garde tout en mémoire
- `return` dans un générateur = `StopIteration(value)` (valeur souvent perdue)
- Confondre itérable réutilisable et iterator à usage unique

## Thèmes recommandés
`llm-serving` (streaming de tokens *fake* — cas canonique), `ml-pipeline`
(DataLoader lazy), `monitoring` (Timeseries), `delivery`.

## Référence « checkpoint » niveau 5
Reproduire **`Sentence`** dans ses 3 formes : iterator manuel → générateur →
generator expression (lazy via `re.finditer`) — cf.
`fluentpython/example-code-2e` dossier `17-it-generator`.

## Lien PyMistral
`pymistral_link: null`. **Fondation du streaming** d'inférence
(`mapping-mistral.md` Couche 1 « streaming tokens », tier S). Thème
`llm-serving` *fake* particulièrement pertinent ici.
