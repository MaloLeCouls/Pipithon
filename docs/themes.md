# themes.md — Thèmes business + vocabulaire

> Extension de `INIT_PROMPT.md` §3.4. Le `theme:` d'un `meta.yaml` est un slug
> de ce fichier. **Toujours du concret métier** — jamais `Foo`/`Bar`/`Animal`.

## Règle d'or de progression (rappel)

- **Chap. 1-7** : thèmes **1-10** uniquement (concrets, quotidiens). Zéro jargon ML.
- **Chap. 8-14** : introduction progressive des thèmes **11-14**.
- **Après chap. 14** : thèmes 11-14 dominants.

---

## Thèmes 1-10 — concrets (chap. 1-7 et au-delà)

### 1. `furniture` — Entreprise de meubles
Classes : `Chair`, `Table`, `Desk`, `Sofa`, `Shelf`, `Order`, `Supplier`,
`Warehouse`, `Catalog`.
Attributs : `ref`, `price`, `stock`, `material`, `width_cm`, `weight_kg`,
`supplier`, `in_stock`.
Verbes : `restock`, `discount`, `assemble`, `ship`, `quote`.
Réfs type : `"A1"`, `"DESK-204"`, `"SOFA-7B"`. Matériaux : `oak`, `pine`,
`steel`, `glass`, `fabric`.

### 2. `delivery` — Livraison / logistique
Classes : `Package`, `Driver`, `Route`, `Address`, `Depot`, `Shipment`,
`Vehicle`.
Attributs : `tracking_id`, `weight_kg`, `eta`, `status`, `zone`, `priority`.
Statuts : `pending`, `picked_up`, `in_transit`, `out_for_delivery`,
`delivered`, `failed`, `returned`.
Verbes : `dispatch`, `assign`, `reroute`, `deliver`, `scan`.

### 3. `ecommerce` — E-commerce simple
Classes : `Product`, `Cart`, `Customer`, `Order`, `LineItem`, `Coupon`,
`Invoice`, `Payment`.
Attributs : `sku`, `unit_price`, `quantity`, `subtotal`, `discount_rate`,
`vat`, `total`.
Verbes : `add_to_cart`, `apply_coupon`, `checkout`, `refund`, `invoice`.

### 4. `gym` — Club de sport / salle
Classes : `Member`, `Subscription`, `GymClass`, `Trainer`, `Booking`,
`Attendance`.
Attributs : `member_id`, `plan`, `start_date`, `expiry`, `capacity`,
`checked_in`.
Plans : `monthly`, `annual`, `student`, `trial`. Verbes : `book`, `cancel`,
`check_in`, `renew`, `freeze`.

### 5. `library` — Bibliothèque
Classes : `Book`, `Author`, `Loan`, `Reader`, `Reservation`, `Branch`.
Attributs : `isbn`, `title`, `due_date`, `copies`, `fine_eur`, `borrowed`.
Verbes : `borrow`, `return_book`, `reserve`, `renew`, `compute_fine`.

### 6. `restaurant` — Restaurant
Classes : `Dish`, `Menu`, `Order`, `Table`, `Reservation`, `Ingredient`,
`Chef`.
Attributs : `dish_id`, `price`, `seats`, `allergens`, `prep_minutes`,
`covers`.
Verbes : `order`, `serve`, `book_table`, `restock_ingredient`, `bill`.

### 7. `clinic` — Cabinet médical
Classes : `Patient`, `Doctor`, `Appointment`, `Prescription`, `Diagnosis`,
`Slot`.
Attributs : `patient_id`, `birth_date`, `specialty`, `scheduled_at`,
`duration_min`. Verbes : `book_slot`, `cancel`, `prescribe`, `diagnose`.
*(Données sensibles : rester factuel, pas de contenu médical réel.)*

### 8. `payroll` — RH / paie
Classes : `Employee`, `Contract`, `Payslip`, `Leave`, `Manager`, `Department`.
Attributs : `emp_id`, `gross`, `net`, `hours`, `tax_rate`, `seniority_years`.
Types contrat : `cdi`, `cdd`, `intern`, `freelance`. Verbes : `compute_net`,
`request_leave`, `approve`, `promote`.

### 9. `streaming` — Plateforme de streaming
Classes : `User`, `Movie`, `Episode`, `Series`, `Watchlist`, `Rating`,
`Recommendation`.
Attributs : `user_id`, `duration_min`, `genre`, `watched`, `score`,
`progress_pct`. Verbes : `watch`, `rate`, `add_to_watchlist`, `recommend`.

### 10. `tasks` — API REST de gestion de tâches
Classes : `Task`, `Project`, `User`, `Tag`, `Sprint`, `Comment`.
Attributs : `task_id`, `status`, `priority`, `deadline`, `assignee`,
`estimate_h`. Statuts : `todo`, `doing`, `review`, `done`, `blocked`.
Verbes : `assign`, `move`, `tag`, `close`, `reopen`.

---

## Thèmes 11-14 — proches métier ML (chap. 8+, dominants après ch. 14)

> ⚠️ Webapp = simulation *fake* (aucun vrai modèle, aucune dépendance ML).
> Du **vocabulaire** métier sur des structures Python pures. **Aucune classe
> PyMistral inventée** tant que le framework n'est pas fourni
> (`context/pymistral-link.md`).

### 11. `llm-serving` — Serveur d'inférence LLM (fake)
Classes : `Token`, `Prompt`, `Response`, `Sampler`, `KVCache`, `Batch`,
`Request`, `Scheduler`.
Attributs : `token_id`, `logprob`, `temperature`, `top_p`, `max_tokens`,
`prompt_len`, `cache_blocks`. Verbes : `tokenize`, `sample`, `batch`,
`evict`, `stream`. Métriques : `ttft_ms`, `itl_ms`, `tokens_per_s`.

### 12. `ml-pipeline` — Pipeline de données ML
Classes : `Dataset`, `Batch`, `Tokenizer`, `Vocabulary`, `DataLoader`,
`Sample`, `Shard`. Attributs : `vocab_size`, `seq_len`, `batch_size`,
`num_workers`, `shuffle`. Verbes : `encode`, `collate`, `shuffle`, `shard`,
`iterate`.

### 13. `monitoring` — Système de monitoring
Classes : `Metric`, `Alert`, `Threshold`, `Dashboard`, `Timeseries`, `Probe`.
Attributs : `name`, `value`, `unit`, `ts`, `severity`, `window_s`.
Sévérités : `info`, `warning`, `critical`. Verbes : `record`, `aggregate`,
`trigger`, `silence`, `rollup`.

### 14. `gpu-cluster` — Cluster GPU / scheduling
Classes : `Job`, `GPU`, `Worker`, `Queue`, `Resource`, `Allocation`, `Node`.
Attributs : `job_id`, `gpus_requested`, `vram_gb`, `priority`, `state`,
`runtime_s`. États : `queued`, `running`, `preempted`, `done`, `failed`.
Verbes : `submit`, `schedule`, `allocate`, `preempt`, `release`.

---

## Recommandation thème ↔ chapitre

`chapter-XX.md` → section « Thèmes recommandés ». Heuristique : varie le thème
entre exos d'un même concept (axe « thème » de la répétition, `pedagogy.md` §3),
en respectant la règle d'or. Ex. `__hash__` (ch 11) : drill sur `furniture`,
`library`, `ecommerce`, `tasks` — pas 8× `furniture`.
