#!/usr/bin/env python3
"""Generate site-pricing.html and site-pricing-he.html"""
import os
os.chdir('/home/claude/repo')

def make_page(is_he=False):
    lang = 'he' if is_he else 'en'
    dir_attr = ' dir="rtl"' if is_he else ''
    font_face = "'Heebo', system-ui, sans-serif" if is_he else "'Plus Jakarta Sans', system-ui, -apple-system, sans-serif"
    fonts = ('<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
             if is_he else
             '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">')

    T = {
        'title': 'EXPOSE — תוכניות תמחור' if is_he else 'EXPOSE — Pricing Plans',
        'og_title': 'EXPOSE תמחור — התחל בחינם, שדרג כשמוכן' if is_he else 'EXPOSE Pricing — Start Free, Scale When Ready',
        'og_desc': 'תמחור פשוט ושקוף. התחל בחינם, שדרג לפרימיום.' if is_he else 'Simple, transparent pricing. Start free, upgrade for the full EXi AI CMO experience.',
        'lang_circle': 'EN' if is_he else 'עב',
        'lang_circle_label': 'English version' if is_he else 'גרסה בעברית',
        'lang_href': 'site-pricing.html' if is_he else 'site-pricing-he.html',
        'drawer_lang': 'English' if is_he else 'עברית',
        'nav_how': 'איך זה עובד' if is_he else 'How it works',
        'nav_creatives': 'ליוצרים' if is_he else 'For Creatives',
        'nav_brands': 'למותגים' if is_he else 'For Brands',
        'nav_about': 'אודות' if is_he else 'About Us',
        'nav_exi': 'הכירו את EXi' if is_he else 'Meet EXi',
        'nav_pricing': 'תמחור' if is_he else 'Pricing',
        'nav_blog': 'בלוג' if is_he else 'Blog',
        'nav_contact': 'צור קשר' if is_he else 'Contact',
        'nav_join': 'הצטרף' if is_he else 'Join',
        'hero_eyebrow': 'תמחור' if is_he else 'Pricing',
        'hero_h1a': 'התחל בחינם.' if is_he else 'Start for free.',
        'hero_h1b': 'שדרג כשתהיה מוכן.' if is_he else 'Scale when you\'re ready.',
        'hero_sub': 'ללא עמלות נסתרות. ללא חוזים. ביטול בכל עת.' if is_he else 'No hidden fees. No contracts. Cancel anytime.',
        'stat1': '+2,439' if is_he else '2,439+',
        'stat1l': 'קריאייטיבים' if is_he else 'Creatives',
        'stat2': '★4.9' if is_he else '4.9★',
        'stat2l': 'דירוג' if is_he else 'Rating',
        'stat3': '14 יום' if is_he else '14-day',
        'stat3l': 'ניסיון חינם' if is_he else 'Free trial',
        'toggle_mo': 'חודשי' if is_he else 'Monthly',
        'toggle_yr': 'שנתי' if is_he else 'Annual',
        'save': 'חסוך 20%' if is_he else 'Save 20%',
        'free_name': 'חינמי' if is_he else 'Free',
        'free_tag': 'כל מה שצריך להתחיל' if is_he else 'Everything you need to get started',
        'free_period': 'לצמיתות' if is_he else 'forever',
        'free_price': '₪0',
        'free_cta': 'הורד את האפליקציה' if is_he else 'Get the App',
        'free_note': 'ללא כרטיס אשראי' if is_he else 'No credit card required',
        'prem_name': 'פרימיום' if is_he else 'Premium',
        'prem_badge': 'הכי פופולרי' if is_he else 'Most Popular',
        'prem_tag': 'חוויית EXi AI CMO המלאה' if is_he else 'The full EXi AI CMO experience',
        'prem_mo': '₪15',
        'prem_yr': '₪12',
        'prem_period': '/חודש' if is_he else '/month',
        'prem_yr_note': 'חיוב ₪144/שנה' if is_he else 'Billed ₪144/year',
        'prem_mo_note': '₪20/חודש ב-iOS ו-Android' if is_he else '₪20/mo on iOS & Android',
        'prem_cta': 'התחל ניסיון חינם 14 יום' if is_he else 'Start 14-Day Free Trial',
        'prem_note': 'ללא כרטיס אשראי' if is_he else 'No credit card required',
        'feat_title': 'מה כלול בכל תוכנית' if is_he else 'Everything in the box',
        'feat_free_col': 'חינמי' if is_he else 'Free',
        'feat_prem_col': 'פרימיום' if is_he else 'Premium',
        'testi_eyebrow': 'אהוב על מותגים ויוצרים' if is_he else 'Loved by brands & creators',
        'testi_h2': 'תוצאות אמיתיות מאנשים אמיתיים' if is_he else 'Real results from real people',
        'faq_eyebrow': 'שאלות נפוצות' if is_he else 'FAQ',
        'faq_h2': 'יש שאלות? יש לנו תשובות.' if is_he else "Questions? We've got answers.",
        'cta_eyebrow': 'התחל היום' if is_he else 'Start today',
        'cta_h2': 'ה-AI CMO שלך מחכה.' if is_he else 'Your AI CMO is waiting.',
        'cta_sub': 'הצטרף ל-2,439+ מותגים שמנהלים קמפיינים חכמים יותר עם EXPOSE.' if is_he else 'Join 2,439+ brands running smarter campaigns with EXPOSE.',
        'cta_btn1': 'התחל ניסיון חינם 14 יום' if is_he else 'Start 14-Day Free Trial',
        'cta_btn2': 'הורד את האפליקציה — חינם' if is_he else 'Get the App — Free',
        'footer_tag': 'מנוע השיווק המופעל על ידי AI ליוצרים ברמה עולמית.' if is_he else 'The AI-powered marketing engine for world-class creatives.',
        'footer_copy': '© 2025 EXPOSE. כל הזכויות שמורות.' if is_he else '© 2025 EXPOSE. All rights reserved.',
        'creatives_href': 'site-he.html' if is_he else 'site.html',
        'brands_href': 'site-brands-he.html' if is_he else 'site-brands.html',
        'about_href': 'site-about-he.html' if is_he else 'site-about.html',
        'exi_href': 'site-exi-he.html' if is_he else 'site-exi.html',
        'blog_href': 'site-blog-he.html' if is_he else 'site-blog.html',
        'contact_href': 'site-contact-he.html' if is_he else 'site-contact.html',
        'pricing_href': 'site-pricing-he.html' if is_he else 'site-pricing.html',
    }

    if is_he:
        features = [
            ('בסיס', [
                ('גישה לקריאייטיבים מאומתים', True, True),
                ('פרויקטים ללא הגבלה', True, True),
                ('תשלומי נאמנות מאובטחים', True, True),
                ('תובנות EXi בסיסיות', True, True),
            ]),
            ('כוח AI', [
                ('EXi AI CMO מלא 24/7', False, True),
                ('יצירת בריף לקמפיין', False, True),
                ('התאמת יוצרים אוטומטית', False, True),
            ]),
            ('אנליטיקה', [
                ('מעקב ביצועי קמפיין', False, True),
                ('מעקב אחר מתחרים', False, True),
                ('האזנה לרשתות חברתיות', False, True),
                ('דוחות שבועיים וחודשיים', False, True),
            ]),
            ('תמיכה', [
                ("תמיכה במייל וצ'אט", True, True),
                ('תמיכה בעדיפות', False, True),
                ('גישה עדיפות ליוצרים', False, True),
            ]),
        ]
        testimonials = [
            ('EXi שינה הכל. ה-ROI שלנו עלה מ-1.2× ל-4.8× בחודש הראשון. הבריף האוטומטי לבדו חוסך לנו 6 שעות בשבוע.',
             'אייה מזרחי', 'מנהלת שיווק, Lumen',
             'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=80&h=80&fit=crop&auto=format'),
            ('התוכנית החינמית הכניסה אותנו לאוויר. שלושה שבועות אחר כך שדרגנו — מעקב המתחרים לבד שווה פי 10 מהמחיר.',
             'טל בן-דוד', "מייסד, Moray Beauty",
             'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&h=80&fit=crop&auto=format'),
            ('הייתי סקפטי לגבי AI CMO. היום EXi מנהל את כל אסטרטגיית התוכן שלנו. זה כמו מנהל שיווק בכיר 24/7.',
             'נועה שחר', 'Brand Lead, Rivet',
             'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&h=80&fit=crop&auto=format'),
        ]
        faqs = [
            ('מה כלול בתוכנית החינמית?',
             'התוכנית החינמית מעניקה גישה מלאה לשוק הקריאייטיבים המאומתים, פרויקטים ללא הגבלה, תשלומי נאמנות מאובטחים ותובנות EXi בסיסיות. לגמרי בחינם — ללא כרטיס אשראי.'),
            ('האם ניתן לעבור בין חיוב חודשי לשנתי?',
             'כן. ניתן לעבור בכל עת. מעבר לשנתי חל בתחילת מחזור החיוב הבא. מעבר לחודשי ייכנס לתוקף בסוף תקופת החיוב השנתית הנוכחית.'),
            ('מדוע המחיר ב-iOS ו-Android גבוה יותר?',
             'Apple ו-Google גובים עמלת פלטפורמה של 30% על רכישות בתוך האפליקציה. לעסקה הטובה ביותר, הירשם דרך האתר שלנו במחיר ₪15/חודש.'),
            ('האם באמת לא צריך כרטיס אשראי לניסיון?',
             'נכון לחלוטין. תוכל להתחיל את ניסיון הפרימיום של 14 יום ללא הזנת פרטי תשלום. בסוף הניסיון תועבר אוטומטית לתוכנית החינמית.'),
            ('מה קורה אחרי ניסיון 14 הימים?',
             'לאחר 14 יום תועבר אוטומטית לתוכנית החינמית. לא תחויב אלא אם תבחר לשדרג באופן פעיל.'),
            ('האם ניתן לבטל בכל עת?',
             'בהחלט. ביטול בלחיצה אחת מהגדרות החשבון. ללא שאלות, ללא דמי ביטול.'),
        ]
        free_features = [
            'גישה לקריאייטיבים מאומתים',
            'פרויקטים ללא הגבלה',
            'תשלומי נאמנות מאובטחים',
            "תובנות EXi בסיסיות",
            "תמיכה במייל וצ'אט",
        ]
        prem_features = [
            'EXi AI CMO מלא 24/7',
            'יצירת בריף לקמפיין',
            'התאמת יוצרים אוטומטית',
            'מעקב ביצועי קמפיין',
            'מעקב אחר מתחרים',
            'האזנה לרשתות חברתיות',
            'דוחות שבועיים וחודשיים',
            'גישה עדיפות ליוצרים',
            'תמיכה בעדיפות',
        ]
        footer_cols = '''<div class="footer-col"><h6>מוצר</h6><a href="{creatives_href}">ליוצרים</a><a href="{brands_href}">למותגים</a><a href="{exi_href}">הכירו את EXi</a><a href="{pricing_href}">תמחור</a></div>
  <div class="footer-col"><h6>חברה</h6><a href="{about_href}">אודות</a><a href="#">קריירה</a><a href="{blog_href}">בלוג</a><a href="#">פרסום</a></div>
  <div class="footer-col"><h6>תמיכה</h6><a href="#">מרכז עזרה</a><a href="#">פרטיות</a><a href="#">תנאים</a><a href="{contact_href}">צור קשר</a></div>'''.format(**T)
    else:
        features = [
            ('Core', [
                ('Access to vetted creatives', True, True),
                ('Unlimited projects', True, True),
                ('Secure escrow payments', True, True),
                ('EXi preview insights', True, True),
            ]),
            ('AI Power', [
                ('Full EXi AI CMO 24/7', False, True),
                ('Campaign brief generation', False, True),
                ('Automated creator matching', False, True),
            ]),
            ('Analytics', [
                ('Campaign performance tracking', False, True),
                ('Competitor tracking', False, True),
                ('Social media listening', False, True),
                ('Weekly & monthly reports', False, True),
            ]),
            ('Support', [
                ('Email & chat support', True, True),
                ('Priority support', False, True),
                ('Priority creator access', False, True),
            ]),
        ]
        testimonials = [
            ('EXi changed everything. Our campaign ROI jumped from 1.2× to 4.8× in the first month. The AI briefing alone saves us 6 hours a week.',
             'Aya Mizrahi', 'Marketing Director, Lumen',
             'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=80&h=80&fit=crop&auto=format'),
            ('The free plan got us started. Three weeks later we upgraded — competitor tracking alone is worth 10× the price.',
             'Tal Ben-David', 'Founder, Moray Beauty',
             'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&h=80&fit=crop&auto=format'),
            ("I was skeptical about an AI CMO. Now EXi runs our entire content strategy. It's like having a senior marketer on call 24/7.",
             'Noa Shachar', 'Brand Lead, Rivet',
             'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&h=80&fit=crop&auto=format'),
        ]
        faqs = [
            ("What's included in the free plan?",
             "The free plan gives you full access to our marketplace of vetted creatives, unlimited projects, secure escrow payments, and basic EXi insights. It's completely free — no credit card required."),
            ('Can I switch between monthly and annual billing?',
             'Yes, you can switch at any time. Switching to annual takes effect at the start of your next billing cycle. Switching to monthly takes effect at the end of your current annual period.'),
            ('Why is there a price difference on iOS & Android?',
             'Apple and Google charge a 30% platform fee on in-app purchases. For the best deal, subscribe through our website at ₪15/month.'),
            ('Is there really no credit card needed for the free trial?',
             'Correct. Start your 14-day Premium trial without any payment details. At the end of the trial, you automatically drop to the free plan — nothing to cancel.'),
            ('What happens after the free trial?',
             "After 14 days you'll automatically move to the free plan. You won't be charged anything unless you actively choose to upgrade."),
            ('Can I cancel any time?',
             'Absolutely. Cancel with one click from your account settings. No questions asked, no cancellation fees.'),
        ]
        free_features = [
            'Access to vetted creatives',
            'Unlimited projects',
            'Secure escrow payments',
            'EXi preview insights',
            'Email & chat support',
        ]
        prem_features = [
            'Full EXi AI CMO 24/7',
            'Campaign brief generation',
            'Automated creator matching',
            'Campaign performance tracking',
            'Competitor tracking',
            'Social media listening',
            'Weekly & monthly reports',
            'Priority creator access',
            'Priority support',
        ]
        footer_cols = '''<div class="footer-col"><h6>Product</h6><a href="{creatives_href}">For Creatives</a><a href="{brands_href}">For Brands</a><a href="{exi_href}">Meet EXi</a><a href="{pricing_href}">Pricing</a></div>
  <div class="footer-col"><h6>Company</h6><a href="{about_href}">About Us</a><a href="#">Careers</a><a href="{blog_href}">Blog</a><a href="#">Press</a></div>
  <div class="footer-col"><h6>Support</h6><a href="#">Help Center</a><a href="#">Privacy</a><a href="#">Terms</a><a href="{contact_href}">Contact</a></div>'''.format(**T)

    # Build feature table rows
    feat_table_html = ''
    for group, rows in features:
        feat_table_html += f'<div class="feat-group-label">{group}</div>\n'
        for name, free_val, prem_val in rows:
            free_icon = ('check', '✓') if free_val else ('cross', '—')
            prem_icon = ('check', '✓') if prem_val else ('cross', '—')
            feat_table_html += f'''<div class="feat-row">
          <span class="feat-row-name">{name}</span>
          <span class="feat-row-val {free_icon[0]}">{free_icon[1]}</span>
          <span class="feat-row-val {prem_icon[0]}">{prem_icon[1]}</span>
        </div>\n'''

    # Build free card features
    free_feats_html = ''
    for f in free_features:
        free_feats_html += f'<div class="feat-item"><span class="feat-icon check"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg></span>{f}</div>\n'

    # Build premium card features
    prem_feats_html = ''
    for f in prem_features:
        prem_feats_html += f'<div class="feat-item"><span class="feat-icon check"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg></span>{f}</div>\n'
    incl_free = ('כולל גם את כל יתרונות החינמי' if is_he else '+ everything in Free')
    prem_feats_html = f'<div class="feat-item feat-plus"><span class="feat-icon plus">+</span>{incl_free}</div>\n' + prem_feats_html

    # Build testimonials HTML
    testi_html = ''
    for quote, name, role, avatar in testimonials:
        testi_html += f'''<div class="testi-card sr">
        <div class="testi-stars">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.9L22 10l-5.5 4.8 1.7 7.2L12 18.3 5.8 22l1.7-7.2L2 10l7.1-1.1z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.9L22 10l-5.5 4.8 1.7 7.2L12 18.3 5.8 22l1.7-7.2L2 10l7.1-1.1z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.9L22 10l-5.5 4.8 1.7 7.2L12 18.3 5.8 22l1.7-7.2L2 10l7.1-1.1z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.9L22 10l-5.5 4.8 1.7 7.2L12 18.3 5.8 22l1.7-7.2L2 10l7.1-1.1z"/></svg>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.9L22 10l-5.5 4.8 1.7 7.2L12 18.3 5.8 22l1.7-7.2L2 10l7.1-1.1z"/></svg>
        </div>
        <p class="testi-quote">"{quote}"</p>
        <div class="testi-author">
          <img class="testi-avatar" src="{avatar}" alt="{name}" loading="lazy">
          <div>
            <div class="testi-name">{name}</div>
            <div class="testi-role">{role}</div>
          </div>
        </div>
      </div>\n'''

    # Build FAQ HTML
    faq_html = ''
    for q, a in faqs:
        faq_html += f'''<div class="faq-item">
        <button class="faq-q">{q}<svg class="faq-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg></button>
        <div class="faq-a"><p>{a}</p></div>
      </div>\n'''

    # Nav dropdown
    if is_he:
        dd_creatives = f'<a href="{T["creatives_href"]}"><span class="dd-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></span>ליוצרים</a>'
        dd_brands = f'<a href="{T["brands_href"]}"><span class="dd-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span>למותגים</a>'
    else:
        dd_creatives = f'<a href="{T["creatives_href"]}"><span class="dd-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></span>For Creatives</a>'
        dd_brands = f'<a href="{T["brands_href"]}"><span class="dd-ico"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span>For Brands</a>'

    html = f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{T['og_desc']}">
<link rel="canonical" href="https://expose.global/pricing">
<meta property="og:type" content="website">
<meta property="og:site_name" content="EXPOSE">
<meta property="og:url" content="https://expose.global/pricing">
<meta property="og:title" content="{T['og_title']}">
<meta property="og:description" content="{T['og_desc']}">
<meta property="og:image" content="https://expose.global/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{T['og_title']}">
<meta name="twitter:description" content="{T['og_desc']}">
<title>{T['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<style>
  :root {{
    --orange:      #FF6A1A;
    --orange-2:    #FF8533;
    --orange-soft: #FFEDE0;
    --orange-glow: #FFD8B8;
    --ink:         #131313;
    --ink-2:       #3A3A3A;
    --gray:        #6E6E6E;
    --gray-2:      #9A9A9A;
    --line:        #ECE7E2;
    --line-2:      #E2DCD4;
    --bg:          #FFFFFF;
    --bg-soft:     #FAF7F2;
    --warm:        #FAF6EF;
    --radius-sm:   12px;
    --radius:      18px;
    --radius-lg:   24px;
    --shadow-sm:   0 1px 2px rgba(20,16,12,.04), 0 2px 8px rgba(20,16,12,.04);
    --shadow:      0 4px 18px rgba(28,18,8,.08), 0 1px 3px rgba(28,18,8,.05);
    --shadow-lg:   0 24px 60px -20px rgba(255,106,26,.35), 0 8px 24px rgba(28,18,8,.06);
  }}
  * {{ box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
  html, body {{ margin: 0; padding: 0; }}
  body {{
    font-family: {font_face};
    color: var(--ink); background: var(--bg);
    line-height: 1.4; -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility; font-size: 15px;
  }}
  img {{ max-width: 100%; display: block; }}
  button {{ font: inherit; cursor: pointer; border: 0; background: none; color: inherit; }}
  a {{ color: inherit; text-decoration: none; }}
  p {{ margin: 0; }}

  /* ── Layout ── */
  .page {{ max-width: 100%; overflow-x: hidden; }}
  .section {{ padding: 56px 20px; }}
  .eyebrow {{
    font-size: 11px; font-weight: 700; letter-spacing: .14em;
    text-transform: uppercase; color: var(--orange);
  }}
  .h-display {{
    font-size: 30px; line-height: 1.08; font-weight: 700;
    letter-spacing: -0.02em; color: var(--ink);
  }}
  .h-section {{
    font-size: 26px; line-height: 1.12; font-weight: 700;
    letter-spacing: -0.02em; color: var(--ink);
  }}
  .italic-accent {{
    font-family: 'Instrument Serif', serif;
    font-style: italic; font-weight: 400; color: var(--orange);
  }}
  .sr {{
    opacity: 0; transform: translateY(18px);
    transition: opacity .55s ease, transform .55s cubic-bezier(.16,1,.3,1);
  }}
  .sr.in {{ opacity: 1; transform: none; }}

  /* ── Nav (mobile base) ── */
  .nav {{
    position: sticky; top: 0; z-index: 50;
    display: grid; grid-template-columns: 40px 1fr auto;
    align-items: center; padding: 14px 18px;
    background: rgba(255,255,255,.85);
    backdrop-filter: saturate(180%) blur(14px);
    -webkit-backdrop-filter: saturate(180%) blur(14px);
    border-bottom: 1px solid rgba(236,231,226,.6);
  }}
  .nav-logo {{
    grid-column: 2; justify-self: center;
    display: flex; align-items: center; gap: 6px;
    font-weight: 800; font-size: 19px; letter-spacing: 0.01em;
  }}
  .nav-logo .spark {{ width: 14px; height: 14px; color: var(--orange); }}
  .nav-menu {{
    grid-column: 1; justify-self: start;
    width: 36px; height: 36px; display: grid; place-items: center;
    border-radius: 10px; color: var(--ink); background: transparent;
  }}
  .nav-right {{ grid-column:3; justify-self:end; display:flex; align-items:center; gap:8px }}
  .nav-login {{
    padding:9px 16px; border-radius:8px; background:var(--orange); color:#fff;
    font-size:12px; font-weight:700; display:inline-flex; align-items:center; gap:6px;
    box-shadow:0 4px 10px rgba(255,106,26,.28); letter-spacing:.02em;
    text-decoration:none; white-space:nowrap;
  }}
  .nav-links {{ display:none; }}
  .lang-circle {{
    display:none; width:30px; height:30px; border-radius:50%;
    align-items:center; justify-content:center; font-size:10px; font-weight:800; letter-spacing:.04em;
    border:1.5px solid rgba(255,106,26,.4); color:var(--orange); background:transparent;
    transition:background .15s,color .15s,border-color .15s; text-decoration:none; flex-shrink:0;
  }}
  .lang-circle:hover {{ background:var(--orange); color:#fff; border-color:var(--orange); }}

  /* ── Drawer ── */
  .drawer-overlay {{
    display:none; position:fixed; inset:0; z-index:200;
    background:rgba(19,19,19,.45); backdrop-filter:blur(4px);
    -webkit-backdrop-filter:blur(4px); opacity:0; transition:opacity .25s ease;
  }}
  .drawer-overlay.open {{ display:block; opacity:1; }}
  .drawer {{
    position:fixed; top:0; left:0; bottom:0;
    width:min(320px,85vw); background:#fff; z-index:201;
    display:flex; flex-direction:column; padding:0;
    transform:translateX(-100%); transition:transform .3s cubic-bezier(.16,1,.3,1);
    box-shadow:8px 0 40px rgba(19,19,19,.12);
  }}
  .drawer.open {{ transform:translateX(0); }}
  [dir="rtl"] .drawer {{ left:auto; right:0; transform:translateX(100%); }}
  [dir="rtl"] .drawer.open {{ transform:translateX(0); }}
  .drawer-head {{
    display:flex; align-items:center; justify-content:space-between;
    padding:20px 22px; border-bottom:1px solid var(--line);
  }}
  .drawer-logo {{
    display:flex; align-items:center; gap:6px;
    font-weight:800; font-size:17px; color:var(--ink);
  }}
  .drawer-logo .spark {{ width:13px; height:13px; color:var(--orange); }}
  .drawer-close {{
    width:32px; height:32px; border-radius:8px; display:grid; place-items:center;
    color:var(--gray); background:var(--bg-soft); border:1px solid var(--line);
  }}
  .drawer-close:hover {{ color:var(--ink); }}
  .drawer-nav {{
    flex:1; padding:16px 12px; display:flex; flex-direction:column;
    gap:2px; overflow-y:auto;
  }}
  .drawer-nav a {{
    display:flex; align-items:center; gap:12px; padding:13px 14px;
    border-radius:12px; font-size:15px; font-weight:600; color:var(--ink-2);
    transition:background .15s ease,color .15s ease; text-decoration:none;
  }}
  .drawer-nav a:hover {{ background:var(--bg-soft); color:var(--ink); }}
  .drawer-nav a.active {{ background:var(--orange-soft); color:var(--orange); }}
  .drawer-nav a .dn-icon {{
    width:34px; height:34px; border-radius:9px; background:var(--bg-soft);
    border:1px solid var(--line); display:grid; place-items:center;
    flex-shrink:0; color:var(--gray);
  }}
  .drawer-nav a.active .dn-icon {{ background:rgba(255,106,26,.12); border-color:rgba(255,106,26,.2); color:var(--orange); }}
  .drawer-nav a:hover .dn-icon {{ color:var(--orange); }}
  .drawer-divider {{ height:1px; background:var(--line); margin:8px 14px; }}
  .drawer-nav .dn-label {{
    font-size:10px; font-weight:700; letter-spacing:.14em;
    text-transform:uppercase; color:var(--gray-2); padding:8px 14px 2px;
  }}
  .drawer-lang-switch {{
    display:flex; align-items:center; gap:8px; padding:12px 22px;
    font-size:13px; font-weight:600; color:var(--gray);
    border-top:1px solid var(--line); text-decoration:none;
    transition:color .15s;
  }}
  .drawer-lang-switch:hover {{ color:var(--orange); }}
  .drawer-foot {{ padding:16px 22px 28px; border-top:1px solid var(--line); }}
  .drawer-foot .btn-orange {{
    display:flex; align-items:center; justify-content:center;
    width:100%; padding:14px; border-radius:12px;
    background:var(--orange); color:#fff;
    font-size:14px; font-weight:700; letter-spacing:.02em;
    box-shadow:0 4px 14px rgba(255,106,26,.32); text-decoration:none;
  }}
  body.drawer-lock {{ overflow:hidden; }}

  /* ── Pricing Hero ── */
  .pricing-hero {{
    padding: 72px 20px 56px;
    text-align: center;
    background: #FFFBF7;
    position: relative;
    overflow: hidden;
  }}
  .pricing-hero::before {{
    content: ''; position: absolute; inset: 0;
    background:
      radial-gradient(ellipse 85% 55% at 50% 0%, rgba(255,140,60,.20) 0%, transparent 70%),
      radial-gradient(ellipse 60% 50% at 20% 60%, rgba(255,106,26,.07) 0%, transparent 55%),
      radial-gradient(ellipse 60% 50% at 80% 40%, rgba(255,106,26,.06) 0%, transparent 55%);
    pointer-events: none;
  }}
  .pricing-hero::after {{
    content: ''; position: absolute; inset: 0;
    background-image: radial-gradient(rgba(255,106,26,.12) 1px, transparent 1.5px);
    background-size: 26px 26px;
    -webkit-mask-image: radial-gradient(70% 60% at 50% 30%, black 10%, transparent 70%);
    mask-image: radial-gradient(70% 60% at 50% 30%, black 10%, transparent 70%);
    pointer-events: none; opacity: .6;
  }}
  .pricing-hero > * {{ position: relative; z-index: 1; }}
  .hero-h1 {{
    font-size: 36px; font-weight: 800; line-height: 1.06;
    letter-spacing: -0.03em; color: var(--ink);
    margin: 10px 0 14px;
  }}
  .hero-h1 .italic-accent {{ font-size: 1em; }}
  .hero-sub {{
    font-size: 15px; color: var(--gray);
    max-width: 340px; margin: 0 auto 28px;
    line-height: 1.55;
  }}
  .trust-row {{
    display: flex; flex-wrap: wrap;
    justify-content: center; gap: 10px;
    margin-bottom: 0;
  }}
  .trust-pill {{
    display: inline-flex; align-items: center; gap: 7px;
    padding: 8px 14px;
    background: rgba(255,255,255,.85);
    border: 1px solid var(--line); border-radius: 99px;
    font-size: 12px; font-weight: 600; color: var(--ink-2);
  }}
  .trust-pill .tp-val {{
    font-weight: 800; color: var(--orange); font-size: 13px;
  }}
  .trust-pill .tp-dot {{
    width: 6px; height: 6px; border-radius: 50%; background: #1FBF6B;
  }}

  /* ── Pricing Section ── */
  .pricing-section {{
    padding: 48px 20px 64px;
    background: var(--bg-soft);
  }}
  .pricing-section-inner {{ max-width: 900px; margin: 0 auto; }}
  .toggle-wrap {{
    display: flex; justify-content: center; margin-bottom: 40px;
  }}
  .price-toggle {{
    display: inline-flex; align-items: center;
    background: var(--bg); border: 1px solid var(--line);
    border-radius: 99px; padding: 4px; gap: 2px;
  }}
  .price-toggle-btn {{
    padding: 9px 22px; border-radius: 99px;
    font-size: 13px; font-weight: 600; color: var(--gray);
    transition: all .2s; cursor: pointer; border: none; background: none;
    position: relative; white-space: nowrap;
  }}
  .price-toggle-btn.active {{
    background: var(--orange); color: #fff;
    box-shadow: 0 2px 10px rgba(255,106,26,.3);
  }}
  .save-badge {{
    position: absolute; top: -9px; right: -4px;
    background: #1FBF6B; color: #fff;
    font-size: 9px; font-weight: 800; padding: 2px 7px;
    border-radius: 99px; letter-spacing: .04em; white-space: nowrap;
    pointer-events: none;
  }}

  /* ── Price Cards ── */
  .price-cards {{
    display: flex; flex-direction: column; gap: 20px;
  }}
  .price-card {{
    background: var(--bg); border: 1.5px solid var(--line);
    border-radius: var(--radius-lg); padding: 32px;
    position: relative; transition: transform .2s, box-shadow .2s;
  }}
  .price-card.premium {{
    border-color: rgba(255,106,26,.35);
    box-shadow: 0 0 0 5px rgba(255,106,26,.06), var(--shadow-lg);
  }}
  .card-badge {{
    position: absolute; top: -13px; left: 50%; transform: translateX(-50%);
    background: var(--orange); color: #fff;
    font-size: 10px; font-weight: 800; letter-spacing: .07em;
    text-transform: uppercase; padding: 5px 16px; border-radius: 99px;
    white-space: nowrap; box-shadow: 0 4px 10px rgba(255,106,26,.3);
  }}
  .card-plan {{ display: flex; align-items: center; gap: 10px; margin-bottom: 4px; }}
  .card-name {{
    font-size: 13px; font-weight: 700; letter-spacing: .07em;
    text-transform: uppercase; color: var(--gray);
  }}
  .premium .card-name {{ color: var(--orange); }}
  .card-tagline {{
    font-size: 14px; color: var(--gray); margin-bottom: 20px; line-height: 1.45;
  }}
  .card-price {{
    display: flex; align-items: flex-end; gap: 3px; margin-bottom: 4px;
  }}
  .price-num {{
    font-size: 56px; font-weight: 800; letter-spacing: -.04em;
    color: var(--ink); line-height: 1;
  }}
  .price-period {{
    font-size: 16px; color: var(--gray); font-weight: 500;
    padding-bottom: 8px;
  }}
  .price-note {{
    font-size: 12px; color: var(--gray-2); margin-bottom: 24px; min-height: 18px;
  }}
  .annual-note {{ display: none; }}
  .card-cta {{
    display: flex; align-items: center; justify-content: center;
    width: 100%; padding: 14px; border-radius: 12px;
    font-size: 14px; font-weight: 700; letter-spacing: .02em;
    text-decoration: none; margin-bottom: 12px; cursor: pointer; border: none;
    transition: transform .15s, box-shadow .15s;
  }}
  .card-cta:active {{ transform: scale(.98); }}
  .card-cta.free-cta {{
    background: var(--bg-soft); color: var(--ink);
    border: 1.5px solid var(--line-2);
  }}
  .card-cta.free-cta:hover {{ background: var(--line); }}
  .card-cta.premium-cta {{
    background: var(--orange); color: #fff;
    box-shadow: 0 4px 16px rgba(255,106,26,.32);
  }}
  .card-cta.premium-cta:hover {{ box-shadow: 0 6px 22px rgba(255,106,26,.4); transform: translateY(-1px); }}
  .card-note-text {{
    text-align: center; font-size: 11px; color: var(--gray-2); margin-bottom: 24px;
  }}
  .card-divider {{ height: 1px; background: var(--line); margin-bottom: 20px; }}
  .card-features {{ display: flex; flex-direction: column; gap: 11px; }}
  .feat-item {{
    display: flex; align-items: center; gap: 10px;
    font-size: 13px; color: var(--ink-2); font-weight: 500;
  }}
  .feat-item.feat-plus {{ color: var(--orange); font-weight: 700; }}
  .feat-item .feat-icon {{
    width: 18px; height: 18px; border-radius: 50%;
    display: grid; place-items: center; flex-shrink: 0;
    font-size: 10px; font-weight: 800;
  }}
  .feat-icon.check {{ background: rgba(31,191,107,.12); color: #1FBF6B; }}
  .feat-icon.plus {{ background: var(--orange-soft); color: var(--orange); }}

  /* ── Feature Comparison ── */
  .feat-compare {{ padding: 56px 20px; background: var(--bg); }}
  .section-header {{ text-align: center; margin-bottom: 36px; }}
  .section-header .h-section {{ margin: 8px 0 0; }}
  .feat-table {{
    max-width: 720px; margin: 0 auto;
    border: 1px solid var(--line); border-radius: var(--radius-lg);
    overflow: hidden;
  }}
  .feat-table-head {{
    display: grid; grid-template-columns: 1fr 80px 80px;
    padding: 14px 20px; border-bottom: 1.5px solid var(--line-2);
    background: var(--bg-soft);
  }}
  .feat-head-col {{
    text-align: center; font-size: 11px; font-weight: 800;
    letter-spacing: .07em; text-transform: uppercase; color: var(--gray);
  }}
  .feat-head-col:first-child {{ text-align: start; }}
  .feat-head-col.premium {{ color: var(--orange); }}
  .feat-group-label {{
    background: var(--warm); padding: 9px 20px;
    font-size: 10px; font-weight: 700; letter-spacing: .12em;
    text-transform: uppercase; color: var(--gray-2);
    border-bottom: 1px solid var(--line);
  }}
  .feat-row {{
    display: grid; grid-template-columns: 1fr 80px 80px;
    align-items: center; padding: 12px 20px;
    border-bottom: 1px solid var(--line); gap: 8px;
  }}
  .feat-row:last-child {{ border-bottom: none; }}
  .feat-row-name {{ font-size: 13px; font-weight: 500; color: var(--ink-2); }}
  .feat-row-val {{ text-align: center; font-size: 13px; font-weight: 700; }}
  .feat-row-val.check {{ color: #1FBF6B; }}
  .feat-row-val.cross {{ color: var(--gray-2); font-size: 16px; }}

  /* ── Testimonials ── */
  .testimonials {{ padding: 56px 20px; background: var(--bg-soft); }}
  .testi-grid {{
    display: flex; flex-direction: column; gap: 16px;
    max-width: 920px; margin: 28px auto 0;
  }}
  .testi-card {{
    background: var(--bg); border: 1px solid var(--line);
    border-radius: var(--radius); padding: 26px;
  }}
  .testi-stars {{ display: flex; gap: 2px; margin-bottom: 14px; color: #F59E0B; }}
  .testi-quote {{
    font-size: 14px; line-height: 1.65; color: var(--ink-2);
    margin-bottom: 18px; font-style: italic;
  }}
  .testi-author {{ display: flex; align-items: center; gap: 12px; }}
  .testi-avatar {{
    width: 42px; height: 42px; border-radius: 50%;
    object-fit: cover; flex-shrink: 0;
    border: 2px solid var(--line);
  }}
  .testi-name {{ font-size: 13px; font-weight: 700; color: var(--ink); }}
  .testi-role {{ font-size: 12px; color: var(--gray); margin-top: 1px; }}

  /* ── FAQ ── */
  .faq-section {{ padding: 56px 20px; background: var(--bg); }}
  .faq-list {{
    max-width: 680px; margin: 28px auto 0;
    display: flex; flex-direction: column; gap: 8px;
  }}
  .faq-item {{
    border: 1px solid var(--line); border-radius: var(--radius-sm); overflow: hidden;
  }}
  .faq-item.open {{ border-color: rgba(255,106,26,.25); }}
  .faq-q {{
    width: 100%; display: flex; align-items: center;
    justify-content: space-between; padding: 16px 20px;
    font-size: 14px; font-weight: 600; color: var(--ink);
    background: var(--bg); cursor: pointer; text-align: start;
    gap: 12px; border: none;
  }}
  .faq-q:hover {{ background: var(--bg-soft); }}
  .faq-chevron {{ flex-shrink: 0; color: var(--gray); transition: transform .2s; }}
  .faq-item.open .faq-chevron {{ transform: rotate(180deg); color: var(--orange); }}
  .faq-a {{
    display: none; padding: 0 20px 16px;
    font-size: 13px; line-height: 1.7; color: var(--gray);
  }}
  .faq-item.open .faq-a {{ display: block; }}

  /* ── CTA Banner ── */
  .pricing-cta {{
    padding: 72px 20px; background: var(--ink);
    text-align: center; position: relative; overflow: hidden;
  }}
  .pricing-cta::before {{
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 80% at 50% -10%, rgba(255,106,26,.22) 0%, transparent 65%);
    pointer-events: none;
  }}
  .pricing-cta::after {{
    content: ''; position: absolute; inset: 0;
    background-image: radial-gradient(rgba(255,106,26,.08) 1px, transparent 1.5px);
    background-size: 28px 28px; pointer-events: none; opacity: .5;
  }}
  .pricing-cta > * {{ position: relative; z-index: 1; }}
  .pricing-cta .eyebrow {{ color: rgba(255,140,60,.8); }}
  .pricing-cta .cta-h2 {{
    font-size: 34px; font-weight: 800; letter-spacing: -.03em;
    color: #fff; margin: 10px 0 10px;
  }}
  .pricing-cta .cta-sub {{
    font-size: 15px; color: rgba(255,255,255,.6);
    max-width: 360px; margin: 0 auto 36px; line-height: 1.55;
  }}
  .cta-btns {{
    display: flex; flex-direction: column;
    align-items: center; gap: 12px;
  }}
  .btn-orange-big {{
    display: inline-flex; align-items: center; justify-content: center;
    padding: 16px 32px; background: var(--orange); color: #fff;
    border-radius: 14px; font-size: 15px; font-weight: 700;
    letter-spacing: .02em; text-decoration: none;
    box-shadow: 0 4px 18px rgba(255,106,26,.45);
    transition: transform .15s, box-shadow .15s;
    cursor: pointer; border: none;
  }}
  .btn-orange-big:hover {{ transform: translateY(-2px); box-shadow: 0 8px 26px rgba(255,106,26,.5); }}
  .btn-ghost-big {{
    display: inline-flex; align-items: center; justify-content: center;
    padding: 15px 32px; background: transparent;
    color: rgba(255,255,255,.7); border-radius: 14px;
    font-size: 15px; font-weight: 600; text-decoration: none;
    border: 1.5px solid rgba(255,255,255,.2);
    transition: border-color .15s, color .15s;
  }}
  .btn-ghost-big:hover {{ border-color: rgba(255,255,255,.45); color: #fff; }}

  /* ── Footer ── */
  .footer {{
    background: var(--ink); color: rgba(255,255,255,.55);
    padding: 48px 20px 32px; font-size: 13px;
  }}
  .footer-brand {{
    display: flex; align-items: center; gap: 6px;
    font-weight: 800; font-size: 18px; color: #fff; margin-bottom: 8px;
  }}
  .footer-brand .spark {{ width: 13px; height: 13px; color: var(--orange); }}
  .footer-tagline {{ color: rgba(255,255,255,.45); margin-bottom: 24px; }}
  .footer-apps {{
    display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 28px;
  }}
  .footer-app-btn {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 9px 16px; border-radius: 10px;
    border: 1px solid rgba(255,255,255,.15);
    color: rgba(255,255,255,.8); font-size: 12px; font-weight: 600;
    transition: border-color .15s, color .15s;
  }}
  .footer-app-btn:hover {{ border-color: rgba(255,255,255,.35); color: #fff; }}
  .footer-cols {{
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 24px 16px; margin-bottom: 32px;
  }}
  .footer-col h6 {{
    font-size: 11px; font-weight: 700; letter-spacing: .1em;
    text-transform: uppercase; color: rgba(255,255,255,.8);
    margin: 0 0 12px;
  }}
  .footer-col a {{
    display: block; color: rgba(255,255,255,.45);
    font-size: 13px; margin-bottom: 8px; transition: color .15s;
  }}
  .footer-col a:hover {{ color: rgba(255,255,255,.85); }}
  .footer-si-grid {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .footer-si {{
    width: 34px; height: 34px; border-radius: 9px;
    display: grid; place-items: center;
    border: 1px solid rgba(255,255,255,.15); color: rgba(255,255,255,.5);
    transition: border-color .15s, color .15s;
  }}
  .footer-si:hover {{ border-color: rgba(255,255,255,.4); color: #fff; }}
  .footer-bottom {{
    padding-top: 20px; border-top: 1px solid rgba(255,255,255,.1);
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 12px;
  }}
  .footer-copy {{ font-size: 12px; color: rgba(255,255,255,.3); }}
  .footer-socials {{ display: flex; gap: 12px; }}
  .footer-socials a {{ color: rgba(255,255,255,.35); transition: color .15s; }}
  .footer-socials a:hover {{ color: rgba(255,255,255,.7); }}

  /* ── Desktop ≥ 900px ── */
  /* ── Desktop nav (≥ 900px) ── */
  @media (min-width: 900px) {{
    .nav {{ grid-template-columns: auto 1fr auto; padding: 0 56px; height: 64px; }}
    .nav-logo {{ grid-column: 1; justify-self: start; font-size: 21px; }}
    .nav-links {{
      grid-column: 2; display: flex; align-items: center;
      justify-content: center; gap: 4px;
      font-size: 14px; font-weight: 500; color: var(--ink-2);
    }}
    .nav-right {{ grid-column: 3; gap: 10px; }}
    .nav-login {{ padding: 10px 20px; font-size: 13px; }}
    .nav-menu {{ display: none; }}
    .lang-circle {{ display: inline-flex; }}
    .nav-links > a {{
      position: relative; padding: 4px 10px; border-radius: 6px;
      transition: color .2s ease;
    }}
    .nav-links > a::after {{
      content: ''; position: absolute;
      bottom: -2px; left: 10px; right: 10px;
      height: 2px; border-radius: 99px; background: var(--orange);
      transform: scaleX(0); transform-origin: left;
      transition: transform .25s cubic-bezier(.16,1,.3,1);
    }}
    .nav-links > a:hover {{ color: var(--orange); }}
    .nav-links > a:hover::after,
    .nav-links > a.active::after {{ transform: scaleX(1); }}
    .nav-links > a.active {{ color: var(--orange); }}
    .nav-dropdown {{ position: relative; }}
    .nav-dd-btn {{
      display: flex; align-items: center; gap: 5px;
      font-size: 14px; font-weight: 500; color: var(--ink-2);
      background: none; border: none; cursor: pointer;
      padding: 4px 10px; border-radius: 6px; font-family: inherit;
      line-height: 1.5; transition: color .2s ease; position: relative;
    }}
    .nav-dd-btn::after {{
      content: ''; position: absolute;
      bottom: -2px; left: 10px; right: 10px;
      height: 2px; border-radius: 99px; background: var(--orange);
      transform: scaleX(0); transform-origin: left;
      transition: transform .25s cubic-bezier(.16,1,.3,1);
    }}
    .nav-dd-btn:hover {{ color: var(--orange); }}
    .nav-dd-btn:hover::after, .nav-dd-btn.active::after {{ transform: scaleX(1); }}
    .nav-dd-btn.active {{ color: var(--orange); }}
    .nav-dd-chevron {{ transition: transform .2s; flex-shrink: 0; }}
    .nav-dropdown:hover .nav-dd-chevron,
    .nav-dropdown:focus-within .nav-dd-chevron {{ transform: rotate(180deg); }}
    .nav-dd-menu {{
      display: none; position: absolute;
      top: calc(100% + 10px); left: 50%; transform: translateX(-50%);
      background: #fff; border: 1px solid rgba(236,231,226,.9);
      border-radius: 14px; padding: 6px;
      box-shadow: 0 8px 32px rgba(19,19,19,.12), 0 2px 8px rgba(19,19,19,.05);
      min-width: 180px; z-index: 100;
    }}
    .nav-dropdown:hover .nav-dd-menu,
    .nav-dropdown:focus-within .nav-dd-menu {{ display: block; }}
    .nav-dd-menu a {{
      display: flex; align-items: center; gap: 10px;
      padding: 10px 12px; border-radius: 9px;
      font-size: 13px; font-weight: 600; color: var(--ink-2);
      text-decoration: none; transition: background .12s, color .12s;
      white-space: nowrap;
    }}
    .nav-dd-menu a .dd-ico {{
      width: 28px; height: 28px; border-radius: 7px;
      background: var(--bg-soft); border: 1px solid var(--line);
      display: grid; place-items: center; flex-shrink: 0; color: var(--gray);
    }}
    .nav-dd-menu a:hover {{ background: var(--orange-soft); color: var(--orange); }}
    .nav-dd-menu a:hover .dd-ico {{ color: var(--orange); border-color: rgba(255,106,26,.2); background: rgba(255,106,26,.1); }}
    .nav-dd-menu a.active {{ background: var(--orange-soft); color: var(--orange); }}
    .nav-dd-menu a.active .dd-ico {{ color: var(--orange); border-color: rgba(255,106,26,.2); background: rgba(255,106,26,.1); }}

    /* Pricing desktop */
    .hero-h1 {{ font-size: 56px; }}
    .hero-sub {{ font-size: 17px; max-width: 440px; }}
    .trust-row {{ gap: 14px; }}
    .trust-pill {{ font-size: 13px; padding: 9px 18px; }}
    .price-cards {{
      flex-direction: row; align-items: stretch; gap: 24px;
    }}
    .price-card {{ flex: 1; }}
    .price-card.premium {{ transform: translateY(-8px); }}
    .testi-grid {{ flex-direction: row; }}
    .testi-card {{ flex: 1; }}
    .cta-btns {{ flex-direction: row; justify-content: center; }}
    .footer-cols {{ grid-template-columns: repeat(4,1fr); }}
    .pricing-hero {{ padding: 96px 20px 72px; }}
    .pricing-section {{ padding: 64px 20px 80px; }}
  }}
</style>
</head>
<body>
<div class="page">

  <!-- Drawer overlay -->
  <div class="drawer-overlay" id="drawerOverlay" aria-hidden="true"></div>

  <!-- Drawer -->
  <aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Navigation">
    <div class="drawer-head">
      <div class="drawer-logo">
        <svg class="spark" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.4 9.6L24 12l-9.6 2.4L12 24l-2.4-9.6L0 12l9.6-2.4z"/></svg>
        EXPOSE
      </div>
      <button class="drawer-close" id="drawerClose" aria-label="Close menu">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>
      </button>
    </div>
    <nav class="drawer-nav">
      <div class="dn-label">{T['nav_how']}</div>
      <a href="{T['creatives_href']}">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></span>
        {T['nav_creatives']}
      </a>
      <a href="{T['brands_href']}">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></span>
        {T['nav_brands']}
      </a>
      <div class="drawer-divider"></div>
      <a href="{T['about_href']}">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
        {T['nav_about']}
      </a>
      <a href="{T['exi_href']}">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.4 9.6L24 12l-9.6 2.4L12 24l-2.4-9.6L0 12l9.6-2.4z"/></svg></span>
        {T['nav_exi']}
      </a>
      <a href="{T['pricing_href']}" class="active">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></span>
        {T['nav_pricing']}
      </a>
      <div class="drawer-divider"></div>
      <a href="{T['blog_href']}">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></span>
        {T['nav_blog']}
      </a>
      <a href="{T['contact_href']}">
        <span class="dn-icon"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></span>
        {T['nav_contact']}
      </a>
    </nav>
    <a href="{T['lang_href']}" class="drawer-lang-switch" aria-label="{T['lang_circle_label']}">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
      &nbsp;{T['drawer_lang']}
    </a>
    <div class="drawer-foot">
      <a href="#" onclick="goToApp(event)" class="btn-orange">{T['nav_join']} EXPOSE — Free</a>
    </div>
  </aside>

  <!-- NAV -->
  <nav class="nav" aria-label="Main navigation">
    <button class="nav-menu" id="navMenuBtn" aria-label="Open menu" aria-expanded="false">
      <svg width="22" height="16" viewBox="0 0 22 16"><path d="M0 1.5h22M0 8h22M0 14.5h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <div class="nav-logo">
      <svg class="spark" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.4 9.6L24 12l-9.6 2.4L12 24l-2.4-9.6L0 12l9.6-2.4z"/></svg>
      EXPOSE
    </div>
    <div class="nav-links">
      <div class="nav-dropdown">
        <button class="nav-dd-btn" aria-haspopup="true">
          {T['nav_how']}
          <svg class="nav-dd-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="nav-dd-menu">
          {dd_creatives}
          {dd_brands}
        </div>
      </div>
      <a href="{T['about_href']}">{T['nav_about']}</a>
      <a href="{T['exi_href']}">{T['nav_exi']}</a>
      <a href="{T['pricing_href']}" class="active">{T['nav_pricing']}</a>
    </div>
    <div class="nav-right">
      <a class="nav-login" href="#" onclick="goToApp(event)">{T['nav_join']}</a>
      <a href="{T['lang_href']}" class="lang-circle" aria-label="{T['lang_circle_label']}">{T['lang_circle']}</a>
    </div>
  </nav>

  <!-- HERO -->
  <header class="pricing-hero">
    <p class="eyebrow">{T['hero_eyebrow']}</p>
    <h1 class="hero-h1">
      {T['hero_h1a']}<br>
      <span class="italic-accent">{T['hero_h1b']}</span>
    </h1>
    <p class="hero-sub">{T['hero_sub']}</p>
    <div class="trust-row">
      <div class="trust-pill">
        <span class="tp-dot"></span>
        <span class="tp-val">{T['stat1']}</span>
        <span>{T['stat1l']}</span>
      </div>
      <div class="trust-pill">
        <span class="tp-val">{T['stat2']}</span>
        <span>{T['stat2l']}</span>
      </div>
      <div class="trust-pill">
        <span class="tp-val">{T['stat3']}</span>
        <span>{T['stat3l']}</span>
      </div>
    </div>
  </header>

  <!-- PRICING CARDS -->
  <section class="pricing-section" id="pricing">
    <div class="pricing-section-inner">
      <div class="toggle-wrap">
        <div class="price-toggle" id="priceToggle" role="group">
          <button class="price-toggle-btn active" data-period="monthly" id="toggleMonthly">{T['toggle_mo']}</button>
          <button class="price-toggle-btn" data-period="annual" id="toggleAnnual">
            {T['toggle_yr']}
            <span class="save-badge">{T['save']}</span>
          </button>
        </div>
      </div>

      <div class="price-cards">
        <!-- FREE card -->
        <div class="price-card sr">
          <div class="card-plan">
            <span class="card-name">{T['free_name']}</span>
          </div>
          <p class="card-tagline">{T['free_tag']}</p>
          <div class="card-price">
            <span class="price-num">{T['free_price']}</span>
          </div>
          <p class="price-note">{T['free_period']}</p>
          <a href="#" onclick="goToApp(event)" class="card-cta free-cta">{T['free_cta']}</a>
          <p class="card-note-text">{T['free_note']}</p>
          <div class="card-divider"></div>
          <div class="card-features">
            {free_feats_html}
          </div>
        </div>

        <!-- PREMIUM card -->
        <div class="price-card premium sr" style="transition-delay:.1s">
          <div class="card-badge">{T['prem_badge']}</div>
          <div class="card-plan">
            <span class="card-name">{T['prem_name']}</span>
          </div>
          <p class="card-tagline">{T['prem_tag']}</p>
          <div class="card-price">
            <span class="price-num" id="premiumPrice">{T['prem_mo']}</span>
            <span class="price-period">{T['prem_period']}</span>
          </div>
          <div class="price-note">
            <span class="monthly-note">{T['prem_mo_note']}</span>
            <span class="annual-note">{T['prem_yr_note']}</span>
          </div>
          <a href="#" onclick="goToApp(event)" class="card-cta premium-cta">{T['prem_cta']}</a>
          <p class="card-note-text">{T['prem_note']}</p>
          <div class="card-divider"></div>
          <div class="card-features">
            {prem_feats_html}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FEATURE COMPARISON TABLE -->
  <section class="feat-compare">
    <div class="section-header sr">
      <p class="eyebrow">{T['feat_title']}</p>
      <h2 class="h-section">{'Free vs Premium' if not is_he else 'חינמי מול פרימיום'}</h2>
    </div>
    <div class="feat-table sr">
      <div class="feat-table-head">
        <span class="feat-head-col">{'Feature' if not is_he else 'תכונה'}</span>
        <span class="feat-head-col">{T['feat_free_col']}</span>
        <span class="feat-head-col premium">{T['feat_prem_col']}</span>
      </div>
      {feat_table_html}
    </div>
  </section>

  <!-- TESTIMONIALS -->
  <section class="testimonials">
    <div class="section-header sr">
      <p class="eyebrow">{T['testi_eyebrow']}</p>
      <h2 class="h-section">{T['testi_h2']}</h2>
    </div>
    <div class="testi-grid">
      {testi_html}
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq-section">
    <div class="section-header sr">
      <p class="eyebrow">{T['faq_eyebrow']}</p>
      <h2 class="h-section">{T['faq_h2']}</h2>
    </div>
    <div class="faq-list">
      {faq_html}
    </div>
  </section>

  <!-- CTA BANNER -->
  <section class="pricing-cta">
    <p class="eyebrow">{T['cta_eyebrow']}</p>
    <h2 class="cta-h2">{T['cta_h2']}</h2>
    <p class="cta-sub">{T['cta_sub']}</p>
    <div class="cta-btns">
      <a href="#" onclick="goToApp(event)" class="btn-orange-big">{T['cta_btn1']}</a>
      <a href="#" onclick="goToApp(event)" class="btn-ghost-big">{T['cta_btn2']}</a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
  <div class="footer-brand"><svg class="spark" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0l2.4 9.6L24 12l-9.6 2.4L12 24l-2.4-9.6L0 12l9.6-2.4z"/></svg>EXPOSE</div>
  <p class="footer-tagline">{T['footer_tag']}</p>
  <div class="footer-apps">
    <a href="#" class="footer-app-btn" aria-label="App Store">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
      App Store
    </a>
    <a href="#" class="footer-app-btn" aria-label="Google Play">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M3.18 23.76c.38.21.83.22 1.24.03l12.58-7.26-2.9-2.9-10.92 10.13zM.1 2.12C.04 2.35 0 2.59 0 2.85v18.3c0 .26.04.5.1.73l.06.06 10.25-10.25v-.24L.16 2.06.1 2.12zM20.11 9.77l-2.95-1.7-3.23 3.23 3.23 3.23 2.98-1.72c.85-.49.85-1.29-.03-1.04zM4.42.21L17 7.47 14.1 10.37 3.18.24C3.59.05 4.04.06 4.42.21z"/></svg>
      Google Play
    </a>
  </div>
  <div class="footer-cols">
    {footer_cols}
    <div class="footer-col"><h6>{'עקבו אחרינו' if is_he else 'Follow us'}</h6>
      <div class="footer-si-grid">
        <a href="https://www.instagram.com/exposse.global?igsh=MTRyeTM3a25yMWU2ZQ%3D%3D&utm_source=qr" target="_blank" rel="noopener" class="footer-si" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
        <a href="https://www.tiktok.com/@expose.platform" target="_blank" rel="noopener" class="footer-si" aria-label="TikTok"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.29 6.29 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.69a8.18 8.18 0 0 0 4.78 1.52V6.79a4.85 4.85 0 0 1-1.01-.1z"/></svg></a>
        <a href="https://www.linkedin.com/company/exposeglobal/" target="_blank" rel="noopener" class="footer-si" aria-label="LinkedIn"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <span class="footer-copy">{T['footer_copy']}</span>
    <div class="footer-socials">
      <a href="https://www.instagram.com/exposse.global?igsh=MTRyeTM3a25yMWU2ZQ%3D%3D&utm_source=qr" target="_blank" rel="noopener" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
      <a href="https://www.linkedin.com/company/exposeglobal/" target="_blank" rel="noopener" aria-label="LinkedIn"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
    </div>
  </div>
</footer>

</div>

<script>
  function goToApp(e) {{
    e.preventDefault();
    window.open('https://app.expose.global', '_blank');
  }}

  // Nav scroll shadow
  (() => {{
    const nav = document.querySelector('.nav');
    if (!nav) return;
    const toggle = () => nav.classList.toggle('scrolled', window.scrollY > 20);
    window.addEventListener('scroll', toggle, {{ passive: true }});
    toggle();
  }})();

  // Drawer
  (() => {{
    const btn = document.getElementById('navMenuBtn');
    const drawer = document.getElementById('drawer');
    const overlay = document.getElementById('drawerOverlay');
    const close = document.getElementById('drawerClose');
    if (!btn || !drawer) return;
    const open = () => {{ drawer.classList.add('open'); overlay.classList.add('open'); document.body.classList.add('drawer-lock'); btn.setAttribute('aria-expanded','true'); }};
    const shut = () => {{ drawer.classList.remove('open'); overlay.classList.remove('open'); document.body.classList.remove('drawer-lock'); btn.setAttribute('aria-expanded','false'); }};
    btn.addEventListener('click', open);
    close && close.addEventListener('click', shut);
    overlay.addEventListener('click', shut);
    document.addEventListener('keydown', e => {{ if (e.key === 'Escape') shut(); }});
  }})();

  // Pricing toggle
  (() => {{
    const monthly = document.getElementById('toggleMonthly');
    const annual = document.getElementById('toggleAnnual');
    const priceEl = document.getElementById('premiumPrice');
    const monthlyNote = document.querySelector('.monthly-note');
    const annualNote = document.querySelector('.annual-note');
    if (!monthly || !annual) return;

    function setMonthly() {{
      monthly.classList.add('active');
      annual.classList.remove('active');
      if (priceEl) priceEl.textContent = '{T['prem_mo']}';
      if (monthlyNote) monthlyNote.style.display = '';
      if (annualNote) annualNote.style.display = 'none';
    }}
    function setAnnual() {{
      annual.classList.add('active');
      monthly.classList.remove('active');
      if (priceEl) priceEl.textContent = '{T['prem_yr']}';
      if (monthlyNote) monthlyNote.style.display = 'none';
      if (annualNote) annualNote.style.display = '';
    }}
    monthly.addEventListener('click', setMonthly);
    annual.addEventListener('click', setAnnual);
    setMonthly();
  }})();

  // FAQ accordion
  (() => {{
    document.querySelectorAll('.faq-item').forEach(item => {{
      item.querySelector('.faq-q').addEventListener('click', () => {{
        const wasOpen = item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
        if (!wasOpen) item.classList.add('open');
      }});
    }});
  }})();

  // Scroll reveal
  (() => {{
    const els = document.querySelectorAll('.sr');
    if (!els.length) return;
    const io = new IntersectionObserver((entries) => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }}
      }});
    }}, {{ threshold: 0.1, rootMargin: '0px 0px -40px 0px' }});
    els.forEach(el => io.observe(el));
  }})();
</script>
</body>
</html>'''
    return html

# Generate both files
en_html = make_page(is_he=False)
he_html = make_page(is_he=True)

with open('site-pricing.html', 'w', encoding='utf-8') as f:
    f.write(en_html)
print('Created site-pricing.html')

with open('site-pricing-he.html', 'w', encoding='utf-8') as f:
    f.write(he_html)
print('Created site-pricing-he.html')

# Update nav pricing links across all existing pages
import re

en_pages = ['site.html', 'site-brands.html', 'site-exi.html', 'site-exi-brands.html',
            'site-about.html', 'site-blog.html', 'site-contact.html']
he_pages = ['site-he.html', 'site-brands-he.html', 'site-exi-he.html', 'site-exi-brands-he.html',
            'site-about-he.html', 'site-blog-he.html', 'site-contact-he.html']

for fname in en_pages:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    new = html.replace('href="#pricing"', 'href="site-pricing.html"')
    if new != html:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'  Updated pricing link: {fname}')
    else:
        print(f'  No change: {fname}')

for fname in he_pages:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    new = html.replace('href="#pricing"', 'href="site-pricing-he.html"')
    if new != html:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'  Updated pricing link: {fname}')
    else:
        print(f'  No change: {fname}')

print('\nDone.')
