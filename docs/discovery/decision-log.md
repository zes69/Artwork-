# Content migration decisions — 2026-09-10

The user requested resuming the repository, scraping saraibcreative.com, and making a site live with its content. Earlier business workflow proposals remain unresolved.

- Preserve the existing static HTML/CSS/JS architecture and navy/blue brand.
- Source pages and public page configuration are archived under `docs/source/`. Asset URLs are mapped to downloaded local files in `assets.json`.
- Import all 15 Gallery Galaxy paintings, plus the 3 additional artworks on the homepage. Gallery data has no captions; do not turn filenames into confirmed artwork titles, dimensions, prices, or stock states.
- Import the complete homepage biography and testimonial, Meet SaraiB biography/philosophy/style, three Sacred Sound video descriptions and source YouTube IDs, media/exhibition content, and art-walk information.
- Event confirmed: September 12, 2026, 2–6 pm, private residence with address provided on RSVP. No private address is published.
- The public product API host did not resolve. Link to the existing store for shopping; no new checkout, inventory, Square integration, fulfillment automation, mailing list, or admin is represented as operational.
- Replace simulated cart, audio playback, and form success messages with actual destination links, YouTube embeds, and email links. Email links open a visitor's mail app; the new site does not send or store submissions.
- Publish a separate hosted copy initially. Moving the existing domain requires domain access and an explicit cutover decision.
