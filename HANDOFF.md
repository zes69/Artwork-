# Handoff — SaraiB Creative storefront mock

_Written 2026-09-10 at the end of the first design session. Everything below is
verifiable from the repo; nothing depends on the previous conversation._

## Where things stand

The four-page mock is **built, rendered, and pushed** on
`claude/storefront-website-design-3xd2jo`. It reflects:

- The captured spec (8 entities, 47 decisions collapsing to ~10 distinct ones:
  single artist, Square, prints drop-shipped to the hometown print shop with an
  automatic email, originals handled personally, built-in audio player, simple
  admin, auto mailing-list signup for buyers, blues-and-greens mystical brand).
- The **homepage** of saraibcreative.com, merged in for real copy: artist name,
  bio ("The Heart Behind the Art / The Obsession with Color"), nav names
  (Gallery Galaxy, Sacred Sound, Meet SaraiB), the book section with Jenny
  Pizot's testimonial and the geni.us link, Psalm 90:17, the Sept 12 2026 art
  walk, "free shipping on all prints", contact email, social links, and the
  "our circle" partner links.
- Her identity: navy `#031a40`, blue `#104491`, olive-gold accent, over the
  captured greens; Cinzel (display), Josefin Sans (labels), Source Sans 3 (body).

A single-file version of all four pages (client-side page switching) was
published as a shareable Claude artifact; it is regenerated from the four HTML
files, not hand-edited.

## What is still placeholder — and why

Only the homepage of saraibcreative.com was available. Her image CDN
(`img1.wsimg.com`) and the site itself were unreachable from the build
environment. So:

| Pending item | Where it shows | Needs |
|---|---|---|
| Artwork titles, medium, size, price | `gallery.html` (9 cards), `index.html` (3 cards) | Store page (`/saraib-store`) and Gallery Galaxy page (`/gallery-galaxy`) |
| Actual painting images, logo, portrait | every `data-art` element | The `SARAIB CREATIVE_files/` folder from a "Save page as → Complete" export, or CDN access |
| Sacred Sound track list, durations, prices | `music.html`, `index.html` player | Sacred Sound page (`/sacred-sound`) |
| Art walk location and times | `about.html#events` | Event page (`/art-walk`) |
| Returns policy | `about.html#shipping` | Artist |
| Whether the CD + print bundle exists | `music.html` | Artist |

All of these are marked in the UI with `class="pending"` so they are visually
distinct from confirmed content. Search the HTML for `pending` to find them.

## Known facts from the site export (for reference)

- Artist: Bracy "SaraiB" Wevers. Started painting November 2024.
- Email: saraibcreative@gmail.com
- Facebook `bracy.wevers`, Instagram `bracyyourself`, YouTube `@BracySaraiBWevers`
- Book link: https://geni.us/gwGoiC
- Partners ("our circle"): mystic-soul.com, tewaltwebsites.com, caroltewalt.com
- Live site is GoDaddy Website Builder with its built-in store (`?olsPage=cart`).
- Site fonts observed: Source Sans Pro, Josefin Sans, Raleway, Cinzel, Righteous.
- Site colours observed: `#031a40`, `#104491`, `#4d6394`, `#676217`.

## Spec gaps worth resolving before real implementation

These came out of reading the captured spec against the storefront; none are
blockers for the mock, all are blockers for a real build.

1. **Painting, Print, CD and Music have no captured fields** beyond id and
   tenant_id — no title, medium, dimensions, year, image, audio file, edition
   size. The mock invents the display shape; the schema needs these.
2. **No inventory field anywhere.** "Original cannot be restocked" is a glossary
   rule with nothing in the schema to enforce it. Product needs at least
   `is_original` and `quantity`.
3. **Order status values are never enumerated**, and the standard/rush variant
   has no field.
4. **Originals fulfilment contradicts itself** in the decision log: some rows
   say the artist delivers to *customers*, others say to the *print shop* for
   logistics. Pick one.
5. `tenant_id` on every entity for a single-tenant site — decide whether
   multi-tenancy is ever coming back, otherwise drop it.
6. "Free shipping on all prints" is live site policy but not in the decision
   log. Assumed to carry over; confirm.
7. `docs/discovery/` holds the five spec files that were supplied. `domain-model.md`,
   `decision-log.md`, `domain-glossary.md`, `role-module-matrix.md` and `graph.json` referenced by `CLAUDE.md` were **never supplied** — `captured-graph.md` is the closest thing to each.

## Suggested next tasks, in order

1. Ask the owner for the missing spec files named above, or derive `decision-log.md` and `domain-glossary.md` from `captured-graph.md`.

2. When the remaining site pages and image folder arrive: replace every
   `.pending` string and every `data-art` placeholder with real content. Keep
   the `data-kind` attribute on gallery cards — the filter chips depend on it.
3. Resolve spec gaps 1–4 above and write them into `decision-log.md`.
4. Only then start the real build: Square checkout, print-shop email on print
   orders, mailing-list integration, and a simple admin for the artist.

## Environment notes

- No build tooling. Preview: `python3 -m http.server 8000`.
- Screenshots were taken with Playwright + the system Chromium; Google Fonts
  is blocked in headless sandboxes, so renders fall back to system serif. The
  published pages load Cinzel correctly.
- Repo visibility is **public** as of this handoff; the owner intends to make
  it private (GitHub → Settings → Danger Zone).
