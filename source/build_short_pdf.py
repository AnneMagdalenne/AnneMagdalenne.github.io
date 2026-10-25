"""Build the condensed 2-page A4 portfolio PDFs (EN + DA) from source/short-portfolio.html.
Needs: pip install segno playwright && python3 -m playwright install chromium
Usage (from the repo root): python3 source/build_short_pdf.py [--png]
Writes Anne-Magdalene-Helles-Borgen-Short-EN.pdf / -DA.pdf in the repo root.
Fails if any page's content is taller than A4."""
import re, sys, pathlib, tempfile
import segno
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
QR = {
    'site': 'https://annemagdalenne.github.io/',
    'linkedin': 'https://www.linkedin.com/in/anne-magdalene-helles-borgen-744077201/',
    'youtube': 'https://www.youtube.com/@amplify__live',
    'ugc': 'https://annemagdalene-ugc.my.canva.site/',
}

html = (SRC / 'short-portfolio.html').read_text()
# Aileron (Amplify Live brand font) is embedded in the main page; reuse that @font-face
aileron = re.search(r'@font-face\{font-family:"Aileron";[^}]*\}', (SRC / 'portfolio.html').read_text()).group(0)
html = html.replace('/*AILERON*/', aileron)
for key, url in QR.items():
    svg = segno.make(url, error='m').svg_inline(border=0, dark='#141418', omitsize=True)
    html = html.replace('{{QR:%s}}' % key, svg)
html = html.replace('<!--BASE-->', '<base href="%s/">' % ROOT.as_uri())

tmp = pathlib.Path(tempfile.mkdtemp()) / 'short.html'
tmp.write_text(html)

ok = True
with sync_playwright() as p:
    browser = p.chromium.launch()
    for lang in ('en', 'da'):
        page = browser.new_page()
        page.goto(tmp.as_uri() + '#' + lang)
        page.emulate_media(media='print')
        page.evaluate('document.fonts.ready')
        page.wait_for_load_state('networkidle')
        report = page.evaluate('''() => [...document.querySelectorAll('.page')].map((pg, i) => {
            pg.querySelectorAll('.contact').forEach(c => c.style.marginTop = '0');
            const pad = parseFloat(getComputedStyle(pg).paddingBottom);
            const bottom = pg.getBoundingClientRect().bottom - pad;
            let max = 0;
            for (const el of pg.children) { if (!el.classList.contains('pfoot')) max = Math.max(max, el.getBoundingClientRect().bottom); }
            pg.querySelectorAll('.contact').forEach(c => c.style.marginTop = '');
            return {page: i + 1, spare_mm: +((bottom - max) / 96 * 25.4).toFixed(1)};
        })''')
        for r in report:
            print(lang.upper(), 'page', r['page'], 'spare', r['spare_mm'], 'mm')
            ok &= r['spare_mm'] >= 0
        out = ROOT / f'Anne-Magdalene-Helles-Borgen-Short-{lang.upper()}.pdf'
        page.pdf(path=str(out), format='A4', print_background=True, prefer_css_page_size=True)
        print('wrote', out.name)
        if '--png' in sys.argv:
            page.set_viewport_size({'width': 794, 'height': 1123})
            page.screenshot(path=str(tmp.parent / f'short-{lang}.png'), full_page=True)
            print('png', tmp.parent / f'short-{lang}.png')
        page.close()
    browser.close()
sys.exit(0 if ok else 1)
