# DESIGN.md · Anne Magdalene Helles Borgen portfolio ("Backstage pass")

Direction: the visual language of festival production. That means the all-access pass, the running order and the line-up poster, applied with restraint so the page still reads as a professional CV.
This direction comes from the brief and Anne's own world (events, festivals, Amplify Live), not from studying reference sites; no UXKIN library was connected.

## Color

| Token | Light | Dark | Role |
|---|---|---|---|
| `--bg` | #F4F4F1 | #111114 | Page background |
| `--surface` | #FFFFFF | #1A1A20 | Cards, the pass, popovers on light |
| `--border` | #DCDBD3 | #2F2F38 | Dividers, card outlines |
| `--muted` | #5D5C65 | #A6A5B0 | Secondary text, labels |
| `--text` | #141418 | #F1F0EB | Body text and headings |
| `--primary` | #2B3FD6 | #9AA5FF | Links, primary buttons, focus ring, active states |
| `--on-primary` | #FFFFFF | #111114 | Text on primary fills |
| `--accent` | #FF5A36 | #FF6B4A | The pass strip and small markers only; never body text |
| `--success` | #1F8A4C | #4CC27F | "Available" status dot |

Amplify Live keeps its own brand colors inside its section only: lime #D1FF00, near-black #181818 and white. Its wordmark heading and skill tiles use **Aileron ExtraBold** (CC0, embedded), as Amplify's brand font.
Contrast: text on bg is 17:1, muted on bg is 6.3:1 and primary on bg is 6.9:1 (dark mode is comparable).

## Typography

- **Archivo** (variable, width 62–125, weight 400–900)
  - Display: width 68, weight 800, uppercase, tight tracking (−0.01em). Used for the h1, the h2s and the Amplify title. The condensed caps give it a line-up poster feel.
  - Body: width 100, weight 400/600.
- **IBM Plex Mono** 400/500: labels, durations, years and running-order times. It is uppercase with 0.08em tracking.

| Step | Size / line height | Use |
|---|---|---|
| xs | 12/16 mono | Labels, meta |
| sm | 14/20 | Captions, chips |
| base | 17/27 | Body |
| lg | 20/30 | Leads, pitch |
| xl | 26/30 | h3, item titles |
| 2xl | clamp(34–52)/0.95 | h2, condensed caps |
| display | clamp(52–112)/0.88 | h1, condensed caps |

Body lines are kept at 60–70 characters.

## Spacing

The page uses an 8-based scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
Sections get 128 px of vertical padding on desktop and 72 px on phones. The content width is 1160 px, with a side gutter of at least 16 px.

## Shape and depth

- Radius: 4 for chips, 10 for cards, 18 for the pass and 999 for pills and buttons.
- Shadow: only the pass gets one (`0 24px 48px -16px rgb(20 20 24 / .35)`). Everything else is flat and separated by borders.

## Components

- **Buttons:** primary is a filled `--primary` pill; secondary is a 1.5 px `--text` outline; quiet is an underlined link. All have a 44 px minimum height, a visible 3 px focus ring and lift 1 px on hover.
- **Chips:** proof buttons with a border and a `→`. Clicking or tapping one goes straight to the project: it opens its gallery page, or scrolls to the section. Hover or keyboard focus shows a short preview popover.
- **Skills table:** the static title "What I bring to the table" sits in a sticky column on the left, beside a two-column table of the seven skills. The last skill spans both columns. Each cell has a condensed-caps title, a short coral bar, the text and proof chips at the bottom. On tablets the title moves above the table; on phones the table is one column.
- **Pass:** the hero signature. It hangs from a two-strap lanyard (a V meeting at the slot, like a neck lanyard). It is a white card with a lanyard slot, a coral "All access" strip, the photo and the name and availability. It is tilted −2° on desktop and flat on phones.
- **Running order:** label/value rows with a mono label column. It is used for the hero facts, the projects, Kaospilot and the background.
- **Navigation:** a sticky top bar with the name, section links (hidden on phones) and the EN/DA toggle. The page has a skip link.
- **Footer:** one quiet line.

## Imagery and icons

- Photos are real and unfiltered: the fairground portrait sits in the pass, and the night-street photo sits in About.
- Amplify Live uses its own logo (`img/amplify/amplify-live-logo.svg`, a lime circle with a transparent background) next to the wordmark, plus five concert photos in one row under its live sessions. Photos are saved at 1400 px wide.
- There is no icon set. Markers are small round dots in `--accent`, used like stage lights.

## Work gallery (added with Motion)

- **Projects and sidequests** are two groups, so their different weight is visible. Projects are large dotted cover cards in `coral`, `ink`, `blue` or `soft` (`--primary-soft` with `--primary` text), two per row; a project never uses `paper`, which is reserved for sidequests. Sidequests sit below their own "Sidequests" heading as small, quiet `paper` cards, five per row. There are no filters.
- **Sidequests open in a peek:** a centred card (max 540 px) over a dimmed, blurred backdrop. It grows out of the clicked card with `animateView` and closes on ×, the backdrop or Esc.
- **Project pages** have a header with the title on the left and a photo slot (4:3) beside it, so the photo is visible without scrolling; on phones it stacks above the title. Below the header come 1–2 sentences about the organisation (researched from public sources), then "My role" with Anne's own work, then "Skills" above the skill pills. Sidequest peeks have no organisation intro. Until a photo is added, the slot shows a dashed "Room for a photo" placeholder in the artifact preview only; the live site hides empty slots. To add a photo, put it in `img/projects/<key>.jpg`, replace the placeholder with an `<img>` and add `has-img` to the figure.
- **Opening a card** runs Motion's page wipe: `animateView()` grows a `clip-path` circle from the click point (0.6 s, easeIn) while the card title morphs into the detail title (0.45 s, ease `[0.28, 0.02, 0.1, 0.99]`). Closing reverses this from the close button.
- **The detail view** is a full-screen panel in the card's cover colour. It has a back button, previous/next arrows, and support for the Esc and arrow keys. The rest of the page is made `inert` while it's open.
- **Library:** Motion 13.5.1 (UMD build). The artifact preview loads it from jsDelivr; the live site self-hosts it in `vendor/`. Everything falls back to instant changes without the View Transition API or when reduced motion is on.

## Amplify Live section

The section has four labelled parts, each marked with a lime mono label and a short rule:
1. **The concept:** what Amplify Live is.
2. **What artists get:** the lime band.
3. **Live sessions:** no text, just a lime label with a long arrow pointing at the cards (it points down on small screens). There are three white video cards plus a lime-outlined "All videos" card for the channel, and a row of five photos. The order is chosen so photos from the same concert never sit next to each other.
4. **What I've learned:** a reflective paragraph, with the key phrase underlined in lime, next to a grid of skill tiles. The tiles are compact and show only their heading. On hover (pointer devices), keyboard focus or tap, a tile turns lime and expands to reveal its description, which is written in the "doing" form ("At række ud, koordinere …").

## About me

This is a black band (`#141418`, the same in both themes) with only the rotating lessons (the "About me" heading is kept for screen readers). A photo of Anne sits beside them and cross-fades to a new one with each lesson (`img/about/`). The four lessons show **one at a time** with no boxes: the quote (condensed caps with a coral opening quote mark), a short description, and where it was learned. A lesson changes every 10 s, and only while the section is on screen. The title resolves calmly through a few flickering letters at a time, in a home-made scramble that stands in for Motion+'s paid `scrambleText`, while the description fades in with Motion's `animate`. Four progress bars show the timing and can be clicked. Rotation pauses on hover, on focus, with the pause button, and in a background tab; it stays off with reduced motion. In print, all four lessons show.

## Kaospilot semesters

The Kaospilot and "Other roles and school" section is separated from the gallery by a normal 1 px divider.

The running-order list ends with S6 highlighted in `--accent` (coral) with dark text, with the line "This is the semester still missing a project. Could it be yours?" linking to Contact.
