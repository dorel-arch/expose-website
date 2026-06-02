#!/usr/bin/env python3
"""Apply Hebrew translations to the -he.html pages using regex to handle multiline HTML."""
import re, os

os.chdir('/home/claude/repo')

def tr(html, en, he):
    """Replace en with he, handling surrounding whitespace/newlines in HTML."""
    # Exact match first
    if en in html:
        html = html.replace(en, he)
        return html
    # Try collapsing whitespace in the source pattern
    pattern = re.escape(en)
    pattern = re.sub(r'\\ ', r'\\s+', pattern)
    html = re.sub(pattern, he, html)
    return html

def translate_page(src, translations):
    with open(src, 'r', encoding='utf-8') as f:
        html = f.read()
    for en, he in translations:
        html = tr(html, en, he)
    with open(src, 'w', encoding='utf-8') as f:
        f.write(html)
    he_count = len(re.findall('[א-ת]', html))
    print(f'  {src}: {he_count} Hebrew chars')

# ─────────────────────────────────────────────
# SHARED (drawer nav, footer, store buttons)
SHARED = [
    # Drawer nav links
    ('Join EXPOSE — It\'s Free', 'הצטרפו ל-EXPOSE — בחינם'),
    ('>For Brands<', '>למותגים<'),
    ('>For Creatives<', '>ליוצרים<'),
    ('>Meet EXi<', '>הכירו את EXi<'),
    ('>About Us<', '>אודותינו<'),
    ('>Contact<', '>צרו קשר<'),
    ('>Pricing<', '>תמחור<'),
    ('>Blog<', '>בלוג<'),
    # Desktop nav links (span-wrapped)
    ('For Brands\n    ', 'למותגים\n    '),
    ('For Creatives\n    ', 'ליוצרים\n    '),
    # nav-login button
    ('>Join<', '>הצטרפו<'),
    # Drawer sub-items
    ('>For Creatives</a>\n        <a', '>ליוצרים</a>\n        <a'),
    ('>For Brands</a>\n      </div>', '>למותגים</a>\n      </div>'),
    # Footer columns
    ('<h6>Product</h6>', '<h6>מוצר</h6>'),
    ('<h6>Company</h6>', '<h6>חברה</h6>'),
    ('<h6>Support</h6>', '<h6>תמיכה</h6>'),
    ('<h6>Follow us</h6>', '<h6>עקבו אחרינו</h6>'),
    # Footer links (as full blocks to avoid partial matches)
    ('>For Creatives</a>', '>ליוצרים</a>'),
    ('>For Brands</a>', '>למותגים</a>'),
    ('>Meet EXi</a>', '>EXi סוכן</a>'),
    ('>About Us</a>', '>אודותינו</a>'),
    ('>Careers</a>', '>קריירה</a>'),
    ('>Press</a>', '>עיתונות</a>'),
    ('>Help Center</a>', '>מרכז עזרה</a>'),
    ('>Privacy</a>', '>פרטיות</a>'),
    ('>Terms</a>', '>תנאי שימוש</a>'),
    ('>Contact</a>', '>צרו קשר</a>'),
    ('>Blog</a>', '>בלוג</a>'),
    ('>Pricing</a>', '>תמחור</a>'),
    # Footer tagline
    ('The AI-powered marketing engine for world-class creatives.', 'מנוע השיווק המופעל על ידי AI ליוצרים ברמה עולמית.'),
    ('AI-powered creative career platform', 'פלטפורמת קריירה יצירתית מבוססת AI'),
    # App store buttons
    ('<div class="store-label">Download on the</div>', '<div class="store-label">הורידו מה-</div>'),
    ('<div class="store-name">App Store</div>', '<div class="store-name">App Store</div>'),
    ('<div class="store-label">Get it on</div>', '<div class="store-label">הורידו מ-</div>'),
    ('<div class="store-name">Google Play</div>', '<div class="store-name">Google Play</div>'),
    # Footer bottom
    ('© 2025 EXPOSE. All rights reserved.', '© 2025 EXPOSE. כל הזכויות שמורות.'),
]

# ─────────────────────────────────────────────
SITE_HE = SHARED + [
    # Title
    ('EXPOSE — Stop Chasing After Clients. Let EXi Run It.', 'EXPOSE — הפסיקו לרדוף אחרי לקוחות. תנו ל-EXi לטפל בזה.'),
    # Meta
    ('EXPOSE is the AI-powered marketing platform for creatives and brands.',
     'EXPOSE היא פלטפורמת השיווק מבוססת AI ליוצרים ומותגים.'),
    # Hero
    ('Stop Chasing After Clients.\n      <span class="it italic-accent">Let EXi Run It.</span>',
     'הפסיקו לרדוף אחרי לקוחות.\n      <span class="it italic-accent">תנו ל-EXi לטפל בזה.</span>'),
    ('The AI platform connecting the world\'s best creatives with the brands that need them — no hustle required.',
     'הפלטפורמה שמחברת את היוצרים הטובים בעולם עם המותגים שזקוקים להם — בלי מאמץ.'),
    ('EXi is live · AI-powered creative matching', 'EXi פעיל · התאמת יוצרים מבוססת AI'),
    # Section: Your career
    ('Your career, supercharged.', 'הקריירה שלכם, בהילוך גבוה.'),
    ('Work offers come to you. <span class="muted" style="color: var(--orange);">Not the other way around.</span>',
     'עבודות מגיעות אליכם. <span class="muted" style="color: var(--orange);">לא להיפך.</span>'),
    # Section: Workflow
    ('>Workflow<', '>תהליך עבודה<'),
    ('Complete career ecosystem', 'מערכת קריירה מלאה'),
    ('expose gives you everything you need to grow, get booked, and get paid.',
     'EXPOSE נותן לכם כל מה שצריך לצמוח, להיות מוזמנים ולקבל תשלום.'),
    ('>Build Your Profile<', '>בנו את הפרופיל<'),
    ('>Get Discovered<', '>היכנסו לרדאר<'),
    ('>Grow Your Career<', '>צמחו בקריירה<'),
    # Section: Personal agent
    ('Your personal agent.', 'הסוכן האישי שלכם.'),
    ('Always working for you.', 'תמיד עובד בשבילכם.'),
    # Features
    ('Your Agent, Not Just an App', 'סוכן AI, לא רק אפליקציה'),
    ('Visible Beyond EXPOSE', 'חשיפה מעבר ל-EXPOSE'),
    ('Know Exactly What You\'re Worth', 'דעו בדיוק את הערך שלכם'),
    ('Briefs Matched to Your Style', 'בריפים מותאמים לסגנון שלכם'),
    # Why EXPOSE
    ('>Why EXPOSE?<', '>למה EXPOSE?<'),
    # Join community
    ('>Join the community<', '>הצטרפו לקהילה<'),
    # Real campaigns
    ('Real campaigns. Real results.', 'קמפיינים אמיתיים. תוצאות אמיתיות.'),
    # Testimonials
    ('Loved by creatives.', 'אהוב על ידי יוצרים.'),
    # FAQ
    ('Got questions? <span class="italic-accent">Ask EXi.</span>',
     'יש שאלות? <span class="italic-accent">שאלו את EXi.</span>'),
    # Final CTA
    ('Stop chasing. Start getting booked.', 'הפסיקו לרדוף. התחילו לקבל עבודות.'),
    # Buttons
    ('>Book Demo<', '>קבעו דמו<'),
    ('>Watch 2-min tour<', '>סיור קצר 2 דק\'<'),
    # Dashboard
    ('>EXi is active<', '>EXi פעיל<'),
    ('Optimizing Your Career', 'מייעל את הקריירה שלכם'),
    ('>Active Proposal<', '>הצעות פעילות<'),
    ('>Profile Views<', '>צפיות בפרופיל<'),
    ('Above industry avg', 'מעל ממוצע התעשייה'),
    ('>Social Media Eng<', '>מעורבות ברשתות<'),
    ('>Projects Matches<', '>התאמות פרויקטים<'),
    ('Earnings this week', 'הכנסות השבוע'),
    # creatives joined ticker
    ('creatives</b> joined in the last hour', 'יוצרים</b> הצטרפו בשעה האחרונה'),
    ('just joined from', 'הצטרף מ-'),
]

BRANDS_HE = SHARED + [
    ('EXPOSE — Stop Guessing Your Marketing. Let EXi Run It.', 'EXPOSE — הפסיקו לנחש שיווק. תנו ל-EXi לטפל בזה.'),
    ('Stop Guessing Your Marketing.\n      <span class="it italic-accent">Let EXi Run It.</span>',
     'הפסיקו לנחש שיווק.\n      <span class="it italic-accent">תנו ל-EXi לטפל בזה.</span>'),
    ('EXi is live · AI-powered brand-creator matching', 'EXi פעיל · התאמת מותגים-יוצרים מבוססת AI'),
    ('The AI marketing platform that finds the right creators, manages your campaigns, and proves ROI — automatically.',
     'פלטפורמת השיווק מבוססת AI שמוצאת את היוצרים הנכונים, מנהלת את הקמפיינים ומוכיחה ROI — אוטומטית.'),
    ('Finally understand your marketing. And make it work.',
     'סוף סוף הבינו את השיווק שלכם. וגרמו לו לעבוד.'),
    ('Complete marketing ecosystem', 'מערכת שיווק מלאה'),
    ('EXPOSE streamlines every step of the modern marketing workflow.',
     'EXPOSE מייעל כל שלב בתהליך השיווק המודרני.'),
    ('Your AI marketing agent.', 'הסוכן השיווקי ה-AI שלכם.'),
    ('That never sleeps.', 'שלעולם לא ישן.'),
    ('>Why EXPOSE?<', '>למה EXPOSE?<'),
    ('Every creative you\'ll need.', 'כל יוצר שתצטרכו.'),
    ('Real campaigns. Real results.', 'קמפיינים אמיתיים. תוצאות אמיתיות.'),
    ('Loved by brands.', 'אהוב על ידי מותגים.'),
    ('Got questions? <span class="italic-accent">Ask EXi.</span>',
     'יש שאלות? <span class="italic-accent">שאלו את EXi.</span>'),
    ('Stop guessing. Start shipping campaigns.', 'הפסיקו לנחש. התחילו לשגר קמפיינים.'),
    # Workflow steps
    ('>Plan Your Strategy<', '>תכננו את האסטרטגיה<'),
    ('>Find Your Team<', '>מצאו את הצוות שלכם<'),
    ('>Scale Your Marketing<', '>הגדילו את השיווק שלכם<'),
    # Features
    ('Instant Marketing Diagnosis', 'אבחון שיווקי מיידי'),
    ('Auto-Optimization', 'ייעול אוטומטי'),
    ('24/7 Management', 'ניהול 24/7'),
    ('Pixel-Level Attribution', 'ייחוס ברמת פיקסל'),
    ('Every impression, click, and conversion tracked in real time — across every campaign.',
     'כל חשיפה, קליק והמרה נעקבים בזמן אמת — בכל קמפיין.'),
    ('Know what\'s working', 'דעו מה עובד'),
    ('EXi reads your data and shows you exactly where to focus to grow faster.',
     'EXi קורא את הנתונים שלכם ומראה בדיוק איפה להתמקד לצמוח מהר יותר.'),
    ('One place, everything', 'מקום אחד, הכל'),
    ('Briefs, creators, content and strategy — all managed by EXi in a single workspace.',
     'בריפים, יוצרים, תוכן ואסטרטגיה — הכל מנוהל על ידי EXi במרחב עבודה אחד.'),
    ('Never misses a beat', 'לעולם לא מפספס'),
    ('>Book a Demo<', '>קבעו דמו<'),
    ('>Book Demo<', '>קבעו דמו<'),
    ('>Watch 2-min tour<', '>סיור קצר 2 דק\'<'),
    # Dashboard
    ('EXi is active\n      Managing your campaigns', 'EXi פעיל\n      מנהל את הקמפיינים שלכם'),
    ('brands</b> joined in the last hour', 'מותגים</b> הצטרפו בשעה האחרונה'),
]

EXI_HE = SHARED + [
    ('EXi — Your AI Agent | EXPOSE', 'EXi — הסוכן ה-AI שלכם | EXPOSE'),
    ('The Agent that works for you 24/7', 'הסוכן שעובד בשבילכם 24/7'),
    ('EXi finds the projects, grows your visibility, and tells you exactly what to do next — so you just show up and create.',
     'EXi מוצא את הפרויקטים, מגדיל את החשיפה שלכם ואומר בדיוק מה לעשות הלאה — כדי שתוכלו להגיע וליצור.'),
    ('EXi knows your world better than you do.',
     'EXi מכיר את העולם שלכם טוב יותר מכם.'),
    ('EXi plugs into every corner of your career — giving you full coverage, 24/7, without lifting a finger.',
     'EXi מתחבר לכל פינה של הקריירה שלכם — מספק כיסוי מלא, 24/7, בלי להרים אצבע.'),
    ('8 live connections', '8 חיבורים פעילים'),
    # Knows grid
    ('Engagement, reach &amp; best posting times', 'מעורבות, טווח וזמני פרסום אופטימליים'),
    ('Trending sounds, reach &amp; video performance', 'צלילים טרנדיים, טווח וביצועי וידאו'),
    ('Scores, optimizes &amp; tracks acceptance rates', 'מדרג, מייעל ועוקב אחר שיעורי קבלה'),
    ('Manages availability &amp; books shoots for you', 'מנהל זמינות ומזמין צילומים בשבילכם'),
    ('In-demand styles, niches &amp; brand activity', 'סגנונות, נישות ופעילות מותגים מבוקשים'),
    ('Earnings tracking &amp; market rate benchmarks', 'מעקב הכנסות ומדדי שוק'),
    ('Scans open briefs &amp; pre-matches to your style', 'סורק בריפים פתוחים ומתאים לסגנונכם'),
    ('Ranks you vs top creatives in your niche', 'מדרג אתכם מול יוצרים מובילים בנישה'),
    ('>Portfolio<', '>פורטפוליו<'),
    ('>Calendar<', '>יומן<'),
    ('>Market Trends<', '>מגמות שוק<'),
    ('>Payments & Rates<', '>תשלומים ותעריפים<'),
    ('>Project Briefs<', '>בריפים<'),
    ('>Industry Benchmarks<', '>מדדי תעשייה<'),
    ('>Live<', '>חי<'),
    ('>Synced<', '>מסונכרן<'),
    ('>Scanning<', '>סורק<'),
    ('>Watching<', '>עוקב<'),
    # Never Sleeps
    ('EXi Never Sleeps', 'EXi לעולם לא ישן'),
    ('While you rest, EXi is scanning markets, optimizing your profile, and grabbing opportunities before they disappear.',
     'בזמן שאתם נחים, EXi סורק שווקים, מייעל את הפרופיל ותופס הזדמנויות לפני שהן נעלמות.'),
    # Career score
    ('You don\'t need an agency to know your worth',
     'אתם לא צריכים סוכנות כדי לדעת את הערך שלכם'),
    # Acts
    ('EXi acts. You approve.', 'EXi פועל. אתם מאשרים.'),
    ('EXi doesn\'t stop when you do.', 'EXi לא מפסיק כשאתם מפסיקים.'),
    ('One agent, total control.', 'סוכן אחד, שליטה מלאה.'),
    ('You\'re always in control', 'אתם תמיד בשליטה'),
    ('Ready to get discovered?', 'מוכנים להיחשף?'),
    # Sleep items
    ('Updates Your Profile Finder', 'מעדכן את מוצא הפרופיל'),
    ('Keeps your profile sharp and positioned for the brands actively searching your style.',
     'שומר את הפרופיל חד ומיוצב למותגים שמחפשים את הסגנון שלכם.'),
    ('Career Growth Alerts', 'התראות צמיחת קריירה'),
    ('Notifies you the moment your visibility spikes or a brand is actively searching your niche.',
     'מודיע לכם ברגע שהחשיפה מזנקת או שמותג מחפש את הנישה שלכם.'),
    ('Initiates Your Screening', 'מתחיל את הסינון בשמכם'),
    ('Pre-screens briefs and drafts your application before you even open the app.',
     'מסנן בריפים ומכין את הגשתכם לפני שפותחים את האפליקציה.'),
    ('Daily Career Reports', 'דוחות קריירה יומיים'),
    ('Instant Opportunity Alerts', 'התראות הזדמנויות מיידיות'),
    ('Your Next Career Move', 'הצעד הקריירה הבא שלכם'),
    # Bento items
    ('Career Management', 'ניהול קריירה'),
    ('Work Intelligence', 'אינטליגנציה מקצועית'),
    ('Portfolio Optimization', 'ייעול פורטפוליו'),
    ('Market Trend Tracking', 'מעקב מגמות שוק'),
    ('Auto Project Matching', 'התאמת פרויקטים אוטומטית'),
    ('Rate Advisor', 'יועץ תעריפים'),
    # Buttons
    ('>Start for Free<', '>התחילו בחינם<'),
    ('>Get Your Full Audit<', '>קבלו את הביקורת המלאה<'),
    ('>Let EXi Work for You<', '>תנו ל-EXi לעבוד בשבילכם<'),
    ('>Book a Meeting<', '>קבעו פגישה<'),
    # Dashboard text
    ('EXi is active\n      Optimizing Your Career', 'EXi פעיל\n      מייעל את הקריירה שלכם'),
    ('Above industry avg', 'מעל ממוצע התעשייה'),
    ('Earnings this week', 'הכנסות השבוע'),
]

EXI_BRANDS_HE = SHARED + [
    ('EXi for Brands — Campaign AI Agent | EXPOSE', 'EXi למותגים — סוכן AI לקמפיינים | EXPOSE'),
    ('The Agent that runs your campaigns 24/7', 'הסוכן שמנהל את הקמפיינים שלכם 24/7'),
    ('EXi finds the right creators, manages the relationships, and optimises performance — so your team can focus on strategy, not logistics.',
     'EXi מוצא את היוצרים הנכונים, מנהל את הקשרים ומייעל ביצועים — כדי שהצוות שלכם יתמקד באסטרטגיה, לא בלוגיסטיקה.'),
    ('EXi knows your brand better than your agency does.',
     'EXi מכיר את המותג שלכם טוב יותר מהסוכנות שלכם.'),
    ('EXi analyses your past campaigns, brand guidelines, and audience data — then finds creators who actually fit.',
     'EXi מנתח קמפיינים קודמים, הנחיות מותג ונתוני קהל — ואז מוצא יוצרים שבאמת מתאימים.'),
    ('8 live connections', '8 חיבורים פעילים'),
    # Knows grid
    ('Business Ad performance, reach &amp; ROAS metrics', 'ביצועי פרסום, טווח ומדדי ROAS'),
    ('Creator performance tracking &amp; content monitoring', 'מעקב ביצועי יוצרים וניטור תוכן'),
    ('Campaign analytics, audience data &amp; trend signals', 'אנליטיקת קמפיין, נתוני קהל ואיתותי מגמות'),
    ('Content calendar management &amp; delivery tracking', 'ניהול לוח תוכן ומעקב אספקה'),
    ('Competitor campaigns, creator moves &amp; market shifts', 'קמפיינים מתחרים, מהלכי יוצרים ומשמרות שוק'),
    ('Invoice tracking, payment status &amp; budget alerts', 'מעקב חשבוניות, סטטוס תשלומים והתראות תקציב'),
    ('Contract terms, compliance checks &amp; deliverable status', 'תנאי חוזה, בדיקות תאימות וסטטוס ספקים'),
    ('Audience overlap, demographic fit &amp; psychographic matching', 'חפיפת קהלים, התאמה דמוגרפית ותאימות פסיכוגרפית'),
    # Sections
    ('EXi Never Sleeps', 'EXi לעולם לא ישן'),
    ('While your team sleeps, EXi is monitoring creator content, tracking campaign pacing, and flagging anything that needs attention.',
     'בזמן שהצוות שלכם ישן, EXi מנטר תוכן יוצרים, עוקב אחר קצב הקמפיין ומסמן כל מה שדורש תשומת לב.'),
    ('Real data. Real ROI. No guesswork.', 'נתונים אמיתיים. ROI אמיתי. בלי ניחושים.'),
    ('EXi acts. You approve.', 'EXi פועל. אתם מאשרים.'),
    ('EXi doesn\'t stop when you do.', 'EXi לא מפסיק כשאתם מפסיקים.'),
    ('One agent, total control.', 'סוכן אחד, שליטה מלאה.'),
    ('You\'re always in control', 'אתם תמיד בשליטה'),
    ('Ready for smarter campaigns?', 'מוכנים לקמפיינים חכמים יותר?'),
    # Sleep items
    ('Monitors Every Campaign 24/7', 'מנטר כל קמפיין 24/7'),
    ('Creator Deliverable Alerts', 'התראות ספקים מיוצרים'),
    ('Budget Pacing Guard', 'שמירת קצב תקציב'),
    ('Daily Campaign Reports', 'דוחות קמפיין יומיים'),
    ('Creator Performance Alerts', 'התראות ביצועי יוצרים'),
    ('Budget Optimization', 'ייעול תקציב'),
    # Bento items
    ('Campaign Management', 'ניהול קמפיין'),
    ('Creator Intelligence', 'אינטליגנציה ליוצרים'),
    ('Content Pipeline', 'צנרת תוכן'),
    ('Budget Optimizer', 'ממטב תקציב'),
    ('Market Intelligence', 'אינטליגנציה שוקית'),
    ('Brand Safety Monitor', 'מוניטור בטיחות מותג'),
    # Buttons
    ('>Start for Free<', '>התחילו בחינם<'),
    ('>View Full Report<', '>צפו בדוח המלא<'),
    ('>Let EXi Run Your Campaigns<', '>תנו ל-EXi לנהל את הקמפיינים שלכם<'),
    ('>Book a Demo<', '>קבעו דמו<'),
    # Dashboard
    ('EXi is active\n      Managing your campaigns', 'EXi פעיל\n      מנהל את הקמפיינים שלכם'),
]

ABOUT_HE = SHARED + [
    ('Built by someone who lived it.', 'נבנה על ידי מי שחי את זה.'),
    ('Our Story', 'הסיפור שלנו'),
    ('We didn\'t build EXPOSE to check a box or chase a trend. The problem was ours — we lived it, and we knew someone had to fix it.',
     'לא בנינו את EXPOSE כדי לסמן תיבה או לרדוף אחרי טרנד. הבעיה הייתה שלנו — חיינו אותה, וידענו שמישהו צריך לתקן אותה.'),
    ('Free forever', 'חינם לתמיד'),
    ('EXPOSE Platform', 'פלטפורמת EXPOSE'),
    ('10K+', '10K+'),
    ('>Creatives<', '>יוצרים<'),
    ('Founded', 'נוסד'),
    # Sections
    ('One freelancer, one broken system.', 'פרילנסר אחד, מערכת שבורה אחת.'),
    ('Three things we refuse to accept.', 'שלושה דברים שאנחנו מסרבים לקבל.'),
    ('How we got here.', 'איך הגענו לכאן.'),
    ('This is just the beginning.', 'זה רק ההתחלה.'),
    ('The principles we build by.', 'העקרונות שאנחנו בונים לפיהם.'),
    ('Real people who care.', 'אנשים אמיתיים שאכפת להם.'),
    ('Ready to be part of something real?', 'מוכנים להיות חלק ממשהו אמיתי?'),
    # Why cards
    ('Fair pay for real work', 'תשלום הוגן לעבודה אמיתית'),
    ('Talent deserves to be seen', 'כישרון ראוי להיראות'),
    ('Marketing should feel human', 'שיווק צריך להרגיש אנושי'),
    # Journey
    ('The problem becomes a mission.', 'הבעיה הופכת למשימה.'),
    ('The first prototype is born.', 'הפרוטוטיפ הראשון נולד.'),
    ('A platform becomes a movement.', 'פלטפורמה הופכת לתנועה.'),
    ('Real work. Real money. Real proof.', 'עבודה אמיתית. כסף אמיתי. הוכחה אמיתית.'),
    ('The best is genuinely ahead.', 'הטוב ביותר עוד לפנינו.'),
    # Origin text
    ('So instead of complaining about it, he started building.',
     'אז במקום להתלונן על זה, הוא התחיל לבנות.'),
    ('EXPOSE is for the creative who deserves better, the brand that wants more, and the agency that\'s tired of guessing.',
     'EXPOSE מיועד ליוצר שמגיע לו יותר, למותג שרוצה יותר, ולסוכנות שעייפה לנחש.'),
    ('And we\'re just getting started.', 'ואנחנו רק בהתחלה.'),
    # Values
    ('Radical Transparency', 'שקיפות מוחלטת'),
    ('Creators First', 'יוצרים קודמים'),
    ('Built to Work For You', 'נבנה לעבוד בשבילכם'),
    ('Experience, Not Theory', 'ניסיון, לא תיאוריה'),
    # Team roles
    ('Founder &amp; CEO', 'מייסד ומנכ"ל'),
    ('Head of Product', 'ראש מחלקת מוצר'),
    ('Lead Engineer', 'מהנדס ראשי'),
    ('Head of Partnerships', 'ראש שיתופי פעולה'),
    # CTA
    ('>Join EXPOSE today<', '>הצטרפו ל-EXPOSE היום<'),
    ('>Join<', '>הצטרפו<'),
]

BLOG_HE = SHARED + [
    ('The creator economy, decoded.', 'כלכלת היוצרים, מפוענחת.'),
    ('EXPOSE Blog', 'בלוג EXPOSE'),
    ('Insights on AI marketing, brand-creator collaboration, and what\'s next for the creative industry.',
     'תובנות על שיווק AI, שיתוף פעולה מותג-יוצר ומה הולך לקרות בתעשייה היצירתית.'),
    # Filter tabs
    ('>All Posts<', '>כל הפוסטים<'),
    ('>AI &amp; Automation<', '>AI ואוטומציה<'),
    ('>Brand Strategy<', '>אסטרטגיית מותג<'),
    ('>Creator Economy<', '>כלכלת יוצרים<'),
    ('>Platform<', '>פלטפורמה<'),
    # Post categories (tags)
    ('>AI &amp; Automation</', '>AI ואוטומציה</'),
    ('>Brand Strategy</', '>אסטרטגיית מותג</'),
    ('>Creator Economy</', '>כלכלת יוצרים</'),
    ('>Platform</', '>פלטפורמה</'),
    # Newsletter
    ('Insights, straight to your inbox.', 'תובנות, ישירות לתיבת הדואר שלכם.'),
    ('Stay in the loop', 'הישארו בעניינים'),
    ('One email per week. No fluff. Just what you need to stay ahead.',
     'אימייל אחד בשבוע. ללא פאפוזות. רק מה שצריך כדי להישאר קדימה.'),
    ('>Subscribe<', '>הירשמו<'),
    ('Your email address', 'כתובת האימייל שלכם'),
    # min read
    ('min read', 'דק\' קריאה'),
    # Featured badge
    ('>Featured<', '>נבחר<'),
]

CONTACT_HE = SHARED + [
    ('Contact Us — EXPOSE', 'צרו קשר — EXPOSE'),
    # Hero
    ('We\'re here.\n    <span class="italic-accent">Say hello.</span>',
     'אנחנו כאן.\n    <span class="italic-accent">שלחו שלום.</span>'),
    ('We built EXPOSE because creatives deserve better tools and brands deserve real connections. Whether you have a big idea, a quick question, or just want to say hi — we genuinely want to hear from you.',
     'בנינו את EXPOSE כי יוצרים מגיעים לכלים טובים יותר ומותגים מגיעים לחיבורים אמיתיים. בין אם יש לכם רעיון גדול, שאלה מהירה, או פשוט רוצים לומר שלום — אנחנו באמת רוצים לשמוע מכם.'),
    ('Usually replies within 24h', 'עונים בדרך כלל תוך 24 שעות'),
    ('Real humans, not bots', 'בני אדם אמיתיים, לא בוטים'),
    ('English &amp; Hebrew', 'עברית ואנגלית'),
    # Form section
    ('>Get in touch<', '>צרו קשר<'),
    ('Tell us what\'s on your mind', 'ספרו לנו מה על הלב'),
    ('Whether you\'re a brand ready to launch campaigns, a creative looking to grow, or just want to explore — we\'d love to start a conversation.',
     'בין אם אתם מותג מוכן להשיק קמפיינים, יוצר שרוצה לצמוח, או פשוט רוצים לחקור — נשמח להתחיל שיחה.'),
    # Topic pills
    ('What\'s this about?', 'על מה זה?'),
    ('>Just saying hi<', '>רק אומרים שלום<'),
    ('>I\'m a Brand<', '>אני מותג<'),
    ('>I\'m a Creative<', '>אני יוצר<'),
    ('>Partnerships<', '>שיתופי פעולה<'),
    ('>Press &amp; Media<', '>עיתונות ומדיה<'),
    # Form labels
    ('>Your name<', '>השם שלכם<'),
    ('What should we call you?', 'מה לקרוא לכם?'),
    ('>Email address<', '>כתובת אימייל<'),
    ('Where can we reach you?', 'איך ניצור איתכם קשר?'),
    ('>Your message<', '>ההודעה שלכם<'),
    ('We\'re all ears. The more context you share, the better we can help — though a simple \'hi\' works too.',
     'אנחנו כולנו אוזניים. ככל שתשתפו יותר הקשר, נוכל לעזור טוב יותר — אם כי גם \'שלום\' פשוט עובד.'),
    ('>Send message<', '>שלחו הודעה<'),
    ('We keep your info private. No spam, ever.', 'אנחנו שומרים על הפרטיות שלכם. אין ספאם, לעולם.'),
    # Success state
    ('>Message sent!<', '>ההודעה נשלחה!<'),
    ('A real person on our team will read this and reply personally. We usually get back within a few hours during business days.',
     'אדם אמיתי בצוות שלנו יקרא את זה ויענה אישית. בדרך כלל חוזרים תוך כמה שעות בימי עסקים.'),
    ('>Send another message<', '>שלחו הודעה נוספת<'),
    # Sidebar
    ('Our team reads every message', 'הצוות שלנו קורא כל הודעה'),
    ('You\'re not talking to a ticket system', 'אתם לא מדברים עם מערכת כרטיסים'),
    ('>Fast response<', '>תגובה מהירה<'),
    ('Usually within a few hours on business days', 'בדרך כלל תוך כמה שעות בימי עסקים'),
    ('>Other ways to reach us<', '>דרכים נוספות ליצירת קשר<'),
    ('>Email<', '>אימייל<'),
    ('>WhatsApp<', '>WhatsApp<'),
    ('>Instagram<', '>Instagram<'),
    ('>TikTok<', '>TikTok<'),
    ('>LinkedIn<', '>LinkedIn<'),
    ('Based in Tel Aviv, Israel · Working with creatives worldwide',
     'מבוססים בתל אביב, ישראל · עובדים עם יוצרים ברחבי העולם'),
    # Starting points section
    ('Not sure where to start?', 'לא בטוחים מאין להתחיל?'),
    ('Pick what fits.\n    <span class="italic-accent">We\'ll take it from there.</span>',
     'בחרו מה מתאים.\n    <span class="italic-accent">אנחנו נמשיך משם.</span>'),
    ('>I\'m a Brand<', '>אני מותג<'),
    ('Looking to launch creator campaigns, find the right talent, or get a personalized product demo from our team.',
     'מחפשים להשיק קמפיינים עם יוצרים, למצוא כישרון מתאים, או לקבל הדגמת מוצר אישית מהצוות שלנו.'),
    ('>I\'m a Creative<', '>אני יוצר<'),
    ('Want to grow my career, get matched with brands that fit my style, or learn more about what EXi can do for me.',
     'רוצה לצמוח בקריירה, להיות מותאם למותגים שמתאימים לסגנוני, או ללמוד עוד על מה ש-EXi יכול לעשות עבורי.'),
    ('>Let\'s Partner<', '>בואו נשתף פעולה<'),
    ('Interested in integrations, media coverage, co-marketing, or a strategic partnership with the EXPOSE team.',
     'מתעניינים באינטגרציות, סיקור מדיה, שיווק משותף, או שותפות אסטרטגית עם צוות EXPOSE.'),
    ('Start a conversation', 'התחילו שיחה'),
]

pages = [
    ('site-he.html', SITE_HE),
    ('site-brands-he.html', BRANDS_HE),
    ('site-exi-he.html', EXI_HE),
    ('site-exi-brands-he.html', EXI_BRANDS_HE),
    ('site-about-he.html', ABOUT_HE),
    ('site-blog-he.html', BLOG_HE),
    ('site-contact-he.html', CONTACT_HE),
]

print('Translating Hebrew pages...')
for fname, trans in pages:
    translate_page(fname, trans)

print('\nDone.')
