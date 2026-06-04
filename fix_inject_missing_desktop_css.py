#!/usr/bin/env python3
"""Inject desktop nav CSS into pages that are missing it."""
import os
os.chdir('/home/claude/repo')

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

    # Check if desktop nav CSS (with correct grid) is already present
    if 'grid-template-columns: auto 1fr auto' in html:
        print(f'  CLEAN: {fname}')
        continue

    # Find the last </style> in <head> and inject before it
    insert_pos = html.find('</style>')
    if insert_pos == -1:
        print(f'  ERROR (no </style>): {fname}')
        continue

    html = html[:insert_pos] + NEW_DESKTOP_NAV_BLOCK + '\n' + html[insert_pos:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  OK: {fname}')

print('\nDone.')
