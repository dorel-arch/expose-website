#!/usr/bin/env python3
"""Inject a full pricing section into the 4 main pages."""
import os
os.chdir('/home/claude/repo')

# ─────────────────────────────────────────────
# PRICING CSS  (injected before </style>)
# ─────────────────────────────────────────────
PRICING_CSS = """
  /* ══════════════════════════════════════════
     PRICING SECTION
     ══════════════════════════════════════════ */
  .pricing {
    padding: 80px 20px 60px;
    background: var(--bg-soft);
    position: relative;
    overflow: hidden;
  }
  .pricing-glow {
    position: absolute; top: -160px; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 600px; border-radius: 50%;
    background: radial-gradient(circle, rgba(255,106,26,.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .pricing-inner {
    max-width: 880px;
    margin: 0 auto;
    position: relative;
  }

  /* Head */
  .pricing-head {
    text-align: center;
    margin-bottom: 36px;
  }
  .pricing-head h2 {
    font-size: clamp(30px, 5vw, 52px);
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    color: var(--ink);
    margin: 10px 0 14px;
  }
  .pricing-sub {
    font-size: 16px;
    color: var(--gray);
    max-width: 400px;
    margin: 0 auto;
    line-height: 1.5;
  }

  /* Toggle */
  .pricing-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin-bottom: 44px;
    flex-wrap: wrap;
  }
  .pt-label {
    font-size: 14px;
    font-weight: 600;
    color: var(--gray-2);
    cursor: pointer;
    transition: color .2s;
    user-select: none;
  }
  .pt-label.active { color: var(--ink); }
  .pt-switch {
    width: 48px; height: 26px; border-radius: 99px;
    background: var(--line-2);
    position: relative; cursor: pointer;
    transition: background .25s;
    flex-shrink: 0;
    display: flex; align-items: center;
  }
  .pt-switch.on { background: var(--orange); }
  .pt-thumb {
    width: 20px; height: 20px; border-radius: 50%;
    background: #fff; position: absolute; left: 3px;
    box-shadow: 0 1px 4px rgba(0,0,0,.18);
    transition: transform .25s cubic-bezier(.16,1,.3,1);
  }
  .pt-switch.on .pt-thumb { transform: translateX(22px); }
  [dir="rtl"] .pt-switch.on .pt-thumb { transform: translateX(-22px); }
  .pt-save-badge {
    background: var(--orange); color: #fff;
    font-size: 11px; font-weight: 800; letter-spacing: .06em;
    padding: 4px 10px; border-radius: 99px;
    opacity: 0; transform: scale(.8) translateY(4px);
    transition: opacity .2s, transform .2s;
    pointer-events: none;
  }
  .pt-save-badge.show { opacity: 1; transform: scale(1) translateY(0); }
  .pt-annual-saving {
    font-size: 12px; color: var(--orange); font-weight: 700;
    opacity: 0; transition: opacity .3s;
    text-align: center; width: 100%; margin-top: -32px; margin-bottom: 8px;
  }
  .pt-annual-saving.show { opacity: 1; }

  /* Cards grid */
  .pricing-cards {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px;
    align-items: start;
    margin-bottom: 40px;
  }

  /* Card base */
  .pc {
    border-radius: 24px;
    padding: 32px 28px 28px;
    display: flex;
    flex-direction: column;
    position: relative;
    transition: transform .3s ease, box-shadow .3s ease;
  }
  .pc:hover { transform: translateY(-4px); }

  /* Free card */
  .pc-free {
    background: #fff;
    border: 1.5px solid var(--line);
    box-shadow: 0 2px 16px rgba(19,19,19,.04);
  }
  .pc-free:hover {
    box-shadow: 0 8px 32px rgba(19,19,19,.08);
    border-color: var(--orange-glow);
  }

  /* Premium card */
  .pc-premium {
    background: var(--orange);
    color: #fff;
    box-shadow:
      0 20px 60px rgba(255,106,26,.4),
      0 6px 20px rgba(255,106,26,.25),
      inset 0 1px 0 rgba(255,255,255,.15);
  }
  .pc-premium:hover {
    box-shadow:
      0 28px 80px rgba(255,106,26,.5),
      0 8px 28px rgba(255,106,26,.3),
      inset 0 1px 0 rgba(255,255,255,.15);
  }
  /* Decorative highlight streak */
  .pc-premium::before {
    content: '';
    position: absolute; inset: 0;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255,255,255,.14) 0%, transparent 50%);
    pointer-events: none;
  }

  /* Trial badge */
  .pc-trial-badge {
    position: absolute;
    top: 20px;
    inset-inline-end: 20px;
    background: #fff;
    color: var(--orange);
    font-size: 10px; font-weight: 800;
    letter-spacing: .1em; text-transform: uppercase;
    padding: 5px 12px; border-radius: 99px;
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
  }

  /* Card icon */
  .pc-icon {
    width: 44px; height: 44px; border-radius: 12px;
    display: grid; place-items: center;
    margin-bottom: 18px;
    flex-shrink: 0;
  }
  .pc-free .pc-icon {
    background: var(--orange-soft);
    color: var(--orange);
    border: 1px solid var(--orange-glow);
  }
  .pc-premium .pc-icon {
    background: rgba(255,255,255,.2);
    color: #fff;
    border: 1px solid rgba(255,255,255,.3);
  }

  /* Tier label */
  .pc-tier-label {
    font-size: 11px; font-weight: 800; letter-spacing: .14em;
    text-transform: uppercase; margin-bottom: 10px;
  }
  .pc-free .pc-tier-label { color: var(--orange); }
  .pc-premium .pc-tier-label { color: rgba(255,255,255,.7); }

  /* Price */
  .pc-price-row {
    display: flex;
    align-items: flex-end;
    gap: 2px;
    margin-bottom: 4px;
  }
  .pc-currency {
    font-size: 20px; font-weight: 800;
    line-height: 1.6;
    margin-bottom: 4px;
  }
  .pc-free .pc-currency { color: var(--gray-2); }
  .pc-premium .pc-currency { color: rgba(255,255,255,.75); }
  .pc-amount {
    font-size: 64px; font-weight: 800;
    letter-spacing: -0.04em; line-height: 1;
    transition: transform .3s cubic-bezier(.16,1,.3,1);
  }
  .pc-free .pc-amount { color: var(--ink); }
  .pc-premium .pc-amount { color: #fff; }
  .pc-price-meta {
    display: flex; flex-direction: column;
    padding-inline-start: 6px;
    padding-bottom: 8px;
  }
  .pc-per-label {
    font-size: 14px; font-weight: 700; line-height: 1.3;
  }
  .pc-premium .pc-per-label { color: rgba(255,255,255,.8); }
  .pc-free .pc-per-label { color: var(--gray); }
  .pc-cancel {
    font-size: 11px; font-weight: 500;
  }
  .pc-premium .pc-cancel { color: rgba(255,255,255,.55); }
  .pc-free .pc-cancel { color: var(--gray-2); }

  .pc-ios-note {
    font-size: 12px; margin: 0 0 14px;
  }
  .pc-premium .pc-ios-note { color: rgba(255,255,255,.6); }
  .pc-free .pc-ios-note { color: var(--gray-2); }

  .pc-tagline {
    font-size: 14px; line-height: 1.5;
    margin-bottom: 20px;
  }
  .pc-free .pc-tagline { color: var(--ink-2); }
  .pc-premium .pc-tagline { color: rgba(255,255,255,.85); }

  /* "includes" label on premium */
  .pc-includes {
    display: flex; align-items: center; gap: 6px;
    font-size: 12px; font-weight: 700; letter-spacing: .02em;
    margin-bottom: 12px; margin-top: 4px;
    color: rgba(255,255,255,.7);
  }

  /* Feature list */
  .pc-features {
    list-style: none; padding: 0; margin: 0 0 28px;
    display: flex; flex-direction: column; gap: 9px;
    flex: 1;
  }
  .pc-features li {
    display: flex; align-items: flex-start;
    gap: 9px; font-size: 14px; line-height: 1.45;
  }
  .pc-features li .pf-icon {
    flex-shrink: 0; width: 18px; height: 18px;
    border-radius: 50%; display: grid; place-items: center;
    margin-top: 1px;
  }
  .pc-free .pf-icon {
    background: var(--orange-soft);
    color: var(--orange);
  }
  .pc-premium .pf-icon {
    background: rgba(255,255,255,.2);
    color: #fff;
  }
  .pc-free .pc-features li { color: var(--ink-2); }
  .pc-premium .pc-features li { color: rgba(255,255,255,.9); }

  /* CTAs */
  .pc-btn {
    display: flex; align-items: center; justify-content: center;
    gap: 7px; padding: 15px 24px; border-radius: 12px;
    font-size: 14px; font-weight: 700; letter-spacing: .01em;
    text-decoration: none; cursor: pointer;
    transition: all .2s ease;
    text-align: center;
  }
  .pc-btn-free {
    background: transparent;
    border: 2px solid var(--orange);
    color: var(--orange);
  }
  .pc-btn-free:hover {
    background: var(--orange);
    color: #fff;
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(255,106,26,.25);
  }
  .pc-btn-premium {
    background: #fff;
    color: var(--orange);
    border: 2px solid #fff;
    box-shadow: 0 4px 16px rgba(0,0,0,.15);
  }
  .pc-btn-premium:hover {
    background: rgba(255,255,255,.92);
    box-shadow: 0 8px 28px rgba(0,0,0,.2);
    transform: translateY(-1px);
  }

  .pc-no-cc {
    display: flex; align-items: center; justify-content: center;
    gap: 5px; text-align: center;
    font-size: 12px; margin: 10px 0 0;
    color: rgba(255,255,255,.6);
  }

  /* Trust row */
  .pricing-trust {
    display: flex; align-items: center; justify-content: center;
    flex-wrap: wrap; gap: 20px;
    padding-top: 28px;
    border-top: 1px solid var(--line);
  }
  .trust-item {
    display: flex; align-items: center; gap: 6px;
    font-size: 13px; font-weight: 500; color: var(--gray);
  }
  .trust-item svg { color: var(--orange); flex-shrink: 0; }

  /* Desktop */
  @media (min-width: 700px) {
    .pricing { padding: 100px 40px 80px; }
    .pricing-cards {
      grid-template-columns: 1fr 1fr;
      align-items: start;
    }
    .pc-premium { transform: translateY(-20px); }
    .pc-premium:hover { transform: translateY(-24px); }
  }
  @media (min-width: 900px) {
    .pricing { padding: 120px max(40px, calc(50% - 480px)) 100px; }
  }
"""

# ─────────────────────────────────────────────
# SVG helper
# ─────────────────────────────────────────────
CHECK_SVG = '<svg class="pf-check" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
LOCK_SVG  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
CYCLE_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>'
GIFT_SVG  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>'
STAR_SVG  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
SHIELD_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
ROCKET_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>'
ARROW_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'

def feature_li(text):
    return f'<li><span class="pf-icon">{CHECK_SVG}</span>{text}</li>'

PRICING_JS = """
  // ── Pricing toggle ──
  (function(){
    var sw = document.getElementById('ptSwitch');
    if (!sw) return;
    var monthly = document.getElementById('ptMonthly');
    var annual  = document.getElementById('ptAnnual');
    var badge   = document.getElementById('ptSaveBadge');
    var saving  = document.getElementById('ptAnnualSaving');
    var price   = document.getElementById('pcPremPrice');
    var iosNote = document.getElementById('pcIosNote');
    var annual_on = false;
    sw.addEventListener('click', function(){
      annual_on = !annual_on;
      sw.classList.toggle('on', annual_on);
      sw.setAttribute('aria-checked', String(annual_on));
      monthly.classList.toggle('active', !annual_on);
      annual.classList.toggle('active', annual_on);
      if (badge) badge.classList.toggle('show', annual_on);
      if (saving) saving.classList.toggle('show', annual_on);
      if (price) {
        price.style.transform = 'scale(.85) translateY(-4px)';
        setTimeout(function(){
          price.textContent = annual_on ? '12' : '15';
          price.style.transform = '';
        }, 150);
      }
      if (iosNote) iosNote.style.opacity = annual_on ? '0' : '';
    });
  })();
"""

# ─────────────────────────────────────────────
# HTML generators
# ─────────────────────────────────────────────

def make_pricing_he(is_brands):
    """Hebrew pricing section."""
    if is_brands:
        h2       = 'תמחור פשוט. <span class="italic-accent">שקוף.</span>'
        sub      = 'בחרו את התוכנית הנכונה לעסק שלכם — תמיד אפשר לשדרג'
        tagline_free = 'שכרו יוצרים מאומתים, נהלו פרויקטים מקצה לקצה.'
        features_free = [
            'גישה ליוצרים מאומתים ומסוננים',
            'פרויקטים ובקשות ללא הגבלה',
            'EXi — תצוגה מקדימה של תובנות שיווקיות',
            'תשלומים מאובטחים דרך אסקרו',
            'תמיכה במייל ובצ\'אט',
        ]
        cta_free = 'הורידו את האפליקציה'
        tagline_prem = 'EXi מלא — ה-CMO שלכם ב-AI, לעסקים שרציניים לגבי צמיחה.'
        includes_lbl = 'כל מה שבחינמי, בתוספת:'
        features_prem = [
            'EXi מלא — ה-CMO שלכם ב-AI 24/7',
            'שאלות ללא הגבלה על אנליטיקה וקמפיינים',
            'מעקב מתחרים ורשתות חברתיות',
            'דוחות שיווק שבועיים וחודשיים',
            'גישה עדיפות לאירועים וצוות EXPOSE',
            'מנוי אחד — ווב, iOS ואנדרואיד',
        ]
        cta_prem  = 'התחילו ניסיון חינם 14 יום'
        ios_note  = 'או ₪20/חודש ב-iOS ואנדרואיד'
        saving_txt = 'חוסכים ₪36 בשנה'
    else:
        h2       = 'פחות ריצות. <span class="italic-accent">יותר עבודות.</span>'
        sub      = 'הצטרפו בחינם — שדרגו כשאתם מוכנים לצמיחה אמיתית'
        tagline_free = 'הצטרפו לפלטפורמה, בנו פורטפוליו, קבלו התאמות חכמות.'
        features_free = [
            'פרופיל מקצועי ופורטפוליו',
            'התאמות חכמות לבריפים רלוונטיים',
            'EXi — תצוגה מקדימה של תובנות',
            'תשלומים מאובטחים דרך אסקרו',
            'תמיכה במייל ובצ\'אט',
        ]
        cta_free = 'הצטרפו חינם'
        tagline_prem = 'EXi מלא — הסוכן החכם שמנהל את הקריירה שלכם 24/7.'
        includes_lbl = 'כל מה שבחינמי, בתוספת:'
        features_prem = [
            'EXi מלא — ניהול קריירה 24/7',
            'שאלות ללא הגבלה על אנליטיקה ועסקאות',
            'מעקב טרנדים ושוק יצירתי',
            'דוחות הכנסות ועמלות שבועיים',
            'גישה עדיפות לאירועים וצוות EXPOSE',
            'מנוי אחד — ווב, iOS ואנדרואיד',
        ]
        cta_prem  = 'התחילו ניסיון חינם 14 יום'
        ios_note  = 'או ₪20/חודש ב-iOS ואנדרואיד'
        saving_txt = 'חוסכים ₪36 בשנה'

    free_lis = '\n              '.join(feature_li(f) for f in features_free)
    prem_lis = '\n              '.join(feature_li(f) for f in features_prem)

    return f"""
  <!-- PRICING -->
  <section class="pricing" id="pricing">
    <div class="pricing-glow" aria-hidden="true"></div>
    <div class="pricing-inner">

      <div class="pricing-head">
        <div class="eyebrow">תמחור</div>
        <h2>{h2}</h2>
        <p class="pricing-sub">{sub}</p>
      </div>

      <div class="pricing-toggle">
        <span class="pt-label active" id="ptMonthly">חודשי</span>
        <button class="pt-switch" id="ptSwitch" role="switch" aria-checked="false" aria-label="מעבר לחיוב שנתי"></button>
        <span class="pt-label" id="ptAnnual">שנתי</span>
        <span class="pt-save-badge" id="ptSaveBadge">חסכו 20%</span>
      </div>
      <p class="pt-annual-saving" id="ptAnnualSaving">{saving_txt} 🎉</p>

      <div class="pricing-cards">

        <!-- FREE -->
        <div class="pc pc-free">
          <div class="pc-icon">{SHIELD_SVG}</div>
          <div class="pc-tier-label">חינמי</div>
          <div class="pc-price-row">
            <span class="pc-currency">₪</span>
            <span class="pc-amount">0</span>
            <div class="pc-price-meta">
              <span class="pc-per-label">/תמיד</span>
              <span class="pc-cancel">ללא תשלום</span>
            </div>
          </div>
          <p class="pc-tagline">{tagline_free}</p>
          <ul class="pc-features">
            {free_lis}
          </ul>
          <a href="#" class="pc-btn pc-btn-free" onclick="goToApp(event)">{cta_free}</a>
        </div>

        <!-- PREMIUM -->
        <div class="pc pc-premium">
          <span class="pc-trial-badge">ניסיון חינם 14 יום</span>
          <div class="pc-icon">{ROCKET_SVG}</div>
          <div class="pc-tier-label">פרמיום</div>
          <div class="pc-price-row">
            <span class="pc-currency">₪</span>
            <span class="pc-amount" id="pcPremPrice">15</span>
            <div class="pc-price-meta">
              <span class="pc-per-label">/חודש</span>
              <span class="pc-cancel">ביטול בכל עת</span>
            </div>
          </div>
          <p class="pc-ios-note" id="pcIosNote">{ios_note}</p>
          <p class="pc-tagline">{tagline_prem}</p>
          <div class="pc-includes">
            {CHECK_SVG}
            {includes_lbl}
          </div>
          <ul class="pc-features">
            {prem_lis}
          </ul>
          <a href="#" class="pc-btn pc-btn-premium" onclick="goToApp(event)">
            {cta_prem} {ARROW_SVG}
          </a>
          <p class="pc-no-cc">{LOCK_SVG} ללא כרטיס אשראי · ביטול בכל עת</p>
        </div>

      </div>

      <div class="pricing-trust">
        <div class="trust-item">{LOCK_SVG} תשלום מאובטח SSL</div>
        <div class="trust-item">{CYCLE_SVG} ביטול בכל עת</div>
        <div class="trust-item">{GIFT_SVG} ניסיון חינם 14 יום</div>
        <div class="trust-item">{STAR_SVG} תמיכה 24/7</div>
      </div>

    </div>
  </section>

"""


def make_pricing_en(is_brands):
    """English pricing section."""
    if is_brands:
        h2       = 'Simple pricing. <span class="italic-accent">Real results.</span>'
        sub      = 'Choose the plan that fits your brand — upgrade anytime'
        tagline_free = 'Hire vetted creatives and run projects end-to-end.'
        features_free = [
            'Access to vetted creatives',
            'Unlimited projects and applications',
            'EXi — preview marketing insights',
            'Secure in-app payments via escrow',
            'Email &amp; chat support',
        ]
        cta_free = 'Get the App'
        tagline_prem = 'Full EXi as your AI CMO — for brands serious about growth.'
        includes_lbl = 'Everything in Free, plus:'
        features_prem = [
            'Full EXi — your AI CMO 24/7',
            'Unlimited Ask EXi on analytics &amp; campaigns',
            'Competitor &amp; social media tracking',
            'Weekly &amp; monthly marketing reports',
            'Priority access to EXPOSE events and team',
            'One subscription — works on web, iOS &amp; Android',
        ]
        cta_prem  = 'Start 14-Day Free Trial'
        ios_note  = 'Or ₪20/mo on iOS &amp; Android'
        saving_txt = "You're saving ₪36/year 🎉"
    else:
        h2       = 'Stop chasing. <span class="italic-accent">Start earning.</span>'
        sub      = 'Join for free — upgrade when you\'re ready to grow'
        tagline_free = 'Build your profile, get smart matches, get paid.'
        features_free = [
            'Professional profile &amp; portfolio',
            'Smart brief matching',
            'EXi — preview marketing insights',
            'Secure in-app payments via escrow',
            'Email &amp; chat support',
        ]
        cta_free = 'Join for Free'
        tagline_prem = 'Full EXi — the AI agent that manages your creative career 24/7.'
        includes_lbl = 'Everything in Free, plus:'
        features_prem = [
            'Full EXi — career management 24/7',
            'Unlimited analytics &amp; deal insights',
            'Market &amp; trend tracking',
            'Weekly earnings &amp; campaign reports',
            'Priority access to EXPOSE events and team',
            'One subscription — web, iOS &amp; Android',
        ]
        cta_prem  = 'Start 14-Day Free Trial'
        ios_note  = 'Or ₪20/mo on iOS &amp; Android'
        saving_txt = "You're saving ₪36/year 🎉"

    free_lis = '\n              '.join(feature_li(f) for f in features_free)
    prem_lis = '\n              '.join(feature_li(f) for f in features_prem)

    return f"""
  <!-- PRICING -->
  <section class="pricing" id="pricing">
    <div class="pricing-glow" aria-hidden="true"></div>
    <div class="pricing-inner">

      <div class="pricing-head">
        <div class="eyebrow">Pricing</div>
        <h2>{h2}</h2>
        <p class="pricing-sub">{sub}</p>
      </div>

      <div class="pricing-toggle">
        <span class="pt-label active" id="ptMonthly">Monthly</span>
        <button class="pt-switch" id="ptSwitch" role="switch" aria-checked="false" aria-label="Switch to annual billing"></button>
        <span class="pt-label" id="ptAnnual">Annual</span>
        <span class="pt-save-badge" id="ptSaveBadge">Save 20%</span>
      </div>
      <p class="pt-annual-saving" id="ptAnnualSaving">{saving_txt}</p>

      <div class="pricing-cards">

        <!-- FREE -->
        <div class="pc pc-free">
          <div class="pc-icon">{SHIELD_SVG}</div>
          <div class="pc-tier-label">Free</div>
          <div class="pc-price-row">
            <span class="pc-currency">₪</span>
            <span class="pc-amount">0</span>
            <div class="pc-price-meta">
              <span class="pc-per-label">/forever</span>
              <span class="pc-cancel">no credit card</span>
            </div>
          </div>
          <p class="pc-tagline">{tagline_free}</p>
          <ul class="pc-features">
            {free_lis}
          </ul>
          <a href="#" class="pc-btn pc-btn-free" onclick="goToApp(event)">{cta_free}</a>
        </div>

        <!-- PREMIUM -->
        <div class="pc pc-premium">
          <span class="pc-trial-badge">14-Day Free Trial</span>
          <div class="pc-icon">{ROCKET_SVG}</div>
          <div class="pc-tier-label">Premium</div>
          <div class="pc-price-row">
            <span class="pc-currency">₪</span>
            <span class="pc-amount" id="pcPremPrice">15</span>
            <div class="pc-price-meta">
              <span class="pc-per-label">/mo</span>
              <span class="pc-cancel">cancel anytime</span>
            </div>
          </div>
          <p class="pc-ios-note" id="pcIosNote">{ios_note}</p>
          <p class="pc-tagline">{tagline_prem}</p>
          <div class="pc-includes">
            {CHECK_SVG}
            {includes_lbl}
          </div>
          <ul class="pc-features">
            {prem_lis}
          </ul>
          <a href="#" class="pc-btn pc-btn-premium" onclick="goToApp(event)">
            {cta_prem} {ARROW_SVG}
          </a>
          <p class="pc-no-cc">{LOCK_SVG} No credit card · Cancel anytime</p>
        </div>

      </div>

      <div class="pricing-trust">
        <div class="trust-item">{LOCK_SVG} SSL Secured</div>
        <div class="trust-item">{CYCLE_SVG} Cancel anytime</div>
        <div class="trust-item">{GIFT_SVG} 14-day free trial</div>
        <div class="trust-item">{STAR_SVG} 24/7 support</div>
      </div>

    </div>
  </section>

"""


# ─────────────────────────────────────────────
# Inject into pages
# ─────────────────────────────────────────────

PAGES = [
    ('site-he.html',        make_pricing_he(False)),
    ('site-brands-he.html', make_pricing_he(True)),
    ('site.html',           make_pricing_en(False)),
    ('site-brands.html',    make_pricing_en(True)),
]

for fname, pricing_html in PAGES:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has pricing section
    if 'id="pricing"' in html:
        print(f'  SKIP (already done): {fname}')
        continue

    changed = False

    # 1. Inject CSS before </style>
    style_pos = html.find('</style>')
    if style_pos != -1:
        html = html[:style_pos] + PRICING_CSS + '\n' + html[style_pos:]
        changed = True

    # 2. Inject HTML before <!-- FINAL CTA -->
    target = '  <!-- FINAL CTA -->'
    if target not in html:
        # fallback: before <section class="final-cta">
        target = '  <section class="final-cta">'
    if target in html:
        html = html.replace(target, pricing_html + target, 1)
        changed = True

    # 3. Inject JS before </script> (last one)
    last_script = html.rfind('</script>')
    if last_script != -1:
        html = html[:last_script] + '\n  ' + PRICING_JS.strip() + '\n' + html[last_script:]
        changed = True

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  OK: {fname}')
    else:
        print(f'  ERROR: {fname}')

print('\nDone.')
