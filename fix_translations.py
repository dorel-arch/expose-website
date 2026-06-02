#!/usr/bin/env python3
"""Fix remaining untranslated strings that have inline HTML tags."""
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

# Shared inline-tag patterns used across exi pages
EXI_SHARED = [
    ('EXi <span class="italic-accent" style="font-size:32px">Never Sleeps</span>',
     'EXi <span class="italic-accent" style="font-size:32px">לעולם לא ישן</span>'),
    ('EXi acts.<br><span class="italic-accent">You approve.</span>',
     'EXi פועל.<br><span class="italic-accent">אתם מאשרים.</span>'),
    ("EXi doesn't stop<br><span class=\"italic-accent\">when you do.</span>",
     'EXi לא מפסיק<br><span class="italic-accent">כשאתם מפסיקים.</span>'),
    ('One agent,<br><span class="italic-accent">total control.</span>',
     'סוכן אחד,<br><span class="italic-accent">שליטה מלאה.</span>'),
    ("You're always<br><span class=\"italic-accent\">in control</span>",
     'אתם תמיד<br><span class="italic-accent">בשליטה</span>'),
]

EXI_HE_FIXES = EXI_SHARED + [
    # h1 - exi page
    ('The Agent that works for you 24/7',
     'הסוכן שעובד בשבילכם 24/7'),
    # Career score section
    ("You don't need an agency<br>to know your <span class=\"italic-accent\">worth</span>",
     'אתם לא צריכים סוכנות<br>כדי לדעת את <span class="italic-accent">הערך שלכם</span>'),
    # CTA
    ('Ready to get<br><span class="italic-accent">discovered?</span>',
     'מוכנים<br><span class="italic-accent">להיחשף?</span>'),
]

EXI_BRANDS_HE_FIXES = EXI_SHARED + [
    # h1 - exi-brands page with styled em tag
    ('The Agent that runs your campaigns <em style="font-family:\'Instrument Serif\',serif;font-style:italic;font-weight:400;color:var(--orange)">24/7</em>',
     'הסוכן שמנהל את הקמפיינים שלכם <em style="font-family:\'Instrument Serif\',serif;font-style:italic;font-weight:400;color:var(--orange)">24/7</em>'),
    # Real data section
    ('Real data. Real ROI.<br>No <span class="italic-accent">guesswork.</span>',
     'נתונים אמיתיים. ROI אמיתי.<br>בלי <span class="italic-accent">ניחושים.</span>'),
    # CTA
    ('Ready for smarter<br><span class="italic-accent">campaigns?</span>',
     'מוכנים לקמפיינים<br><span class="italic-accent">חכמים יותר?</span>'),
]

ABOUT_HE_FIXES = [
    ('This is just<br><em>the beginning.</em>',
     'זה רק<br><em>ההתחלה.</em>'),
    ('Real people who <em class="italic-accent">care.</em>',
     'אנשים אמיתיים ש<em class="italic-accent">אכפת להם.</em>'),
    ('Ready to be part of<br><em class="italic-accent">something real?</em>',
     'מוכנים להיות חלק מ<br><em class="italic-accent">משהו אמיתי?</em>'),
]

BRANDS_HE_FIXES = [
    ('Finally understand your marketing. <span class="muted" style="color: var(--orange);">And make it work.</span>',
     'סוף סוף הבינו את השיווק שלכם. <span class="muted" style="color: var(--orange);">וגרמו לו לעבוד.</span>'),
]

print('Fixing remaining translations...')
fix('site-exi-he.html', EXI_HE_FIXES)
fix('site-exi-brands-he.html', EXI_BRANDS_HE_FIXES)
fix('site-about-he.html', ABOUT_HE_FIXES)
fix('site-brands-he.html', BRANDS_HE_FIXES)
print('\nDone.')
