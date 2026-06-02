import os, re

os.chdir('/home/claude/repo')

PAGES = [
    ('site.html',            'site-he.html',           'site-he.html'),
    ('site-brands.html',     'site-brands-he.html',    'site-brands-he.html'),
    ('site-exi.html',        'site-exi-he.html',       'site-exi-he.html'),
    ('site-exi-brands.html', 'site-exi-brands-he.html','site-exi-brands-he.html'),
    ('site-about.html',      'site-about-he.html',     'site-about-he.html'),
    ('site-blog.html',       'site-blog-he.html',      'site-blog-he.html'),
    ('site-contact.html',    'site-contact-he.html',   'site-contact-he.html'),
]

LANG_SWITCH_CSS = """
/* ── Language switcher ── */
.lang-switch {
  font-size: 12px; font-weight: 700;
  padding: 6px 14px; border-radius: 20px;
  border: 1.5px solid rgba(255,106,26,.4);
  color: var(--orange); background: transparent;
  transition: background .15s, color .15s, border-color .15s;
  text-decoration: none; display: inline-flex;
  align-items: center; gap: 5px; line-height: 1;
  white-space: nowrap;
}
.lang-switch:hover { background: var(--orange); color: #fff; border-color: var(--orange); }
.lang-switch-globe { width: 12px; height: 12px; flex-shrink: 0; }
/* Mobile: hide in top nav, show in drawer */
@media(max-width:899px) { nav > .lang-switch { display: none; } }
/* Desktop: show in top nav */
@media(min-width:900px) { .drawer-lang-switch { display: none; } }
"""

GLOBE_SVG = '<svg class="lang-switch-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'

def make_en_switcher(he_url):
    return (f'<a href="{he_url}" class="lang-switch" aria-label="גרסה בעברית">'
            f'{GLOBE_SVG}עברית</a>')

def make_he_switcher(en_url):
    return (f'<a href="{en_url}" class="lang-switch" aria-label="English version">'
            f'{GLOBE_SVG}EN</a>')

def make_drawer_en(he_url):
    return (f'\n    <a href="{he_url}" class="lang-switch drawer-lang-switch" '
            f'style="margin:12px 24px;display:flex;" aria-label="גרסה בעברית">'
            f'{GLOBE_SVG}עברית</a>')

def make_drawer_he(en_url):
    return (f'\n    <a href="{en_url}" class="lang-switch drawer-lang-switch" '
            f'style="margin:12px 24px;display:flex;" aria-label="English version">'
            f'{GLOBE_SVG}EN</a>')

def process(src, dst, label, switcher_nav, switcher_drawer):
    with open(src, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject CSS (only once)
    if 'lang-switch-globe' not in html:
        idx = html.rfind('</style>')
        if idx != -1:
            html = html[:idx] + LANG_SWITCH_CSS + html[idx:]

    # 2. Remove old lang-switch anchors from nav (clean slate)
    html = re.sub(r'\s*<a [^>]*class="lang-switch"[^>]*>.*?</a>', '', html)

    # 3. Inject into top nav — after </nav> last button, before </nav>
    # Strategy A: after nav-login
    if '<a class="nav-login"' in html:
        html = html.replace(
            '</nav>\n\n  <!-- HERO',
            f'{switcher_nav}\n</nav>\n\n  <!-- HERO',
            1
        )
        # also handle no blank line
        if label + '\n</nav>' not in html:
            html = re.sub(
                r'(goToApp\(event\)">(?:Join|הצטרפו)</a>)\s*\n(\s*</nav>)',
                r'\1\n  ' + switcher_nav.strip() + r'\n\2',
                html, count=1
            )
    # Strategy B: replace the empty <div></div> placeholder
    elif '  <div></div>\n</nav>' in html:
        html = html.replace('  <div></div>\n</nav>', f'  {switcher_nav.strip()}\n</nav>', 1)
    # Strategy C: insert before </nav> (fallback)
    else:
        html = re.sub(r'(\s*</nav>)', f'\n  {switcher_nav.strip()}\1', html, count=1)

    # 4. Inject into drawer — before </drawer-foot> or before last </nav> in drawer
    drawer_btn = 'drawer-lang-switch'
    if drawer_btn not in html:
        # Insert before the drawer-foot div
        html = html.replace(
            '<div class="drawer-foot">',
            switcher_drawer + '\n  <div class="drawer-foot">',
            1
        )

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Fixed: {dst}')


for en, he, _ in PAGES:
    # Fix English page
    process(en, en, 'EN',
            make_en_switcher(he),
            make_drawer_en(he))
    # Fix Hebrew page
    process(he, he, 'HE',
            make_he_switcher(en),
            make_drawer_he(en))

print('\nAll done.')
