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
- **Skills table:** a 4 × 2 grid. The first cell is the inverted heading cell (`--text` background); the seven skills each get a cell with a condensed-caps title, a short coral bar, the text and proof chips at the bottom. It becomes two columns on tablets and one on phones.
- **Pass:** the hero signature. It is a white card with a lanyard slot, a coral "All access" strip, the photo and the name and availability. It is tilted −2° on desktop and flat on phones.
- **Running order:** label/value rows with a mono label column. It is used for the hero facts, the projects, Kaospilot and the background.
- **Navigation:** a sticky top bar with the name, section links (hidden on phones) and the EN/DA toggle. The page has a skip link.
- **Footer:** one quiet line.

## Imagery and icons

- Photos are real and unfiltered: the fairground portrait sits in the pass, and the night-street photo sits in About.
- There is no icon set. Markers are small round dots in `--accent`, used like stage lights.

## Work gallery (added with Motion)

- **Projects and sidequests** are two groups, so their different weight is visible. Projects are large dotted cover cards in `blue`, `coral`, `ink` or `paper`, two per row. Sidequests sit below their own "Sidequests" heading as small, quiet `paper` cards, five per row. There are no filters.
- **Opening a card** runs Motion's page wipe: `animateView()` grows a `clip-path` circle from the click point (0.6 s, easeIn) while the card title morphs into the detail title (0.45 s, ease `[0.28, 0.02, 0.1, 0.99]`). Closing reverses this from the close button.
- **The detail view** is a full-screen panel in the card's cover colour. It has a back button, previous/next arrows, and support for the Esc and arrow keys. The rest of the page is made `inert` while it's open.
- **Library:** Motion 13.5.1 (UMD build). The artifact preview loads it from jsDelivr; the live site self-hosts it in `vendor/`. Everything falls back to instant changes without the View Transition API or when reduced motion is on.

## Amplify Live section

The section has three labelled parts, each marked with a lime mono label and a short rule:
1. **The concept:** what Amplify Live is.
2. **What artists get:** the lime band.
3. **What I've learned:** a reflective paragraph, with the key phrase underlined in lime, next to a grid of skill tiles. Each tile shows only its heading. On hover (pointer devices), keyboard focus or tap, the tile turns lime and reveals its description.

## Lessons gallery ("What shaped how I work")

The four lessons form a horizontal scroll-snap gallery of tall cards, using the same cover colours as the work gallery. It has previous/next buttons, and a progress bar driven by Motion's `scroll()` on the track's horizontal scroll. In print it becomes a 2 × 2 grid.
