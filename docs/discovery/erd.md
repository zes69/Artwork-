# Entity relationship diagram — Artwork sales website

This diagram contains every captured entity (8) and relationship (8).

```mermaid
erDiagram
  E1_Painting {
    uuid id
    uuid tenant_id
  }
  E2_Print {
    uuid id
    uuid tenant_id
  }
  E3_CD {
    uuid id
    uuid tenant_id
  }
  E4_Music {
    uuid id
    uuid tenant_id
  }
  E5_Product {
    uuid id
    uuid tenant_id
    text sku
    text name
    numeric_12_2_ price
  }
  E6_Order {
    uuid id
    uuid tenant_id
    uuid customer_id
    text status
    numeric_12_2_ total
    timestamptz created_at
  }
  E7_PrinterNotification {
    uuid id
    uuid order_id
    timestamptz sent_at
    text printer_email
  }
  E8_Customer {
    uuid id
    uuid tenant_id
    text name
    text email
    text phone
    timestamptz created_at
    timestamptz deleted_at
  }
  E1_Painting }o--|| E5_Product : "represents"
  E2_Print }o--|| E5_Product : "represents"
  E3_CD }o--|| E5_Product : "represents"
  E2_Print }o--|| E1_Painting : "reproduced_from"
  E3_CD ||--o{ E4_Music : "contains"
  E6_Order ||--o{ E5_Product : "contains"
  E7_PrinterNotification }o--|| E6_Order : "notifies about"
  E6_Order }o--|| E8_Customer : "placed by"
```

## Name legend

| Diagram identifier | Captured entity |
|---|---|
| `E1_Painting` | Painting |
| `E2_Print` | Print |
| `E3_CD` | CD |
| `E4_Music` | Music |
| `E5_Product` | Product |
| `E6_Order` | Order |
| `E7_PrinterNotification` | PrinterNotification |
| `E8_Customer` | Customer |

## Relationship inventory

| # | Source | Kind | Target | Label |
|---:|---|---|---|---|
| 1 | Painting | belongs_to | Product | represents |
| 2 | Print | belongs_to | Product | represents |
| 3 | CD | belongs_to | Product | represents |
| 4 | Print | belongs_to | Painting | reproduced_from |
| 5 | CD | has_many | Music | contains |
| 6 | Order | has_many | Product | contains |
| 7 | PrinterNotification | belongs_to | Order | notifies about |
| 8 | Order | belongs_to | Customer | placed by |
