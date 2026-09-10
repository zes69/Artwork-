# River & Reed Studio — storefront design mock

A four-page static mock of the single-artist storefront described in `docs/discovery/`.
Placeholder copy and generated placeholder artwork throughout — swap in the official
copy and photography when it lands.

## Pages

| File | Page | What it covers |
|---|---|---|
| `index.html` | Home | Hero, recent work, studio story, album teaser, mailing-list band |
| `gallery.html` | Gallery | Originals / prints / sold filters, product cards, fulfilment explainer |
| `music.html` | Music | Track player, CD + bundle + download products, liner notes |
| `about.html` | About & Contact | Bio, shipping/prints/commissions, contact form, FAQ |

## Design notes

- Palette is the captured brand direction: deep sea blues, moss and sage greens,
  a warm gold accent, warm paper ground. Cormorant Garamond over Inter.
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
