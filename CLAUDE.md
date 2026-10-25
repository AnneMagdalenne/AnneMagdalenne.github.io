# Portfolio site: how to work here

- Live site: https://annemagdalenne.github.io (GitHub Pages, deploys automatically from `main`, root folder).
- **Edit `source/portfolio.html`, never `index.html` by hand.** It is the body-only page (no doctype/head) that is also published as the Claude artifact preview.
- Rebuild the site after every edit: `python3 source/build_site.py https://annemagdalenne.github.io/` (writes `index.html` with head, meta tags and self-hosted fonts).
- The page is bilingual: every visible text exists twice, as `lang="en"` and `lang="da"` siblings. Change both.
- The downloadable PDFs are a one-page CV (`Anne-Magdalene-Helles-Borgen-CV-EN/DA.pdf`), not a print of the site. Source: `source/short-portfolio.html` (both languages, `#en` / `#da`). Rebuild with `python3 source/build_short_pdf.py` (needs `segno` and Playwright); it fails if a page overflows A4. Update it when CV-relevant content on the site changes.
- Design: the "Backstage pass" system in `DESIGN.md`; use its tokens and components. Fonts (Archivo, IBM Plex Mono) and Motion (`vendor/`) are self-hosted on the live site, so there are no third-party requests. Images: `portrait-fair.jpg`, `night.jpg`, `og-image.jpg` (1200×630 share preview).
- Owner preferences: plain, direct, non-academic copy; professional look; Amplify Live section uses its brand colours (lime #D1FF00, near-black #181818, white).

## Version control workflow (required for every change)

`main` is the live website. **Claude never commits or pushes to `main`.** Every change goes through a branch and a pull request, and Anne decides what reaches `main`.

### Roles

- **Claude** creates the branch, makes the change, rebuilds, checks, pushes and opens the pull request. Claude also fixes review feedback on the same branch.
- **Anne** reviews the pull request (and the artifact preview), asks for changes, and merges it into `main`. Merging is what publishes the change.

### Steps for each change

1. **Start from the latest `main`.**
   `git fetch origin && git switch main && git pull --ff-only origin main`
2. **Create a branch** named `<type>/<short-description>` in lowercase with dashes:
   - `content/` for text, photos and new projects
   - `design/` for colours, layout and typography
   - `feature/` for new sections and interactions (e.g. animations)
   - `fix/` for something broken
   - `docs/` for these notes, README, DESIGN.md
   - `experiment/` for try-outs that may never be merged (see below)

   Example: `git switch -c content/update-amplify-text`
3. **Make the change** in `source/portfolio.html` (and assets). Then, in the same branch:
   - rebuild `index.html` with `source/build_site.py`;
   - regenerate the PDFs if visible content changed;
   - check the page in a browser (phone and desktop, EN and DA, no console errors).

   `main` must always be ready to go live, so the built files travel with the change.
4. **Commit** in small, logical commits with a short imperative message ("Update Amplify Live intro", not "changes"). End every message with the attribution lines the session asks for.
5. **Push the branch:** `git push -u origin <branch>`.
6. **Open a pull request** into `main`. The title is a plain summary. The description covers:
   - **What changed** and why, in plain words.
   - **How it was checked** (devices, languages).
   - **Preview:** the artifact link, updated to this branch's version.
   - Anything Anne needs to decide.
7. **Update the artifact preview** (https://claude.ai/artifact/JZamhp6SXVSW17XeCXKmJF) from the branch's `source/portfolio.html`, so Anne can see the change before merging. Note that the artifact shows the branch under review, not necessarily `main`.
8. **Review:** Anne comments on the pull request or the artifact. Claude pushes fixes as new commits to the same branch. Never open a new pull request for review fixes.
9. **Merge (Anne):** use **"Squash and merge"**, so `main` gets one clean commit per change, then delete the branch. GitHub Pages republishes within a few minutes.
10. **After the merge (Claude):** update local `main`, confirm the live site shows the change, and delete the local branch.

### Rules

- One topic per branch and pull request. Don't bundle unrelated changes.
- If two pull requests are open and one is merged, rebase the other on the new `main` before it is merged: `git fetch origin && git rebase origin/main`, then push with `git push --force-with-lease`. Force-pushing is only ever allowed on Claude's own feature branches, never on `main`.
- Never rewrite history on `main`, and never merge a pull request on Anne's behalf unless she explicitly asks for that specific one.
- If a merged change needs undoing, use a new branch with `git revert`, through a pull request like everything else.
- **Experiments**, such as the "Backstage Pass" redesign, live on `experiment/...` branches and are only merged into `main` if Anne explicitly decides so.
- Files that are only working material (screenshots, zips, drafts) don't belong in the repository, which is public.
