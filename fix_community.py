#!/usr/bin/env python3
"""Fix community section, dashboard stats, and exi-brands bento/notifications."""
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
SITE_COMMUNITY = [
    # Stats cards
    ('<div class="stat-label">Median time to first booking</div>',
     '<div class="stat-label">זמן חציוני להזמנה ראשונה</div>'),
    ('<div class="stat-label">Avg. monthly income lift</div>',
     '<div class="stat-label">עלייה ממוצעת בהכנסה חודשית</div>'),
    ('<span class="online-tag">Live now</span>',
     '<span class="online-tag">חי עכשיו</span>'),
    ('<div class="stat-label">EXPOSE never stops working</div>',
     '<div class="stat-label">EXPOSE לעולם לא מפסיק לעבוד</div>'),
    ('<svg width="9" height="9" viewBox="0 0 12 12" fill="currentColor"><path d="M2 9l4-5 4 5z"/></svg>\n          Trending',
     '<svg width="9" height="9" viewBox="0 0 12 12" fill="currentColor"><path d="M2 9l4-5 4 5z"/></svg>\n          טרנד'),
    # Community intro
    ('<p class="sr s1">of getting booked, paid, and growing together.</p>',
     '<p class="sr s1">של קבלת עבודות, קבלת תשלום וצמיחה יחד.</p>'),
    # Filter tabs
    ('<button class="active"><span class="emo">✨</span>All</button>',
     '<button class="active"><span class="emo">✨</span>הכל</button>'),
    ('<button data-c="rose"><span class="emo">📷</span>Photography</button>',
     '<button data-c="rose"><span class="emo">📷</span>צילום</button>'),
    ('<button data-c="peach"><span class="emo">✏️</span>Design</button>',
     '<button data-c="peach"><span class="emo">✏️</span>עיצוב</button>'),
    ('<button data-c="blush"><span class="emo">💃</span>Modeling</button>',
     '<button data-c="blush"><span class="emo">💃</span>מודלינג</button>'),
    ('<button data-c="ink"><span class="emo">🎬</span>Video</button>',
     '<button data-c="ink"><span class="emo">🎬</span>וידאו</button>'),
    ('<button data-c="lilac"><span class="emo">🎞️</span>Motion</button>',
     '<button data-c="lilac"><span class="emo">🎞️</span>מוציון</button>'),
    ('<button data-c="cream"><span class="emo">✍️</span>Copywriting</button>',
     '<button data-c="cream"><span class="emo">✍️</span>כתיבה</button>'),
    ('<button data-c="mint"><span class="emo">🎨</span>Illustration</button>',
     '<button data-c="mint"><span class="emo">🎨</span>איורים</button>'),
    ('<button data-c="clay"><span class="emo">🪄</span>Branding</button>',
     '<button data-c="clay"><span class="emo">🪄</span>מיתוג</button>'),
    ('<button data-c="sand"><span class="emo">👗</span>Styling</button>',
     '<button data-c="sand"><span class="emo">👗</span>סטיילינג</button>'),
    ('<button data-c="sky"><span class="emo">🧊</span>3D</button>',
     '<button data-c="sky"><span class="emo">🧊</span>תלת-מימד</button>'),
    ('<button data-c="peach"><span class="emo">📱</span>Social</button>',
     '<button data-c="peach"><span class="emo">📱</span>סושיאל</button>'),
    ('<button data-c="moss"><span class="emo">📍</span>UI / UX</button>',
     '<button data-c="moss"><span class="emo">📍</span>UI / UX</button>'),
    ('<button data-c="rose"><span class="emo">🎵</span>Music</button>',
     '<button data-c="rose"><span class="emo">🎵</span>מוזיקה</button>'),
    # Creator cards
    ('<span class="live-badge">Active now</span>', '<span class="live-badge">פעיל עכשיו</span>'),
    ('<span class="booked-pop">Just booked</span>', '<span class="booked-pop">הוזמן זה עתה</span>'),
    ('<div class="role">Photographer</div>', '<div class="role">צלם/ת</div>'),
    ('<div class="role">Model · Tel Aviv</div>', '<div class="role">דוגמן/ית · תל אביב</div>'),
    ('<div class="price">from $85/hr</div>', '<div class="price">מ-$85/שעה</div>'),
    ('<div class="price">from $95/hr</div>', '<div class="price">מ-$95/שעה</div>'),
    ('<div class="price">from $120/hr</div>', '<div class="price">מ-$120/שעה</div>'),
    ('<div class="price">from $110/hr</div>', '<div class="price">מ-$110/שעה</div>'),
    # Testimonial role tags
    ('<span class="role-tag">Photographer</span>', '<span class="role-tag">צלם/ת</span>'),
    ('<span>Photographer · Tel Aviv</span>', '<span>צלם/ת · תל אביב</span>'),
    ('<span>Model · Tel Aviv</span>', '<span>דוגמן/ית · תל אביב</span>'),
]

# ─── site-brands-he.html ───────────────────────────────
BRANDS_DASHBOARD = [
    # Dashboard campaign mini
    ('<div class="ms-title">Campaigns</div>', '<div class="ms-title">קמפיינים</div>'),
    ('<div class="ms-live"><span class="ms-dot"></span>3 active campaigns · All on track</div>',
     '<div class="ms-live"><span class="ms-dot"></span>3 קמפיינים פעילים · הכל על המסלול</div>'),
    ('<div class="ms-card-h"><b>Summer Campaign</b></div>',
     '<div class="ms-card-h"><b>קמפיין קיץ</b></div>'),
    ('<div class="ms-card-sub">Brief sent · 3 creators matched</div>',
     '<div class="ms-card-sub">בריף נשלח · 3 יוצרים הותאמו</div>'),
    # Workflow section
    ('<div class="eyebrow sr">Workflow</div>', '<div class="eyebrow sr">תהליך עבודה</div>'),
    ('<p>The right crew, briefed and ready to launch every campaign on time, on brand.</p>',
     '<p>הצוות הנכון, עם בריף ומוכן להשיק כל קמפיין בזמן ובהתאמה למותג.</p>'),
    ('<span class="agent-status"><span class="status-dot"></span>Online · Working for you</span>',
     '<span class="agent-status"><span class="status-dot"></span>מחובר · עובד בשבילכם</span>'),
    # Stats
    ('<span class="city-pin">Shipping campaigns weekly</span>',
     '<span class="city-pin">משגרים קמפיינים שבועית</span>'),
    # Stats card labels
    ('<div class="stat-label">Median time to first booking</div>',
     '<div class="stat-label">זמן חציוני לקמפיין ראשון</div>'),
    ('<div class="stat-label">Avg. monthly income lift</div>',
     '<div class="stat-label">גידול ממוצע ב-ROI חודשי</div>'),
    ('<span class="online-tag">Live now</span>',
     '<span class="online-tag">חי עכשיו</span>'),
    ('<div class="stat-label">EXPOSE never stops working</div>',
     '<div class="stat-label">EXPOSE לעולם לא מפסיק לעבוד</div>'),
    ('<svg width="9" height="9" viewBox="0 0 12 12" fill="currentColor"><path d="M2 9l4-5 4 5z"/></svg>\n          Trending',
     '<svg width="9" height="9" viewBox="0 0 12 12" fill="currentColor"><path d="M2 9l4-5 4 5z"/></svg>\n          טרנד'),
    # Community section
    ('<p class="sr s1">of getting booked, paid, and growing together.</p>',
     '<p class="sr s1">של קבלת עבודות, קבלת תשלום וצמיחה יחד.</p>'),
]

# ─── site-exi-brands-he.html ───────────────────────────────
EXI_BRANDS_BENTO = [
    # Daily automation ns-cards
    ('<div class="eyebrow sr">Daily automation</div>', '<div class="eyebrow sr">אוטומציה יומית</div>'),
    ('<p>Every morning: reach, spend, ROI, and what EXi did overnight for each campaign.</p>',
     '<p>כל בוקר: טווח, הוצאות, ROI ומה EXi עשה בלילה לכל קמפיין.</p>'),
    ('            Every morning\n          </div>',
     '            כל בוקר\n          </div>'),
    ('<p>Flags underperforming creators before they drain your budget — with a suggested action.</p>',
     '<p>מסמן יוצרים חלשים לפני שמרוקנים את התקציב — עם פעולה מוצעת.</p>'),
    ('            Real-time\n          </div>',
     '            בזמן אמת\n          </div>'),
    ('<p>Continuously shifts spend to top performers and pauses what isn\'t working — zero manual effort.</p>',
     '<p>מעביר הוצאות ללא הרף לביצועים המובילים ומשהה מה שלא עובד — אפס מאמץ ידני.</p>'),
    ('            Always on\n          </div>',
     '            תמיד פעיל\n          </div>'),
    # One agent section
    ('<div class="eyebrow sr">Everything in one place</div>',
     '<div class="eyebrow sr">הכל במקום אחד</div>'),
    ('<p class="sub sr s2">EXi runs your entire creator marketing operation — from brief to final report.</p>',
     '<p class="sub sr s2">EXi מנהל את כל פעולות השיווק עם יוצרים שלכם — מהבריף ועד לדוח הסופי.</p>'),
    ('<div class="bento-badge">Core feature</div>', '<div class="bento-badge">תכונת ליבה</div>'),
    ('<p>Every brief, creator, deadline and deliverable tracked in one clean view. No more spreadsheets.</p>',
     '<p>כל בריף, יוצר, דדליין וספק מעוקב בתצוגה אחת ומסודרת. לא עוד גיליונות.</p>'),
    ('<p>Smart matching to your brief, budget and brand.</p>',
     '<p>התאמה חכמה לבריף, לתקציב ולמותג שלכם.</p>'),
    ('<p>Tracks every deliverable and approval in real time.</p>',
     '<p>עוקב אחר כל ספק ואישור בזמן אמת.</p>'),
    ('<p>Maximizes ROI from every campaign dollar.</p>',
     '<p>ממקסם ROI מכל שקל בקמפיין.</p>'),
    ('<p>Industry trends and competitor brand insights.</p>',
     '<p>מגמות תעשייה ותובנות על מותגים מתחרים.</p>'),
    ('<p>Flags compliance issues before they go live.</p>',
     '<p>מסמן בעיות תאימות לפני שיוצאים לאוויר.</p>'),
    # Transparent by design
    ('<div class="eyebrow sr">Transparent by design</div>',
     '<div class="eyebrow sr">שקיפות בעיצוב</div>'),
    ('<p class="control-sub sr s2">EXi acts fast, but never without you. Every creator action and budget move needs your sign-off before it happens.</p>',
     '<p class="control-sub sr s2">EXi פועל מהר, אבל לעולם לא בלעדיכם. כל פעולה של יוצר ומהלך תקציבי צריך את אישורכם לפני שמתרחש.</p>'),
    # Notifications
    ('<span class="notif-title">4 creator matches for Spring brief</span>',
     '<span class="notif-title">4 התאמות יוצרים לבריף אביב</span>'),
    ('<span class="notif-time">Just now</span>', '<span class="notif-time">עכשיו</span>'),
    ('<div class="notif-msg">EXi found 4 creators with 90%+ fit for your Spring lifestyle campaign. Review profiles before submitting.</div>',
     '<div class="notif-msg">EXi מצא 4 יוצרים עם 90%+ התאמה לקמפיין הלייפסטייל שלכם לאביב. סקרו פרופילים לפני השליחה.</div>'),
    ('<button class="nb primary" onclick="approveNotif(this)">View Matches</button>',
     '<button class="nb primary" onclick="approveNotif(this)">הציגו התאמות</button>'),
    ('<button class="nb secondary">Skip</button>', '<button class="nb secondary">דלגו</button>'),
    ('<span class="notif-title">@mia_k submitted content for review</span>',
     '<span class="notif-title">@mia_k הגישה תוכן לסקירה</span>'),
    ('<span class="notif-time">1h ago</span>', '<span class="notif-time">לפני שעה</span>'),
    ('<div class="notif-msg">Deliverable ready for your Spring brief. EXi flagged it as on-brand — approve to go live.</div>',
     '<div class="notif-msg">ספק מוכן לבריף האביב שלכם. EXi סימן אותו כתואם מותג — אשרו להוצאה לאוויר.</div>'),
    ('<button class="nb primary" onclick="approveNotif(this)">Review Now</button>',
     '<button class="nb primary" onclick="approveNotif(this)">סקרו עכשיו</button>'),
    ('<button class="nb secondary">Later</button>', '<button class="nb secondary">אחר כך</button>'),
    ('<span class="notif-title">Budget pacing alert — Campaign #3</span>',
     '<span class="notif-title">התראת קצב תקציב — קמפיין #3</span>'),
    ('<span class="notif-time">3h ago</span>', '<span class="notif-time">לפני 3 שעות</span>'),
    ('<div class="notif-msg">Campaign #3 is outperforming. EXi recommends adding $2,000 to capture more reach before the brief closes.</div>',
     '<div class="notif-msg">קמפיין #3 מניב ביצועים גבוהים. EXi ממליץ להוסיף $2,000 כדי לתפוס יותר טווח לפני שהבריף נסגר.</div>'),
    ('<button class="nb primary" onclick="approveNotif(this)">Approve</button>',
     '<button class="nb primary" onclick="approveNotif(this)">אשרו</button>'),
    # CTA paragraph with partial Hebrew
    ('הצטרפו 380+ brands already running better creator marketing through EXPOSE.',
     'הצטרפו ל-380+ מותגים שכבר מנהלים שיווק יוצרים טוב יותר דרך EXPOSE.'),
]

print('Applying community & remaining translations...')
fix('site-he.html', SITE_COMMUNITY)
fix('site-brands-he.html', BRANDS_DASHBOARD)
fix('site-exi-brands-he.html', EXI_BRANDS_BENTO)
print('\nDone.')
