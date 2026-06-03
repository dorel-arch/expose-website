#!/usr/bin/env python3
"""Final cleanup of remaining English content."""
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

SITE_LAST = [
    # Dashboard mini stats
    ('<div class="ms-title">New Briefs</div>', '<div class="ms-title">בריפים חדשים</div>'),
    ('<div class="ms-live"><span class="ms-dot"></span>3 brands matched you today</div>',
     '<div class="ms-live"><span class="ms-dot"></span>3 מותגים התאימו לכם היום</div>'),
    ('<div class="ms-card-h"><b>Adidas Originals</b></div>',
     '<div class="ms-card-h"><b>Adidas Originals</b></div>'),
    # Agent status
    ('<span class="agent-status"><span class="status-dot"></span>Online · Working for you</span>',
     '<span class="agent-status"><span class="status-dot"></span>מחובר · עובד בשבילכם</span>'),
    # Stats section
    ('<p class="sr s1">Real numbers. Real results.</p>',
     '<p class="sr s1">מספרים אמיתיים. תוצאות אמיתיות.</p>'),
    ('<div class="stat-label">Verified creatives</div>',
     '<div class="stat-label">יוצרים מאומתים</div>'),
    ('<span class="city-pin">Across 14 cities</span>',
     '<span class="city-pin">ב-14 ערים</span>'),
]

BRANDS_LAST = [
    ('<a class="btn btn-dark" href="#" onclick="goToApp(event)">Find Talent</a>',
     '<a class="btn btn-dark" href="#" onclick="goToApp(event)">מצאו יוצרים</a>'),
    # Push notifications
    ('<div class="pp-title">Spring Editorial — 2.4M impressions</div>',
     '<div class="pp-title">אדיטוריאל אביב — 2.4M חשיפות</div>'),
    ('<div class="pp-meta"><b>+34% ROI</b> · 5 days remaining</div>',
     '<div class="pp-meta"><b>+34% ROI</b> · 5 ימים נותרו</div>'),
    ('<div class="pp-head">Creator booked <span class="pp-ago">2m</span></div>',
     '<div class="pp-head">יוצר הוזמן <span class="pp-ago">2m</span></div>'),
    ('<div class="pp-title">Sofia Rossi confirmed</div>',
     '<div class="pp-title">Sofia Rossi אישרה</div>'),
    ('<div class="pp-meta">Content goes live in 48h</div>',
     '<div class="pp-meta">תוכן יוצא לאוויר תוך 48 שעות</div>'),
    # Dashboard campaign card
    ('<div class="ms-card-h"><b>Spring Editorial</b>',
     '<div class="ms-card-h"><b>אדיטוריאל אביב</b>'),
    ('<div class="ms-card-sub">2.4M reach · Sofia Rossi</div>',
     '<div class="ms-card-sub">2.4M טווח · Sofia Rossi</div>'),
]

EXI_BRANDS_LAST = [
    # "Action, not noise" on this page too
    ('<div class="eyebrow sr">Action, not noise</div>',
     '<div class="eyebrow sr">פעולה, לא רעש</div>'),
    # Action cards
    ('<div class="ac-brand">Spring Campaign</div>', '<div class="ac-brand">קמפיין אביב</div>'),
    ('<div class="ac-title">Match 5 Creators for Lifestyle Brief</div>',
     '<div class="ac-title">התאמת 5 יוצרים לבריף לייפסטייל</div>'),
    ('<div class="ac-desc">Lifestyle &amp; fashion niche — 4-week timeline, 3 deliverables each</div>',
     '<div class="ac-desc">נישת לייפסטייל ואופנה — לוח 4 שבועות, 3 ספקים לכל יוצר</div>'),
    ('          93% avg. fit score\n        </div>',
     '          93% ניקוד התאמה ממוצע\n        </div>'),
    ('<button class="ac-btn approve" onclick="approveCard(this)">Approve</button>',
     '<button class="ac-btn approve" onclick="approveCard(this)">אשרו</button>'),
    ('<button class="ac-btn skip" onclick="skipCard(this)">Skip</button>',
     '<button class="ac-btn skip" onclick="skipCard(this)">דלגו</button>'),
    ('<div class="ac-brand">Performance</div>', '<div class="ac-brand">ביצועים</div>'),
    ('<div class="ac-title">Pause @creator — Below Engagement Target</div>',
     '<div class="ac-title">השהיית @creator — מתחת ליעד המעורבות</div>'),
    ('<div class="ac-desc">Engagement dropped 40% below brief threshold — EXi suggests pausing</div>',
     '<div class="ac-desc">המעורבות ירדה 40% מתחת לסף הבריף — EXi מציע להשהות</div>'),
    ('          Save $1,200 in spend\n        </div>',
     '          חיסכון של $1,200 בהוצאות\n        </div>'),
    # Budget card (partial Hebrew already)
    ('<div class="ac-title">הקצה מחדש $2,000 to Campaign #3</div>',
     '<div class="ac-title">הקצו מחדש $2,000 לקמפיין #3</div>'),
    ('<div class="ac-desc">Campaign #3 is outperforming target by 2.1x — more budget = more ROI</div>',
     '<div class="ac-desc">קמפיין #3 עולה על היעד ב-2.1x — יותר תקציב = יותר ROI</div>'),
    ('          +2.1x ROI potential\n        </div>',
     '          +2.1x פוטנציאל ROI\n        </div>'),
]

ABOUT_LAST = [
    # Team role
    ('<div class="tc-role">Co-Founder &amp; CTO</div>',
     '<div class="tc-role">מייסד שותף ו-CTO</div>'),
    # Team quote
    ('<blockquote>We\'re not just building a product, we\'re building a home for creative professionals. A place where people learn, grow, and support each other. That\'s what gets me up in the morning.</blockquote>',
     '<blockquote>אנחנו לא רק בונים מוצר, אנחנו בונים בית לאנשי יצירה. מקום שבו אנשים לומדים, צומחים ותומכים אחד בשני. זה מה שגורם לי לקום בבוקר.</blockquote>'),
    # Activity timestamps
    ('<div class="hm-act-time">2m ago</div>', '<div class="hm-act-time">לפני 2 דק\'</div>'),
    ('<div class="hm-act-time">5m ago</div>', '<div class="hm-act-time">לפני 5 דק\'</div>'),
]

CONTACT_LAST = [
    # Language support note (plain & not &amp;)
    ('        English & Hebrew\n', '        עברית ואנגלית\n'),
]

print('Applying last translations...')
fix('site-he.html', SITE_LAST)
fix('site-brands-he.html', BRANDS_LAST)
fix('site-exi-brands-he.html', EXI_BRANDS_LAST)
fix('site-about-he.html', ABOUT_LAST)
fix('site-contact-he.html', CONTACT_LAST)
print('\nDone.')
