#!/usr/bin/env python3
"""Final remaining translations — counter labels, activity feeds, dashboard mini."""
import re, os

os.chdir('/home/claude/repo')

def fix(fname, fixes):
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    for en, he in fixes:
        if en in html:
            html = html.replace(en, he)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    he_count = len(re.findall('[א-ת]', html))
    print(f'  {fname}: {he_count} Hebrew chars')

SITE_FIXES = [
    # Counter stat labels (site-he has same fc-stat section)
    ('<span class="lbl">Briefs / mo</span>', '<span class="lbl">בריפים / חודש</span>'),
    ('<span class="lbl">Rating</span>', '<span class="lbl">דירוג</span>'),
    ('<span class="lbl">Paid out</span>', '<span class="lbl">שולם</span>'),
    ('<span class="lbl">Cities</span>', '<span class="lbl">ערים</span>'),
    # Dashboard mini brief cards subtitles
    ('<div class="ms-card-sub">אדיטוריאל campaign</div>',
     '<div class="ms-card-sub">קמפיין אדיטוריאל</div>'),
    ('<div class="ms-card-sub">Photography · SS25</div>',
     '<div class="ms-card-sub">צילום · SS25</div>'),
    ('<div class="ms-card-sub">אדיטוריאל set</div>',
     '<div class="ms-card-sub">סט אדיטוריאל</div>'),
    # ms-time deadline labels
    ('<span class="ms-time">5 days</span>', '<span class="ms-time">5 ימים</span>'),
    ('<span class="ms-time">2 days</span>', '<span class="ms-time">2 ימים</span>'),
    ('<span class="ms-time">1 week</span>', '<span class="ms-time">שבוע</span>'),
    # Activity ticker feed (creators)
    ('</b> got booked for Vogue Italia<span class="ago">',
     '</b> הוזמן/ה ל-Vogue Italia<span class="ago">'),
    ('</b> shipped a Nike editorial<span class="ago">',
     '</b> שיגר/ה אדיטוריאל Nike<span class="ago">'),
    ('</b> raised her rate to $140/hr<span class="ago">',
     '</b> העלתה את התעריף ל-$140/שעה<span class="ago">'),
    ('</b> got 3 new matches<span class="ago">',
     '</b> קיבל/ה 3 התאמות חדשות<span class="ago">'),
    ('</b> closed a brand campaign<span class="ago">',
     '</b> סגר/ה קמפיין מותג<span class="ago">'),
    ('</b> hit $10K this month<span class="ago">',
     '</b> הגיע/ה ל-$10K החודש<span class="ago">'),
]

BRANDS_FIXES = [
    # Hero card "Booked" notification
    ('<div class="hc-head"><span class="live-dot"></span> Booked</div>',
     '<div class="hc-head"><span class="live-dot"></span> הוזמן</div>'),
    # Hero subtitle (main platform description)
    ('<p class="hero-sub sr s1">The AI platform that finds, books, and manages top creative talent for your brand — so you scale faster with less effort.</p>',
     '<p class="hero-sub sr s1">הפלטפורמה המופעלת על ידי AI שמוצאת, מזמינה ומנהלת את הכישרונות היצירתיים המובילים עבור המותג שלכם — כדי שתצמחו מהר יותר עם פחות מאמץ.</p>'),
    # "AI insights" feature label
    ('<div class="eyebrow sr">AI insights</div>', '<div class="eyebrow sr">תובנות AI</div>'),
    # "now" timestamp
    ('<span class="pp-ago">now</span>', '<span class="pp-ago">עכשיו</span>'),
    # Campaign ticker activity items missing translation
    ('<b>Northwind</b> shipped to 4 markets<span',
     '<b>Northwind</b> שיגרה ל-4 שווקים<span'),
    ('<b>Sonas</b> matched with 12 creators<span',
     '<b>Sonas</b> הותאמה עם 12 יוצרים<span'),
    ('<b>Asanaké</b> just joined<span',
     '<b>Asanaké</b> הצטרפה זה עתה<span'),
    ('<b>Form Studio</b> closed a launch<span',
     '<b>Form Studio</b> סגרה השקה<span'),
    # Filter buttons
    ('<button data-c="peach"><span class="emo">✏️</span>Design</button>',
     '<button data-c="peach"><span class="emo">✏️</span>עיצוב</button>'),
    ('<button data-c="lilac"><span class="emo">🎞️</span>Motion</button>',
     '<button data-c="lilac"><span class="emo">🎞️</span>מוציון</button>'),
    ('<button data-c="sand"><span class="emo">👗</span>Styling</button>',
     '<button data-c="sand"><span class="emo">👗</span>סטיילינג</button>'),
    # Dashboard card sub for Run Club SS25
    ('<div class="ms-card-sub">Run Club SS25</div>',
     '<div class="ms-card-sub">Run Club SS25</div>'),
    # Testimonial role labels remaining
    ('<span>Brand Manager · Rivet Supply</span>', '<span>מנהל/ת מותג · Rivet Supply</span>'),
    ('<span>Growth Lead · Moray Beauty</span>', '<span>מוביל/ת צמיחה · Moray Beauty</span>'),
    ('<span>CMO · Asanaké</span>', '<span>CMO · Asanaké</span>'),
    ('<span>CMO · Lumen Skincare</span>', '<span>CMO · Lumen Skincare</span>'),
    ('<span>Founder · Northwind</span>', '<span>מייסד/ת · Northwind</span>'),
    ('<span>Marketing Director · Sonas</span>', '<span>מנהל/ת שיווק · Sonas</span>'),
    ('<span class="role-tag">Growth</span>', '<span class="role-tag">צמיחה</span>'),
    ('<span class="role-tag">Brand Mgr</span>', '<span class="role-tag">מנהל/ת מותג</span>'),
    ('<span class="role-tag">Mkt Director</span>', '<span class="role-tag">מנהל/ת שיווק</span>'),
]

print('Applying final remaining translations...')
fix('site-he.html', SITE_FIXES)
fix('site-brands-he.html', BRANDS_FIXES)
print('\nDone.')
