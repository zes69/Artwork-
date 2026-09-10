# SaraiB Creative

Six static pages populated from saraibcreative.com on September 10, 2026. Includes 15 gallery paintings, 3 additional homepage artworks, artist biography, book testimonial, three YouTube music videos, media coverage, and art-walk details. Original blue/navy design retained.

## Preview and build

Run `python3 -m http.server 8000` in this folder. Run `python3 scripts/build.py` to validate links, image files and mock removal, then produce deployment files in `dist/`.

The clean paths `/gallery-galaxy`, `/sacred-sound`, `/meet-saraib`, `/media`, and `/art-walk` are also included in the deployment output.

## Source content

`docs/source/` contains archived public HTML, page configuration, and an image URL-to-local-path manifest. The deployed bundle contains only the six pages and their referenced assets, not these snapshots.

`scripts/collect_assets.py` retrieves source artwork. `scripts/import_content.py` rebuilds content from snapshots and needs Beautiful Soup 4. Normal preview and deployment do not require that library.

## Commerce and contact

Shopping links open the existing SaraiB store. The public product API could not be resolved during migration, so prices, titles, availability, and checkout were not invented. Contact and RSVP links open email. New Square checkout, print-shop notifications, a mailing list, and admin remain future work.
