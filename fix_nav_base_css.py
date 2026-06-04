#!/usr/bin/env python3
"""
Fix base (mobile) nav CSS across all pages so Join button and lang-circle
are identical everywhere.
"""
import re, os
os.chdir('/home/claude/repo')

# ── shared CSS snippets (minified) ────────────────────────────────────────────

NAV_RIGHT_BASE  = '.nav-right{grid-column:3;justify-self:end;display:flex;align-items:center;gap:8px}'
NAV_LOGIN_BASE  = '.nav-login{padding:9px 16px;border-radius:8px;background:var(--orange);color:#fff;font-size:12px;font-weight:700;display:inline-flex;align-items:center;gap:6px;box-shadow:0 4px 10px rgba(255,106,26,.28);letter-spacing:.02em;text-decoration:none;white-space:nowrap}'
NAV_LINKS_HIDE  = '.nav-links{display:none}'
LANG_CIRCLE_BASE = '.lang-circle{display:none;width:30px;height:30px;border-radius:50%;align-items:center;justify-content:center;font-size:10px;font-weight:800;letter-spacing:.04em;border:1.5px solid rgba(255,106,26,.4);color:var(--orange);background:transparent;transition:background .15s,color .15s,border-color .15s;text-decoration:none;flex-shrink:0}'

# Pretty-printed equivalents for blog pages
NAV_RIGHT_PP = (
    '  .nav-right {\n'
    '    grid-column: 3; justify-self: end;\n'
    '    display: flex; align-items: center; gap: 8px;\n'
    '  }\n'
)
NAV_LOGIN_PP = (
    '  .nav-login {\n'
    '    padding: 9px 16px; border-radius: 8px;\n'
    '    background: var(--orange); color: #fff;\n'
    '    font-size: 12px; font-weight: 700;\n'
    '    display: inline-flex; align-items: center; gap: 6px;\n'
    '    box-shadow: 0 4px 10px rgba(255,106,26,.28);\n'
    '    letter-spacing: 0.02em; text-decoration: none; white-space: nowrap;\n'
    '  }\n'
)
LANG_CIRCLE_PP = (
    '  .lang-circle {\n'
    '    display: none;\n'
    '    width: 30px; height: 30px; border-radius: 50%;\n'
    '    align-items: center; justify-content: center;\n'
    '    font-size: 10px; font-weight: 800; letter-spacing: 0.04em;\n'
    '    border: 1.5px solid rgba(255,106,26,.4);\n'
    '    color: var(--orange); background: transparent;\n'
    '    transition: background .15s, color .15s, border-color .15s;\n'
    '    text-decoration: none; flex-shrink: 0;\n'
    '  }\n'
    '  .lang-circle:hover { background: var(--orange); color: #fff; border-color: var(--orange); }\n'
)

def base_css(html):
    """Return only the text before the first @media block — the mobile base CSS."""
    m = re.search(r'@media\s*\(', html)
    return html[:m.start()] if m else html

def has_base(html, snippet):
    """True if snippet is in the base (pre-media-query) CSS section."""
    return snippet in base_css(html)


def patch_minified(html):
    """EXi + Contact pages: fully minified nav block, missing most mobile rules."""
    changed = False

    # 1. Fix grid columns
    old_grid = 'grid-template-columns:40px 1fr 40px'
    if old_grid in base_css(html):
        html = html.replace(old_grid, 'grid-template-columns:40px 1fr auto', 1)
        changed = True

    # 2. After .nav-menu{…} inject missing rules (check only base section)
    if not has_base(html, '.nav-right'):
        m = re.search(r'(\.nav-menu\{[^}]+\})', html)
        if m and m.start() < (html.find('@media') or len(html)):
            inject = '\n' + NAV_RIGHT_BASE + '\n' + NAV_LOGIN_BASE + '\n' + NAV_LINKS_HIDE + '\n' + LANG_CIRCLE_BASE
            html = html[:m.end()] + inject + html[m.end():]
            changed = True

    return html, changed


def patch_blog(html):
    """Blog pages: pretty-printed nav block with old grid + nav-login at grid-col:3."""
    changed = False

    # 1. Fix grid
    old = 'display: grid; grid-template-columns: 40px 1fr 40px;'
    if old in base_css(html):
        html = html.replace(old, 'display: grid; grid-template-columns: 40px 1fr auto;', 1)
        changed = True

    # 2. Replace old nav-login (had grid-column:3, wrong padding)
    old_login = (
        '  .nav-login {\n'
        '    grid-column: 3; justify-self: end;\n'
        '    padding: 9px 18px; border-radius: 8px;\n'
        '    background: var(--orange); color: #fff;\n'
        '    font-size: 12px; font-weight: 700;\n'
        '    box-shadow: 0 4px 10px rgba(255,106,26,.28);\n'
        '  }\n'
    )
    if old_login in base_css(html):
        html = html.replace(old_login, NAV_LOGIN_PP, 1)
        changed = True

    # 3. Insert nav-right + lang-circle (if missing from base)
    if not has_base(html, '.nav-right'):
        insert_before = '  .nav-links { display: none; }\n'
        if insert_before in base_css(html):
            html = html.replace(
                insert_before,
                NAV_RIGHT_PP + insert_before + LANG_CIRCLE_PP,
                1
            )
            changed = True

    return html, changed


def patch_about(html):
    """About pages: minified nav with old grid + old nav-login with grid-column:3."""
    changed = False

    # 1. Fix grid
    if 'grid-template-columns:40px 1fr 40px' in base_css(html):
        html = html.replace('grid-template-columns:40px 1fr 40px', 'grid-template-columns:40px 1fr auto', 1)
        changed = True

    # 2. Replace old nav-login (with grid-column:3)
    old_login = '.nav-login{grid-column:3;justify-self:end;padding:9px 18px;border-radius:8px;background:var(--orange);color:#fff;font-size:12px;font-weight:700;box-shadow:0 4px 10px rgba(255,106,26,.28)}'
    if old_login in base_css(html):
        html = html.replace(old_login, NAV_LOGIN_BASE, 1)
        changed = True

    # 3. Add nav-right + lang-circle after .nav-links{display:none} (if missing from base)
    if not has_base(html, '.nav-right'):
        needle = '.nav-links{display:none}'
        if needle in base_css(html):
            html = html.replace(
                needle,
                needle + '\n  ' + NAV_RIGHT_BASE + '\n  ' + LANG_CIRCLE_BASE,
                1
            )
            changed = True

    return html, changed


TASKS = {
    'site-exi.html':           patch_minified,
    'site-exi-brands.html':    patch_minified,
    'site-exi-he.html':        patch_minified,
    'site-exi-brands-he.html': patch_minified,
    'site-contact.html':       patch_minified,
    'site-contact-he.html':    patch_minified,
    'site-blog.html':          patch_blog,
    'site-blog-he.html':       patch_blog,
    'site-about.html':         patch_about,
    'site-about-he.html':      patch_about,
}

for fname, patcher in TASKS.items():
    if not os.path.exists(fname):
        print(f'  SKIP (missing): {fname}')
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    html, changed = patcher(html)
    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        # Quick sanity check
        base = base_css(html)
        ok = all(s in base for s in ['40px 1fr auto', '.nav-right', '.nav-login', '.lang-circle'])
        print(f'  OK{"" if ok else " ⚠ still missing something"}: {fname}')
    else:
        # Check if already clean
        base = base_css(html)
        ok = all(s in base for s in ['40px 1fr auto', '.nav-right', '.nav-login', '.lang-circle'])
        print(f'  {"CLEAN" if ok else "WARN (no match found)"}: {fname}')

print('\nDone.')
