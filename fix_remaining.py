#!/usr/bin/env python3
"""Fix all remaining untranslated strings in Hebrew pages."""
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

# ─── site-he.html ───────────────────────────────
SITE_FIXES = [
    # Animated h2 (word-by-word spans)
    ('<span class="word" style="--i:0">Stop</span>',
     '<span class="word" style="--i:0">הפסיקו</span>'),
    ('<span class="word" style="--i:1">chasing.</span>',
     '<span class="word" style="--i:1">לרדוף.</span>'),
    ('<span class="word" style="--i:2">Start</span>',
     '<span class="word" style="--i:2">התחילו</span>'),
    ('<span class="word" style="--i:3">getting</span>',
     '<span class="word" style="--i:3">לקבל</span>'),
    ('<span class="word" style="--i:4">booked.</span>',
     '<span class="word" style="--i:4">עבודות.</span>'),
    # fc-sub paragraph
    ("Your portfolio is already enough. The next brief is sitting in EXi's inbox — <b>open the app and it's yours.</b>",
     'הפורטפוליו שלכם כבר מספיק. הבריף הבא מחכה בתיבת הדואר של EXi — <b>פתחו את האפליקציה והוא שלכם.</b>'),
    # fc-cta primary button
    ('Start free — get matched <span class="arrow">→</span>',
     'התחילו בחינם — קבלו התאמות <span class="arrow">→</span>'),
    # Watch demo link
    ('        Watch 60-sec demo\n      </a>',
     '        סיור 60 שניות\n      </a>'),
    # fc-meta checkmarks
    ('✓ Free forever for creatives', '✓ חינם לתמיד ליוצרים'),
    ('✓ No credit card', '✓ ללא כרטיס אשראי'),
    ('✓ 2-min setup', '✓ הגדרה ב-2 דקות'),
    # Stats labels
    ('        <span class="lbl">Creatives</span>\n      </div>\n      <div class="fc-stat cream">',
     '        <span class="lbl">יוצרים</span>\n      </div>\n      <div class="fc-stat cream">'),
    ('        <span class="lbl">Brands matched</span>',
     '        <span class="lbl">מותגים הותאמו</span>'),
    ('        <span class="lbl">Avg. first booking</span>',
     '        <span class="lbl">הזמנה ראשונה ממוצעת</span>'),
    # footer About link
    ('>About</a>', '>אודותינו</a>'),
    # FAQ answers placeholder text (visible)
    ('Get started free', 'התחילו בחינם'),
]

# ─── site-brands-he.html ───────────────────────────────
BRANDS_FIXES = [
    # Animated h2
    ('<span class="word" style="--i:0">Stop</span>',
     '<span class="word" style="--i:0">הפסיקו</span>'),
    ('<span class="word" style="--i:1">guessing.</span>',
     '<span class="word" style="--i:1">לנחש.</span>'),
    ('<span class="word" style="--i:2">Start</span>',
     '<span class="word" style="--i:2">התחילו</span>'),
    ('<span class="word" style="--i:3">shipping</span>',
     '<span class="word" style="--i:3">לשגר</span>'),
    ('<span class="word" style="--i:4">campaigns.</span>',
     '<span class="word" style="--i:4">קמפיינים.</span>'),
    # fc-sub paragraph
    ("Brief in 60 seconds. EXi matches you with vetted creators, runs the campaign, and — <b>shows you the ROI before you ship the next one.</b>",
     'בריף תוך 60 שניות. EXi מתאים לכם יוצרים מאומתים, מנהל את הקמפיין — <b>ומציג לכם את ה-ROI לפני שמשגרים את הבא.</b>'),
    # fc-cta primary
    ('Book a demo <span class="arrow">→</span>',
     'קבעו דמו <span class="arrow">→</span>'),
    # fc-meta checkmarks
    ('✓ 14-day free trial', '✓ ניסיון חינם 14 יום'),
    ('✓ No success fees', '✓ ללא עמלת הצלחה'),
    ('✓ White-glove onboarding', '✓ הטמעה מלאה'),
    # Stats labels
    ('        <span class="lbl">Brands active</span>',
     '        <span class="lbl">מותגים פעילים</span>'),
    ('        <span class="lbl">Creatives in network</span>',
     '        <span class="lbl">יוצרים ברשת</span>'),
    ('        <span class="lbl">Avg. campaign ROI</span>',
     '        <span class="lbl">ROI קמפיין ממוצע</span>'),
    ('>About</a>', '>אודותינו</a>'),
    ('Get started free', 'התחילו בחינם'),
]

# ─── site-exi-he.html ───────────────────────────────
EXI_FIXES = [
    # CTA eyebrow
    ('<div class="cta-eyebrow">Get started free</div>',
     '<div class="cta-eyebrow">התחילו בחינם</div>'),
    # CTA paragraph (partially translated - Join → הצטרפו was applied)
    ('הצטרפו thousands of creatives already getting booked through EXPOSE.',
     'הצטרפו לאלפי יוצרים שכבר מקבלים עבודות דרך EXPOSE.'),
    ('>About</a>', '>אודותינו</a>'),
]

# ─── site-exi-brands-he.html ───────────────────────────────
EXI_BRANDS_FIXES = [
    ('<div class="cta-eyebrow">Get started free</div>',
     '<div class="cta-eyebrow">התחילו בחינם</div>'),
    # Check if Join was similarly partially translated
    ('הצטרפו thousands of brands',
     'הצטרפו לאלפי מותגים'),
    ('>About</a>', '>אודותינו</a>'),
]

# ─── site-about-he.html ───────────────────────────────
ABOUT_FIXES = [
    ('>About</a>', '>אודותינו</a>'),
]

# ─── site-blog-he.html ───────────────────────────────
BLOG_FIXES = [
    ('>About</a>', '>אודותינו</a>'),
    # Blog post titles (translate the main featured + sidebar ones)
    ('How AI Is Reshaping Campaign Management in 2025',
     'כיצד AI משנה את ניהול הקמפיינים ב-2025'),
    ('Why Brands Are Pivoting to Micro-Creators in 2025',
     'למה מותגים עוברים למיקרו-יוצרים ב-2025'),
    ('The כלכלת יוצרים Is Worth $500B — Here\'s What It Means for You',
     'כלכלת היוצרים שווה $500B — מה זה אומר עליכם'),
    ('5 Things Every Creative Brief Must Include (But Usually Doesn\'t)',
     '5 דברים שכל בריף יצירתי חייב לכלול (אבל בדרך כלל לא)'),
    ('EXi vs. Manual Workflows: A Real Side-by-Side Breakdown',
     'EXi מול תהליכים ידניים: השוואה מעמיקה'),
    ('How to Land Your First Brand Deal as an Independent Creator',
     'איך להשיג את עסקת המותג הראשונה שלכם כיוצר עצמאי'),
    ('AI-Generated vs. Human Content: What\'s Actually Winning in 2025',
     'תוכן שנוצר על ידי AI מול תוכן אנושי: מה באמת מנצח ב-2025'),
    ('The Real Cost of Managing Campaigns Without AI in 2025',
     'העלות האמיתית של ניהול קמפיינים ללא AI ב-2025'),
    ('From Freelancer to Studio: How to Scale Your Creative Business',
     'מפרילנסר לסטודיו: איך להגדיל את העסק היצירתי שלכם'),
    # Blog post meta text
    ('min read', 'דק\' קריאה'),
    # Input placeholder
    ('Your email address', 'כתובת האימייל שלכם'),
]

# ─── site-contact-he.html ───────────────────────────────
CONTACT_FIXES = [
    ('>About</a>', '>אודותינו</a>'),
]

print('Fixing remaining translations...')
fix('site-he.html', SITE_FIXES)
fix('site-brands-he.html', BRANDS_FIXES)
fix('site-exi-he.html', EXI_FIXES)
fix('site-exi-brands-he.html', EXI_BRANDS_FIXES)
fix('site-about-he.html', ABOUT_FIXES)
fix('site-blog-he.html', BLOG_FIXES)
fix('site-contact-he.html', CONTACT_FIXES)
print('\nDone.')
