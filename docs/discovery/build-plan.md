# Build plan

## Delivery rules

- Tasks are ≤8 points; one task equals one PR.
- Tests and living business logic ship with each task.
- Start with `domain-model.md`, `erd.md`, `decision-log.md`, and `role-module-matrix.md`.

## Sequence

1. Resolve OPEN day-one decisions and catalog REVIEW verdicts.
2. Establish tenancy, authentication, authorization, audit, and storage foundations.
3. Implement entity modules in captured phase order using the inventory below.
4. Add integrations and automation only where captured decisions authorize them.
5. Run QA, security, deployment, and acceptance validation against `graph.json`.

---

## Complete captured-scope implementation inventory

This inventory is generated directly from the graph and contains every captured entity (8). Each row is an independently refinable task that must remain ≤8 points and ship as one PR. Entity fields and all 8 relationships are specified in `domain-model.md` and `erd.md`.

| # | Phase | Entity/module | Owning role | Build task |
|---:|---|---|---|---|
| 1 | MVP | Painting | — | Implement the captured fields, validation, persistence, authorization, and relationships for **Painting**; split before build if it exceeds 8 points. |
| 2 | MVP | Print | — | Implement the captured fields, validation, persistence, authorization, and relationships for **Print**; split before build if it exceeds 8 points. |
| 3 | MVP | CD | — | Implement the captured fields, validation, persistence, authorization, and relationships for **CD**; split before build if it exceeds 8 points. |
| 4 | MVP | Music | — | Implement the captured fields, validation, persistence, authorization, and relationships for **Music**; split before build if it exceeds 8 points. |
| 5 | MVP | Product | admin | Implement the captured fields, validation, persistence, authorization, and relationships for **Product**; split before build if it exceeds 8 points. |
| 6 | MVP | Order | sales | Implement the captured fields, validation, persistence, authorization, and relationships for **Order**; split before build if it exceeds 8 points. |
| 7 | MVP | PrinterNotification | — | Implement the captured fields, validation, persistence, authorization, and relationships for **PrinterNotification**; split before build if it exceeds 8 points. |
| 8 | MVP | Customer | sales | Implement the captured fields, validation, persistence, authorization, and relationships for **Customer**; split before build if it exceeds 8 points. |

## Captured decision and vocabulary gates

- Resolve implementation against all 47 rows in `decision-log.md`.
- Use all 4 terms in `domain-glossary.md` consistently in schema, APIs, and UI copy.
- Validate the 3 captured roles against `role-module-matrix.md` before implementing authorization.
