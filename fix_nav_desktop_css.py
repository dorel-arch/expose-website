#!/usr/bin/env python3
"""Fix desktop nav CSS across all pages — replace old nav rules and inject dropdown CSS."""
import re, os
os.chdir('/home/claude/repo')

# New dropdown + desktop nav additions to inject
# (injected right before the </style> or at end of nav-related media query)
NEW_DESKTOP_NAV_BLOCK = """
  /* ── Desktop nav (≥ 900px) ── */
  @media (min-width: 900px) {
    .nav { grid-template-columns: auto 1fr auto; padding: 0 56px; height: 64px; }
    .nav-logo { grid-column: 1; justify-self: start; font-size: 21px; }
    .nav-links {
      grid-column: 2; display: flex; align-items: center;
      justify-content: center; gap: 4px;
      font-size: 14px; font-weight: 500; color: var(--ink-2);
    }
    .nav-right { grid-column: 3; gap: 10px; }
    .nav-login { padding: 10px 20px; font-size: 13px; }
    .nav-menu { display: none; }
    .lang-circle { display: inline-flex; }

    .nav-links > a {
      position: relative; padding: 4px 10px; border-radius: 6px;
      transition: color .2s ease;
    }
    .nav-links > a::after {
      content: ''; position: absolute;
      bottom: -2px; left: 10px; right: 10px;
      height: 2px; border-radius: 99px; background: var(--orange);
      transform: scaleX(0); transform-origin: left;
      transition: transform .25s cubic-bezier(.16,1,.3,1);
    }
    .nav-links > a:hover { color: var(--orange); }
    .nav-links > a:hover::after,
    .nav-links > a.active::after { transform: scaleX(1); }
    .nav-links > a.active { color: var(--orange); }

    .nav-dropdown { position: relative; }
    .nav-dd-btn {
      display: flex; align-items: center; gap: 5px;
      font-size: 14px; font-weight: 500; color: var(--ink-2);
      background: none; border: none; cursor: pointer;
      padding: 4px 10px; border-radius: 6px; font-family: inherit;
      line-height: 1.5; transition: color .2s ease; position: relative;
    }
    .nav-dd-btn::after {
      content: ''; position: absolute;
      bottom: -2px; left: 10px; right: 10px;
      height: 2px; border-radius: 99px; background: var(--orange);
      transform: scaleX(0); transform-origin: left;
      transition: transform .25s cubic-bezier(.16,1,.3,1);
    }
    .nav-dd-btn:hover { color: var(--orange); }
    .nav-dd-btn:hover::after, .nav-dd-btn.active::after { transform: scaleX(1); }
    .nav-dd-btn.active { color: var(--orange); }
    .nav-dd-chevron { transition: transform .2s; flex-shrink: 0; }
    .nav-dropdown:hover .nav-dd-chevron,
    .nav-dropdown:focus-within .nav-dd-chevron { transform: rotate(180deg); }
    .nav-dd-menu {
      display: none; position: absolute;
      top: calc(100% + 10px); left: 50%; transform: translateX(-50%);
      background: #fff; border: 1px solid rgba(236,231,226,.9);
      border-radius: 14px; padding: 6px;
      box-shadow: 0 8px 32px rgba(19,19,19,.12), 0 2px 8px rgba(19,19,19,.05);
      min-width: 180px; z-index: 100;
    }
    .nav-dropdown:hover .nav-dd-menu,
    .nav-dropdown:focus-within .nav-dd-menu { display: block; }
    .nav-dd-menu a {
      display: flex; align-items: center; gap: 10px;
      padding: 10px 12px; border-radius: 9px;
      font-size: 13px; font-weight: 600; color: var(--ink-2);
      text-decoration: none; transition: background .12s, color .12s;
      white-space: nowrap;
    }
    .nav-dd-menu a .dd-ico {
      width: 28px; height: 28px; border-radius: 7px;
      background: var(--bg-soft); border: 1px solid var(--line);
      display: grid; place-items: center; flex-shrink: 0; color: var(--gray);
    }
    .nav-dd-menu a:hover { background: var(--orange-soft); color: var(--orange); }
    .nav-dd-menu a:hover .dd-ico { color: var(--orange); border-color: rgba(255,106,26,.2); background: rgba(255,106,26,.1); }
    .nav-dd-menu a.active { background: var(--orange-soft); color: var(--orange); }
    .nav-dd-menu a.active .dd-ico { color: var(--orange); border-color: rgba(255,106,26,.2); background: rgba(255,106,26,.1); }
  }"""

# Patterns for OLD desktop nav CSS to remove/replace
OLD_PATTERNS = [
    # site-he.html, site-brands-he.html, site.html, site-brands.html style (pretty-printed)
    re.compile(
        r'    \.nav \{\s*grid-template-columns: 1fr auto 1fr;.*?\.nav-menu \{ display: none; \}',
        re.DOTALL),
    # site-about, site-blog style (minified in @media block)
    re.compile(
        r'    \.nav\{grid-template-columns:1fr auto 1fr;[^}]+\}\s*\.nav-logo\{grid-column:1;[^}]+\}\s*\.nav-links\{grid-column:2;[^}]+\}.*?\.nav-menu\{display:none\}',
        re.DOTALL),
    # site-exi style
    re.compile(
        r'\.nav\s*\{[^}]*grid-template-columns:1fr auto 1fr[^}]*\}.*?\.nav-menu\s*\{[^}]*display:none[^}]*\}',
        re.DOTALL),
    # site-contact style
    re.compile(
        r'    \.nav\{[^}]*grid-template-columns:1fr auto 1fr[^}]*\}.*?\.nav-menu\{display:none\}',
        re.DOTALL),
]

# Also remove old separate nav-links CSS block (outside media query) if it exists
OLD_NAV_LINKS_CSS = re.compile(
    r'\s*/\* ── Nav link hover indicator ── \*/\s*\.nav-links a \{[^}]+\}[^{]*\.nav-links a::after \{[^}]+\}[^{]*\.nav-links a:hover::after,[^{]*\.nav-links a\.active::after \{ transform: scaleX\(1\); \}',
    re.DOTALL)

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
        print(f'  SKIP: {fname}')
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # 1. Remove old desktop nav CSS
    for pat in OLD_PATTERNS:
        new_html = pat.sub('', html, count=1)
        if new_html != html:
            html = new_html
            changed = True
            break

    # 2. Remove old standalone nav-links underline CSS (if outside media query)
    new_html = OLD_NAV_LINKS_CSS.sub('', html, count=1)
    if new_html != html:
        html = new_html
        changed = True

    # 3. Skip if desktop nav CSS already present
    if 'nav-dd-btn' in html:
        print(f'  SKIP (already done): {fname}')
        continue

    # 4. Inject new desktop nav CSS block before </style>
    # Find the last </style> tag that's in the <head>
    insert_pos = html.find('</style>')
    if insert_pos == -1:
        print(f'  ERROR (no </style>): {fname}')
        continue

    html = html[:insert_pos] + NEW_DESKTOP_NAV_BLOCK + '\n' + html[insert_pos:]
    changed = True

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  OK: {fname}')

print('\nDone.')
