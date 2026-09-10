# AGENTS.md — SaraiB Creative storefront

Standing rules for any agent working in this repo. Read `HANDOFF.md` next for
current state and the open task list.

## What this is
A four-page static storefront mock for a single artist, Bracy "SaraiB" Wevers
(saraibcreative.com). Plain HTML/CSS/JS, no build step, no framework.

## Source of truth, in order
1. The user's instructions in the current session.
2. The captured spec in `docs/discovery/` (domain model, decisions, glossary).
   Do not replace captured facts with defaults; record new decisions in
   `docs/discovery/decision-log.md`.
3. The live site's copy and identity (saraibcreative.com) for words, names,
   palette and type.

## Repo layout
- `index.html`, `gallery.html`, `music.html`, `about.html` — the four pages.
  They share header/footer markup; keep them in sync when you change one.
- `assets/styles.css` — the whole design system. Tokens live in `:root`.
- `assets/main.js` — mock behaviour only: placeholder art, nav toggle,
  gallery filters, cart badge, fake player, fake form submits.
- `docs/discovery/` — the captured spec (see HANDOFF.md if missing).

## Conventions
- Static files only. Preview with `python3 -m http.server 8000`.
- Glossary terms are load-bearing: **Original** (one of a kind, never
  restocked), **Print** (restockable, drop-shipped), **Print shop** (the
  hometown printer that receives orders by email), **Drop ship**.
- Sold originals show no buy button and say "Sold — original, not reprinted".
- Anything not yet confirmed by the artist or the site is rendered with the
  `.pending` class in italics. Never invent titles, prices or track names and
  present them as real.
- Placeholder art: any element with `data-art="<seed>"` gets a deterministic
  SVG wash from `main.js`. Replace with `<img>` when real images arrive.
- Payment is Square. Mailing list: buyers auto-enrolled, everyone else opts in.
- Commit messages: imperative subject, a short body explaining why.
- Do not open pull requests unless asked.

## Branch
Work on `claude/storefront-website-design-3xd2jo`. It is currently also the
repo's default branch.
