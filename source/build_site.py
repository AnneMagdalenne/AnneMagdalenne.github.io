"""Build index.html (the live site) from source/portfolio.html.
source/portfolio.html is the body-only page also used for the Claude artifact preview.
Usage (from the repo root): python3 source/build_site.py https://annemagdalenne.github.io/"""
import sys, re, shutil, pathlib
SRC = pathlib.Path(__file__).with_name('portfolio.html')
OUT = pathlib.Path(__file__).resolve().parent.parent
base = (sys.argv[1].rstrip('/') + '/') if len(sys.argv) > 1 else ''

s = SRC.read_text()
title = re.search(r'<title>(.*?)</title>', s).group(1)
s = re.sub(r'<title>.*?</title>\n', '', s)
s = re.sub(r'<meta name="claude:[^>]*>\n', '', s)
s = re.sub(r'<link [^>]*fonts\.g[^>]*>\n', '', s)
m = re.search(r'<style>.*?</style>\n', s, re.S)
style, body = m.group(0), (s[:m.start()] + s[m.end():]).strip()

desc = ('Project portfolio of Anne Magdalene Helles Borgen: event producer, community builder and '
        'systems thinker. Kaospilot, Team 31. Available for internships from February 2027.')
img = base + 'og-image.jpg'
head = f'''<!doctype html>
<html lang="en" class="is-site">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1B1531">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{f'<link rel="canonical" href="{base}">' if base else ''}
<meta property="og:type" content="website">
<meta property="og:title" content="{title} · Project portfolio">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
{f'<meta property="og:url" content="{base}">' if base else ''}
<meta name="twitter:card" content="summary_large_image">
<style>
@font-face{{font-family:"Schibsted Grotesk";src:url("fonts/schibsted-grotesk-latin-wght-normal.woff2") format("woff2");font-weight:400 900;font-style:normal;font-display:swap}}
@font-face{{font-family:"IBM Plex Mono";src:url("fonts/ibm-plex-mono-latin-400-normal.woff2") format("woff2");font-weight:400;font-style:normal;font-display:swap}}
@font-face{{font-family:"IBM Plex Mono";src:url("fonts/ibm-plex-mono-latin-500-normal.woff2") format("woff2");font-weight:500;font-style:normal;font-display:swap}}
html{{-webkit-text-size-adjust:100%;text-size-adjust:100%}}
body{{margin:0}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
{style}</head>
<body>
{body}
</body>
</html>
'''
head = re.sub(r'\n\n+', '\n', head.replace('\n\n<meta property="og:type"', '\n<meta property="og:type"'))
(OUT / 'index.html').write_text(head)
print('built', OUT, 'base=' + (base or '(relative)'))
