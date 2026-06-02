#!/usr/bin/env python3
"""Generate Hebrew RTL versions of all 7 EXPOSE website pages."""

import re

# ──────────────────────────────────────────────
# RTL CSS + language switcher CSS (injected before </style>)
RTL_CSS = """
/* ── Hebrew RTL overrides ── */
[dir="rtl"] body { font-family: 'Heebo', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }
[dir="rtl"] .eyebrow { letter-spacing: 0; }
[dir="rtl"] .h-display, [dir="rtl"] .h-section { letter-spacing: -0.01em; }
[dir="rtl"] .drawer { left: auto; right: 0; transform: translateX(100%); }
[dir="rtl"] .drawer.open { transform: translateX(0); }
[dir="rtl"] .da-toggle { text-align: right; }
[dir="rtl"] .footer-cols { direction: rtl; }
[dir="rtl"] .footer-brand { direction: rtl; }
[dir="rtl"] .footer-si-grid { direction: ltr; }
[dir="rtl"] .footer-apps { direction: ltr; }
[dir="rtl"] .store-btn { direction: ltr; }
[dir="rtl"] .footer-bottom { direction: rtl; }
[dir="rtl"] .footer-socials { direction: ltr; }
[dir="rtl"] .kc { text-align: right; direction: rtl; }
[dir="rtl"] .sleeps-item { text-align: right; direction: rtl; }
[dir="rtl"] .ns-card { text-align: right; direction: rtl; }
[dir="rtl"] .act-card { text-align: right; direction: rtl; }
[dir="rtl"] .bento-cell { text-align: right; direction: rtl; }
[dir="rtl"] .notif { direction: rtl; }
[dir="rtl"] .notif-btns { direction: ltr; }
[dir="rtl"] .dash-status { text-align: right; direction: rtl; }
[dir="rtl"] .dc-label { text-align: right; }
[dir="rtl"] .dash-frame { direction: rtl; }
[dir="rtl"] .dash-grid { direction: rtl; }
[dir="rtl"] .dc-trend { direction: ltr; }
[dir="rtl"] .dc-bars { direction: ltr; }
[dir="rtl"] .hm-stats { direction: rtl; }
[dir="rtl"] .tc-main { direction: rtl; }
[dir="rtl"] .tc-info { text-align: right; }
[dir="rtl"] .cs-team { direction: rtl; }
[dir="rtl"] .cc { direction: rtl; }
[dir="rtl"] .cc-arr { margin-left: 0; margin-right: auto; transform: scaleX(-1); }
[dir="rtl"] .cc:hover .cc-arr { transform: scaleX(-1) translateX(-4px); }
[dir="rtl"] .ta-cta { direction: ltr; justify-content: flex-end; }
[dir="rtl"] .cf-header { text-align: right; }
[dir="rtl"] .topic-pills { direction: rtl; }
[dir="rtl"] .cf-row { direction: rtl; }
[dir="rtl"] .cf-field { text-align: right; }
[dir="rtl"] .cf-field label { letter-spacing: 0; }
[dir="rtl"] .cf-chars { right: auto; left: 16px; }
[dir="rtl"] .cf-footer { direction: rtl; }
[dir="rtl"] .cf-privacy { direction: rtl; }
[dir="rtl"] .sb-head { direction: rtl; }
[dir="rtl"] .sb-fill { background: linear-gradient(270deg,var(--orange),#FF8533); }
[dir="rtl"] .score-bars-card { direction: rtl; }
[dir="rtl"] .ta-inner { direction: rtl; }
[dir="rtl"] .ta-card { text-align: right; direction: rtl; }
[dir="rtl"] .knows-grid { direction: rtl; }
[dir="rtl"] .cs-location { direction: rtl; }
[dir="rtl"] .value-card { text-align: right; direction: rtl; }
[dir="rtl"] .why-cards { direction: rtl; }
[dir="rtl"] .why-card { text-align: right; direction: rtl; }
[dir="rtl"] .section-origin, [dir="rtl"] .section-journey { text-align: right; direction: rtl; }
[dir="rtl"] .manifesto-h { letter-spacing: -0.02em; }
[dir="rtl"] .hero-stats { direction: rtl; }
[dir="rtl"] .hs-chip { direction: rtl; }
[dir="rtl"] .post-meta { direction: rtl; }
[dir="rtl"] .pf-body, [dir="rtl"] .pc-body { text-align: right; direction: rtl; }
[dir="rtl"] .blog-hero { text-align: center; }
[dir="rtl"] .filter-tabs { direction: rtl; }
[dir="rtl"] .cta-form { direction: rtl; }
[dir="rtl"] .nb { direction: ltr; }
[dir="rtl"] .ch-badges { direction: rtl; }
[dir="rtl"] .cs-promise { direction: rtl; }
[dir="rtl"] .cs-promise-badge { margin-left: 0; margin-right: auto; }
[dir="rtl"] .footer-copy { direction: rtl; }
[dir="rtl"] .ac-body { text-align: right; }
[dir="rtl"] .ac-actions { direction: ltr; }
[dir="rtl"] .drawer-nav a { text-align: right; padding: 14px 24px; }
[dir="rtl"] .da-sub-list a { padding: 12px 42px 12px 24px; }
[dir="rtl"] .drawer-close { margin-left: 0; margin-right: auto; }
[dir="rtl"] .drawer-head { flex-direction: row-reverse; }
[dir="rtl"] .bento { direction: rtl; }
[dir="rtl"] .no-stop-sub, [dir="rtl"] .sleeps-sub, [dir="rtl"] .knows-sub, [dir="rtl"] .score-sub, [dir="rtl"] .acts-sub, [dir="rtl"] .control-sub { text-align: center; direction: rtl; }
[dir="rtl"] .fc-cta-row { direction: rtl; }
[dir="rtl"] .feature-card { text-align: right; direction: rtl; }
[dir="rtl"] .step { text-align: right; direction: rtl; }
[dir="rtl"] .stat-chip { direction: rtl; }
[dir="rtl"] .social-proof { direction: rtl; }
[dir="rtl"] .pf-body h2, [dir="rtl"] .pc-title { text-align: right; }
[dir="rtl"] .nav-links { direction: rtl; }
[dir="rtl"] .hero-text { text-align: right; direction: rtl; }
[dir="rtl"] .hero-sub, [dir="rtl"] .ch-sub { text-align: right; }
[dir="rtl"] h1, [dir="rtl"] h2, [dir="rtl"] h3, [dir="rtl"] h4, [dir="rtl"] h5, [dir="rtl"] h6 { text-align: right; }
[dir="rtl"] p { text-align: right; }
[dir="rtl"] .hero h1, [dir="rtl"] .ch h1 { text-align: center; }
[dir="rtl"] .hero-sub, [dir="rtl"] .ch-sub { text-align: center; }
[dir="rtl"] .cta-sec h2, [dir="rtl"] .cta-sec p { text-align: center; }
[dir="rtl"] .cta-eyebrow, [dir="rtl"] .eyebrow { text-align: center; }
[dir="rtl"] .knows h2, [dir="rtl"] .sleeps h2, [dir="rtl"] .score-sec h2, [dir="rtl"] .acts h2, [dir="rtl"] .no-stop h2, [dir="rtl"] .one-agent h2, [dir="rtl"] .control h2 { text-align: right; }
[dir="rtl"] .cf-success { direction: rtl; }

/* Language switcher */
.lang-switch {
  font-size: 12px; font-weight: 700; letter-spacing: .04em;
  padding: 6px 12px; border-radius: 20px;
  border: 1px solid rgba(255,106,26,.35);
  color: var(--orange); background: transparent;
  transition: background .15s, color .15s;
  cursor: pointer; text-decoration: none;
  display: inline-block; line-height: 1;
}
.lang-switch:hover { background: var(--orange); color: #fff; }
[dir="rtl"] .lang-switch { margin-left: 0; margin-right: 4px; }
"""

# ──────────────────────────────────────────────
# Heebo font link
HEEBO_FONT = '<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

# ──────────────────────────────────────────────
# Shared nav link mapping: English → Hebrew page
LINKS_MAP = {
    'site.html':             'site-he.html',
    'site-brands.html':      'site-brands-he.html',
    'site-exi.html':         'site-exi-he.html',
    'site-exi-brands.html':  'site-exi-brands-he.html',
    'site-about.html':       'site-about-he.html',
    'site-blog.html':        'site-blog-he.html',
    'site-contact.html':     'site-contact-he.html',
}

# ──────────────────────────────────────────────
# Per-page text translations (English → Hebrew)
# Order matters – longer strings first to avoid partial replacement
COMMON_TRANSLATIONS = [
    # ── Drawer nav ──
    ('Join EXPOSE — It\'s Free', 'הצטרפו ל-EXPOSE — חינם'),
    ('For Brands', 'למותגים'),
    ('For Creatives', 'ליוצרים'),
    ('Meet EXi', 'הכירו את EXi'),
    ('EXi for Creatives', 'EXi ליוצרים'),
    ('EXi for Brands', 'EXi למותגים'),
    ('About Us', 'אודותינו'),
    ('Pricing', 'תמחור'),
    ('Blog', 'בלוג'),
    ('Contact', 'צרו קשר'),
    ('Join', 'הצטרפו'),
    # ── Footer columns ──
    ('Product', 'מוצר'),
    ('Company', 'חברה'),
    ('Support', 'תמיכה'),
    ('Follow us', 'עקבו אחרינו'),
    ('For Creatives', 'ליוצרים'),
    ('For Brands', 'למותגים'),
    ('Meet EXi', 'EXi סוכן'),
    ('About Us', 'אודותינו'),
    ('Careers', 'קריירה'),
    ('Press', 'עיתונות'),
    ('Help Center', 'מרכז עזרה'),
    ('Privacy', 'פרטיות'),
    ('Terms', 'תנאי שימוש'),
    ('© 2025 EXPOSE. All rights reserved.', '© 2025 EXPOSE. כל הזכויות שמורות.'),
    # ── App Store buttons ──
    ('Download on the', 'הורידו מה-'),
    ('App Store', 'App Store'),
    ('Get it on', 'הורידו מ-'),
    ('Google Play', 'Google Play'),
    # ── Footer tagline ──
    ('The AI-powered marketing engine for world-class creatives.', 'מנוע השיווק המופעל על ידי AI ליוצרים ברמה עולמית.'),
    ('AI-powered creative career platform', 'פלטפורמת קריירה יצירתית מבוססת AI'),
    # ── Aria labels ──
    ('Open menu', 'פתח תפריט'),
    ('Close menu', 'סגור תפריט'),
    ('aria-label="Instagram"', 'aria-label="Instagram"'),
]

PAGE_TRANSLATIONS = {
    'site.html': [
        # Title / meta
        ('EXPOSE — Stop Chasing After Clients. Let EXi Run It.', 'EXPOSE — הפסיקו לרדוף אחרי לקוחות. תנו ל-EXi לטפל בזה.'),
        ('EXPOSE is the AI-powered marketing platform for creatives and brands. Let EXi, your AI agent, run your campaigns, match you with creators, and grow your career — 24/7.', 'EXPOSE היא פלטפורמת השיווק המופעלת על ידי AI ליוצרים ומותגים. תנו ל-EXi, סוכן ה-AI שלכם, לנהל את הקמפיינים, למצוא התאמות ולצמוח — 24/7.'),
        # Hero
        ('Stop Chasing After Clients.<br>Let EXi Run It.', 'הפסיקו לרדוף אחרי לקוחות.<br>תנו ל-EXi לטפל בזה.'),
        ('Stop Chasing After Clients. Let EXi Run It.', 'הפסיקו לרדוף אחרי לקוחות. תנו ל-EXi לטפל בזה.'),
        ('EXi manages your profile, finds opportunities, handles brand outreach, and grows your career — all while you focus on creating.', 'EXi מנהל את הפרופיל שלכם, מוצא הזדמנויות, מתקשר עם מותגים ומגדל את הקריירה שלכם — בזמן שאתם יוצרים.'),
        ('Join EXPOSE — It\'s Free', 'הצטרפו ל-EXPOSE — חינם'),
        ('Book Demo', 'קבעו דמו'),
        ('Watch 2-min tour', 'צפו בסיור קצר'),
        # Stats
        ('Creators joined', 'יוצרים הצטרפו'),
        ('Average earnings boost', 'עלייה ממוצעת בהכנסות'),
        ('Brands on platform', 'מותגים בפלטפורמה'),
        # How it works
        ('HOW IT WORKS', 'איך זה עובד'),
        ('EXi matches you to the right opportunities', 'EXi מחבר אתכם להזדמנויות הנכונות'),
        ('Complete Your Profile', 'השלימו את הפרופיל'),
        ('Tell us your style, niche, and what brands you want to work with.', 'ספרו לנו את הסגנון, הנישה והמותגים שאתם רוצים לעבוד איתם.'),
        ('EXi Finds Matches', 'EXi מוצא התאמות'),
        ('Your agent scans opportunities and connects you to the right brands.', 'הסוכן שלכם סורק הזדמנויות ומחבר אתכם למותגים הנכונים.'),
        ('Grow Your Career', 'צמחו בקריירה'),
        ('Land deals, build your rep, and level up — EXi handles the rest.', 'קבלו עסקאות, בנו מוניטין והתקדמו — EXi מטפל בשאר.'),
        ('Browse all professionals', 'עיינו בכל המקצוענים'),
        # Social proof
        ('Real creators. Real results.', 'יוצרים אמיתיים. תוצאות אמיתיות.'),
        ('Join the creatives already growing with EXPOSE', 'הצטרפו ליוצרים שכבר צומחים עם EXPOSE'),
        ('Start free — get matched', 'התחילו בחינם — קבלו התאמות'),
        # What you get
        ('WHAT YOU GET', 'מה תקבלו'),
        ('Everything you need to grow your creative career', 'כל מה שצריך לצמוח בקריירה היצירתית שלכם'),
        ('A profile that sells for you', 'פרופיל שמוכר בשבילכם'),
        ('EXi builds and manages your digital presence, optimizing it for the brands actively searching your style.', 'EXi בונה ומנהל את הנוכחות הדיגיטלית שלכם, ומייעל אותה למותגים שמחפשים את הסגנון שלכם.'),
        ('Opportunities that come to you', 'הזדמנויות שמגיעות אליכם'),
        ('Stop searching and applying. EXi proactively pitches you to brands that match your vibe and values.', 'הפסיקו לחפש ולהגיש מועמדות. EXi מציג אתכם למותגים שמתאימים לסגנון ולערכים שלכם.'),
        ('Analytics that drive growth', 'אנליטיקה שמניעה צמיחה'),
        ('See exactly what\'s working. EXi tracks performance across all platforms and tells you what to post next.', 'ראו בדיוק מה עובד. EXi עוקב אחרי הביצועים בכל הפלטפורמות ואומר לכם מה לפרסם הלאה.'),
        # CTA
        ('Ready to stop chasing clients?', 'מוכנים להפסיק לרדוף אחרי לקוחות?'),
        ('Join EXPOSE and let EXi run your career — 24/7, while you focus on what you do best.', 'הצטרפו ל-EXPOSE ותנו ל-EXi לנהל את הקריירה שלכם — 24/7, בזמן שאתם מתמקדים בדבר שאתם הכי טובים בו.'),
        ('Get matched now', 'קבלו התאמות עכשיו'),
        ('Book a free demo', 'קבעו דמו חינם'),
        # Dashboard labels
        ('EXi is active', 'EXi פעיל'),
        ('Optimizing Your Career', 'מייעל את הקריירה שלכם'),
        ('Active Proposal', 'הצעות פעילות'),
        ('Profile Views', 'צפיות בפרופיל'),
        ('Above industry avg', 'מעל ממוצע התעשייה'),
        ('Social Media Eng', 'מעורבות ברשתות'),
        ('Projects Matches', 'התאמות פרויקטים'),
        ('Earnings this week', 'הכנסות השבוע'),
    ],

    'site-brands.html': [
        ('EXPOSE — Stop Guessing Your Marketing. Let EXi Run It.', 'EXPOSE — הפסיקו לנחש שיווק. תנו ל-EXi לטפל בזה.'),
        ('Stop Guessing Your Marketing.<br>Let EXi Run It.', 'הפסיקו לנחש שיווק.<br>תנו ל-EXi לטפל בזה.'),
        ('Stop Guessing Your Marketing. Let EXi Run It.', 'הפסיקו לנחש שיווק. תנו ל-EXi לטפל בזה.'),
        ('EXi manages your creator relationships, optimizes campaigns, and reports results — so you can focus on your brand, not the logistics.', 'EXi מנהל את מערכות היחסים עם היוצרים, מייעל קמפיינים ומדווח תוצאות — כדי שתוכלו להתמקד במותג שלכם, לא בלוגיסטיקה.'),
        ('Book a Demo', 'קבעו דמו'),
        ('Book Demo', 'קבעו דמו'),
        ('Watch 2-min tour', 'צפו בסיור קצר'),
        # How it works
        ('HOW IT WORKS', 'איך זה עובד'),
        ('EXi manages your marketing end-to-end', 'EXi מנהל את השיווק שלכם מקצה לקצה'),
        ('Create a Brief', 'צרו בריף'),
        ('Tell us about your brand, goals, and target audience — EXi handles the rest.', 'ספרו לנו על המותג שלכם, היעדים וקהל היעד — EXi מטפל בשאר.'),
        ('EXi Matches Creators', 'EXi מתאים יוצרים'),
        ('Your agent finds the right creators and starts managing the campaign automatically.', 'הסוכן שלכם מוצא את היוצרים הנכונים ומתחיל לנהל את הקמפיין אוטומטית.'),
        ('Track &amp; Report', 'עקבו ודווחו'),
        ('Track & Report', 'עקבו ודווחו'),
        ('See real-time performance and optimise your campaigns with AI-driven insights.', 'ראו ביצועים בזמן אמת ושפרו את הקמפיינים עם תובנות מבוססות AI.'),
        # Features
        ('WHAT YOU GET', 'מה תקבלו'),
        ('Everything you need to run creator marketing that actually works', 'כל מה שצריך להפעיל שיווק יוצרים שעובד באמת'),
        ('Smart Campaign Management', 'ניהול קמפיין חכם'),
        ('EXi matches, manages, and optimises creator campaigns — automatically.', 'EXi מתאים, מנהל ומייעל קמפיינים עם יוצרים — אוטומטית.'),
        ('Access to Vetted Creator Network', 'גישה לרשת יוצרים מאומתת'),
        ('Thousands of professional creators — all with proven performance track records.', 'אלפי יוצרים מקצוענים — כולם עם רקורד ביצועים מוכח.'),
        ('Real-time ROI &amp; Reporting', 'ROI ודיווח בזמן אמת'),
        ('Real-time ROI & Reporting', 'ROI ודיווח בזמן אמת'),
        ('See exactly what\'s working and why — so every dollar counts.', 'ראו בדיוק מה עובד ולמה — כדי שכל שקל יספר.'),
        # CTA
        ('Ready to upgrade your marketing?', 'מוכנים לשדרג את השיווק שלכם?'),
        ('Join EXPOSE and let EXi manage your creator campaigns — smarter, faster, better.', 'הצטרפו ל-EXPOSE ותנו ל-EXi לנהל את קמפיינים היוצרים שלכם — חכם יותר, מהיר יותר, טוב יותר.'),
        ('Start for free', 'התחילו בחינם'),
        ('Book a free demo', 'קבעו דמו חינם'),
        # Dashboard
        ('EXi is active', 'EXi פעיל'),
        ('Managing Your Campaigns', 'מנהל את הקמפיינים שלכם'),
        ('Active Campaigns', 'קמפיינים פעילים'),
        ('Creator Matches', 'התאמות יוצרים'),
        ('Campaign ROI', 'ROI קמפיין'),
        ('Total Reach', 'טווח הגעה כולל'),
        ('Campaign Spend', 'הוצאות קמפיין'),
    ],

    'site-exi.html': [
        ('EXi — Your AI Agent | EXPOSE', 'EXi — הסוכן ה-AI שלך | EXPOSE'),
        ('Meet EXi — the AI agent built for creatives. EXi knows your portfolio, pitches you to brands, manages client relationships, and tracks your earnings. Free to start.', 'הכירו את EXi — הסוכן ה-AI שנבנה ליוצרים. EXi מכיר את הפורטפוליו שלכם, מציג אתכם למותגים, מנהל קשרי לקוחות ועוקב אחר ההכנסות שלכם. חינם להתחיל.'),
        ('The Agent that<br>works for you <span class="italic-accent" style="color:var(--orange)">24/7</span>', 'הסוכן שעובד<br>בשבילכם <span class="italic-accent" style="color:var(--orange)">24/7</span>'),
        ('EXi finds the projects, grows your visibility, and tells you exactly what to do next — so you just show up and create.', 'EXi מוצא את הפרויקטים, מגדיל את החשיפה שלכם ואומר בדיוק מה לעשות הלאה — כדי שתוכלו להגיע וליצור.'),
        # Knows section
        ('Always connected', 'תמיד מחובר'),
        ('EXi knows your world<br><span class="italic-accent">better than you do.</span>', 'EXi מכיר את העולם שלכם<br><span class="italic-accent">טוב יותר מכם.</span>'),
        ('EXi plugs into every corner of your career — giving you full coverage, 24/7, without lifting a finger.', 'EXi מתחבר לכל פינה של הקריירה שלכם — ומספק כיסוי מלא, 24/7, בלי שתצטרכו להרים אצבע.'),
        ('8 live connections', '8 חיבורים חיים'),
        # KC cards
        ('Engagement, reach &amp; best posting times', 'מעורבות, טווח וזמני הפרסום הטובים ביותר'),
        ('Trending sounds, reach &amp; video performance', 'צלילים טרנדיים, טווח וביצועי וידאו'),
        ('Scores, optimizes &amp; tracks acceptance rates', 'מדרג, מייעל ועוקב אחר שיעורי קבלה'),
        ('Manages availability &amp; books shoots for you', 'מנהל זמינות ומזמין צילומים בשבילכם'),
        ('In-demand styles, niches &amp; brand activity', 'סגנונות, נישות ופעילות מותגים מבוקשים'),
        ('Earnings tracking &amp; market rate benchmarks', 'מעקב הכנסות ואמות מידה של תעשייה'),
        ('Scans open briefs &amp; pre-matches to your style', 'סורק בריפים פתוחים ומתאים מראש לסגנונכם'),
        ('Ranks you vs top creatives in your niche', 'מדרג אתכם מול יוצרים מובילים בנישה שלכם'),
        ('Portfolio', 'פורטפוליו'),
        ('Calendar', 'יומן'),
        ('Market Trends', 'מגמות שוק'),
        ('Payments & Rates', 'תשלומים ותעריפים'),
        ('Project Briefs', 'בריפים'),
        ('Industry Benchmarks', 'מדדי תעשייה'),
        ('Live', 'חי'),
        ('Synced', 'מסונכרן'),
        ('Scanning', 'סורק'),
        ('Watching', 'עוקב'),
        # Never Sleeps
        ('Always working', 'תמיד עובד'),
        ('EXi <span class="italic-accent" style="font-size:32px">Never Sleeps</span>', 'EXi <span class="italic-accent" style="font-size:32px">לעולם לא ישן</span>'),
        ('While you rest, EXi is scanning markets, optimizing your profile, and grabbing opportunities before they disappear.', 'בזמן שאתם נחים, EXi סורק שווקים, מייעל את הפרופיל שלכם ותופס הזדמנויות לפני שהן נעלמות.'),
        ('Updates Your Profile Finder', 'מעדכן את מוצא הפרופיל שלכם'),
        ('Keeps your profile sharp and positioned for the brands actively searching your style.', 'שומר את הפרופיל שלכם חד ממוקד למותגים שמחפשים את הסגנון שלכם.'),
        ('Career Growth Alerts', 'התראות צמיחת קריירה'),
        ('Notifies you the moment your visibility spikes or a brand is actively searching your niche.', 'מודיע לכם ברגע שהחשיפה שלכם מזנקת או שמותג מחפש את הנישה שלכם.'),
        ('Initiates Your Screening', 'מתחיל את הסינון שלכם'),
        ('Pre-screens briefs and drafts your application before you even open the app.', 'מסנן בריפים מראש ומכין את הגשתכם לפני שפותחים את האפליקציה.'),
        # Career Score
        ('Know your value', 'דעו את הערך שלכם'),
        ('Your Career Score', 'הציון המקצועי שלכם'),
        ('Your AI-generated score that benchmarks you against top talent in your niche — and shows exactly how to improve.', 'הציון המופעל על ידי AI שמדרג אתכם מול הכשרונות המובילים בנישה שלכם — ומראה בדיוק איך להשתפר.'),
        ('Portfolio Strength', 'חוזק הפורטפוליו'),
        ('Brand Alignment', 'התאמה למותגים'),
        ('Engagement Quality', 'איכות מעורבות'),
        ('Get Your Full Audit', 'קבלו את הביקורת המלאה'),
        # Acts
        ('EXi takes action', 'EXi פועל בשבילכם'),
        ('EXi doesn\'t just find opportunities — it acts on them for you.', 'EXi לא רק מוצא הזדמנויות — הוא פועל עליהן בשבילכם.'),
        ('Approve', 'אישור'),
        ('Skip', 'דלג'),
        ('Let EXi Work for You', 'תנו ל-EXi לעבוד בשבילכם'),
        # No-stop
        ('EXi doesn\'t stop.', 'EXi לא מפסיק.'),
        ('The features that keep your career moving — even when you\'re offline.', 'הפיצ\'רים שמניעים את הקריירה שלכם — גם כשאתם לא מחוברים.'),
        ('Pitch Automation', 'אוטומציה של פיץ\'ים'),
        ('EXi crafts and sends personalized pitches to brands that match your profile.', 'EXi מכין ושולח פיץ\'ים מותאמים אישית למותגים שמתאימים לפרופיל שלכם.'),
        ('Contract Management', 'ניהול חוזים'),
        ('Review, flag issues, and track contract status — automatically.', 'סוקר, מסמן בעיות ועוקב אחר סטטוס חוזים — אוטומטית.'),
        ('Income Tracking', 'מעקב הכנסות'),
        ('Know exactly what you\'ve earned, what\'s pending, and what\'s next.', 'דעו בדיוק מה הרווחתם, מה ממתין ומה הולך לקרות.'),
        ('Continuous hourly', 'כל שעה ברציפות'),
        ('Automatic', 'אוטומטי'),
        ('Real-time', 'בזמן אמת'),
        ('Start for Free', 'התחילו בחינם'),
        # One agent bento
        ('One agent. Everything you need.', 'סוכן אחד. כל מה שצריך.'),
        ('Replace your entire freelance stack with one AI agent.', 'החליפו את כל הכלים שלכם בסוכן AI אחד.'),
        ('Profile Engine', 'מנוע פרופיל'),
        ('Continuously optimizes your profile for maximum brand appeal.', 'מייעל את הפרופיל שלכם ללא הרף למשיכה מקסימלית למותגים.'),
        ('Smart Matching', 'התאמה חכמה'),
        ('AI that understands fit beyond just follower count.', 'AI שמבין התאמה מעבר לספירת עוקבים בלבד.'),
        ('Deal Flow', 'זרימת עסקאות'),
        ('Pitches sent, tracked, and closed — without your involvement.', 'פיץ\'ים נשלחים, נעקבים ונסגרים — בלי מעורבותכם.'),
        ('Earnings Hub', 'מרכז הכנסות'),
        ('All your income, invoices, and payment status in one place.', 'כל ההכנסות, החשבוניות וסטטוס התשלום במקום אחד.'),
        ('Analytics', 'אנליטיקה'),
        ('Platform-by-platform insights to grow smarter.', 'תובנות לפי פלטפורמה לצמיחה חכמה יותר.'),
        ('Your Creative CRM', 'ה-CRM היצירתי שלכם'),
        ('Every brand relationship, managed and optimised by EXi.', 'כל מערכת יחסים עם מותג, מנוהלת ומייועלת על ידי EXi.'),
        # Control
        ('You\'re always in control.', 'אתם תמיד בשליטה.'),
        ('EXi works autonomously — but every action is transparent and reversible.', 'EXi פועל באופן עצמאי — אך כל פעולה שקופה וניתנת לביטול.'),
        ('New Brand Match', 'התאמת מותג חדשה'),
        ('Now', 'עכשיו'),
        ('EXi matched you with', 'EXi התאים אתכם ל-'),
        ('View', 'צפייה'),
        ('Decline', 'דחייה'),
        ('Contract Ready', 'חוזה מוכן'),
        ('2m ago', 'לפני 2 דקות'),
        ('EXi reviewed and flagged', 'EXi סקר וסימן'),
        ('Review', 'סקירה'),
        ('Profile Updated', 'פרופיל עודכן'),
        ('5m ago', 'לפני 5 דקות'),
        ('EXi updated your portfolio based on trending briefs.', 'EXi עדכן את הפורטפוליו שלכם על פי בריפים טרנדיים.'),
        # CTA
        ('Ready to let EXi work for you?', 'מוכנים לתת ל-EXi לעבוד בשבילכם?'),
        ('Join thousands of creatives who\'ve handed their career admin to EXi — and never looked back.', 'הצטרפו לאלפי יוצרים שמסרו את הניהול הקריירה שלהם ל-EXi — ולא הסתכלו אחורה.'),
        ('Start for Free', 'התחילו בחינם'),
        ('Book a Meeting', 'קבעו פגישה'),
        ('exi.agent — live session', 'exi.agent — סשן חי'),
    ],

    'site-exi-brands.html': [
        ('EXi for Brands — Campaign AI Agent | EXPOSE', 'EXi למותגים — סוכן AI לקמפיינים | EXPOSE'),
        ('Meet EXi for Brands — the AI agent that runs your creator campaigns end-to-end. Finds creators, manages relationships, tracks performance, and reports ROI. Automatically.', 'הכירו את EXi למותגים — הסוכן ה-AI שמנהל את קמפיינים היוצרים שלכם מקצה לקצה. מוצא יוצרים, מנהל קשרים, עוקב אחר ביצועים ומדווח ROI. אוטומטית.'),
        ('The Agent that runs<br>your campaigns <span class="italic-accent" style="color:var(--orange)">24/7</span>', 'הסוכן שמנהל<br>את הקמפיינים שלכם <span class="italic-accent" style="color:var(--orange)">24/7</span>'),
        ('EXi finds the right creators, manages the relationships, and optimises performance — so your team can focus on strategy, not logistics.', 'EXi מוצא את היוצרים הנכונים, מנהל את הקשרים ומייעל את הביצועים — כדי שהצוות שלכם יוכל להתמקד באסטרטגיה, לא בלוגיסטיקה.'),
        # Knows
        ('Always learning', 'תמיד לומד'),
        ('EXi knows your brand<br><span class="italic-accent">better than your agency does.</span>', 'EXi מכיר את המותג שלכם<br><span class="italic-accent">טוב יותר מהסוכנות שלכם.</span>'),
        ('EXi analyses your past campaigns, brand guidelines, and audience data — then finds creators who actually fit.', 'EXi מנתח את הקמפיינים הקודמים, הנחיות המותג ונתוני הקהל — ואז מוצא יוצרים שבאמת מתאימים.'),
        ('Brief Analysis', 'ניתוח בריף'),
        ('Parses and interprets campaign briefs to extract key requirements.', 'מנתח ופותר בריפים לחילוץ דרישות מפתח.'),
        ('Brand Fit Scoring', 'ציון התאמה למותג'),
        ('Matches creators to your brand values, audience, and aesthetic.', 'מתאים יוצרים לערכי המותג, הקהל והאסתטיקה שלכם.'),
        ('Performance Prediction', 'חיזוי ביצועים'),
        ('Predicts campaign performance before you commit budget.', 'מנבא ביצועי קמפיין לפני שמחייבים תקציב.'),
        ('Audience Alignment', 'התאמת קהל'),
        ('Verifies creator audiences match your target demographics.', 'מאמת שקהלי היוצרים תואמים לדמוגרפיה המטרה שלכם.'),
        # Brand Score
        ('Know your brand', 'הכירו את המותג שלכם'),
        ('Your Brand Score', 'ציון המותג שלכם'),
        ('EXi scores your campaigns, creators, and content — so you know exactly what\'s driving results.', 'EXi מדרג את הקמפיינים, היוצרים והתוכן שלכם — כדי שתדעו בדיוק מה מניע תוצאות.'),
        ('Creator Match Quality', 'איכות התאמת יוצרים'),
        ('Content Performance', 'ביצועי תוכן'),
        ('Audience Relevance', 'רלוונטיות קהל'),
        ('View Full Report', 'צפו בדוח המלא'),
        # Never sleeps
        ('Always optimising', 'תמיד מייעל'),
        ('EXi <span class="italic-accent" style="font-size:32px">Never Stops</span>', 'EXi <span class="italic-accent" style="font-size:32px">לעולם לא מפסיק</span>'),
        ('While your team is focused on strategy, EXi is managing creator relationships, tracking content, and optimising spend.', 'בזמן שהצוות שלכם מתמקד באסטרטגיה, EXi מנהל קשרי יוצרים, עוקב אחר תוכן ומייעל הוצאות.'),
        ('Creator Outreach', 'פנייה ליוצרים'),
        ('EXi identifies, contacts, and negotiates with creators on your behalf.', 'EXi מזהה, יוצר קשר ומשא ומתן עם יוצרים בשמכם.'),
        ('Content Monitoring', 'ניטור תוכן'),
        ('Tracks all creator content for brand safety and performance.', 'עוקב אחר כל תוכן יוצרים לבטיחות מותג וביצועים.'),
        ('Budget Optimisation', 'ייעול תקציב'),
        ('Reallocates spend in real-time based on performance data.', 'מקצה מחדש הוצאות בזמן אמת על בסיס נתוני ביצועים.'),
        # Acts
        ('EXi runs your campaigns.', 'EXi מנהל את הקמפיינים שלכם.'),
        ('From brief to report — EXi handles the entire creator campaign lifecycle.', 'מבריף לדוח — EXi מנהל את מחזור החיים המלא של קמפיין יוצרים.'),
        ('Let EXi Run Your Campaigns', 'תנו ל-EXi לנהל את הקמפיינים שלכם'),
        # One bento
        ('One agent. Your entire campaign stack.', 'סוכן אחד. כל ערימת הקמפיינים שלכם.'),
        ('Replace your agency workflows with one AI agent.', 'החליפו את זרימות עבודת הסוכנות שלכם בסוכן AI אחד.'),
        ('Campaign Engine', 'מנוע קמפיין'),
        ('End-to-end campaign management from brief to closeout.', 'ניהול קמפיין מלא מבריף לסגירה.'),
        ('Creator Intelligence', 'אינטליגנציה ליוצרים'),
        ('Deep creator analysis beyond follower count.', 'ניתוח עמוק של יוצרים מעבר לספירת עוקבים.'),
        ('Contract Automation', 'אוטומציה של חוזים'),
        ('EXi drafts and tracks all creator agreements.', 'EXi מכין ועוקב אחר כל הסכמי יוצרים.'),
        ('ROI Dashboard', 'לוח ROI'),
        ('Real-time visibility into every dollar spent and earned.', 'נראות בזמן אמת לכל שקל שהוצא והורווח.'),
        ('Audience Insights', 'תובנות קהל'),
        ('Deep audience data across all creator partnerships.', 'נתוני קהל עמוקים בכל שיתופי פעולה עם יוצרים.'),
        ('Compliance Monitoring', 'ניטור תאימות'),
        ('Ensures all content meets brand and legal standards.', 'מבטיח שכל התוכן עומד בסטנדרטים של המותג והחוק.'),
        # Control
        ('Full visibility. Always.', 'נראות מלאה. תמיד.'),
        ('EXi acts autonomously — but your team stays in the loop on every decision.', 'EXi פועל באופן עצמאי — אבל הצוות שלכם מעורב בכל החלטה.'),
        ('Creator Matched', 'יוצר הותאם'),
        ('EXi matched', 'EXi התאים'),
        ('for your campaign.', 'לקמפיין שלכם.'),
        ('Accept', 'קבלו'),
        ('Campaign Alert', 'התראת קמפיין'),
        ('Spend is 15% above target for', 'ההוצאה גבוהה ב-15% מהיעד ל-'),
        ('Reallocate', 'הקצה מחדש'),
        ('Ignore', 'התעלם'),
        ('Report Ready', 'דוח מוכן'),
        ('Weekly performance report for', 'דוח ביצועים שבועי ל-'),
        ('campaign is ready.', 'הקמפיין מוכן.'),
        # CTA
        ('Ready to let EXi run your campaigns?', 'מוכנים לתת ל-EXi לנהל את הקמפיינים שלכם?'),
        ('Join brands already running smarter campaigns with EXi — and see the difference in your first week.', 'הצטרפו למותגים שכבר מנהלים קמפיינים חכמים יותר עם EXi — וראו את ההבדל בשבוע הראשון.'),
        ('Start for Free', 'התחילו בחינם'),
        ('Book a Demo', 'קבעו דמו'),
    ],

    'site-about.html': [
        ('EXPOSE — Built By Someone Who Lived It.', 'EXPOSE — נבנה על ידי מי שחי את זה.'),
        ('Built by someone<br>who <em class="italic-accent">lived it.</em>', 'נבנה על ידי מי<br>ש<em class="italic-accent">חי את זה.</em>'),
        ('We didn\'t build EXPOSE to check a box or chase a trend. The problem was ours — we lived it, and we knew someone had to fix it.', 'לא בנינו את EXPOSE כדי לסמן תיבה או לרדוף אחרי טרנד. הבעיה הייתה שלנו — חיינו אותה, וידענו שמישהו צריך לפתור אותה.'),
        ('Our Story', 'הסיפור שלנו'),
        ('10K+', '10K+'),
        ('Creatives', 'יוצרים'),
        ('Founded', 'נוסד'),
        ('Live', 'חי'),
        ('Projects', 'פרויקטים'),
        ('Free forever', 'חינם לתמיד'),
        ('EXPOSE Platform', 'פלטפורמת EXPOSE'),
        # Origin
        ('Where it started', 'איך זה התחיל'),
        ('The problem nobody was solving', 'הבעיה שאף אחד לא פתר'),
        ('Dorel Shnaiderman built EXPOSE after years of navigating the creator economy first-hand. The tools were broken, the platforms were extractive, and talented creatives were leaving money on the table every single day.', 'דורל שניידרמן בנה את EXPOSE לאחר שנים של ניווט בכלכלת היוצרים מכלי ראשון. הכלים היו שבורים, הפלטפורמות היו ממצות, ויוצרים מוכשרים איבדו כסף כל יום.'),
        ('EXPOSE was built to fix that. Not as another platform that takes a cut — but as a tool that genuinely works for creatives.', 'EXPOSE נבנה כדי לתקן את זה. לא כעוד פלטפורמה שלוקחת עמלה — אלא ככלי שעובד באמת עבור יוצרים.'),
        # Why section
        ('Why we built this', 'למה בנינו את זה'),
        ('The creative industry is broken — and we\'re fixing it', 'תעשיית הקריאייטיב שבורה — ואנחנו מתקנים אותה'),
        ('Creatives were undervalued', 'יוצרים לא קיבלו את הערך שלהם'),
        ('Talented creators were spending 60% of their time on admin, chasing payments, and doing work that should be automated.', 'יוצרים מוכשרים בזבזו 60% מהזמן על ניהול, מרדיפות אחרי תשלומים ועבודה שהייתה אמורה להיות אוטומטית.'),
        ('The tools weren\'t built for creators', 'הכלים לא נבנו ליוצרים'),
        ('Generic freelance platforms weren\'t designed with the creative workflow in mind. So we built one that was.', 'פלטפורמות פרילנס גנריות לא תוכננו עם זרימת העבודה היצירתית בראש. אז בנינו אחת שכן.'),
        ('Brands were guessing', 'מותגים ניחשו'),
        ('Most brand-creator matches were based on follower count, not fit. The result? Mediocre campaigns and wasted budgets.', 'רוב ההתאמות מותג-יוצר התבססו על ספירת עוקבים, לא התאמה. התוצאה? קמפיינים בינוניים ותקציבים מבוזבזים.'),
        # Journey
        ('How we got here', 'איך הגענו לכאן'),
        ('The EXPOSE journey', 'מסע EXPOSE'),
        ('Dorel\'s first campaign as a creator — 3 brands, 6 weeks of back-and-forth, $0 in payment after 90 days.', 'הקמפיין הראשון של דורל כיוצר — 3 מותגים, 6 שבועות של תכתובות, 0 תשלום אחרי 90 ימים.'),
        ('The idea: what if an AI agent could handle everything a creator hates doing?', 'הרעיון: מה אם סוכן AI יוכל לטפל בכל מה שיוצר שונא לעשות?'),
        ('First version of EXi goes live. 200 beta users in the first week.', 'הגרסה הראשונה של EXi עולה לאוויר. 200 משתמשי בטא בשבוע הראשון.'),
        ('EXPOSE officially launches. 10K+ creatives. Growing every day.', 'EXPOSE משיק רשמית. 10K+ יוצרים. גדל בכל יום.'),
        # Manifesto
        ('We believe the best creators shouldn\'t have to fight for what they\'re worth.', 'אנחנו מאמינים שהיוצרים הטובים ביותר לא צריכים להילחם על מה שהם שווים.'),
        ('The creative economy is a $500B industry. Most of that value flows to the platforms — not the creators who power them.', 'כלכלת הקריאייטיב היא תעשייה של 500 מיליארד דולר. רוב הערך הזה זורם לפלטפורמות — לא ליוצרים שמניעים אותן.'),
        ('We\'re changing that.', 'אנחנו משנים את זה.'),
        # Values
        ('What we stand for', 'על מה אנחנו עומדים'),
        ('Our values', 'הערכים שלנו'),
        ('Radical Transparency', 'שקיפות מוחלטת'),
        ('No surprises, no hidden fees, no fine print. Just honest tools that do what they say.', 'אין הפתעות, אין עמלות נסתרות, אין אותיות קטנות. רק כלים כנים שעושים מה שהם אומרים.'),
        ('Creators First', 'יוצרים קודמים'),
        ('Every decision we make starts with one question: does this genuinely help creators?', 'כל החלטה שאנחנו מקבלים מתחילה בשאלה אחת: האם זה עוזר ליוצרים באמת?'),
        ('Built to Work For You', 'נבנה לעבוד בשבילכם'),
        ('We\'re not a marketplace that takes a cut. We\'re a tool that works for you.', 'אנחנו לא מרקטפלייס שלוקח עמלה. אנחנו כלי שעובד בשבילכם.'),
        ('Community', 'קהילה'),
        ('When you win, we all win. We\'re building the infrastructure for the creative economy to thrive.', 'כשאתם מנצחים, כולנו מנצחים. אנחנו בונים את התשתית לשגשוג כלכלת הקריאייטיב.'),
        # Team
        ('The team', 'הצוות'),
        ('The people behind EXPOSE', 'האנשים מאחורי EXPOSE'),
        ('A small team with a big mission — making the creative economy fairer for everyone.', 'צוות קטן עם משימה גדולה — הפיכת כלכלת הקריאייטיב להוגנת יותר לכולם.'),
        ('Founder &amp; CEO', 'מייסד ומנכ"ל'),
        ('Head of Product', 'ראש מחלקת מוצר'),
        ('Lead Engineer', 'מהנדס ראשי'),
        ('Head of Partnerships', 'ראש שיתופי פעולה'),
        # CTA
        ('Ready to join?', 'מוכנים להצטרף?'),
        ('Join EXPOSE today', 'הצטרפו ל-EXPOSE היום'),
        ('We\'re building the future of creative work. Come be part of it.', 'אנחנו בונים את עתיד העבודה היצירתית. בואו להיות חלק ממנו.'),
    ],

    'site-blog.html': [
        ('EXPOSE Blog — The Creator Economy, Decoded', 'בלוג EXPOSE — כלכלת היוצרים, מפוענחת'),
        ('The creator economy,<br><em class="italic-accent">decoded.</em>', 'כלכלת היוצרים,<br><em class="italic-accent">מפוענחת.</em>'),
        ('Insights on AI marketing, brand-creator collaboration, and what\'s next for the creative industry.', 'תובנות על שיווק AI, שיתוף פעולה מותג-יוצר ומה הולך לקרות בתעשייה היצירתית.'),
        ('EXPOSE Blog', 'בלוג EXPOSE'),
        # Filter tabs
        ('All Posts', 'כל הפוסטים'),
        ('AI &amp; Automation', 'AI ואוטומציה'),
        ('Brand Strategy', 'אסטרטגיית מותג'),
        ('Creator Economy', 'כלכלת יוצרים'),
        ('Platform', 'פלטפורמה'),
        # Post categories
        ('AI &amp; Automation', 'AI ואוטומציה'),
        ('Brand Strategy', 'אסטרטגיית מותג'),
        ('Creator Economy', 'כלכלת יוצרים'),
        ('Featured', 'נבחר'),
        # Post metadata
        ('min read', 'דקות קריאה'),
        ('min', 'דקות'),
        # Newsletter
        ('Stay in the loop', 'הישארו בעניינים'),
        ('Get weekly insights on creator economy trends delivered to your inbox.', 'קבלו תובנות שבועיות על מגמות כלכלת היוצרים ישירות לתיבת הדואר שלכם.'),
        ('Your email address', 'כתובת האימייל שלכם'),
        ('Subscribe', 'הירשמו'),
        ('No spam. Unsubscribe anytime.', 'אין ספאם. הסרה בכל עת.'),
    ],

    'site-contact.html': [
        ('Contact Us — EXPOSE', 'צרו קשר — EXPOSE'),
        ('Get in touch with the EXPOSE team. We\'re real people who love what we do — and we\'d love to hear from you. Usually reply within 24 hours.', 'צרו קשר עם צוות EXPOSE. אנחנו אנשים אמיתיים שאוהבים את מה שאנחנו עושים — ונשמח לשמוע מכם. בדרך כלל עונים תוך 24 שעות.'),
        # Hero
        ('We\'re here.<br><span class="italic-accent">Say hello.</span>', 'אנחנו כאן.<br><span class="italic-accent">שלחו שלום.</span>'),
        ('We built EXPOSE because creatives deserve better tools and brands deserve real connections. Whether you have a big idea, a quick question, or just want to say hi — we genuinely want to hear from you.', 'בנינו את EXPOSE כי יוצרים מגיעים לכלים טובים יותר ומותגים מגיעים לחיבורים אמיתיים. בין אם יש לכם רעיון גדול, שאלה מהירה, או פשוט רוצים לומר שלום — אנחנו באמת רוצים לשמוע מכם.'),
        ('Usually replies within 24h', 'בדרך כלל עונים תוך 24 שעות'),
        ('Real humans, not bots', 'בני אדם אמיתיים, לא בוטים'),
        ('English &amp; Hebrew', 'עברית ואנגלית'),
        # Form section
        ('Get in touch', 'צרו קשר'),
        ('Tell us what\'s on your mind', 'ספרו לנו מה אתם חושבים'),
        ('Whether you\'re a brand ready to launch campaigns, a creative looking to grow, or just want to explore — we\'d love to start a conversation.', 'בין אם אתם מותג מוכן להשיק קמפיינים, יוצר שרוצה לצמוח, או פשוט רוצים לחקור — נשמח להתחיל שיחה.'),
        # Topic pills
        ('What\'s this about?', 'על מה זה?'),
        ('Just saying hi', 'רק אומרים שלום'),
        ('I\'m a Brand', 'אני מותג'),
        ('I\'m a Creative', 'אני יוצר'),
        ('Partnerships', 'שיתופי פעולה'),
        ('Press &amp; Media', 'עיתונות ומדיה'),
        ('Press & Media', 'עיתונות ומדיה'),
        # Form fields
        ('Your name', 'השם שלכם'),
        ('What should we call you?', 'מה לקרוא לכם?'),
        ('Email address', 'כתובת אימייל'),
        ('Where can we reach you?', 'איך ניצור איתכם קשר?'),
        ('Your message', 'ההודעה שלכם'),
        ('We\'re all ears. The more context you share, the better we can help — though a simple \'hi\' works too.', 'אנחנו כולנו אוזניים. ככל שתשתפו יותר הקשר, כך נוכל לעזור טוב יותר — אם כי גם \'שלום\' פשוט עובד.'),
        ('Send message', 'שלחו הודעה'),
        ('We keep your info private. No spam, ever.', 'אנחנו שומרים על הפרטיות שלכם. אין ספאם, לעולם.'),
        # Success state
        ('Message sent!', 'ההודעה נשלחה!'),
        ('A real person on our team will read this and reply personally. We usually get back within a few hours during business days.', 'אדם אמיתי בצוות שלנו יקרא את זה ויענה אישית. בדרך כלל חוזרים תוך כמה שעות בימי עסקים.'),
        ('Send another message', 'שלחו הודעה נוספת'),
        # Sidebar
        ('Our team reads every message', 'הצוות שלנו קורא כל הודעה'),
        ('You\'re not talking to a ticket system', 'אתם לא מדברים עם מערכת כרטיסים'),
        ('Fast response', 'תגובה מהירה'),
        ('Usually within a few hours on business days', 'בדרך כלל תוך כמה שעות בימי עסקים'),
        ('Other ways to reach us', 'דרכים נוספות ליצירת קשר'),
        ('hello@expose.global', 'hello@expose.global'),
        ('Email', 'אימייל'),
        ('+972 79-698-9365', '+972 79-698-9365'),
        ('EXPOSE Global', 'EXPOSE Global'),
        ('@exposse.global', '@exposse.global'),
        ('@expose.global', '@expose.global'),
        ('Based in Tel Aviv, Israel · Working with creatives worldwide', 'מבוססים בתל אביב, ישראל · עובדים עם יוצרים ברחבי העולם'),
        # Starting points
        ('Not sure where to start?', 'לא בטוחים מאין להתחיל?'),
        ('Pick what fits.<br><span class="italic-accent">We\'ll take it from there.</span>', 'בחרו מה מתאים.<br><span class="italic-accent">אנחנו נמשיך משם.</span>'),
        ('I\'m a Brand', 'אני מותג'),
        ('Looking to launch creator campaigns, find the right talent, or get a personalized product demo from our team.', 'מחפשים להשיק קמפיינים עם יוצרים, למצוא כישרון מתאים, או לקבל הדגמת מוצר מותאמת אישית מהצוות שלנו.'),
        ('I\'m a Creative', 'אני יוצר'),
        ('Want to grow my career, get matched with brands that fit my style, or learn more about what EXi can do for me.', 'רוצה לצמוח בקריירה, להיות מותאם למותגים שמתאימים לסגנוני, או ללמוד עוד על מה ש-EXi יכול לעשות עבורי.'),
        ('Let\'s Partner', 'בואו נשתף פעולה'),
        ('Interested in integrations, media coverage, co-marketing, or a strategic partnership with the EXPOSE team.', 'מתעניינים באינטגרציות, סיקור מדיה, שיווק משותף, או שותפות אסטרטגית עם צוות EXPOSE.'),
        ('Start a conversation', 'התחילו שיחה'),
    ],
}


def add_heebo_font(html: str) -> str:
    """Add Heebo font after existing font link."""
    return html.replace(
        'rel="stylesheet">',
        'rel="stylesheet">\n' + HEEBO_FONT,
        1
    )


def set_rtl(html: str) -> str:
    """Set lang=he and dir=rtl."""
    html = html.replace('<html lang="en">', '<html lang="he" dir="rtl">', 1)
    return html


def add_rtl_css(html: str) -> str:
    """Add RTL overrides before </style>."""
    idx = html.rfind('</style>')
    if idx == -1:
        return html
    return html[:idx] + RTL_CSS + html[idx:]


def add_lang_switcher(html: str, en_page: str) -> str:
    """Add language switcher button linking to English page."""
    switcher = f'<a href="{en_page}" class="lang-switch" aria-label="English version">EN</a>'
    # Insert before closing </nav>
    html = html.replace('  <div></div>\n</nav>', f'  {switcher}\n</nav>', 1)
    # Fallback: try to insert after nav-logo div
    if f'href="{en_page}"' not in html:
        html = html.replace(
            '</div>\n</nav>',
            f'</div>\n  {switcher}\n</nav>',
            1
        )
    return html


def update_internal_links(html: str) -> str:
    """Replace English .html links with Hebrew -he.html counterparts."""
    for en, he in LINKS_MAP.items():
        html = html.replace(f'href="{en}"', f'href="{he}"')
        html = html.replace(f"href='{en}'", f"href='{he}'")
    return html


def apply_translations(html: str, page_key: str) -> str:
    """Apply all text translations for the given page."""
    translations = list(COMMON_TRANSLATIONS)
    if page_key in PAGE_TRANSLATIONS:
        translations = list(PAGE_TRANSLATIONS[page_key]) + translations
    for en, he in translations:
        html = html.replace(en, he)
    return html


def process_page(src_file: str, dst_file: str, en_page: str) -> None:
    """Read, transform, and write a Hebrew page."""
    with open(src_file, 'r', encoding='utf-8') as f:
        html = f.read()

    html = set_rtl(html)
    html = add_heebo_font(html)
    html = add_rtl_css(html)
    html = update_internal_links(html)
    html = apply_translations(html, en_page)
    html = add_lang_switcher(html, en_page)

    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Created: {dst_file}')


def add_en_switcher(src_file: str, he_page: str) -> None:
    """Add language switcher to English page linking to Hebrew counterpart."""
    with open(src_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Only add if not already present
    if f'href="{he_page}"' in html:
        print(f'  Switcher already in {src_file}')
        return

    switcher = f'<a href="{he_page}" class="lang-switch" aria-label="גרסה בעברית">עברית</a>'
    lang_switch_css = """
/* Language switcher */
.lang-switch {
  font-size: 12px; font-weight: 700; letter-spacing: .04em;
  padding: 6px 12px; border-radius: 20px;
  border: 1px solid rgba(255,106,26,.35);
  color: var(--orange); background: transparent;
  transition: background .15s, color .15s;
  cursor: pointer; text-decoration: none;
  display: inline-block; line-height: 1;
}
.lang-switch:hover { background: var(--orange); color: #fff; }
"""

    # Add CSS if not present
    if '.lang-switch' not in html:
        idx = html.rfind('</style>')
        if idx != -1:
            html = html[:idx] + lang_switch_css + html[idx:]

    # Insert before </nav>
    html = html.replace('  <div></div>\n</nav>', f'  {switcher}\n</nav>', 1)
    if f'href="{he_page}"' not in html:
        html = html.replace('</div>\n</nav>', f'</div>\n  {switcher}\n</nav>', 1)

    with open(src_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Updated EN: {src_file}')


PAGES = [
    ('site.html',            'site-he.html'),
    ('site-brands.html',     'site-brands-he.html'),
    ('site-exi.html',        'site-exi-he.html'),
    ('site-exi-brands.html', 'site-exi-brands-he.html'),
    ('site-about.html',      'site-about-he.html'),
    ('site-blog.html',       'site-blog-he.html'),
    ('site-contact.html',    'site-contact-he.html'),
]

import os
os.chdir('/home/claude/repo')

print('Creating Hebrew pages...')
for en, he in PAGES:
    process_page(en, he, en)

print('\nAdding language switcher to English pages...')
for en, he in PAGES:
    add_en_switcher(en, he)

print('\nDone! Files created:')
for _, he in PAGES:
    size = os.path.getsize(he)
    print(f'  {he} ({size:,} bytes)')
