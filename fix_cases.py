#!/usr/bin/env python3
"""Fix case studies, campaigns section, and remaining creator cards."""
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

# Shared case study labels
CASE_SHARED = [
    # Case meta labels (with SVG)
    ('<span class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 19c.7-3.2 3.3-5 6.5-5s5.8 1.8 6.5 5"/><circle cx="17" cy="7" r="2.6"/><path d="M16 13c2.7 0 4.7 1.4 5.5 4"/></svg>Crew</span>',
     '<span class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 19c.7-3.2 3.3-5 6.5-5s5.8 1.8 6.5 5"/><circle cx="17" cy="7" r="2.6"/><path d="M16 13c2.7 0 4.7 1.4 5.5 4"/></svg>צוות</span>'),
    ('<span class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>Shot in</span>',
     '<span class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 22s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>צולם ב-</span>'),
    ('<span class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>Time</span>',
     '<span class="lbl"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>זמן</span>'),
    ('<span class="lbl">The crew</span>', '<span class="lbl">הצוות</span>'),
    # Location values
    ('<span class="val">Milan, IT</span>', '<span class="val">מילאנו, IT</span>'),
    ('<span class="val">Lisbon, PT</span>', '<span class="val">ליסבון, PT</span>'),
    ('<span class="val">Tokyo, JP</span>', '<span class="val">טוקיו, JP</span>'),
    ('<span class="val">Madrid, ES</span>', '<span class="val">מדריד, ES</span>'),
    ('<span class="val">Paris, FR</span>', '<span class="val">פריז, FR</span>'),
    ('<span class="val">Tel Aviv, IL</span>', '<span class="val">תל אביב, IL</span>'),
    # Case tags
    ('<span class="case-tag">Lookbook</span>', '<span class="case-tag">לוקבוק</span>'),
    ('<span class="case-tag">Editorial</span>', '<span class="case-tag">אדיטוריאל</span>'),
    # Campaign titles with brands (only the descriptive part)
    ('<b class="title">Sonas Sunshine — FW24 Hero Campaign</b>',
     '<b class="title">Sonas Sunshine — קמפיין FW24 ראשי</b>'),
    # Weeks values
    ('<span class="val">3 weeks</span>', '<span class="val">3 שבועות</span>'),
    ('<span class="val">4 weeks</span>', '<span class="val">4 שבועות</span>'),
    ('<span class="val">5 weeks</span>', '<span class="val">5 שבועות</span>'),
    ('<span class="val">6 weeks</span>', '<span class="val">6 שבועות</span>'),
    ('<span class="val">2 weeks</span>', '<span class="val">2 שבועות</span>'),
    ('<span class="val">8 pros</span>', '<span class="val">8 מקצועניים</span>'),
    ('<span class="val">5 pros</span>', '<span class="val">5 מקצועניים</span>'),
    ('<span class="val">6 pros</span>', '<span class="val">6 מקצועניים</span>'),
    ('<span class="val">4 pros</span>', '<span class="val">4 מקצועניים</span>'),
    ('<span class="val">3 pros</span>', '<span class="val">3 מקצועניים</span>'),
    # Browse/see more
    ('        Browse all campaigns', '        עיינו בכל הקמפיינים'),
]

SITE_CASES = CASE_SHARED + [
    # Creator roles in community section (different from JS data)
    ('<div class="role">Art Director</div>', '<div class="role">ניהול אמנותי</div>'),
    ('<div class="role">Motion Designer</div>', '<div class="role">מעצב/ת מוציון</div>'),
]

BRANDS_CASES = CASE_SHARED + [
    # Creator grid in brands page
    ('<span class="live-badge">Active now</span>', '<span class="live-badge">פעיל עכשיו</span>'),
    ('<span class="booked-pop">Just booked</span>', '<span class="booked-pop">הוזמן זה עתה</span>'),
    ('<div class="role">Photographer</div>', '<div class="role">צלם/ת</div>'),
    ('<div class="role">Model · Tel Aviv</div>', '<div class="role">דוגמן/ית · תל אביב</div>'),
    ('<div class="role">Art Director</div>', '<div class="role">ניהול אמנותי</div>'),
    ('<div class="role">Motion Designer</div>', '<div class="role">מעצב/ת מוציון</div>'),
    ('<div class="price">from $85/hr</div>', '<div class="price">מ-$85/שעה</div>'),
    ('<div class="price">from $95/hr</div>', '<div class="price">מ-$95/שעה</div>'),
    ('<div class="price">from $120/hr</div>', '<div class="price">מ-$120/שעה</div>'),
    ('<div class="price">from $110/hr</div>', '<div class="price">מ-$110/שעה</div>'),
    # Browse CTA
    ('>Browse all 2,400+ creatives →</a>', '>עיינו בכל 2,400+ יוצרים →</a>'),
    # Campaigns section intro
    ('<p class="sr s1">See what brands have already shipped on EXPOSE this season.</p>',
     '<p class="sr s1">ראו מה מותגים כבר שיגרו דרך EXPOSE בעונה הזו.</p>'),
]

print('Fixing case studies and creator cards...')
fix('site-he.html', SITE_CASES)
fix('site-brands-he.html', BRANDS_CASES)
print('\nDone.')
