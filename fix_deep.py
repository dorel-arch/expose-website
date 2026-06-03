#!/usr/bin/env python3
"""Deep fix: translate all remaining content including cards, FAQs, notifications, testimonials."""
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

# ─── TESTIMONIALS shared across site-he and site-brands-he ───────────────────
TESTI_CREATIVES = [
    ('"EXi turned an underperforming brief into 405 leads in 71 days. I didn\'t even know I\'d be earning this much from creative work."',
     '"EXi הפך בריף חלש ל-405 לידים תוך 71 יום. לא ידעתי שאוכל להרוויח כל כך הרבה מעבודה יצירתית."'),
    ('"My first month I booked two editorials and a campaign. EXi pitched me to brands I would\'ve been too shy to email."',
     '"בחודש הראשון קיבלתי שני אדיטוריאלים וקמפיין. EXi פנה למותגים שהייתי ביישן מכדי לפנות אליהם."'),
    ('"I used to spend hours filling forms trying to reach brands. EXPOSE did it for me in 4 weeks. I now know I can compete."',
     '"נהגתי לבזבז שעות על טפסים לניסיון להגיע למותגים. EXPOSE עשה את זה עבורי תוך 4 שבועות. עכשיו אני יודע שאני יכול להתחרות."'),
    ('"It\'s like having an agent that never sleeps. Three branded gigs in my first 6 weeks — and EXi raised my rates."',
     '"זה כמו שיש לך סוכן שלעולם לא ישן. שלושה פרויקטים ממותגים בשישה שבועות הראשונים — ו-EXi העלה לי את התעריפים."'),
    ('"The brief matching is uncanny — every project feels like it was made for me. Pay lands on time, every time."',
     '"ההתאמה לבריפים מדויקת להפליא — כל פרויקט מרגיש כאילו נוצר עבורי. התשלום מגיע בזמן, בכל פעם."'),
    ('"EXi told us exactly what to post, when, and why. Engagement doubled by week three. It\'s a marketing director that never stops."',
     '"EXi אמר לנו בדיוק מה לפרסם, מתי ולמה. המעורבות הוכפלה עד השבוע השלישי. זה מנהל שיווק שלעולם לא מפסיק."'),
    ('"I went from one shoot a month to four. EXi knows my style better than half my agents did."',
     '"עברתי מצילום אחד בחודש לארבעה. EXi מכיר את הסגנון שלי טוב יותר ממחצית הסוכנים שלי."'),
    ('"Two cover commissions in my second month. The whole pitching nightmare just… disappeared."',
     '"שתי עבודות עטיפה בחודש השני. הסיוט של הפיצ\'ים פשוט... נעלם."'),
    ('"Briefs that actually match my voice. I closed a brand campaign two days after joining — I wasn\'t ready."',
     '"בריפים שבאמת מתאימים לקול שלי. סגרתי קמפיין מותג יומיים אחרי ההצטרפות — לא הייתי מוכן."'),
    ('"The escrow is what sold me. No more chasing invoices for 90 days. Money lands, work flows."',
     '"הנאמנות היא מה שמכר אותי. לא עוד רדיפה אחרי חשבוניות 90 יום. הכסף מגיע, העבודה זורמת."'),
    ('"EXi rewrote my portfolio intro overnight. My acceptance rate jumped from 12% to 38%."',
     '"EXi כתב מחדש את מבוא הפורטפוליו שלי בלילה. שיעור הקבלה שלי קפץ מ-12% ל-38%."'),
    ('"I stopped agency hopping. Two Vogue Italia features in one season — straight through the app."',
     '"הפסקתי לקפוץ בין סוכנויות. שתי פיצ\'רים ב-Vogue Italia בעונה אחת — ישירות דרך האפליקציה."'),
]

TESTI_BRANDS = [
    ('"We shipped a launch in 6 days that used to take 6 weeks. EXi found the right creators on the first try."',
     '"שיגרנו השקה תוך 6 ימים שנהגה לקחת 6 שבועות. EXi מצא את היוצרים הנכונים בפעם הראשונה."'),
    ('"Our first influencer campaign generated 4.2× ROI. EXPOSE took the guesswork out of marketing — for good."',
     '"קמפיין האינפלואנסרים הראשון שלנו יצר ROI של 4.2×. EXPOSE הסיר את הניחושים מהשיווק — לתמיד."'),
    ('"12 perfect matches in 10 minutes. I used to spend three weeks on outreach for the same result."',
     '"12 התאמות מושלמות ב-10 דקות. נהגתי לבזבז שלושה שבועות על פנייה לאותה תוצאה."'),
    ('"Pixel-level attribution means I can prove influencer spend works. CFO finally signed off on scaling."',
     '"ייחוס ברמת פיקסל אומר שאני יכול להוכיח שהוצאות האינפלואנסרים עובדות. ה-CFO סוף סוף אישר הרחבה."'),
    ('"EXi flagged a creator running engagement fraud before we paid them. That alone paid for the platform."',
     '"EXi זיהה יוצר שמריץ הונאת מעורבות לפני שלמנו לו. זה לבד שילם על הפלטפורמה."'),
    ('"Our quarterly campaign launches are now monthly. Same team, 4× output, half the back-and-forth."',
     '"ההשקות הרבעוניות שלנו הפכו לחודשיות. אותו צוות, פלט של 4×, חצי ממשחקי הפינג פונג."'),
]

# ─── site-he.html ───────────────────────────────
SITE_DEEP = TESTI_CREATIVES + [
    # Check-list items
    ('<span class="cl-title">Work comes to you</span>',
     '<span class="cl-title">עבודה מגיעה אליכם</span>'),
    ('<span class="cl-sub">EXi matches your style and sends your profile directly to the right brands — no cold pitching.</span>',
     '<span class="cl-sub">EXi מתאים את הסגנון שלכם ושולח את הפרופיל ישירות למותגים הנכונים — בלי פנייה קרה.</span>'),
    ('<span class="cl-title">EXi is your personal agent</span>',
     '<span class="cl-title">EXi הוא הסוכן האישי שלכם</span>'),
    ('<span class="cl-sub">Know exactly what to post, how to improve your profile, and what gets you seen by more brands.</span>',
     '<span class="cl-sub">דעו בדיוק מה לפרסם, איך לשפר את הפרופיל, ומה גורם לכם להיראות על ידי יותר מותגים.</span>'),
    ('<span class="cl-title">Manage your career in one place</span>',
     '<span class="cl-title">נהלו את הקריירה במקום אחד</span>'),
    ('<span class="cl-sub">Briefs, portfolio, bookings and progress — all tracked in one clean dashboard.</span>',
     '<span class="cl-sub">בריפים, פורטפוליו, הזמנות ותהליך — הכל מעוקב בלוח בקרה אחד ומסודר.</span>'),
    ('<span class="cl-title">Stop juggling platforms</span>',
     '<span class="cl-title">הפסיקו ללכת בין פלטפורמות</span>'),
    ('<span class="cl-sub">No more switching between 10 apps. Everything work-related happens right here.</span>',
     '<span class="cl-sub">לא עוד מעבר בין 10 אפליקציות. הכל שקשור לעבודה קורה כאן.</span>'),
    # Mobile benefit cards
    ('<p class="mb-title">Work finds you</p>',
     '<p class="mb-title">עבודה מוצאת אתכם</p>'),
    ('<p class="mb-desc">EXi constantly matches your profile to new briefs — get discovered without lifting a finger.</p>',
     '<p class="mb-desc">EXi מתאים את הפרופיל שלכם לבריפים חדשים ללא הרף — תיחשפו בלי להרים אצבע.</p>'),
    ('<span class="mb-tag">Avg. 3 matches/week</span>', '<span class="mb-tag">ממוצע 3 התאמות/שבוע</span>'),
    ('<p class="mb-title">EXi is your agent</p>', '<p class="mb-title">EXi הוא הסוכן שלכם</p>'),
    ('<p class="mb-desc">Personalized tips on what to post, how to improve, and what gets you more exposure.</p>',
     '<p class="mb-desc">טיפים אישיים על מה לפרסם, איך להשתפר, ומה מביא לכם יותר חשיפה.</p>'),
    ('<span class="mb-tag">Personal AI agent</span>', '<span class="mb-tag">סוכן AI אישי</span>'),
    ('<p class="mb-title">Your career, organized</p>', '<p class="mb-title">הקריירה שלכם, מסודרת</p>'),
    ('<p class="mb-desc">Briefs, bookings, portfolio and career progress — all in one clean dashboard, nothing scattered.</p>',
     '<p class="mb-desc">בריפים, הזמנות, פורטפוליו ותהליך קריירה — הכל בלוח בקרה אחד ומסודר, בלי בלגן.</p>'),
    ('<span class="mb-tag">Zero juggling</span>', '<span class="mb-tag">אפס ריבוי משימות</span>'),
    ('<p class="mb-title">One platform, everything</p>', '<p class="mb-title">פלטפורמה אחת, הכל</p>'),
    ('<p class="mb-desc">No more 10 tabs open. Every part of your work life — contracts, briefs, calendar — lives here.</p>',
     '<p class="mb-desc">לא עוד 10 טאבים פתוחים. כל חלק מחיי העבודה שלכם — חוזים, בריפים, יומן — כאן.</p>'),
    ('<span class="mb-tag">All-in-one</span>', '<span class="mb-tag">הכל כלול</span>'),
    # CTA button
    ('>Find Talent</a>', '>מצאו יוצרים</a>'),
    # Push notifications
    ('<div class="pp-head">EXi · brief match <span class="pp-ago">now</span></div>',
     '<div class="pp-head">EXi · התאמת בריף <span class="pp-ago">עכשיו</span></div>'),
    ('<div class="pp-meta">Cleared to your account</div>',
     '<div class="pp-meta">הועבר לחשבון שלכם</div>'),
    # FAQ questions and answers
    ('data-q="How does EXi find me work?"',
     'data-q="איך EXi מוצא לי עבודה?"'),
    ('data-a="I scan live briefs across the platform 24/7, match you to ones your portfolio and rates fit, and submit a tailored pitch automatically. You only see the matches that actually fit your style."',
     'data-a="אני סורק בריפים פעילים בפלטפורמה 24/7, מתאים לכם את אלה שהפורטפוליו והתעריפים שלכם מתאימים אליהם, ושולח פיצ\'ים מותאמים אוטומטית. אתם רואים רק את ההתאמות שבאמת מתאימות לסגנונכם."'),
    ('data-q="How much does EXPOSE take?"',
     'data-q="כמה EXPOSE לוקח?"'),
    ('data-a="6% of project value — about a third of what a traditional agent would charge. No subscription fees, no hidden costs, no charges for unsuccessful pitches."',
     'data-a="6% מערך הפרויקט — כשליש ממה שסוכן מסורתי יגבה. אין דמי מנוי, אין עלויות נסתרות, ואין חיובים על פיצ\'ים לא מוצלחים."'),
    ('data-q="When and how do I get paid?"',
     'data-q="מתי ואיך אני מקבל תשלום?"'),
    ('data-a="Brands fund the project upfront into escrow. The moment you ship a milestone, the cash releases — usually within 24h. No chasing invoices, no 90-day net terms."',
     'data-a="המותגים ממנים את הפרויקט מראש לנאמנות. ברגע ששולחים אבן דרך, הכסף משתחרר — בדרך כלל תוך 24 שעות. לא עוד רדיפה אחרי חשבוניות, לא תנאי 90 יום."'),
    ('data-q="Do I need experience?"',
     'data-q="האם אני צריך ניסיון?"'),
    ('data-a="No — I work for anyone serious about a creative career. I\'ll review your portfolio in seconds and tell you exactly what to build first to attract your first paid brief."',
     'data-a="לא — אני עובד עבור כל מי שרציני לגבי קריירה יצירתית. אסקור את הפורטפוליו שלכם בשניות ואספר בדיוק מה לבנות קודם כדי למשוך את הבריף בתשלום הראשון."'),
    ('data-q="How do you know my style?"',
     'data-q="איך אתה מכיר את הסגנון שלי?"'),
    ('data-a="I read your portfolio, social posts, and engagement data — then map the gap between where you are and the brands you want. The more you use me, the sharper my picks get."',
     'data-a="אני קורא את הפורטפוליו, פוסטים ברשתות ונתוני מעורבות — ואז ממפה את הפער בין המקום שאתם נמצאים לבין המותגים שאתם רוצים. ככל שמשתמשים בי יותר, ההתאמות שלי מדויקות יותר."'),
    ('data-q="Can I turn down a brief?"',
     'data-q="אני יכול לדחות בריף?"'),
    ('data-a="Always. Every match goes to you first — I never commit you to anything. Decline as many as you like; I learn from each one and refine the next batch."',
     'data-a="תמיד. כל התאמה מגיעה אליכם קודם — לעולם לא מחייב אתכם לכלום. דחו כמה שתרצו; אני לומד מכל אחת ומשפר את הבאות."'),
]

# ─── site-brands-he.html ───────────────────────────────
BRANDS_DEEP = TESTI_BRANDS + [
    # Check-list items
    ('<span class="cl-title">Live data, every metric</span>',
     '<span class="cl-title">נתונים חיים, כל מדד</span>'),
    ('<span class="cl-sub">Impressions, engagement, conversions and ROI — all updated in real time.</span>',
     '<span class="cl-sub">חשיפות, מעורבות, המרות ו-ROI — הכל מתעדכן בזמן אמת.</span>'),
    ('<span class="cl-title">Understand what\'s working</span>',
     '<span class="cl-title">הבינו מה עובד</span>'),
    ('<span class="cl-sub">EXi reads your numbers and tells you exactly what\'s driving results — and what isn\'t.</span>',
     '<span class="cl-sub">EXi קורא את המספרים שלכם ואומר בדיוק מה מניע תוצאות — ומה לא.</span>'),
    ('<span class="cl-title">Your full marketing stack</span>',
     '<span class="cl-title">סטאק השיווק המלא שלכם</span>'),
    ('<span class="cl-sub">Briefs, creators, content and strategy — all in one place, managed by EXi.</span>',
     '<span class="cl-sub">בריפים, יוצרים, תוכן ואסטרטגיה — הכל במקום אחד, מנוהל על ידי EXi.</span>'),
    ('<span class="cl-title">Always-on optimization</span>',
     '<span class="cl-title">אופטימיזציה ללא הפסקה</span>'),
    ('<span class="cl-sub">EXi monitors and improves your campaigns continuously — no manual work needed.</span>',
     '<span class="cl-sub">EXi מנטר ומשפר את הקמפיינים שלכם ללא הרף — ללא צורך בעבודה ידנית.</span>'),
    # Mobile benefit cards
    ('<p class="mb-title">See everything live</p>', '<p class="mb-title">ראו הכל בשידור חי</p>'),
    ('<span class="mb-tag">Live dashboard</span>', '<span class="mb-tag">לוח בקרה חי</span>'),
    ('<span class="mb-tag">Zero app-switching</span>', '<span class="mb-tag">אפס מעבר בין אפליקציות</span>'),
    ('<p class="mb-desc">EXi monitors your campaigns 24/7 and optimizes in real time — while you focus on the big picture.</p>',
     '<p class="mb-desc">EXi מנטר את הקמפיינים שלכם 24/7 ומייעל בזמן אמת — בזמן שאתם מתמקדים בתמונה הגדולה.</p>'),
    ('<span class="mb-tag">24/7 AI agent</span>', '<span class="mb-tag">סוכן AI 24/7</span>'),
    # FAQ
    ('data-q="How fast can I launch a campaign?"',
     'data-q="כמה מהר אני יכול להשיק קמפיין?"'),
    ('data-a="Most brands launch their first campaign within 6 days. If you arrive with a brief, I can generate 12 matching creators in under 10 minutes."',
     'data-a="רוב המותגים משיקים את הקמפיין הראשון תוך 6 ימים. אם מגיעים עם בריף, אני יכול לייצר 12 יוצרים מתאימים תוך פחות מ-10 דקות."'),
    ('data-q="How do you vet creators?"',
     'data-q="איך אתם בודקים יוצרים?"'),
    ('data-a="Every creator passes audience-authenticity checks, engagement-fraud detection, and a manual editorial review before joining EXPOSE. I remove anyone whose audience quality dips below our bar."',
     'data-a="כל יוצר עובר בדיקות אותנטיות קהל, זיהוי הונאת מעורבות וסקירה עריכתית ידנית לפני ההצטרפות. אני מסיר כל מי שאיכות הקהל שלו יורדת מתחת לסף שלנו."'),
    ('data-q="How is ROI tracked?"',
     'data-q="איך ROI נמדד?"'),
    ('data-a="Pixel-level attribution back to revenue. Every post carries a UTM tag, and I track reach, engagement, link-level CTR, conversions, and — for e-commerce — revenue per creator."',
     'data-a="ייחוס ברמת פיקסל עד להכנסות. כל פוסט נושא תג UTM, ואני עוקב אחר טווח, מעורבות, CTR ברמת קישור, המרות — ולמסחר אלקטרוני — הכנסות לכל יוצר."'),
    ('data-q="What does pricing look like?"',
     'data-q="איך נראה התמחור?"'),
    ('data-a="A flat monthly fee for the workspace — no success fees, no cut of creator payouts. Plans start at $390/mo. Creator budgets are separate and transparent. 14-day free trial on every plan."',
     'data-a="דמי מנוי חודשיים קבועים לסביבת העבודה — ללא עמלת הצלחה, ללא קיצוץ מתשלומי יוצרים. תוכניות מתחילות ב-$390 לחודש. תקציבי יוצרים נפרדים ושקופים. ניסיון חינם של 14 ימים בכל תוכנית."'),
    ('data-q="Can I bring my own creators?"',
     'data-q="האם אני יכול להביא את היוצרים שלי?"'),
    ('data-a="Yes — invite your existing roster into your workspace and manage them alongside new matches. Same contracts, same dashboard, same payouts."',
     'data-a="כן — הזמינו את הרשימה הקיימת שלכם לסביבת העבודה ונהלו אותם לצד התאמות חדשות. אותם חוזים, אותו לוח בקרה, אותם תשלומים."'),
    ('data-q="Do you handle international markets?"',
     'data-q="האם אתם מטפלים בשווקים בינלאומיים?"'),
    ('data-a="40+ markets with local creator pools, native-language briefs, and region-specific compliance (GDPR, LGPD, etc.). One workspace, every region."',
     'data-a="40+ שווקים עם מאגרי יוצרים מקומיים, בריפים בשפות מקוריות ותאימות ספציפית לאזור (GDPR, LGPD וכו\'). סביבת עבודה אחת, כל אזור."'),
]

# ─── site-exi-he.html ───────────────────────────────
EXI_DEEP = [
    # Daily automation section
    ('<div class="eyebrow sr">Daily automation</div>', '<div class="eyebrow sr">אוטומציה יומית</div>'),
    ('<p class="no-stop-sub sr s2">Every day, EXi runs these tasks on your behalf — finding opportunities, improving your profile, and keeping your career growing.</p>',
     '<p class="no-stop-sub sr s2">כל יום, EXi מבצע משימות אלה בשמכם — מוצא הזדמנויות, משפר את הפרופיל ושומר על צמיחת הקריירה.</p>'),
    ('<p>A concise summary of your visibility, new briefs, and what EXi did overnight — delivered every morning.</p>',
     '<p>סיכום תמציתי של הנראות שלכם, בריפים חדשים ומה ה-EXi עשה בלילה — מגיע כל בוקר.</p>'),
    ('            Every morning\n          </div>',
     '            כל בוקר\n          </div>'),
    ('<p>Brands searching for your style right now — EXi flags them before anyone else sees the brief.</p>',
     '<p>מותגים שמחפשים את הסגנון שלכם עכשיו — EXi מסמן אותם לפני שמישהו אחר רואה את הבריף.</p>'),
    ('<p>EXi tells you exactly what to do next — which brands to target, what to post, how to level up your score.</p>',
     '<p>EXi אומר לכם בדיוק מה לעשות הלאה — אילו מותגים לטרגט, מה לפרסם, איך לשפר את הניקוד.</p>'),
    ('            Weekly strategy\n          </div>',
     '            אסטרטגיה שבועית\n          </div>'),
    # One agent section
    ('<div class="eyebrow sr">Everything in one place</div>',
     '<div class="eyebrow sr">הכל במקום אחד</div>'),
    ('<p class="sub sr s2">EXi doesn\'t just assist — it runs your entire career operation from a single dashboard.</p>',
     '<p class="sub sr s2">EXi לא רק מסייע — הוא מנהל את כל פעולות הקריירה שלכם מלוח בקרה אחד.</p>'),
    ('<div class="bento-badge">Core feature</div>', '<div class="bento-badge">תכונת ליבה</div>'),
    ('<p>Every booking, brief, deadline, and conversation — tracked and managed in one clean view. No more spreadsheets.</p>',
     '<p>כל הזמנה, בריף, דדליין ושיחה — מעוקבים ומנוהלים בתצוגה אחת ומסודרת. לא עוד גיליונות.</p>'),
    ('<p>Only surfaces briefs that truly fit your style and goals.</p>',
     '<p>מציג רק בריפים שבאמת מתאימים לסגנון ולמטרות שלכם.</p>'),
    # Fix mixed Hebrew/English h4
    ('<h4>פורטפוליו Optimization</h4>', '<h4>ייעול פורטפוליו</h4>'),
    ('<p>Constantly strengthens your portfolio for better acceptance rates.</p>',
     '<p>מחזק ללא הרף את הפורטפוליו לשיעורי קבלה טובים יותר.</p>'),
    ('<p>Monitors what brands are looking for so you always stay ahead.</p>',
     '<p>עוקב אחר מה שמותגים מחפשים כדי שתמיד תהיו צעד קדימה.</p>'),
    ('<p>Applies to new briefs on your behalf before you even ask.</p>',
     '<p>מגיש לבריפים חדשים בשמכם לפני שאפילו שאלתם.</p>'),
    ('<p>Tells you exactly what to charge so you stop leaving money on the table.</p>',
     '<p>אומר לכם בדיוק מה לגבות כדי שתפסיקו להשאיר כסף על השולחן.</p>'),
    # Control section
    ('<div class="eyebrow sr">Transparent by design</div>',
     '<div class="eyebrow sr">שקיפות בעיצוב</div>'),
    ('<p class="control-sub sr s2">EXi works hard, but never surprises you. Every action is visible and needs your approval before it happens.</p>',
     '<p class="control-sub sr s2">EXi עובד קשה, אבל לעולם לא מפתיע. כל פעולה גלויה וצריכה את אישורכם לפני שהיא מתרחשת.</p>'),
    # Notifications
    ('<span class="notif-title">New brief match found</span>',
     '<span class="notif-title">נמצאה התאמת בריף חדשה</span>'),
    ('<span class="notif-time">Just now</span>', '<span class="notif-time">עכשיו</span>'),
    ('<div class="notif-msg">Zara is looking for a lifestyle photographer. Match score: 96%. EXi has drafted your application — review before sending.</div>',
     '<div class="notif-msg">Zara מחפשת צלמת לייפסטייל. ניקוד התאמה: 96%. EXi הכין את הגשתכם — סקרו לפני השליחה.</div>'),
    ('<button class="nb primary" onclick="approveNotif(this)">Apply עכשיו</button>',
     '<button class="nb primary" onclick="approveNotif(this)">הגישו עכשיו</button>'),
    ('<span class="notif-title">Rate increase recommended</span>',
     '<span class="notif-title">מומלץ להעלות תעריף</span>'),
    ('<span class="notif-time">2h ago</span>', '<span class="notif-time">לפני שעתיים</span>'),
    ('<div class="notif-msg">Your market value rose 28% — EXi suggests raising your min. rate to $850/day. אישור to update your profile.</div>',
     '<div class="notif-msg">ערך השוק שלכם עלה 28% — EXi מציע להעלות את התעריף המינימלי ל-$850/יום. אשרו לעדכן את הפרופיל.</div>'),
    ('<button class="nb primary" onclick="approveNotif(this)">Update Rate</button>',
     '<button class="nb primary" onclick="approveNotif(this)">עדכנו תעריף</button>'),
    ('<button class="nb secondary">Later</button>', '<button class="nb secondary">אחר כך</button>'),
    ('<span class="notif-title">פורטפוליו updated overnight</span>',
     '<span class="notif-title">פורטפוליו עודכן בלילה</span>'),
    ('<span class="notif-time">This morning</span>', '<span class="notif-time">הבוקר</span>'),
    ('<div class="notif-msg">EXi rewrote your intro section. Projected acceptance rate improvement: +18%. אישור changes to go live.</div>',
     '<div class="notif-msg">EXi כתב מחדש את מדור הפתיחה שלכם. שיפור צפוי בשיעור הקבלה: +18%. אשרו כדי שיצא לאוויר.</div>'),
    # Action cards
    ('<div class="ac-brand">Rates</div>', '<div class="ac-brand">תעריפים</div>'),
    ('<div class="ac-title">Raise Your Minimum Daily Rate</div>',
     '<div class="ac-title">העלו את התעריף היומי המינימלי</div>'),
    ('<div class="ac-desc">Market data shows you\'re under-charging by 30% for your category</div>',
     '<div class="ac-desc">נתוני שוק מראים שאתם גובים 30% פחות ממה שמגיע לכם בקטגוריה שלכם</div>'),
    ('          +30% income potential\n        </div>',
     '          +30% פוטנציאל הכנסה\n        </div>'),
    ('<div class="ac-desc">Lifestyle photography brief — 3 deliverables, 2-week timeline</div>',
     '<div class="ac-desc">בריף צילום לייפסטייל — 3 ספקים, לוח זמנים של שבועיים</div>'),
    ('          94% match\n        </div>',
     '          94% התאמה\n        </div>'),
    ('<div class="ac-desc">EXi rewrote it to boost brand appeal — projected +22% acceptance rate</div>',
     '<div class="ac-desc">EXi כתב מחדש להגביר את המשיכה למותגים — שיעור קבלה צפוי +22%</div>'),
    ('          +22% acceptance\n        </div>',
     '          +22% קבלה\n        </div>'),
    ('<button class="act-approve-all" onclick="approveAll()">אישור All</button>',
     '<button class="act-approve-all" onclick="approveAll()">אשרו הכל</button>'),
]

# ─── site-exi-brands-he.html ───────────────────────────────
EXI_BRANDS_DEEP = [
    # Always monitoring section
    ('<div class="eyebrow sr">Always monitoring</div>',
     '<div class="eyebrow sr">תמיד מנטר</div>'),
    # Sleep items paragraphs
    ('<p>Tracks performance metrics in real time and flags deviations before they hurt results.</p>',
     '<p>עוקב אחר מדדי ביצועים בזמן אמת ומסמן סטיות לפני שפוגעות בתוצאות.</p>'),
    ('<p>Notifies you the moment a creator submits content so you can review and approve fast.</p>',
     '<p>מודיע לכם ברגע שיוצר מגיש תוכן כדי שתוכלו לסקור ולאשר מהר.</p>'),
    ('<p>Watches spend vs. target and reallocates budget to top performers automatically.</p>',
     '<p>עוקב אחר הוצאות מול יעד ומחלק מחדש את התקציב לביצועים המובילים אוטומטית.</p>'),
    # Campaign health section
    ('<div class="eyebrow sr">Campaign health</div>',
     '<div class="eyebrow sr">בריאות קמפיין</div>'),
    ('<p class="score-sub sr s2">EXi gives you a real-time campaign health score based on content quality, reach, and actual ROI.</p>',
     '<p class="score-sub sr s2">EXi נותן לכם ניקוד בריאות קמפיין בזמן אמת בהתבסס על איכות תוכן, טווח וROI אמיתי.</p>'),
    ('<div class="gauge-label">Campaign Score</div>',
     '<div class="gauge-label">ניקוד קמפיין</div>'),
    ('<div class="sb-head">Content Quality <span>', '<div class="sb-head">איכות תוכן <span>'),
    ('<div class="sb-head">Audience Reach <span>', '<div class="sb-head">טווח קהל <span>'),
    ('<div class="sb-head">ROI Performance <span>', '<div class="sb-head">ביצועי ROI <span>'),
    # "Watching" badge
    ('<div class="kc-badge-dot"></div>Watching</div>',
     '<div class="kc-badge-dot"></div>עוקב</div>'),
    # Live session label
    ('<div class="tb-title">exi.agent — live session</div>',
     '<div class="tb-title">exi.agent — סשן חי</div>'),
]

# ─── site-about-he.html ───────────────────────────────
ABOUT_DEEP = [
    # Our Values eyebrow
    ('<span class="section-eyebrow sr">Our Values</span>',
     '<span class="section-eyebrow sr">הערכים שלנו</span>'),
    # Values card paragraphs
    ('<p>No hidden fees, no vague pricing, no fine print surprises. We tell you exactly what we take — and why.</p>',
     '<p>אין עמלות נסתרות, אין תמחור מעורפל, אין הפתעות באותיות הקטנות. אנחנו אומרים לכם בדיוק מה אנחנו לוקחים — ולמה.</p>'),
    ('<p>Every product decision starts with one question: does this make a creative\'s life better? If not, we don\'t build it.</p>',
     '<p>כל החלטת מוצר מתחילה בשאלה אחת: האם זה משפר את חיי היוצר? אם לא, אנחנו לא בונים את זה.</p>'),
    ('<p>We built EXi to handle the things you hate — so you can spend more time on the things you love.</p>',
     '<p>בנינו את EXi כדי לטפל בדברים שאתם שונאים — כדי שתוכלו לבלות יותר זמן על הדברים שאתם אוהבים.</p>'),
    ('<p>Our team has been in the creative industry. We know these problems because we\'ve lived them. We don\'t guess.</p>',
     '<p>הצוות שלנו היה בתעשייה היצירתית. אנחנו מכירים את הבעיות האלה כי חיינו אותן. אנחנו לא מנחשים.</p>'),
    # Team section
    ('<span class="section-eyebrow sr">The Team</span>',
     '<span class="section-eyebrow sr">הצוות</span>'),
    ('<p class="team-intro-sub sr s2">We\'re not a faceless startup. We\'re four people who wake up every morning thinking about how to make your creative career better.</p>',
     '<p class="team-intro-sub sr s2">אנחנו לא סטארטאפ אנונימי. אנחנו ארבעה אנשים שמתעוררים כל בוקר וחושבים על איך לשפר את הקריירה היצירתית שלכם.</p>'),
    # Activity feed "just now"
    ('<div class="hm-act-time">just now</div>',
     '<div class="hm-act-time">עכשיו</div>'),
]

print('Applying deep translations...')
fix('site-he.html', SITE_DEEP)
fix('site-brands-he.html', BRANDS_DEEP)
fix('site-exi-he.html', EXI_DEEP)
fix('site-exi-brands-he.html', EXI_BRANDS_DEEP)
fix('site-about-he.html', ABOUT_DEEP)
print('\nDone.')
