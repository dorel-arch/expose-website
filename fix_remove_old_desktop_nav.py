#!/usr/bin/env python3
"""Remove old desktop nav CSS blocks (1fr auto 1fr grid) from all pages."""
import re, os
os.chdir('/home/claude/repo')

# Match and remove old desktop nav CSS rules within the 900px media query.
# Pattern covers pretty-printed variants.
# The block starts with .nav { grid-template-columns: 1fr auto 1fr...
# and ends with .nav-menu { display: none; }
OLD_PATTERNS = [
    # Pretty-printed with nav-links a:hover { color... and multi-line nav-login
    re.compile(
        r'    \.nav \{\s*\n\s*grid-template-columns: 1fr auto 1fr;.*?\.nav-menu \{ display: none; \}\n',
        re.DOTALL),
    # Pretty-printed with single-line nav-login
    re.compile(
        r'    \.nav \{\s*\n\s*grid-template-columns: 1fr auto 1fr;.*?\.nav-menu \{ display: none; \}\n',
        re.DOTALL),
    # Minified block
    re.compile(
        r'    \.nav\{grid-template-columns:1fr auto 1fr;[^}]+\}.*?\.nav-menu\{display:none\}\n',
        re.DOTALL),
    # Any remaining variant (fallback)
    re.compile(
        r'\.nav\s*\{[^}]*grid-template-columns:\s*1fr auto 1fr[^}]*\}.*?\.nav-menu\s*\{[^}]*display:\s*none[^}]*\}\n?',
        re.DOTALL),
]

ALL_FILES = [
    'site-he.html', 'site-brands-he.html', 'site-exi-he.html',
    'site-exi-brands-he.html', 'site-about-he.html', 'site-blog-he.html',
    'site-contact-he.html',
    'site.html', 'site-brands.html', 'site-exi.html',
    'site-exi-brands.html', 'site-about.html', 'site-blog.html',
    'site-contact.html',
]

for fname in ALL_FILES:
    if not os.path.exists(fname):
        print(f'  SKIP (missing): {fname}')
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    if '1fr auto 1fr' not in html:
        print(f'  CLEAN: {fname}')
        continue

    changed = False
    for pat in OLD_PATTERNS:
        new_html = pat.sub('', html, count=1)
        if new_html != html:
            html = new_html
            changed = True
            break

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        still_has = '1fr auto 1fr' in html
        print(f'  OK{"  ⚠ still has old!" if still_has else ""}: {fname}')
    else:
        print(f'  WARN (no pattern matched): {fname}')

print('\nDone.')
