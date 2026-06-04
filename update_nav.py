#!/usr/bin/env python3
"""Update navigation to unified design across all 14 pages."""
import re, os
os.chdir('/home/claude/repo')

# ─── Shared SVG icons ────────────────────────────────────────────────────────
SPARK = '<svg class="spark" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.4 9.6L24 12l-9.6 2.4L12 24l-2.4-9.6L0 12l9.6-2.4z"/></svg>'
ICO_PERSON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
ICO_BRANDS = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>'
ICO_ABOUT  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
ICO_EXI    = SPARK.replace('class="spark"', 'width="15" height="15"')
ICO_PRICE  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'
ICO_BLOG   = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
ICO_MAIL   = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'
ICO_GLOBE  = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'
ICO_CHEVRON = '<svg class="nav-dd-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>'
ICO_CLOSE  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>'
ICO_BURGER = '<svg width="22" height="16" viewBox="0 0 22 16"><path d="M0 1.5h22M0 8h22M0 14.5h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

# ─── New nav CSS (replaces old nav CSS block) ─────────────────────────────────
NEW_NAV_CSS_LIGHT = """  /* ───────── Top nav ───────── */
  .nav {
    position: sticky; top: 0; z-index: 50;
    display: grid; grid-template-columns: 40px 1fr auto;
    align-items: center;
    padding: 14px 18px;
    background: rgba(255,255,255,.85);
    backdrop-filter: saturate(180%) blur(14px);
    -webkit-backdrop-filter: saturate(180%) blur(14px);
    border-bottom: 1px solid rgba(236,231,226,.6);
  }
  .nav-logo {
    grid-column: 2; justify-self: center;
    display: flex; align-items: center; gap: 6px;
    font-weight: 800; font-size: 19px; letter-spacing: 0.01em;
  }
  .nav-logo .spark { width: 14px; height: 14px; color: var(--orange); }
  .nav-menu {
    grid-column: 1; justify-self: start;
    width: 36px; height: 36px;
    display: grid; place-items: center;
    border-radius: 10px; color: var(--ink); background: transparent;
  }
  .nav-right {
    grid-column: 3; justify-self: end;
    display: flex; align-items: center; gap: 8px;
  }
  .nav-login {
    padding: 9px 16px; border-radius: 8px;
    background: var(--orange); color: #fff;
    font-size: 12px; font-weight: 700;
    display: inline-flex; align-items: center; gap: 6px;
    box-shadow: 0 4px 10px rgba(255,106,26,.28);
    letter-spacing: 0.02em; text-decoration: none;
    white-space: nowrap;
  }
  .nav-links { display: none; }
  .lang-circle {
    display: none;
    width: 30px; height: 30px; border-radius: 50%;
    align-items: center; justify-content: center;
    font-size: 10px; font-weight: 800; letter-spacing: 0.04em;
    border: 1.5px solid rgba(255,106,26,.4);
    color: var(--orange); background: transparent;
    transition: background .15s, color .15s, border-color .15s;
    text-decoration: none; flex-shrink: 0;
  }
  .lang-circle:hover { background: var(--orange); color: #fff; border-color: var(--orange); }"""

# Dark nav variant (contact page)
NEW_NAV_CSS_DARK = """  /* ───────── Top nav ───────── */
  .nav {
    position: sticky; top: 0; z-index: 50;
    display: grid; grid-template-columns: 40px 1fr auto;
    align-items: center;
    padding: 14px 18px;
    background: rgba(13,13,13,.82);
    backdrop-filter: saturate(140%) blur(16px);
    -webkit-backdrop-filter: saturate(140%) blur(16px);
    border-bottom: 1px solid rgba(255,255,255,.07);
  }
  .nav-logo {
    grid-column: 2; justify-self: center;
    display: flex; align-items: center; gap: 6px;
    font-weight: 800; font-size: 19px; letter-spacing: 0.01em; color: #fff;
  }
  .nav-logo .spark { width: 14px; height: 14px; color: var(--orange); }
  .nav-menu {
    grid-column: 1; justify-self: start;
    width: 36px; height: 36px;
    display: grid; place-items: center;
    border-radius: 10px; color: #fff; background: transparent;
  }
  .nav-right {
    grid-column: 3; justify-self: end;
    display: flex; align-items: center; gap: 8px;
  }
  .nav-login {
    padding: 9px 16px; border-radius: 8px;
    background: var(--orange); color: #fff;
    font-size: 12px; font-weight: 700;
    display: inline-flex; align-items: center; gap: 6px;
    box-shadow: 0 4px 10px rgba(255,106,26,.28);
    letter-spacing: 0.02em; text-decoration: none;
    white-space: nowrap;
  }
  .nav-links { display: none; }
  .lang-circle {
    display: none;
    width: 30px; height: 30px; border-radius: 50%;
    align-items: center; justify-content: center;
    font-size: 10px; font-weight: 800; letter-spacing: 0.04em;
    border: 1.5px solid rgba(255,106,26,.45);
    color: var(--orange); background: transparent;
    transition: background .15s, color .15s, border-color .15s;
    text-decoration: none; flex-shrink: 0;
  }
  .lang-circle:hover { background: var(--orange); color: #fff; border-color: var(--orange); }"""

# ─── Desktop nav additions (900px+) ──────────────────────────────────────────
DESKTOP_NAV_CSS = """
  @media (min-width: 900px) {
    .nav {
      grid-template-columns: auto 1fr auto;
      padding: 0 56px;
      height: 64px;
    }
    .nav-logo { grid-column: 1; justify-self: start; font-size: 21px; }
    .nav-links {
      grid-column: 2;
      display: flex; align-items: center; justify-content: center; gap: 4px;
      font-size: 14px; font-weight: 500; color: var(--ink-2);
    }
    .nav-right { grid-column: 3; gap: 10px; }
    .nav-login { padding: 10px 20px; font-size: 13px; }
    .nav-menu { display: none; }
    .lang-circle { display: inline-flex; }

    /* Nav link hover underline */
    .nav-links > a {
      position: relative; padding: 4px 10px;
      transition: color .2s ease; border-radius: 6px;
    }
    .nav-links > a::after {
      content: ''; position: absolute;
      bottom: -2px; left: 10px; right: 10px;
      height: 2px; border-radius: 99px;
      background: var(--orange);
      transform: scaleX(0); transform-origin: left;
      transition: transform .25s cubic-bezier(.16,1,.3,1);
    }
    .nav-links > a:hover { color: var(--orange); }
    .nav-links > a:hover::after,
    .nav-links > a.active::after { transform: scaleX(1); }
    .nav-links > a.active { color: var(--orange); }

    /* Dropdown */
    .nav-dropdown { position: relative; }
    .nav-dd-btn {
      display: flex; align-items: center; gap: 5px;
      font-size: 14px; font-weight: 500; color: var(--ink-2);
      background: none; border: none; cursor: pointer;
      padding: 4px 10px; border-radius: 6px;
      font-family: inherit; line-height: 1.5;
      transition: color .2s ease; position: relative;
    }
    .nav-dd-btn::after {
      content: ''; position: absolute;
      bottom: -2px; left: 10px; right: 10px;
      height: 2px; border-radius: 99px;
      background: var(--orange);
      transform: scaleX(0); transform-origin: left;
      transition: transform .25s cubic-bezier(.16,1,.3,1);
    }
    .nav-dd-btn:hover { color: var(--orange); }
    .nav-dd-btn:hover::after,
    .nav-dd-btn.active::after { transform: scaleX(1); }
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
      text-decoration: none;
      transition: background .12s, color .12s; white-space: nowrap;
    }
    .nav-dd-menu a .dd-ico {
      width: 28px; height: 28px; border-radius: 7px;
      background: var(--bg-soft); border: 1px solid var(--line);
      display: grid; place-items: center; flex-shrink: 0;
      color: var(--gray);
    }
    .nav-dd-menu a:hover { background: var(--orange-soft); color: var(--orange); }
    .nav-dd-menu a:hover .dd-ico { color: var(--orange); border-color: rgba(255,106,26,.2); background: rgba(255,106,26,.1); }
    .nav-dd-menu a.active { background: var(--orange-soft); color: var(--orange); }
    .nav-dd-menu a.active .dd-ico { color: var(--orange); border-color: rgba(255,106,26,.2); background: rgba(255,106,26,.1); }
  }"""

# ─── Drawer CSS (mobile) ──────────────────────────────────────────────────────
DRAWER_CSS = """
  /* ── Mobile drawer ── */
  .drawer-overlay {
    display: none; position: fixed; inset: 0; z-index: 200;
    background: rgba(19,19,19,.45); backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px); opacity: 0;
    transition: opacity .25s ease;
  }
  .drawer-overlay.open { display: block; opacity: 1; }
  .drawer {
    position: fixed; top: 0; left: 0; bottom: 0;
    width: min(320px, 85vw); background: #fff; z-index: 201;
    display: flex; flex-direction: column; padding: 0;
    transform: translateX(-100%);
    transition: transform .3s cubic-bezier(.16,1,.3,1);
    box-shadow: 8px 0 40px rgba(19,19,19,.12);
  }
  .drawer.open { transform: translateX(0); }
  [dir="rtl"] .drawer { left: auto; right: 0; transform: translateX(100%); }
  [dir="rtl"] .drawer.open { transform: translateX(0); }
  .drawer-head {
    display: flex; align-items: center; justify-content: space-between;
    padding: 20px 22px; border-bottom: 1px solid var(--line);
  }
  .drawer-logo {
    display: flex; align-items: center; gap: 6px;
    font-weight: 800; font-size: 17px; color: var(--ink);
  }
  .drawer-logo .spark { width: 13px; height: 13px; color: var(--orange); }
  .drawer-close {
    width: 32px; height: 32px; border-radius: 8px;
    display: grid; place-items: center;
    color: var(--gray); background: var(--bg-soft);
    border: 1px solid var(--line);
  }
  .drawer-close:hover { color: var(--ink); }
  .drawer-nav {
    flex: 1; padding: 16px 12px;
    display: flex; flex-direction: column; gap: 2px; overflow-y: auto;
  }
  .drawer-nav a {
    display: flex; align-items: center; gap: 12px;
    padding: 13px 14px; border-radius: 12px;
    font-size: 15px; font-weight: 600; color: var(--ink-2);
    transition: background .15s ease, color .15s ease; text-decoration: none;
  }
  .drawer-nav a:hover { background: var(--bg-soft); color: var(--ink); }
  .drawer-nav a.active { background: var(--orange-soft); color: var(--orange); }
  .drawer-nav a .dn-icon {
    width: 34px; height: 34px; border-radius: 9px;
    background: var(--bg-soft); border: 1px solid var(--line);
    display: grid; place-items: center; flex-shrink: 0; color: var(--gray);
  }
  .drawer-nav a.active .dn-icon { background: rgba(255,106,26,.12); border-color: rgba(255,106,26,.2); color: var(--orange); }
  .drawer-nav a:hover .dn-icon { color: var(--orange); }
  .drawer-divider { height: 1px; background: var(--line); margin: 8px 14px; }
  .drawer-nav .dn-label {
    font-size: 10px; font-weight: 700; letter-spacing: .14em;
    text-transform: uppercase; color: var(--gray-2); padding: 8px 14px 2px;
  }
  .drawer-foot {
    padding: 16px 22px 28px; border-top: 1px solid var(--line);
  }
  .drawer-foot .btn-orange {
    display: flex; align-items: center; justify-content: center;
    width: 100%; padding: 14px; border-radius: 12px;
    background: var(--orange); color: #fff;
    font-size: 14px; font-weight: 700; letter-spacing: .02em;
    box-shadow: 0 4px 14px rgba(255,106,26,.32); text-decoration: none;
  }
  body.drawer-lock { overflow: hidden; }"""

LANG_SWITCH_CSS = """
  /* Language switcher (drawer only on mobile) */
  .drawer-lang-switch {
    font-size: 12px; font-weight: 700; letter-spacing: .04em;
    padding: 6px 14px; border-radius: 20px;
    border: 1.5px solid rgba(255,106,26,.4);
    color: var(--orange); background: transparent;
    transition: background .15s, color .15s, border-color .15s;
    text-decoration: none; display: inline-flex;
    align-items: center; gap: 5px; line-height: 1;
    white-space: nowrap; margin: 12px 24px 4px;
  }
  .drawer-lang-switch:hover { background: var(--orange); color: #fff; border-color: var(--orange); }
  @media(min-width:900px) { .drawer-lang-switch { display: none; } }"""

# ─── Nav HTML builder ─────────────────────────────────────────────────────────
def make_nav_html(active, lang_url, lang_label, lang_aria, he=True, dark=False):
    """Build the top <nav> HTML."""
    join_text = 'הצטרפו' if he else 'Join'
    how_text   = 'איך זה עובד' if he else 'How it works'
    pro_text   = 'בעל מקצוע'  if he else 'For Creatives'
    biz_text   = 'בעל עסק'    if he else 'For Brands'
    about_text = 'מי אנחנו'   if he else 'About Us'
    exi_text   = 'הכירו את EXi'
    price_text = 'תמחור'      if he else 'Pricing'
    pro_url    = 'site-he.html'     if he else 'site.html'
    biz_url    = 'site-brands-he.html' if he else 'site-brands.html'
    about_url  = 'site-about-he.html'  if he else 'site-about.html'
    exi_url    = 'site-exi-he.html'    if he else 'site-exi.html'
    open_lbl   = 'פתח תפריט' if he else 'Open menu'
    nav_aria   = 'ניווט ראשי' if he else 'Main navigation'

    how_active  = ' active' if active in ('creatives','brands') else ''
    pro_active  = ' class="active"' if active == 'creatives' else ''
    biz_active  = ' class="active"' if active == 'brands'    else ''
    abt_active  = ' class="active"' if active == 'about'     else ''
    exi_active  = ' class="active"' if active == 'exi'       else ''

    return f"""  <!-- NAV -->
  <nav class="nav" aria-label="{nav_aria}">
    <button class="nav-menu" id="navMenuBtn" aria-label="{open_lbl}" aria-expanded="false">
      {ICO_BURGER}
    </button>
    <div class="nav-logo">
      {SPARK}
      EXPOSE
    </div>
    <div class="nav-links">
      <div class="nav-dropdown">
        <button class="nav-dd-btn{how_active}" aria-haspopup="true">
          {how_text}
          {ICO_CHEVRON}
        </button>
        <div class="nav-dd-menu">
          <a href="{pro_url}"{pro_active}>
            <span class="dd-ico">{ICO_PERSON}</span>{pro_text}
          </a>
          <a href="{biz_url}"{biz_active}>
            <span class="dd-ico">{ICO_BRANDS}</span>{biz_text}
          </a>
        </div>
      </div>
      <a href="{about_url}"{abt_active}>{about_text}</a>
      <a href="{exi_url}"{exi_active}>{exi_text}</a>
      <a href="#pricing">{price_text}</a>
    </div>
    <div class="nav-right">
      <a class="nav-login" href="#" onclick="goToApp(event)">{join_text}</a>
      <a href="{lang_url}" class="lang-circle" aria-label="{lang_aria}">{lang_label}</a>
    </div>
  </nav>"""

def make_drawer_html(active, lang_url, lang_label, lang_aria, he=True):
    pro_text   = 'בעל מקצוע'  if he else 'For Creatives'
    biz_text   = 'בעל עסק'    if he else 'For Brands'
    how_sec    = 'איך זה עובד' if he else 'How it works'
    about_text = 'מי אנחנו'   if he else 'About Us'
    exi_text   = 'הכירו את EXi'
    price_text = 'תמחור'      if he else 'Pricing'
    blog_text  = 'בלוג'       if he else 'Blog'
    contact_text='צרו קשר'    if he else 'Contact'
    join_text  = 'הצטרפו ל-EXPOSE — חינם' if he else 'Join EXPOSE — Free'
    close_lbl  = 'סגור תפריט' if he else 'Close menu'

    pro_url    = 'site-he.html'         if he else 'site.html'
    biz_url    = 'site-brands-he.html'  if he else 'site-brands.html'
    about_url  = 'site-about-he.html'   if he else 'site-about.html'
    exi_url    = 'site-exi-he.html'     if he else 'site-exi.html'
    blog_url   = 'site-blog-he.html'    if he else 'site-blog.html'
    contact_url= 'site-contact-he.html' if he else 'site-contact.html'

    pro_active  = ' active' if active == 'creatives' else ''
    biz_active  = ' active' if active == 'brands'    else ''
    abt_active  = ' active' if active == 'about'     else ''
    exi_active  = ' active' if active == 'exi'       else ''
    blog_active = ' active' if active == 'blog'      else ''
    con_active  = ' active' if active == 'contact'   else ''

    lang_text = 'English' if he else 'עברית'

    return f"""  <!-- Mobile drawer overlay -->
  <div class="drawer-overlay" id="drawerOverlay" aria-hidden="true"></div>

  <!-- Mobile drawer -->
  <aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="{'ניווט' if he else 'Navigation'}">
    <div class="drawer-head">
      <div class="drawer-logo">
        {SPARK.replace('class="spark"','class="spark"')}
        EXPOSE
      </div>
      <button class="drawer-close" id="drawerClose" aria-label="{close_lbl}">
        {ICO_CLOSE}
      </button>
    </div>
    <nav class="drawer-nav">
      <div class="dn-label">{how_sec}</div>
      <a href="{pro_url}" class="{pro_active.strip() or None}">
        <span class="dn-icon">{ICO_PERSON}</span>
        {pro_text}
      </a>
      <a href="{biz_url}" class="{biz_active.strip() or None}">
        <span class="dn-icon">{ICO_BRANDS}</span>
        {biz_text}
      </a>
      <div class="drawer-divider"></div>
      <a href="{about_url}" class="{abt_active.strip() or None}">
        <span class="dn-icon">{ICO_ABOUT}</span>
        {about_text}
      </a>
      <a href="{exi_url}" class="{exi_active.strip() or None}">
        <span class="dn-icon">{ICO_EXI}</span>
        {exi_text}
      </a>
      <a href="#pricing">
        <span class="dn-icon">{ICO_PRICE}</span>
        {price_text}
      </a>
      <div class="drawer-divider"></div>
      <a href="{blog_url}" class="{blog_active.strip() or None}">
        <span class="dn-icon">{ICO_BLOG}</span>
        {blog_text}
      </a>
      <a href="{contact_url}" class="{con_active.strip() or None}">
        <span class="dn-icon">{ICO_MAIL}</span>
        {contact_text}
      </a>
    </nav>
    <a href="{lang_url}" class="drawer-lang-switch" aria-label="{lang_aria}">
      {ICO_GLOBE}&nbsp;{lang_text}
    </a>
    <div class="drawer-foot">
      <a href="#" onclick="goToApp(event)" class="btn-orange">{join_text}</a>
    </div>
  </aside>"""

# ─── CSS replacement helpers ──────────────────────────────────────────────────
OLD_NAV_CSS_PATTERN = r'/\* ─+\s*Top nav\s*─+ \*/.*?\.nav-cta \{ display: none; \}'
OLD_DRAWER_CSS_PATTERN = r'/\* ─+\s*Mobile drawer\s*─+ \*/.*?body\.drawer-lock \{ overflow: hidden; \}'
OLD_LANG_CSS_PATTERN = r'/\* Language switcher \*/.*?@media\(min-width:900px\) \{ \.drawer-lang-switch \{ display: none; \} \}'

# Also for minified CSS (exi, contact pages)
OLD_NAV_CSS_MINI = r'\.nav\{[^}]+\}[^{]*\.nav-logo\{[^}]+\}[^{]*\.nav-logo \.spark\{[^}]+\}[^{]*\.nav-menu\{[^}]+\}'

OLD_DESKTOP_NAV_PATTERN = r'@media \(min-width: 900px\) \{[^}]*\.nav-logo \{ grid-column: 1;.*?\.nav-menu \{ display: none; \}\s*\}'

def replace_section(html, pattern, replacement, flags=re.DOTALL):
    new_html = re.sub(pattern, replacement, html, count=1, flags=flags)
    if new_html == html:
        return html, False
    return new_html, True

# ─── Per-page config ──────────────────────────────────────────────────────────
PAGES = [
    # (filename, active, lang_url, lang_label, lang_aria, is_he, is_dark)
    ('site-he.html',            'creatives', 'site.html',            'EN', 'English version', True,  False),
    ('site-brands-he.html',     'brands',    'site-brands.html',     'EN', 'English version', True,  False),
    ('site-exi-he.html',        'exi',       'site-exi.html',        'EN', 'English version', True,  False),
    ('site-exi-brands-he.html', 'exi',       'site-exi-brands.html', 'EN', 'English version', True,  False),
    ('site-about-he.html',      'about',     'site-about.html',      'EN', 'English version', True,  False),
    ('site-blog-he.html',       'blog',      'site-blog.html',       'EN', 'English version', True,  False),
    ('site-contact-he.html',    'contact',   'site-contact.html',    'EN', 'English version', True,  True),
    ('site.html',               'creatives', 'site-he.html',         'עב', 'גרסה בעברית',    False, False),
    ('site-brands.html',        'brands',    'site-brands-he.html',  'עב', 'גרסה בעברית',    False, False),
    ('site-exi.html',           'exi',       'site-exi-he.html',     'עב', 'גרסה בעברית',    False, False),
    ('site-exi-brands.html',    'exi',       'site-exi-brands-he.html','עב','גרסה בעברית',   False, False),
    ('site-about.html',         'about',     'site-about-he.html',   'עב', 'גרסה בעברית',    False, False),
    ('site-blog.html',          'blog',      'site-blog-he.html',    'עב', 'גרסה בעברית',    False, False),
    ('site-contact.html',       'contact',   'site-contact-he.html', 'עב', 'גרסה בעברית',    False, True),
]

# ─── Process each page ────────────────────────────────────────────────────────
def clean_class_none(html):
    """Remove class="None" artifacts from template."""
    html = html.replace(' class="None"', '')
    html = html.replace("class='None'", '')
    return html

for fname, active, lang_url, lang_label, lang_aria, is_he, is_dark in PAGES:
    if not os.path.exists(fname):
        print(f'  SKIP (missing): {fname}')
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    nav_css = NEW_NAV_CSS_DARK if is_dark else NEW_NAV_CSS_LIGHT
    new_drawer = make_drawer_html(active, lang_url, lang_label, lang_aria, is_he)
    new_nav    = make_nav_html(active, lang_url, lang_label, lang_aria, is_he, is_dark)

    # 1. Replace nav CSS (mobile/base)
    html, ok1 = replace_section(html,
        r'/\* ─+\s*Top nav\s*─+ \*/.*?\.nav-links \{ display: none; \}\s*\.nav-cta \{ display: none; \}',
        nav_css)
    if not ok1:
        # Try alternative patterns (minified or variant)
        html, ok1 = replace_section(html,
            r'/\* ─+\s*Top nav\s*─+ \*/.*?\.nav-links\s*\{\s*display:\s*none;\s*\}',
            nav_css)

    # 2. Replace or inject drawer CSS
    html, ok2 = replace_section(html,
        r'/\* ─+\s*Mobile drawer\s*─+ \*/.*?body\.drawer-lock \{ overflow: hidden; \}',
        DRAWER_CSS.strip())
    if not ok2:
        # Try compact variant (exi, contact)
        html, ok2 = replace_section(html,
            r'\.drawer-overlay\{[^}]+\}.*?body\.drawer-lock\{overflow:hidden\}',
            DRAWER_CSS.strip())

    # 3. Replace lang-switch CSS with new lang-circle + drawer-lang-switch CSS
    html, ok3 = replace_section(html,
        r'/\* Language switcher \*/.*?@media\(min-width:900px\)\s*\{\s*\.drawer-lang-switch\s*\{\s*display:\s*none;\s*\}\s*\}',
        LANG_SWITCH_CSS.strip())
    if not ok3:
        # Try the double-rule variant
        html, ok3 = replace_section(html,
            r'/\* ─+\s*Language switcher\s*─+ \*/.*?@media\(min-width:900px\)\s*\{\s*\.drawer-lang-switch\s*\{\s*display:\s*none;\s*\}\s*\}',
            LANG_SWITCH_CSS.strip())

    # 4. Replace desktop nav @media block
    html, ok4 = replace_section(html,
        r'@media \(min-width: 900px\) \{[^}]*\n\s+\.nav \{[^}]+\}\s+\.nav-logo \{ grid-column: 1;[^}]+\}\s+\.nav-links \{[^}]+\}\s+\.nav-links a:hover \{[^}]+\}\s+\.nav-login \{[^}]+\}\s+\.nav-menu \{ display: none; \}',
        DESKTOP_NAV_CSS.strip())

    # 5. Replace the drawer HTML
    html, ok5 = replace_section(html,
        r'<!-- Mobile drawer overlay -->.*?</aside>',
        new_drawer)
    if not ok5:
        html, ok5 = replace_section(html,
            r'<aside class="drawer".*?</aside>',
            new_drawer)

    # 6. Replace the nav HTML
    html, ok6 = replace_section(html,
        r'(?:<!-- NAV -->\s*|<!-- Nav -->\s*)?<nav class="nav"[^>]*>.*?</nav>',
        new_nav)

    html = clean_class_none(html)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

    status = f'css:{ok1}/{ok2}/{ok3}/{ok4} html:{ok5}/{ok6}'
    print(f'  {fname}: {status}')

print('\nDone.')
