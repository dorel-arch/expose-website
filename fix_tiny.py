#!/usr/bin/env python3
"""Tiny final fixes for remaining labels."""
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

SITE_TINY = [
    # Creator roles in testimonials
    ('<span>Motion Designer · Berlin</span>', '<span>מעצב/ת מוציון · ברלין</span>'),
    # Case study tags
    ('<span class="case-tag">FW24 Campaign</span>', '<span class="case-tag">קמפיין FW24</span>'),
    ('<span class="case-id">Project №1247</span>', '<span class="case-id">פרויקט №1247</span>'),
    # JS creator card data roles (inside script tags - skip)
]

BRANDS_TINY = [
    # Stats labels
    ('<div class="stat-label">Brief to first creator booked</div>',
     '<div class="stat-label">מבריף עד הזמנת יוצר ראשון</div>'),
    ('<div class="stat-label">Avg. ROI vs traditional agency</div>',
     '<div class="stat-label">ROI ממוצע לעומת סוכנות מסורתית</div>'),
    ('<div class="stat-label">EXi monitors your campaigns</div>',
     '<div class="stat-label">EXi מנטר את הקמפיינים שלכם</div>'),
    ('<svg width="9" height="9" viewBox="0 0 12 12" fill="currentColor"><path d="M2 9l4-5 4 5z"/></svg>\n          vs agencies',
     '<svg width="9" height="9" viewBox="0 0 12 12" fill="currentColor"><path d="M2 9l4-5 4 5z"/></svg>\n          לעומת סוכנויות'),
    # Browse section
    ('<p class="sr s1">Browse 2,400+ vetted creatives — ready to ship your next campaign.</p>',
     '<p class="sr s1">עיינו ב-2,400+ יוצרים מאומתים — מוכנים לשגר את הקמפיין הבא שלכם.</p>'),
    # Brands filter tabs
    ('<button data-c="blush"><span class="emo">💃</span>Modeling</button>',
     '<button data-c="blush"><span class="emo">💃</span>מודלינג</button>'),
    ('<button data-c="cream"><span class="emo">✍️</span>Copywriting</button>',
     '<button data-c="cream"><span class="emo">✍️</span>כתיבה</button>'),
    ('<button data-c="mint"><span class="emo">🎨</span>Illustration</button>',
     '<button data-c="mint"><span class="emo">🎨</span>איורים</button>'),
    ('<button data-c="clay"><span class="emo">🪄</span>Branding</button>',
     '<button data-c="clay"><span class="emo">🪄</span>מיתוג</button>'),
]

print('Applying tiny remaining fixes...')
fix('site-he.html', SITE_TINY)
fix('site-brands-he.html', BRANDS_TINY)
print('\nDone.')
