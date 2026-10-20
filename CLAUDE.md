# Portfolio site: how to work here

- Live site: https://annemagdalenne.github.io (GitHub Pages, deploys from `main`, root folder).
- **Edit `source/portfolio.html`, never `index.html` by hand.** It is the body-only page (no doctype/head) that is also published as the Claude artifact preview.
- Rebuild the site after every edit: `python3 source/build_site.py https://annemagdalenne.github.io/` (writes `index.html` with head, meta tags and self-hosted fonts).
- The page is bilingual: every visible text exists twice, as `lang="en"` and `lang="da"` siblings. Change both.
- PDFs (`Anne-Magdalene-Helles-Borgen-Portfolio-EN/DA.pdf`) are printed from `index.html#en` / `#da` with Chromium (print media, A4, backgrounds on). Regenerate them when content changes.
- Fonts are self-hosted in `fonts/` (no Google Fonts requests). Images: `portrait-fair.jpg`, `night.jpg`, `og-image.jpg` (1200×630 share preview).
- Owner preferences: plain, direct, non-academic copy; professional look; Amplify Live section uses its brand colours (lime #D1FF00, near-black #181818, white).
