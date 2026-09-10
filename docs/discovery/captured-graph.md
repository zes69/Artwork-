# Captured graph — Artwork sales website

The domain graph captured in the Discovery Wizard mapper — entities, relationships, roles, glossary and decisions exactly as mapped, with nothing inferred, elaborated or dropped. This is the source of truth the rest of `docs/discovery/` is built from; `docs/discovery/graph.json` is the machine-readable copy. Generated directly from the capture (no model), so it never drifts from what was actually mapped.

## Entities

### Painting (phase: MVP)
An original artwork created by the artist using oil or watercolor
Fields:
- id: uuid
- tenant_id: uuid

### Print (phase: MVP)
A reproduction of an original artwork
Fields:
- id: uuid
- tenant_id: uuid

### CD (phase: MVP)
A music CD created or curated by the artist
Fields:
- id: uuid
- tenant_id: uuid

### Music (phase: MVP)
Digital audio content that can be played on the website
Fields:
- id: uuid
- tenant_id: uuid

### Product (phase: MVP, owning role: admin)
A catalog item that can be sold.
Fields:
- id: uuid
- tenant_id: uuid
- sku: text
- name: text
- price: numeric(12,2)

### Order (phase: MVP, owning role: sales)
A transaction moving through a lifecycle.
Variants: standard, rush
Fields:
- id: uuid
- tenant_id: uuid
- customer_id: uuid
- status: text
- total: numeric(12,2)
- created_at: timestamptz

### PrinterNotification (phase: MVP)
An automated email notification sent to the local print shop when a print order is received
Fields:
- id: uuid
- order_id: uuid
- sent_at: timestamptz
- printer_email: text

### Customer (phase: MVP, owning role: sales)
A person or company you sell to or serve.
Variants: individual, business
Fields:
- id: uuid
- tenant_id: uuid
- name: text
- email: text (nullable)
- phone: text (nullable)
- created_at: timestamptz
- deleted_at: timestamptz (nullable)

## Relationships

- Painting belongs_to Product ("represents")
- Print belongs_to Product ("represents")
- CD belongs_to Product ("represents")
- Print belongs_to Painting ("reproduced_from")
- CD has_many Music ("contains")
- Order has_many Product ("contains")
- PrinterNotification belongs_to Order ("notifies about")
- Order belongs_to Customer ("placed by")

## Roles

- Artist — Creates and sells paintings, prints, and CDs
- Customer — Visitor who purchases artwork and music
- Printer — Local print shop that fulfills print orders

## Glossary

- Original — One-of-a-kind artwork that cannot be restocked once sold
- Print — Reproduced copy of artwork that can be restocked and resold multiple times
- Drop ship — Send orders directly to a third-party printer (in this case, a local printer in the artist's hometown) rather than fulfilling from inventory
- Print shop — Local printer in the artist's hometown who receives print orders via email and produces prints on-site

## Decisions

- Multi-artist or Single-artist → Single artist only
- Payment processor → Square
- Tenancy → Single artist (not multi-artist marketplace)
- Payment Processing → Square
- Artist Scope → Single artist storefront (not multi-vendor)
- Site Scope → Single artist storefront
- Artist Count → Single artist storefront
- Fulfillment model → Drop ship to local printer
- Scope → Single artist storefront, not a multi-artist marketplace
- Print order fulfillment → Automatic email notification to local printer
- Print fulfillment → Drop ship to local print shop via automated email notification
- Music Playback → Built-in audio player on website
- Fulfillment Model for Prints → Drop ship to local printer via automated email notification
- Fulfillment for Originals → Artist manually delivers originals to printer
- Original Paintings Fulfillment → Artist manually delivers original to printer for logistics coordination
- Print Order Notifications → Automatic email to printer
- Target User → Single artist storefront (not multi-vendor)
- Admin UI Complexity → Simple, non-technical user interface
- Print notification → Automatic email to print shop on print order
- Content management → Artist manages website directly (no intermediary)
- Complexity level → Simple, non-technical interface
- Print Order Notification → Automatic email to printer
- Website Scope → Single artist storefront (not multi-artist marketplace)
- Admin Complexity → Simple, non-technical interface for artist to manage content
- Music Integration → Audio player embedded on website for music showcase and CD sales
- Artist Inventory Model → Drop ship prints to local printer; originals handled personally
- Original artwork fulfillment → Artist personally delivers originals to customers
- Admin access → Artist manages website and inventory herself
- Audience → Single artist storefront, not multi-artist marketplace
- Inventory Model → Drop ship - originals handled by artist, prints sent to local printer
- Website Management → Artist manages her own website
- Site management → Artist manages her own content (artwork, music, pricing)
- Brand aesthetic → Blues and greens, spiritual/hippie/mystical vibe
- Customer Email List → Automatic signup for buyers; optional signup for non-buyers
- Original Handling → Artist manually delivers originals to customers
- Multi-artist Support → Single artist storefront only
- Customer Mailing List → Automatic signup for buyers, open signup for non-buyers
- Target Audience → Single artist storefront (not multi-artist marketplace)
- Mailing List → Automatic signup for buyers, optional signup for non-buyers; tool agnostic (Mailchimp or built-in)
- Print Shop Notifications → Automatic email notifications to printer for print orders
- Mailing list integration → Whatever is easiest (likely third-party service like Mailchimp)
- Customer scope → Single artist storefront, not multi-vendor
- Original fulfillment → Artist manually delivers originals to print shop
- Original Painting Fulfillment → Artist brings original to print shop manually
- Mailing List Management → Integrate with Mailchimp or similar, whatever is easiest
- Admin Interface Complexity → Keep simple and non-technical for artist user
- Tenancy Model → Single artist storefront

## Topic coverage

- Product & Vision (product_vision): covered
- Actors, Roles & Portals (actors_roles): covered
- Tenancy (tenancy): covered
- Domain & Entities (domain_entities): covered
- Lifecycle / States (lifecycle): partial
- Money & Calculations (money_calc): covered
- Documents & E-Sign (documents): covered
- Integrations (integrations): covered
- Data Lifecycle (data_lifecycle): partial
- Industry Idiosyncrasies (idiosyncrasies): covered
- Existing System (existing_system): covered
- Non-Functionals (non_functionals): partial
- Secrets & Credentials (secrets): not_started
- Design System & UX (design_ux): partial
- Verification & Acceptance (verification): not_started
