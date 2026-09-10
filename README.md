# SaraiB Creative — storefront design mock

A four-page static mock of the single-artist storefront described in `docs/discovery/`,
built around the copy and identity of saraibcreative.com (Bracy "SaraiB" Wevers).
Artwork is generated placeholder imagery until the site's image files are supplied.

## Pages

| File | Page | What it covers |
|---|---|---|
| `index.html` | Home | Event strip, "Obsession with Color" hero, gallery teaser, book, Sacred Sound teaser, Psalm 90:17 |
| `gallery.html` | Gallery Galaxy | Originals / prints / sold filters, product cards, fulfilment explainer |
| `music.html` | Sacred Sound | Track player, CD + bundle + download, media links |
| `about.html` | Meet SaraiB | Bio, events/shipping/prints, contact form, verse |

## Design notes

- Palette merges saraibcreative.com (navy `#031a40`, blue `#104491`, olive-gold)
  with the captured blues-and-greens direction. Cinzel display, Josefin Sans
  labels, Source Sans 3 body — the faces her current site uses.
- Anything still marked *pending* in the UI (artwork titles, prices, track list)
  is waiting on the store, Gallery Galaxy and Sacred Sound pages.
- Product cards distinguish **Original** (one of a kind, cannot restock) from
  **Print** (restockable, drop-shipped) per the glossary.
- Copy reflects captured decisions: drop ship to the local print shop, originals
  handled personally by the artist, Square checkout, automatic mailing-list
  signup for buyers with open signup for everyone else.

## Running it

Static files, no build step:

```
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Mock behaviour

`assets/main.js` fakes the interactive parts — deterministic SVG placeholder art,
gallery filters, cart badge, audio player, and form submissions. No backend,
no payments, nothing persisted.
