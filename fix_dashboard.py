#!/usr/bin/env python3
"""Fix dashboard labels and remaining content in Hebrew pages."""
import re, os

os.chdir('/home/claude/repo')

def tr(html, en, he):
    if en in html:
        html = html.replace(en, he)
    return html

def fix(fname, fixes):
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    for en, he in fixes:
        html = tr(html, en, he)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    he_count = len(re.findall('[א-ת]', html))
    print(f'  {fname}: {he_count} Hebrew chars')

# ─── site-exi-he.html dashboard ───────────────────────────────
EXI_DASHBOARD = [
    # Dashboard header text
    ('<p>Optimizing Your Career', '<p>מייעל את הקריירה שלכם'),
    # Dashboard card labels
    ('<div class="dc-label">Active Proposal</div>',
     '<div class="dc-label">הצעות פעילות</div>'),
    # Broken translation from earlier: "Profile צפייהs"
    ('<div class="dc-label">Profile צפייהs</div>',
     '<div class="dc-label">צפיות בפרופיל</div>'),
    ('<div class="dc-label">Social Media Eng</div>',
     '<div class="dc-label">מעורבות רשתות</div>'),
    ('<div class="dc-label">Projects Matches</div>',
     '<div class="dc-label">התאמות פרויקטים</div>'),
    # Knows grid items (content in <p> tags inside the grid)
    ('Engagement, reach &amp; best posting times',
     'מעורבות, טווח וזמני פרסום אופטימליים'),
    ('Trending sounds, reach &amp; video performance',
     'צלילים טרנדיים, טווח וביצועי וידאו'),
    ('Scores, optimizes &amp; tracks acceptance rates',
     'מדרג, מייעל ועוקב אחר שיעורי קבלה'),
    ('Manages availability &amp; books shoots for you',
     'מנהל זמינות ומזמין צילומים בשבילכם'),
    ('In-demand styles, niches &amp; brand activity',
     'סגנונות, נישות ופעילות מותגים מבוקשים'),
    ('Earnings tracking &amp; market rate benchmarks',
     'מעקב הכנסות ומדדי שוק'),
    ('Scans open briefs &amp; pre-matches to your style',
     'סורק בריפים פתוחים ומתאים לסגנונכם'),
    ('Ranks you vs top creatives in your niche',
     'מדרג אתכם מול יוצרים מובילים בנישה'),
]

# ─── site-exi-brands-he.html dashboard ───────────────────────────────
EXI_BRANDS_DASHBOARD = [
    ('<span class="dash-title">EXI BRAND DASHBOARD</span>',
     '<span class="dash-title">לוח בקרה EXi</span>'),
    ('<p>Managing your campaigns', '<p>מנהל את הקמפיינים שלכם'),
    ('<div class="dc-label">Active Campaigns</div>',
     '<div class="dc-label">קמפיינים פעילים</div>'),
    ('<div class="dc-label">Creator Match Rate</div>',
     '<div class="dc-label">שיעור התאמת יוצרים</div>'),
    ('<div class="dc-trend" style="text-transform:uppercase;font-size:9px;letter-spacing:.06em">Above Average</div>',
     '<div class="dc-trend" style="text-transform:uppercase;font-size:9px;letter-spacing:.06em">מעל ממוצע</div>'),
    ('<div class="dc-label">Social Media Eng</div>',
     '<div class="dc-label">מעורבות רשתות</div>'),
    ('<div class="dc-label">Content Ready</div>',
     '<div class="dc-label">תוכן מוכן</div>'),
    ('          24/7 monitoring',
     '          ניטור 24/7'),
    ('<div class="de-label">Campaign reach this week</div>',
     '<div class="de-label">טווח קמפיין השבוע</div>'),
    # Knows grid
    ('Business Ad performance, reach &amp; ROAS metrics',
     'ביצועי פרסום, טווח ומדדי ROAS'),
    ('Creator performance tracking &amp; content monitoring',
     'מעקב ביצועי יוצרים וניטור תוכן'),
    ('Campaign analytics, audience data &amp; trend signals',
     'אנליטיקת קמפיין, נתוני קהל ואיתותי מגמות'),
    ('Content calendar management &amp; delivery tracking',
     'ניהול לוח תוכן ומעקב אספקה'),
    ('Competitor campaigns, creator moves &amp; market shifts',
     'קמפיינים מתחרים, מהלכי יוצרים ומשמרות שוק'),
    ('Invoice tracking, payment status &amp; budget alerts',
     'מעקב חשבוניות, סטטוס תשלומים והתראות תקציב'),
    ('Contract terms, compliance checks &amp; deliverable status',
     'תנאי חוזה, בדיקות תאימות וסטטוס ספקים'),
    ('Audience overlap, demographic fit &amp; psychographic matching',
     'חפיפת קהלים, התאמה דמוגרפית ותאימות פסיכוגרפית'),
]

# ─── site-about-he.html ───────────────────────────────
ABOUT_FIXES = [
    ('<span class="section-eyebrow sr">The Origin</span>',
     '<span class="section-eyebrow sr">הסיפור</span>'),
    ('<span class="section-eyebrow sr">Why We Exist</span>',
     '<span class="section-eyebrow sr">למה אנחנו כאן</span>'),
    # Origin bio paragraph
    ("Dorel Shnaiderman spent years as a working creative — shooting campaigns, designing brands, chasing down clients for payments that never came on time. He watched brilliant people go unnoticed while average work got pushed by the right agencies. The unfairness wasn't subtle. It was baked in.",
     'דורל שניידרמן בילה שנים כיוצר עצמאי — צולם קמפיינים, עיצב מותגים, ורדף אחרי לקוחות לתשלומים שאחרו. הוא צפה באנשים מוכשרים שנשארים בצל בזמן שעבודות בינוניות קיבלו את הבמה. חוסר הצדק לא היה עדין. הוא היה מובנה במערכת.'),
    # Activity feed in hero section
    ('Recent activity', 'פעילות אחרונה'),
    ('Creator matched with campaign', 'יוצר הותאם לקמפיין'),
    ('New brand brief posted', 'בריף מותג חדש פורסם'),
    ('Payment sent to creator', 'תשלום נשלח ליוצר'),
    ('4.9 avg. rating', 'דירוג ממוצע 4.9'),
]

# ─── site-he.html remaining dashboard content ───────────────────────────────
SITE_DASHBOARD = [
    # Hero dashboard remaining
    ('New brief match', 'התאמה לבריף חדש'),
    ('Editorial — Vogue Italia', 'אדיטוריאל — Vogue Italia'),
    ('· 3 weeks · Milan', '· 3 שבועות · מילאנו'),
    ('Payment landed', 'תשלום התקבל'),
    ('+$8,500 from Nike', '+$8,500 מ-Nike'),
    ('2 min ago · Cleared', 'לפני 2 דק\' · הועבר'),
    ('12 pitches sent today', '12 פיצ\'ים נשלחו היום'),
    ('Asanaké — SS25 Lookbook', 'Asanaké — SS25 לוקבוק'),
    ('· 5 weeks · Lisbon', '· 5 שבועות · ליסבון'),
    ('Editorial', 'אדיטוריאל'),
    # fc-stats labels
    ('        <span class="lbl">Creatives</span>', '        <span class="lbl">יוצרים</span>'),
]

# ─── site-brands-he.html remaining ───────────────────────────────
BRANDS_DASHBOARD = [
    ('Campaign live', 'קמפיין פעיל'),
    ('Nike — Summer Drop \'25', 'Nike — Summer Drop \'25'),
    ('14 creatives', '14 יוצרים'),
    ('· 3 cities · Active', '· 3 ערים · פעיל'),
    ('+340% engagement', '+340% מעורבות'),
    ('8 briefs matched today', '8 בריפים הותאמו היום'),
    ('Asanaké — SS25 Campaign', 'Asanaké — SS25 קמפיין'),
    ('· 6 weeks · Paris', '· 6 שבועות · פריז'),
    ('Photography', 'צילום'),
    ('        <span class="lbl">Brands active</span>', '        <span class="lbl">מותגים פעילים</span>'),
    ('        <span class="lbl">Creatives in network</span>', '        <span class="lbl">יוצרים ברשת</span>'),
    ('        <span class="lbl">Avg. campaign ROI</span>', '        <span class="lbl">ROI קמפיין ממוצע</span>'),
]

print('Fixing dashboard and remaining content...')
fix('site-exi-he.html', EXI_DASHBOARD)
fix('site-exi-brands-he.html', EXI_BRANDS_DASHBOARD)
fix('site-about-he.html', ABOUT_FIXES)
fix('site-he.html', SITE_DASHBOARD)
fix('site-brands-he.html', BRANDS_DASHBOARD)
print('\nDone.')
