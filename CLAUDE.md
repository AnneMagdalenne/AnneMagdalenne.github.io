# Portfolio site: how to work here

- Live site: https://annemagdalenne.github.io (GitHub Pages, deploys from `main`, root folder).
- **Edit `source/portfolio.html`, never `index.html` by hand.** It is the body-only page (no doctype/head) that is also published as the Claude artifact preview.
- Rebuild the site after every edit: `python3 source/build_site.py https://annemagdalenne.github.io/` (writes `index.html` with head, meta tags and self-hosted fonts).
- The page is bilingual: every visible text exists twice, as `lang="en"` and `lang="da"` siblings. Change both.
- The downloadable PDFs are a one-page CV (`Anne-Magdalene-Helles-Borgen-CV-EN/DA.pdf`), not a print of the site. Source: `source/short-portfolio.html` (both languages, `#en` / `#da`). Rebuild with `python3 source/build_short_pdf.py` (needs `segno` and Playwright); it fails if a page overflows A4. Update it when CV-relevant content on the site changes.
- Design: the "Backstage pass" system in `DESIGN.md`; use its tokens and components. Fonts (Archivo, IBM Plex Mono) and Motion (`vendor/`) are self-hosted on the live site, so there are no third-party requests. Images: `portrait-fair.jpg`, `night.jpg`, `og-image.jpg` (1200×630 share preview).
- Owner preferences: plain, direct, non-academic copy; professional look; Amplify Live section uses its brand colours (lime #D1FF00, near-black #181818, white).
