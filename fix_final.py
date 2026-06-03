#!/usr/bin/env python3
"""Final comprehensive fix for all remaining English content in Hebrew pages."""
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

# Creative disciplines (shared across site-he and site-brands-he)
DISCIPLINES = [
    ('<span class="dot"></span>Branding</span>', '<span class="dot"></span>מיתוג</span>'),
    ('<span class="dot"></span>Photography</span>', '<span class="dot"></span>צילום</span>'),
    ('<span class="dot"></span>Video Editing</span>', '<span class="dot"></span>עריכת וידאו</span>'),
    ('<span class="dot"></span>Modeling</span>', '<span class="dot"></span>מודלינג</span>'),
    ('<span class="dot"></span>Copywriting</span>', '<span class="dot"></span>כתיבה שיווקית</span>'),
    ('<span class="dot"></span>Social Posting</span>', '<span class="dot"></span>סושיאל</span>'),
    ('<span class="dot"></span>Illustration</span>', '<span class="dot"></span>איורים</span>'),
    ('<span class="dot"></span>Art Direction</span>', '<span class="dot"></span>ניהול אמנותי</span>'),
    ('<span class="dot"></span>Animation</span>', '<span class="dot"></span>אנימציה</span>'),
]

# ─── site-he.html ───────────────────────────────
SITE_FINAL = DISCIPLINES + [
    ('<b>2,439+</b> verified creatives', '<b>2,439+</b> יוצרים מאומתים'),
    ('<span class="stars">★★★★★</span> 4.9 <span class="dot">·</span> trusted in 14 cities',
     '<span class="stars">★★★★★</span> 4.9 <span class="dot">·</span> נאמן ב-14 ערים'),
    ('Full marketing visibility.', 'נראות שיווקית מלאה.'),
]

# ─── site-brands-he.html ───────────────────────────────
BRANDS_FINAL = DISCIPLINES + [
    ('<b>2,439+</b> verified creatives', '<b>2,439+</b> יוצרים מאומתים'),
    ('brands shipping weekly', 'מותגים משגרים שבועית'),
    ('<span class="stars">★★★★★</span> 4.9 <span class="dot">·</span> trusted in 14 cities',
     '<span class="stars">★★★★★</span> 4.9 <span class="dot">·</span> נאמן ב-14 ערים'),
    ('Full marketing visibility.', 'נראות שיווקית מלאה.'),
]

# ─── site-exi-he.html ───────────────────────────────
EXI_FINAL = [
    # Career score section labels (without &amp;, using plain &)
    ('<div class="gauge-label">Career Score</div>', '<div class="gauge-label">ציון קריירה</div>'),
    ('<div class="sb-head">Profile Visibility <span>', '<div class="sb-head">נראות פרופיל <span>'),
    ('<div class="sb-head">Social Performance <span>', '<div class="sb-head">ביצועי סושיאל <span>'),
    # Action eyebrow
    ('<div class="eyebrow sr">Action, not noise</div>', '<div class="eyebrow sr">פעולה, לא רעש</div>'),
    # kc-desc items with plain & (not &amp;)
    ('<div class="kc-desc">Engagement, reach & best posting times</div>',
     '<div class="kc-desc">מעורבות, טווח וזמני פרסום אופטימליים</div>'),
    ('<div class="kc-desc">Trending sounds, reach & video performance</div>',
     '<div class="kc-desc">צלילים טרנדיים, טווח וביצועי וידאו</div>'),
    ('<div class="kc-desc">Scores, optimizes & tracks acceptance rates</div>',
     '<div class="kc-desc">מדרג, מייעל ועוקב אחר שיעורי קבלה</div>'),
    ('<div class="kc-desc">Manages availability & books shoots for you</div>',
     '<div class="kc-desc">מנהל זמינות ומזמין צילומים בשבילכם</div>'),
    ('<div class="kc-desc">In-demand styles, niches & brand activity</div>',
     '<div class="kc-desc">סגנונות, נישות ופעילות מותגים מבוקשים</div>'),
    ('<div class="kc-desc">Earnings tracking & market rate benchmarks</div>',
     '<div class="kc-desc">מעקב הכנסות ומדדי שוק</div>'),
    ('<div class="kc-desc">Scans open briefs & pre-matches to your style</div>',
     '<div class="kc-desc">סורק בריפים פתוחים ומתאים לסגנונכם</div>'),
]

# ─── site-exi-brands-he.html ───────────────────────────────
EXI_BRANDS_FINAL = [
    ('<div class="eyebrow sr">Always connected</div>',
     '<div class="eyebrow sr">תמיד מחובר</div>'),
    # kc items with &amp;
    ('<div class="kc-desc">Ad performance, reach &amp; ROAS metrics</div>',
     '<div class="kc-desc">ביצועי פרסום, טווח ומדדי ROAS</div>'),
    ('<div class="kc-desc">Video views, CPM &amp; conversion tracking</div>',
     '<div class="kc-desc">צפיות וידאו, CPM ומעקב המרות</div>'),
    ('<div class="kc-title">Creator Database</div>', '<div class="kc-title">מאגר יוצרים</div>'),
    ('<div class="kc-desc">800+ vetted creatives across 40 niches</div>',
     '<div class="kc-desc">800+ יוצרים מאומתים ב-40 נישות</div>'),
    ('<div class="kc-title">Campaign Budget</div>', '<div class="kc-title">תקציב קמפיין</div>'),
    ('<div class="kc-desc">Spend tracking, pacing &amp; ROI optimization</div>',
     '<div class="kc-desc">מעקב הוצאות, קצב ואופטימיזציית ROI</div>'),
    ('<div class="kc-title">Market Analytics</div>', '<div class="kc-title">אנליטיקת שוק</div>'),
    ('<div class="kc-desc">Competitor brand activity &amp; trend signals</div>',
     '<div class="kc-desc">פעילות מתחרים ואיתותי מגמות</div>'),
    ('<div class="kc-desc">Deliverables, deadlines &amp; approvals workflow</div>',
     '<div class="kc-desc">ספקים, דדליינים ותהליך אישורים</div>'),
    # Fix broken CRM translation "צרו קשרs"
    ('<div class="kc-title">CRM &amp; צרו קשרs</div>', '<div class="kc-title">CRM וקשרי יוצרים</div>'),
    ('<div class="kc-desc">Creator history, relationships &amp; performance</div>',
     '<div class="kc-desc">היסטוריה, קשרים וביצועי יוצרים</div>'),
    ('<div class="kc-title">Brand Safety</div>', '<div class="kc-title">בטיחות מותג</div>'),
    ('<div class="kc-desc">Compliance checks &amp; risk monitoring 24/7</div>',
     '<div class="kc-desc">בדיקות תאימות וניטור סיכונים 24/7</div>'),
]

# ─── site-about-he.html ───────────────────────────────
ABOUT_FINAL = [
    # Why cards body text
    ("Visibility shouldn't be a privilege for people with big followings or industry connections. The right brief should find the right creator — every time.",
     'נראות לא צריכה להיות זכות יוחד לבעלי עוקבים רבים. הבריף הנכון צריך למצוא את היוצר הנכון — בכל פעם.'),
    ("We help creatives present themselves authentically. No cringe-worthy self-promotion. Just the right message, to the right people, at the right time.",
     'אנחנו עוזרים ליוצרים להציג את עצמם באותנטיות. ללא קידום עצמי מביך. רק המסר הנכון, לאנשים הנכונים, בזמן הנכון.'),
    # Journey section eyebrow
    ('<span class="section-eyebrow sr">The Journey</span>',
     '<span class="section-eyebrow sr">המסע</span>'),
    # Journey dates
    ('<div class="tl-date">Q1 2024 — The Idea Clicks</div>',
     '<div class="tl-date">Q1 2024 — הרעיון מתחדד</div>'),
    ('<div class="tl-date">Q2 2024 — Building Begins</div>',
     '<div class="tl-date">Q2 2024 — הבנייה מתחילה</div>'),
    ('<div class="tl-date">Q3 2024 — Finding Our Voice</div>',
     '<div class="tl-date">Q3 2024 — מוצאים את הקול שלנו</div>'),
    ('<div class="tl-date">2025 — Just Getting Started</div>',
     '<div class="tl-date">2025 — רק מתחילים</div>'),
    # Journey paragraphs
    ('After years of freelancing frustrations, the core idea takes shape. What if AI could handle all the admin that kills creative flow?',
     'אחרי שנים של תסכולי פרילנס, הרעיון הבסיסי מתגבש. מה אם AI יוכל לטפל בכל הבירוקרטיה שהורגת את הזרימה היצירתית?'),
    ('The first prototype is built. Rough around the edges, but EXi matches a creator with a brief for the very first time.',
     'הפרוטוטיפ הראשון נבנה. גס בקצוות, אבל EXi מתאים יוצר לבריף בפעם הראשונה.'),
    ("The brand identity comes together. EXPOSE isn't just a platform — it's a movement for creators who are done playing small.",
     'זהות המותג מתגבשת. EXPOSE הוא לא רק פלטפורמה — זו תנועה ליוצרים שסיימו לשחק קטן.'),
    ('First real users. Real projects. Real money moving to real creators. The feedback loop tells us we\'re on the right track.',
     'המשתמשים הראשונים האמיתיים. פרויקטים אמיתיים. כסף אמיתי זורם ליוצרים אמיתיים. לולאת הפידבק אומרת שאנחנו בדרך הנכונה.'),
    ('Expanding to brands. Building EXi into the most powerful creative agent in the market. הטוב ביותר עוד לפנינו.',
     'מתרחבים למותגים. בונים את EXi לסוכן היצירתי החזק ביותר בשוק. הטוב ביותר עוד לפנינו.'),
    # Manifesto
    ('<span class="manifesto-label sr">What We Believe</span>',
     '<span class="manifesto-label sr">מה אנחנו מאמינים</span>'),
    ("We're building the infrastructure for creative professionals to do their best work — and get paid what they deserve for it.",
     'אנחנו בונים את התשתית שמאפשרת לאנשי יצירה לעשות את עבודתם הטובה ביותר — ולקבל תשלום הוגן עליה.'),
    # Q4 date (has Hebrew "חי" in it)
    ('<div class="tl-date">Q4 2024 — We Go חי</div>',
     '<div class="tl-date">Q4 2024 — יוצאים לשוק</div>'),
]

# ─── site-blog-he.html ───────────────────────────────
BLOG_FINAL = [
    # Post excerpts
    ("The numbers are staggering. But the real story is in where the money is flowing — and who's being left behind.",
     'המספרים מדהימים. אבל הסיפור האמיתי הוא לאן הכסף זורם — ומי נשאר מאחור.'),
    ("A bad brief is the root cause of most failed campaigns. Here's exactly what to write — and what to stop leaving out.",
     'בריף גרוע הוא שורש רוב הקמפיינים שנכשלים. הנה בדיוק מה לכתוב — ומה להפסיק להשמיט.'),
    ("We ran the same campaign two ways. The results were uncomfortable — but unsurprising. The numbers are in.",
     'הרצנו את אותו הקמפיין בשתי דרכים. התוצאות היו לא נוחות — אך לא מפתיעות. המספרים בפנים.'),
    ("No agency. No 100K followers. No problem. The exact playbook for getting brands to come to you — and saying yes.",
     'בלי סוכנות. בלי 100K עוקבים. אין בעיה. המדריך המדויק לגרום למותגים לפנות אליכם — ולומר כן.'),
    ("We analyzed 10,000 posts. The answer isn't what most people expect — and it changes everything about your content strategy.",
     'ניתחנו 10,000 פוסטים. התשובה היא לא מה שרוב האנשים מצפים — והיא משנה הכל באסטרטגיית התוכן שלכם.'),
    ('Time, money, missed opportunities. We quantified what manual campaign ops actually costs — and it\'s not pretty.',
     'זמן, כסף, הזדמנויות שאבדו. כימתנו את מה שניהול קמפיינים ידני באמת עולה — והתוצאה לא יפה.'),
    ('From Freelancer to Studio: How to Scale Your Creative Business — the step-by-step playbook.',
     'ממדריך מפרילנסר לסטודיו — המדריך צעד אחר צעד להרחבת העסק היצירתי שלכם.'),
    # Empty category
    ('No posts in this category yet — check back soon.',
     'אין פוסטים בקטגוריה זו עדיין — חזרו בקרוב.'),
    # Newsletter sub-text
    ('One email per week. No fluff. Just what matters in the creator economy.',
     'אימייל אחד בשבוע. ללא פאפוזות. רק מה שחשוב בכלכלת היוצרים.'),
]

print('Applying final translations...')
fix('site-he.html', SITE_FINAL)
fix('site-brands-he.html', BRANDS_FINAL)
fix('site-exi-he.html', EXI_FINAL)
fix('site-exi-brands-he.html', EXI_BRANDS_FINAL)
fix('site-about-he.html', ABOUT_FINAL)
fix('site-blog-he.html', BLOG_FINAL)
print('\nDone.')
