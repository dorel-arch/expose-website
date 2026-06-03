#!/usr/bin/env python3
"""Comprehensive final translations — all remaining English content."""
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

# ─── Shared across site-he.html and site-brands-he.html ───────────────────────
SHARED = [
    # Scroll indicator
    ('<span>Scroll</span>', '<span>גלול</span>'),
    # Profile progress tags
    ('<span class="vp-tag done">Photos</span>', '<span class="vp-tag done">תמונות</span>'),
    ('<span class="vp-tag done">Bio</span>', '<span class="vp-tag done">ביו</span>'),
    ('<span class="vp-tag">Skills</span>', '<span class="vp-tag">כישורים</span>'),
    # EXi hero card
    ('<div class="hc-head"><span class="live-dot"></span> EXi at work</div>',
     '<div class="hc-head"><span class="live-dot"></span> EXi בפעולה</div>'),
    # Category chips in scrolling banner
    ('<span class="chip"><span class="dot"></span>Design</span>',
     '<span class="chip"><span class="dot"></span>עיצוב</span>'),
    ('<span class="chip" aria-hidden="true"><span class="dot"></span>Design</span>',
     '<span class="chip" aria-hidden="true"><span class="dot"></span>עיצוב</span>'),
    ('<span class="chip"><span class="dot"></span>Motion</span>',
     '<span class="chip"><span class="dot"></span>מוציון</span>'),
    ('<span class="chip" aria-hidden="true"><span class="dot"></span>Motion</span>',
     '<span class="chip" aria-hidden="true"><span class="dot"></span>מוציון</span>'),
    ('<span class="chip"><span class="dot"></span>Styling</span>',
     '<span class="chip"><span class="dot"></span>סטיילינג</span>'),
    ('<span class="chip" aria-hidden="true"><span class="dot"></span>Styling</span>',
     '<span class="chip" aria-hidden="true"><span class="dot"></span>סטיילינג</span>'),
    ('<span class="chip"><span class="dot"></span>Growth</span>',
     '<span class="chip"><span class="dot"></span>צמיחה</span>'),
    ('<span class="chip" aria-hidden="true"><span class="dot"></span>Growth</span>',
     '<span class="chip" aria-hidden="true"><span class="dot"></span>צמיחה</span>'),
    ('<span class="chip"><span class="dot"></span>UI / UX</span>',
     '<span class="chip"><span class="dot"></span>UI / UX</span>'),
    # Case study: identity tag and titles
    ('<span class="case-tag">Identity</span>', '<span class="case-tag">זהות מותג</span>'),
    ('<b class="title">Asanaké — SS25 Summer Lookbook</b>',
     '<b class="title">Asanaké — SS25 לוקבוק קיץ</b>'),
    ('<b class="title">Mira Studio — Brand Identity Refresh</b>',
     '<b class="title">Mira Studio — רענון זהות מותג</b>'),
    # EXi FAQ chat UI
    ('<span class="agent-status"><span class="status-dot"></span>Online · typically replies in 1s</span>',
     '<span class="agent-status"><span class="status-dot"></span>מחובר · מגיב תוך שנייה</span>'),
    ('          Clear\n        </button>',
     '          נקה\n        </button>'),
    ('<div class="faq-prompt">Suggested questions</div>',
     '<div class="faq-prompt">שאלות מוצעות</div>'),
    # FAQ sub
    ('<p class="faq-sub sr s1">Tap a question below — EXi answers in real time.</p>',
     '<p class="faq-sub sr s1">הקליקו על שאלה — EXi עונה בזמן אמת.</p>'),
]

# ─── site-he.html ─────────────────────────────────────────────────────────────
SITE_FIXES = SHARED + [
    # Hero card: booked notification
    ('<div class="hc-head"><span class="live-dot"></span> Booked</div>',
     '<div class="hc-head"><span class="live-dot"></span> הוזמן</div>'),
    # Feature descriptions (profile optimizer)
    ('<p style="font-size: 16px">EXPOSE maps your portfolio, identifies what\'s missing, and tells you exactly what to add to attract the brands you want.</p>',
     '<p style="font-size: 16px">EXPOSE ממפה את הפורטפוליו שלכם, מזהה מה חסר, ואומר בדיוק מה להוסיף כדי למשוך את המותגים שאתם רוצים.</p>'),
    ('<p style="font-size: 16px">EXPOSE matches your profile and style with brands actively looking for someone like you — and submits your profile automatically.</p>',
     '<p style="font-size: 16px">EXPOSE מתאים את הפרופיל והסגנון שלכם למותגים שמחפשים בפעילות מישהו כמוכם — ושולח את הפרופיל שלכם אוטומטית.</p>'),
    ('<p style="font-size: 16px">EXPOSE tracks your bookings, monitors your social-media visibility, and tells you exactly what to do to get more work and earn more.</p>',
     '<p style="font-size: 16px">EXPOSE עוקב אחר ההזמנות שלכם, מנטר את הנראות ברשתות, ואומר בדיוק מה לעשות כדי להשיג יותר עבודה ולהרוויח יותר.</p>'),
    # EXi agent section
    ('<p class="sr s1">EXi watches your visibility, lines the right projects, submits your work, and tells you exactly what to do to grow. You never figure it out alone.</p>',
     '<p class="sr s1">EXi עוקב אחר הנראות שלכם, מאתר פרויקטים מתאימים, שולח את העבודות שלכם, ואומר בדיוק מה לעשות כדי לצמוח. לעולם לא תתמודדו עם זה לבד.</p>'),
    ('<p>EXi negotiates briefing, secures briefings, and works for you 24/7.</p>',
     '<p>EXi מנהל משא ומתן, מאבטח בריפים, ועובד בשבילכם 24/7.</p>'),
    ('<p>EXi notices you socially — and tells you exactly what to post.</p>',
     '<p>EXi מנטר את הנוכחות שלכם ברשתות — ואומר בדיוק מה לפרסם.</p>'),
    ('<p>EXi tells you what to charge — so you stop earning money on the table.</p>',
     '<p>EXi אומר לכם מה לגבות — כדי שתפסיקו להשאיר כסף על השולחן.</p>'),
    ('<p>EXi reads your portfolio and only surfaces briefs that genuinely fit you — no noise.</p>',
     '<p>EXi קורא את הפורטפוליו שלכם ומציג רק בריפים שמתאימים לכם באמת — ללא רעש.</p>'),
    # Cases section intro
    ('<p class="sr s1">Real projects, real brands, real pay — booked on EXPOSE this season.</p>',
     '<p class="sr s1">פרויקטים אמיתיים, מותגים אמיתיים, שכר אמיתי — הוזמנו דרך EXPOSE בעונה הזו.</p>'),
    # Nike Run Club case title (fix mixed Hebrew/English)
    ('<b class="title">Nike Run Club — SS25 אדיטוריאל Series</b>',
     '<b class="title">Nike Run Club — SS25 סדרת אדיטוריאל</b>'),
    # Testimonial role tags
    ('<span class="role-tag">Stylist</span>', '<span class="role-tag">סטייליסט/ית</span>'),
    ('<span class="role-tag">Director</span>', '<span class="role-tag">במאי/ת</span>'),
    ('<span class="role-tag">Designer</span>', '<span class="role-tag">מעצב/ת</span>'),
    ('<span class="role-tag">Motion</span>', '<span class="role-tag">מוציון</span>'),
    ('<span class="role-tag">Founder</span>', '<span class="role-tag">מייסד/ת</span>'),
    ('<span class="role-tag">Cinematographer</span>', '<span class="role-tag">קולנוען/ית</span>'),
    ('<span class="role-tag">Illustrator</span>', '<span class="role-tag">מאייר/ת</span>'),
    ('<span class="role-tag">Copywriter</span>', '<span class="role-tag">קופירייטר/ית</span>'),
    ('<span class="role-tag">UI/UX</span>', '<span class="role-tag">UI/UX</span>'),
    ('<span class="role-tag">Model</span>', '<span class="role-tag">דוגמן/ית</span>'),
    # Testimonial author role+city spans
    ('<span>Stylist · Tel Aviv</span>', '<span>סטייליסט/ית · תל אביב</span>'),
    ('<span>Creative Director · Berlin</span>', '<span>מנהל/ת יצירתי/ת · ברלין</span>'),
    ('<span>Brand Designer · Osaka</span>', '<span>מעצב/ת מותג · אוסקה</span>'),
    ('<span>Founder · Form Studio</span>', '<span>מייסד/ת · Form Studio</span>'),
    ('<span>Cinematographer · Madrid</span>', '<span>קולנוען/ית · מדריד</span>'),
    ('<span>Illustrator · Seoul</span>', '<span>מאייר/ת · סיאול</span>'),
    ('<span>Copywriter · NYC</span>', '<span>קופירייטר/ית · ניו יורק</span>'),
    ('<span>UI / UX · Cairo</span>', '<span>UI / UX · קהיר</span>'),
    ('<span>דוגמן/ית · תל אביב</span>', '<span>דוגמן/ית · תל אביב</span>'),  # already done, no-op
    # FAQ question chips (display text)
    ('<span class="dot"></span>How does EXi find me work?',
     '<span class="dot"></span>איך EXi מוצא לי עבודה?'),
    ('<span class="dot"></span>How much do you take?',
     '<span class="dot"></span>כמה אחוזים אתם לוקחים?'),
    ('<span class="dot"></span>How does payment work?',
     '<span class="dot"></span>איך עובד התשלום?'),
    ('<span class="dot"></span>Do I need experience?',
     '<span class="dot"></span>האם אני צריך ניסיון?'),
    ('<span class="dot"></span>How do you know my style?',
     '<span class="dot"></span>איך אתם מכירים את הסגנון שלי?'),
    ('<span class="dot"></span>Can I decline briefs?',
     '<span class="dot"></span>האם אני יכול לדחות בריפים?'),
]

# ─── site-brands-he.html ──────────────────────────────────────────────────────
BRANDS_FIXES = SHARED + [
    # Hero card status
    ('<div class="hc-head"><span class="hc-payicon">↑</span> ROI this week</div>',
     '<div class="hc-head"><span class="hc-payicon">↑</span> ROI השבוע</div>'),
    ('<div class="hc-meta">vs last campaign · EXi-optimised</div>',
     '<div class="hc-meta">לעומת קמפיין קודם · אוּיעל ע"י EXi</div>'),
    # Dashboard status badges
    ('<div class="ms-badge" style="background:#1FBF6B;color:#fff">Live</div>',
     '<div class="ms-badge" style="background:#1FBF6B;color:#fff">פעיל</div>'),
    ('<span class="ms-tag new" style="background:#e6f9f0;color:#1FBF6B">Live</span>',
     '<span class="ms-tag new" style="background:#e6f9f0;color:#1FBF6B">פעיל</span>'),
    ('<span class="ms-time">Pending</span>', '<span class="ms-time">ממתין</span>'),
    # EXi feature descriptions
    ('<p style="font-size: 16px">EXi analyzes your brand, audience, and competitors — then builds a clear marketing plan tailored to you.</p>',
     '<p style="font-size: 16px">EXi מנתח את המותג, הקהל והמתחרים שלכם — ובונה תוכנית שיווק ברורה המותאמת עבורכם.</p>'),
    ('<p style="font-size: 16px">EXi matches you with the right creative pros for your project — based on your style, budget, location, and timeline.</p>',
     '<p style="font-size: 16px">EXi מתאים לכם את אנשי היצירה הנכונים לפרויקט — לפי הסגנון, התקציב, המיקום ולוח הזמנים שלכם.</p>'),
    ('<p style="font-size: 16px">EXi tracks your activity, monitors campaign performance, and makes sure nothing gets missed.</p>',
     '<p style="font-size: 16px">EXi עוקב אחר הפעילות שלכם, מנטר ביצועי קמפיינים, ומוודא שלא נפסיד שום דבר.</p>'),
    ('<p class="sr s1">EXi monitors your channels, tracks competition, detects gaps, builds campaigns, matches your team — and reports back, all in real time.</p>',
     '<p class="sr s1">EXi מנטר את הערוצים שלכם, עוקב אחרי המתחרים, מזהה פערים, בונה קמפיינים, מתאים את הצוות — ומדווח הכל בזמן אמת.</p>'),
    ('<p>EXi scans your performance and tells you exactly what\'s pulling your ROI down.</p>',
     '<p>EXi סורק את הביצועים שלכם ואומר בדיוק מה גורר את ה-ROI כלפי מטה.</p>'),
    ('<p>Real-time tweaks, live ROI tracking, and content that performs better with every campaign.</p>',
     '<p>כיוונונים בזמן אמת, מעקב ROI חי, ותוכן שמשתפר עם כל קמפיין.</p>'),
    ('<p>EXi tracks every post back to revenue — so you know exactly which creator drove which dollar.</p>',
     '<p>EXi עוקב אחרי כל פוסט עד להכנסה — כדי שתדעו בדיוק איזה יוצר הניע כל שקל.</p>'),
    # Stats section
    ('<p class="sr s1">Brands that use EXPOSE ship faster, spend smarter, and scale bigger.</p>',
     '<p class="sr s1">מותגים שמשתמשים ב-EXPOSE משגרים מהר יותר, מוציאים בחוכמה, וגדלים בגדול.</p>'),
    ('<div class="stat-label">Brands trust EXPOSE</div>',
     '<div class="stat-label">מותגים סומכים על EXPOSE</div>'),
    # Creator grid filter — All button
    ('<button class="active"><span class="emo">✨</span>All</button>',
     '<button class="active"><span class="emo">✨</span>הכל</button>'),
    ('<button data-c="ink"><span class="emo">🎬</span>Video</button>',
     '<button data-c="ink"><span class="emo">🎬</span>וידאו</button>'),
    ('<button data-c="peach"><span class="emo">📱</span>Social</button>',
     '<button data-c="peach"><span class="emo">📱</span>סושיאל</button>'),
    ('<button data-c="rose"><span class="emo">🎵</span>Music</button>',
     '<button data-c="rose"><span class="emo">🎵</span>מוזיקה</button>'),
    # Case tag
    ('<span class="case-tag">FW24 Campaign</span>', '<span class="case-tag">קמפיין FW24</span>'),
    # Nike Run Club case title
    ('<b class="title">Nike Run Club — SS25 Editorial Series</b>',
     '<b class="title">Nike Run Club — SS25 סדרת אדיטוריאל</b>'),
    # New English brand testimonials (second set of 6)
    ('<p class="testi-quote">"From scattered Notion docs and Instagram DMs to one dashboard. We never go back."</p>',
     '<p class="testi-quote">"ממסמכי Notion מפוזרים ו-DMs באינסטגרם — לדשבורד אחד. אנחנו לא חוזרים לאחור."</p>'),
    ('<p class="testi-quote">"Sold through our summer drop in 9 days. EXPOSE made us look like we\'d been doing this for years."</p>',
     '<p class="testi-quote">"מכרנו את קולקציית הקיץ ב-9 ימים. EXPOSE גרם לנו להיראות כאילו עושים את זה שנים."</p>'),
    ('<p class="testi-quote">"ROI doubled in the first quarter. Briefing went from 2 hours to 2 minutes."</p>',
     '<p class="testi-quote">"ה-ROI הוכפל ברבעון הראשון. הגשת הבריף ירדה מ-2 שעות ל-2 דקות."</p>'),
    ('<p class="testi-quote">"The match quality is uncanny. Every creator EXi sent us was on-brand, on-budget, and ready to ship."</p>',
     '<p class="testi-quote">"איכות ההתאמה מדהימה. כל יוצר שEXi שלח לנו היה תואם מותג, בתקציב, ומוכן לשגר."</p>'),
    ('<p class="testi-quote">"I used to lose sleep over influencer ROI. Now I sleep — and the campaigns run themselves."</p>',
     '<p class="testi-quote">"פעם הייתי מאבד שינה על ROI של אינפלואנסרים. עכשיו אני ישן — והקמפיינים רצים לבד."</p>'),
    ('<p class="testi-quote">"We launched in 4 markets simultaneously. EXi handled the local creator pools — we just approved."</p>',
     '<p class="testi-quote">"השקנו ב-4 שווקים במקביל. EXi טיפל במאגרי היוצרים המקומיים — אנחנו רק אישרנו."</p>'),
    # Testimonial author name+role spans (new set)
    ('<span>Head of Brand · Mira Studio</span>', '<span>ראש מותג · Mira Studio</span>'),
    ('<span>Founder · Rivet Supply</span>', '<span>מייסד/ת · Rivet Supply</span>'),
    ('<span>Performance Lead · Nordica</span>', '<span>מוביל/ת ביצועים · Nordica</span>'),
    ('<span>Brand Strategist · Vogue IT</span>', '<span>אסטרטג/ית מותג · Vogue IT</span>'),
    ('<span>CEO · Form Studio</span>', '<span>מנכ"ל · Form Studio</span>'),
    ('<span>Content Lead · Asanaké</span>', '<span>מוביל/ת תוכן · Asanaké</span>'),
    # Role tags in brands testimonials
    ('<span class="role-tag">Head of Brand</span>', '<span class="role-tag">ראש מותג</span>'),
    ('<span class="role-tag">Performance</span>', '<span class="role-tag">ביצועים</span>'),
    ('<span class="role-tag">Strategist</span>', '<span class="role-tag">אסטרטג/ית</span>'),
    ('<span class="role-tag">Content Lead</span>', '<span class="role-tag">מוביל/ת תוכן</span>'),
    ('<span class="role-tag">Founder</span>', '<span class="role-tag">מייסד/ת</span>'),
    # EXi chat section eyebrow
    ('<span class="faq-eyebrow"><span class="live-dot"></span>Live Q&amp;A <span class="sp">·</span> with EXi</span>',
     '<span class="faq-eyebrow"><span class="live-dot"></span>שאלות חיות <span class="sp">·</span> עם EXi</span>'),
    ('<p class="faq-sub sr s1">Tap a question below — EXi answers in real time. No waiting on hold, no contact forms.</p>',
     '<p class="faq-sub sr s1">הקליקו על שאלה — EXi עונה בזמן אמת. ללא המתנה, ללא טפסי יצירת קשר.</p>'),
    # Counter labels
    ('<span class="lbl">Creatives</span>', '<span class="lbl">יוצרים</span>'),
    ('<span class="lbl">Briefs / mo</span>', '<span class="lbl">בריפים / חודש</span>'),
    ('<span class="lbl">Rating</span>', '<span class="lbl">דירוג</span>'),
    ('<span class="lbl">Paid out</span>', '<span class="lbl">שולם</span>'),
    ('<span class="lbl">Cities</span>', '<span class="lbl">ערים</span>'),
    # Activity ticker feed
    ('</b> launched a $45K campaign<span class="ago">',
     '</b> השיקה קמפיין של $45K<span class="ago">'),
    ('</b> just joined<span class="ago">',
     '</b> הצטרפה זה עתה<span class="ago">'),
    ('</b> hit 4.2× ROI today<span class="ago">',
     '</b> הגיעה ל-4.2× ROI היום<span class="ago">'),
    ('</b> shipped to 4 markets<span class="ago">',
     '</b> שיגרה ל-4 שווקים<span class="ago">'),
    ('</b> matched with 12 creators<span class="ago">',
     '</b> הותאמה עם 12 יוצרים<span class="ago">'),
    ('</b> closed a launch<span class="ago">',
     '</b> סגרה השקה<span class="ago">'),
    ('</b> unlocked Growth plan<span class="ago">',
     '</b> פתחה את תוכנית Growth<span class="ago">'),
    # FAQ question chips (display text)
    ('<span class="dot"></span>How fast can I launch?',
     '<span class="dot"></span>כמה מהר אני יכול להשיק?'),
    ('<span class="dot"></span>How do you vet creators?',
     '<span class="dot"></span>איך אתם מאמתים יוצרים?'),
    ('<span class="dot"></span>How is ROI tracked?',
     '<span class="dot"></span>איך ROI נמדד?'),
    ('<span class="dot"></span>What does it cost?',
     '<span class="dot"></span>מה זה עולה?'),
    ('<span class="dot"></span>Can I bring my roster?',
     '<span class="dot"></span>האם אני יכול להביא את הרוסטר שלי?'),
    ('<span class="dot"></span>Do you support global markets?',
     '<span class="dot"></span>האם אתם תומכים בשווקים גלובליים?'),
    # "EXi is live" floating indicator
    ('\n      EXi is live · AI-powered talent matching for brands',
     '\n      EXi פעיל · התאמת יוצרים מבוססת AI למותגים'),
]

print('Applying final comprehensive translations...')
fix('site-he.html', SITE_FIXES)
fix('site-brands-he.html', BRANDS_FIXES)
print('\nDone.')
