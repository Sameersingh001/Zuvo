
import os

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ZUVO  Smart School Bus Tracking</title>
  <meta name="description" content="ZUVO is India's most trusted school bus tracking platform." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>

<!-- NAVBAR -->
<nav class="nav" id="navbar">
  <div class="nav-inner">
    <a href="#" class="nav-logo" onclick="showPage('home');return false">
      <div class="nav-logo-icon">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="6" width="20" height="12" rx="3"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/><path d="M2 10h20"/></svg>
      </div>
      <span class="nav-logo-text">ZUVO</span>
    </a>
    <div class="nav-links" id="navLinks">
      <a href="#" class="nav-link" onclick="showPage('home');return false">Home</a>
      <a href="#" class="nav-link" onclick="showPage('about');return false">About</a>
      <a href="#" class="nav-link" onclick="showPage('pricing');return false">Pricing</a>
      <a href="#" class="nav-link" onclick="showPage('contact');return false">Contact</a>
      <a href="#" class="nav-link" onclick="showPage('legal');return false">Legal</a>
      <a href="#" class="nav-link" onclick="showPage('refund');return false">Refund</a>
    </div>
    <div class="nav-actions">
      <a href="../admin/index.html" class="btn-ghost">Admin Login</a>
      <a href="#" class="btn-primary" onclick="showPage('pricing');return false">Get Started</a>
    </div>
    <button class="hamburger" id="hamburger" onclick="toggleMenu()" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- ======= HOME PAGE ======= -->
<div class="page active" id="page-home">
  <section class="hero">
    <div class="hero-blob b1"></div>
    <div class="hero-blob b2"></div>
    <div class="container hero-container">
      <div class="hero-content">
        <div class="hero-badge anim a1"><span class="badge-dot"></span>Live GPS · iOS &amp; Android</div>
        <h1 class="hero-title anim a2">Know Where Your<br/><span class="gradient-text">Child's Bus Is</span><br/>At All Times</h1>
        <p class="hero-sub anim a3">ZUVO gives parents real-time bus location, instant arrival alerts, and peace of mind  while giving schools complete fleet control.</p>
        <div class="hero-cta anim a4">
          <a href="#" onclick="showPage('pricing');return false" class="btn-hp">Start Free Trial</a>
          <a href="#" onclick="showPage('about');return false" class="btn-hg">Learn More →</a>
        </div>
        <div class="hero-trust anim a5">
          <div class="ti"><span class="tn">5s</span><span>GPS Telemetry</span></div>
          <div class="td"></div>
          <div class="ti"><span class="tn">AIS-140</span><span>Compliant</span></div>
          <div class="td"></div>
          <div class="ti"><span class="tn">Zero</span><span>Hardware Setup</span></div>
        </div>
      </div>
      <div class="hero-card-wrap anim a3">
        <div class="hero-card animate-float">
          <div class="hc-head"><div class="hc-dot"></div><span>Bus MH01AB1234  Live</span><span class="hc-time">8:47 AM</span></div>
          <div class="hc-map">
            <div class="hc-road hcr1"></div>
            <div class="hc-road hcr2"></div>
            <div class="hc-pin bus-pin"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M2 10h20"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/></svg></div>
            <div class="hc-pin dest-pin">🏫</div>
          </div>
          <div class="hc-stats">
            <div class="hc-s"><span>ETA</span><strong>8 min</strong></div>
            <div class="hc-s"><span>Speed</span><strong>42 km/h</strong></div>
            <div class="hc-s"><span>Driver</span><strong>Ramesh K.</strong></div>
          </div>
          <div class="hc-alert"><span>🔔</span><span>Arriving at School Gate in 8 mins</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="features">
    <div class="container">
      <div class="sec-hd"><div class="sec-badge">Features</div><h2 class="sec-title">Everything you need.<br/>Nothing you don't.</h2><p class="sec-sub">Built for schools, parents, and drivers across India.</p></div>
      <div class="features-grid">
        <div class="feat-card" data-anim><div class="feat-icon" style="--c:#2563eb;--cb:#eff6ff"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div><h3>Real-Time GPS</h3><p>Live updates every 5 seconds. Know where every bus is, always.</p></div>
        <div class="feat-card" data-anim><div class="feat-icon" style="--c:#7c3aed;--cb:#f5f3ff"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg></div><h3>Instant Alerts</h3><p>Push notifications when bus starts, reaches a stop, or is near home.</p></div>
        <div class="feat-card" data-anim><div class="feat-icon" style="--c:#059669;--cb:#ecfdf5"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div><h3>Driver Management</h3><p>Add drivers, assign vehicles, track licenses and monitor performance.</p></div>
        <div class="feat-card" data-anim><div class="feat-icon" style="--c:#ea580c;--cb:#fff7ed"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div><h3>Route Planning</h3><p>Design multi-stop routes on interactive map with drag-and-drop stops.</p></div>
        <div class="feat-card" data-anim><div class="feat-icon" style="--c:#db2777;--cb:#fdf2f8"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.15 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.08 1h3a2 2 0 0 1 2 1.72c.13 1 .37 1.98.72 2.93a2 2 0 0 1-.45 2.11L7.09 9a16 16 0 0 0 7.85 7.85l1.24-1.24a2 2 0 0 1 2.11-.45c.95.35 1.93.59 2.93.72A2 2 0 0 1 22 16.92z"/></svg></div><h3>SOS Alerts</h3><p>One-tap SOS from drivers instantly notifies school admin with location.</p></div>
        <div class="feat-card" data-anim><div class="feat-icon" style="--c:#0891b2;--cb:#ecfeff"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div><h3>Admin Dashboard</h3><p>Full fleet analytics, trip reports, and live overview in one place.</p></div>
      </div>
    </div>
  </section>

  <section class="section steps-section">
    <div class="container">
      <div class="sec-hd"><div class="sec-badge">How It Works</div><h2 class="sec-title">Up and running in 4 steps</h2></div>
      <div class="steps-wrap">
        <div class="step-card" data-anim><div class="step-num">01</div><h3>Create Account</h3><p>Register as a school admin in minutes.</p></div>
        <div class="step-arr">→</div>
        <div class="step-card" data-anim><div class="step-num">02</div><h3>Add Fleet</h3><p>Add vehicles, drivers, and plan routes.</p></div>
        <div class="step-arr">→</div>
        <div class="step-card" data-anim><div class="step-num">03</div><h3>Invite Parents</h3><p>Parents download ZUVO and link to their child.</p></div>
        <div class="step-arr">→</div>
        <div class="step-card" data-anim><div class="step-num">04</div><h3>Go Live!</h3><p>Real-time updates for everyone.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="sec-hd"><div class="sec-badge">Testimonials</div><h2 class="sec-title">Loved across India</h2></div>
      <div class="test-grid">
        <div class="test-card" data-anim><div class="stars">★★★★★</div><p>"ZUVO changed our morning routine. I know exactly when the bus arrives. No more 20-minute waits!"</p><div class="test-author"><div class="ta" style="background:#eff6ff;color:#2563eb">P</div><div><strong>Priya Mehta</strong><span>Parent, Delhi Public School</span></div></div></div>
        <div class="test-card" data-anim><div class="stars">★★★★★</div><p>"Managing 30 buses used to be a nightmare. With ZUVO dashboard, it's now a 5-minute morning check."</p><div class="test-author"><div class="ta" style="background:#f5f3ff;color:#7c3aed">R</div><div><strong>Rajesh Kumar</strong><span>Principal, Sunrise Academy, Mumbai</span></div></div></div>
        <div class="test-card" data-anim><div class="stars">★★★★★</div><p>"The SOS feature gives peace of mind. If anything goes wrong, my school is notified instantly."</p><div class="test-author"><div class="ta" style="background:#ecfdf5;color:#059669">S</div><div><strong>Sunita Sharma</strong><span>Parent, Bengaluru</span></div></div></div>
      </div>
    </div>
  </section>

  <section class="cta-section">
    <div class="cta-glow"></div>
    <div class="container">
      <h2 class="cta-title">Ready to transform school transport?</h2>
      <p class="cta-sub">Pre-register today for early rollout and private beta access.</p>
      <div class="cta-btns">
        <a href="../admin/index.html" class="btn-cta-p">Start Free Trial</a>
        <a href="#" class="btn-cta-g" onclick="showPage('contact');return false">Talk to Sales →</a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="6" width="20" height="12" rx="3"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/><path d="M2 10h20"/></svg><span>ZUVO</span></div>
          <p>India's trusted school bus tracking platform. Keeping kids safe, every journey.</p>
          <div class="footer-social"><a href="#">𝕏</a><a href="#">in</a><a href="#">f</a></div>
        </div>
        <div class="footer-col"><h4>Product</h4><a href="#" onclick="showPage('home');return false">Home</a><a href="#" onclick="showPage('pricing');return false">Pricing</a><a href="#features">Features</a></div>
        <div class="footer-col"><h4>Company</h4><a href="#" onclick="showPage('about');return false">About Us</a><a href="#" onclick="showPage('contact');return false">Contact</a><a href="#">Blog</a></div>
        <div class="footer-col"><h4>Legal</h4><a href="#" onclick="showPage('legal');return false">Terms &amp; Privacy</a><a href="#" onclick="showPage('refund');return false">Refund Policy</a><a href="#" onclick="showPage('legal');return false">Cookie Policy</a></div>
      </div>
      <div class="footer-bottom"><p>© 2026 ZUVO Technologies Pvt. Ltd. All rights reserved. Made with ❤️ in India</p></div>
    </div>
  </footer>
</div>

<!-- ======= ABOUT PAGE ======= -->
<div class="page" id="page-about">
  <section class="page-hero"><div class="page-hero-glow"></div><div class="container"><div class="sec-badge" style="margin-bottom:16px">Our Story</div><h1 class="page-hero-title">We make school<br/><span class="gradient-text">commutes safer</span></h1><p class="page-hero-sub">Founded in 2023, ZUVO was born from a simple idea: every parent deserves to know their child is safe.</p></div></section>
  <section class="section"><div class="container"><div class="about-grid">
    <div data-anim style="max-width:800px;margin:0 auto;text-align:center"><h2 style="font-size:1.9rem;font-weight:800;color:#0f172a;margin-bottom:20px;line-height:1.3">Born From A Parent's Morning Worry</h2><p style="color:#475569;line-height:1.9;margin-bottom:14px">ZUVO was founded after our CEO spent 45 minutes waiting for his daughter's school bus with zero information. That frustration became a mission.</p><p style="color:#475569;line-height:1.9;margin-bottom:14px">We are building India's most dependable school bus tracking ecosystem designed for parents and schools.</p></div>
  </div></div></section>
  <section class="section" style="background:#f8fafc"><div class="container"><div class="sec-hd"><div class="sec-badge">Values</div><h2 class="sec-title">What drives us</h2></div><div class="values-grid"><div class="val-card" data-anim><div class="vi">🛡️</div><h3>Safety First</h3><p>Every feature: does this make a child safer?</p></div><div class="val-card" data-anim><div class="vi">🤝</div><h3>Transparency</h3><p>No hidden features, no dark patterns.</p></div><div class="val-card" data-anim><div class="vi">🚀</div><h3>Built for India</h3><p>Designed for Indian roads and schools.</p></div><div class="val-card" data-anim><div class="vi">💡</div><h3>Always Improving</h3><p>Weekly updates based on real feedback.</p></div></div></div></section>
  <section class="section"><div class="container"><div class="sec-hd"><div class="sec-badge">Team</div><h2 class="sec-title">People behind ZUVO</h2></div><div class="team-grid"><div class="team-card" data-anim><div class="team-av" style="background:linear-gradient(135deg,#2563eb,#7c3aed)">AV</div><h3>Arjun Verma</h3><span>CEO &amp; Co-Founder</span><p>Former product lead at Ola. Parent. Passionate about safety.</p></div><div class="team-card" data-anim><div class="team-av" style="background:linear-gradient(135deg,#7c3aed,#db2777)">PG</div><h3>Priya Gupta</h3><span>CTO &amp; Co-Founder</span><p>Ex-Google engineer. Real-time systems at scale.</p></div><div class="team-card" data-anim><div class="team-av" style="background:linear-gradient(135deg,#059669,#0891b2)">RS</div><h3>Rahul Sharma</h3><span>Head of Design</span><p>Obsessed with simplicity. Great UX saves lives.</p></div></div></div></section>
  <section class="cta-section"><div class="cta-glow"></div><div class="container"><h2 class="cta-title">Join the ZUVO family</h2><p class="cta-sub">Make school transport safer for every child.</p><div class="cta-btns"><a href="../admin/index.html" class="btn-cta-p">Get Started Free</a><a href="#" class="btn-cta-g" onclick="showPage('contact');return false">Contact Us →</a></div></div></section>
  <footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none"><p>© 2026 ZUVO Technologies Pvt. Ltd.</p><p><a href="#" onclick="showPage('home');return false" style="color:#94a3b8">← Home</a></p></div></div></footer>
</div>

<!-- ======= PRICING PAGE ======= -->
<div class="page" id="page-pricing">
  <section class="page-hero"><div class="page-hero-glow"></div><div class="container"><div class="sec-badge" style="margin-bottom:16px">Pricing</div><h1 class="page-hero-title">Simple, <span class="gradient-text">transparent</span> pricing</h1><p class="page-hero-sub">Start free. Scale as you grow. No hidden fees.</p>
  <div class="billing-toggle"><span class="btl active" id="btl-m" onclick="setBilling('m')">Monthly</span><div class="bts" onclick="toggleBilling()"><div class="btt" id="btt"></div></div><span class="btl" id="btl-y" onclick="setBilling('y')">Yearly <span class="save-tag">Save 20%</span></span></div>
  </div></section>
  <section class="section" style="padding-top:32px"><div class="container">
    <div class="pricing-grid">
      <div class="pc" data-anim><div class="pc-ico" style="background:#f1f5f9"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div><h3>Free Trial</h3><div class="pc-price"><span class="pcc">₹</span><span class="pca" data-m="0" data-y="0">0</span><span class="pcp">/mo</span></div><p class="pcd">Perfect to explore ZUVO</p><ul class="pcf"><li><span class="fy">✓</span>5 Vehicles</li><li><span class="fy">✓</span>5 Drivers</li><li><span class="fy">✓</span>200 Students</li><li><span class="fy">✓</span>Basic Tracking</li><li><span class="fn">✗</span>Analytics</li><li><span class="fn">✗</span>Priority Support</li></ul><a href="../admin/index.html" class="pc-btn ghost">Start Free</a></div>
      <div class="pc popular" data-anim><div class="pop-tag">Most Popular</div><div class="pc-ico" style="background:#eff6ff"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div><h3>Basic</h3><div class="pc-price"><span class="pcc">₹</span><span class="pca" data-m="499" data-y="4790">499</span><span class="pcp">/mo</span></div><p class="pcd">For growing schools</p><ul class="pcf"><li><span class="fy">✓</span>10 Vehicles</li><li><span class="fy">✓</span>10 Drivers</li><li><span class="fy">✓</span>500 Students</li><li><span class="fy">✓</span>Real-Time GPS</li><li><span class="fy">✓</span>Push Alerts</li><li><span class="fn">✗</span>Priority Support</li></ul><a href="../admin/index.html" class="pc-btn primary">Get Started</a></div>
      <div class="pc" data-anim><div class="pc-ico" style="background:#f5f3ff"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div><h3>Pro</h3><div class="pc-price"><span class="pcc">₹</span><span class="pca" data-m="899" data-y="8630">899</span><span class="pcp">/mo</span></div><p class="pcd">For large schools</p><ul class="pcf"><li><span class="fy">✓</span>50 Vehicles</li><li><span class="fy">✓</span>Unlimited Drivers</li><li><span class="fy">✓</span>Unlimited Students</li><li><span class="fy">✓</span>Advanced Analytics</li><li><span class="fy">✓</span>SOS Alerts</li><li><span class="fy">✓</span>Priority Support</li></ul><a href="../admin/index.html" class="pc-btn purple">Get Started</a></div>
      <div class="pc ent" data-anim><div class="pc-ico" style="background:#ecfdf5"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div><h3>Enterprise</h3><div class="pc-price" style="margin-bottom:8px"><span class="pca" style="font-size:1.8rem">Custom</span></div><p class="pcd">School chains &amp; districts</p><ul class="pcf"><li><span class="fy">✓</span>Unlimited Everything</li><li><span class="fy">✓</span>Custom Branding</li><li><span class="fy">✓</span>Dedicated Manager</li><li><span class="fy">✓</span>SLA Guarantee</li><li><span class="fy">✓</span>API Access</li><li><span class="fy">✓</span>24/7 Support</li></ul><a href="#" class="pc-btn green" onclick="showPage('contact');return false">Contact Sales</a></div>
    </div>
    <div class="faq-sec" data-anim>
      <h2 style="text-align:center;font-size:1.6rem;font-weight:800;color:#0f172a;margin-bottom:32px">Frequently Asked Questions</h2>
      <div class="faq-list">
        <div class="faq-item"><button class="fq" onclick="toggleFaq(this)">Can I switch plans later?<span class="fi">+</span></button><div class="fa">Yes! Upgrade or downgrade anytime from Admin Dashboard. Billing is prorated.</div></div>
        <div class="faq-item"><button class="fq" onclick="toggleFaq(this)">Is there a free trial?<span class="fi">+</span></button><div class="fa">Yes! All new accounts get 14 days free with Pro features. No credit card required.</div></div>
        <div class="faq-item"><button class="fq" onclick="toggleFaq(this)">How does billing work?<span class="fi">+</span></button><div class="fa">Payments via Razorpay in INR. Monthly or yearly billing. GST invoices for all paid plans.</div></div>
        <div class="faq-item"><button class="fq" onclick="toggleFaq(this)">Is my data secure?<span class="fi">+</span></button><div class="fa">All data encrypted in transit and at rest. We comply with India's Digital Personal Data Protection Act 2023.</div></div>
        <div class="faq-item"><button class="fq" onclick="toggleFaq(this)">What payment methods?<span class="fi">+</span></button><div class="fa">Credit/debit cards, UPI, net banking, and wallets via Razorpay.</div></div>
      </div>
    </div>
  </div></section>
  <footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none"><p>© 2026 ZUVO Technologies Pvt. Ltd.</p><p><a href="#" onclick="showPage('home');return false" style="color:#94a3b8">← Home</a></p></div></div></footer>
</div>

<!-- ======= CONTACT PAGE ======= -->
<div class="page" id="page-contact">
  <section class="page-hero"><div class="page-hero-glow"></div><div class="container"><div class="sec-badge" style="margin-bottom:16px">Contact &amp; Help</div><h1 class="page-hero-title">We're here to <span class="gradient-text">help you</span></h1><p class="page-hero-sub">Our team responds within 2 hours on business days.</p></div></section>
  <section class="section" style="padding-top:32px"><div class="container">
    <div class="contact-grid">
      <div class="cfc" data-anim>
        <h2>Send us a message</h2>
        <p style="color:#64748b;margin-bottom:24px">Fill this form and we'll get back within 2-4 hours.</p>
        <form id="contactForm" onsubmit="handleContact(event)">
          <div class="cf-row"><div class="cfg"><label>Full Name *</label><input type="text" placeholder="Arjun Sharma" required /></div><div class="cfg"><label>Email *</label><input type="email" placeholder="arjun@school.com" required /></div></div>
          <div class="cfg"><label>Phone</label><input type="tel" placeholder="+91 98765 43210" /></div>
          <div class="cfg"><label>Inquiry Type *</label><select required><option value="">Select type</option><option>General Question</option><option>Sales / Pricing</option><option>Technical Support</option><option>Billing</option><option>Partnership</option></select></div>
          <div class="cfg"><label>School Name</label><input type="text" placeholder="Sunrise Academy" /></div>
          <div class="cfg"><label>Message *</label><textarea rows="5" placeholder="How can we help you?" required></textarea></div>
          <button type="submit" class="btn-submit">Send Message →</button>
        </form>
        <div id="cSuccess" style="display:none" class="success-msg"><div style="font-size:3rem;margin-bottom:16px">✅</div><h3>Message Sent!</h3><p>We'll get back within 2-4 hours.</p></div>
      </div>
      <div class="cic" data-anim>
        <div class="ci-card"><div class="ci-i">📧</div><div><h4>Email Us</h4><p>support@zuvo.app</p><span>~2 hour response</span></div></div>
        <div class="ci-card"><div class="ci-i">📞</div><div><h4>Call Us</h4><p>+91 98765 43210</p><span>Mon-Sat, 9AM-6PM IST</span></div></div>
        <div class="ci-card"><div class="ci-i">💬</div><div><h4>WhatsApp</h4><p>+91 98765 43210</p><span>Quick responses</span></div></div>
        <div class="ci-card"><div class="ci-i">🏢</div><div><h4>Office</h4><p>91Springboard, Koramangala</p><span>Bengaluru, KA 560034</span></div></div>
        <div class="help-links"><h3>Quick Help</h3><a href="#" class="hl"><span>📖</span><div><strong>Documentation</strong><small>Setup guides &amp; tutorials</small></div></a><a href="#" class="hl"><span>🎥</span><div><strong>Video Tutorials</strong><small>Step-by-step walkthroughs</small></div></a><a href="#" class="hl"><span>❓</span><div><strong>FAQ</strong><small>Common questions</small></div></a><a href="#" class="hl"><span>🐛</span><div><strong>Report Bug</strong><small>Help us improve</small></div></a></div>
      </div>
    </div>
  </div></section>
  <footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none"><p>© 2026 ZUVO Technologies Pvt. Ltd.</p><p><a href="#" onclick="showPage('home');return false" style="color:#94a3b8">← Home</a></p></div></div></footer>
</div>

<!-- ======= LEGAL PAGE ======= -->
<div class="page" id="page-legal">
  <section class="page-hero" style="padding:80px 0 50px"><div class="page-hero-glow"></div><div class="container"><div class="sec-badge" style="margin-bottom:16px">Legal</div><h1 class="page-hero-title">Terms &amp; <span class="gradient-text">Privacy</span></h1><p class="page-hero-sub">Last updated: September 25, 2026</p></div></section>
  <section class="section" style="padding-top:32px"><div class="container"><div class="legal-layout">
    <div class="ltoc">
      <h4>Contents</h4>
      <a href="#" onclick="scrollLegal('tos')">Terms of Service</a>
      <a href="#" onclick="scrollLegal('privacy')">Privacy Policy</a>
      <a href="#" onclick="scrollLegal('cookies')">Cookie Policy</a>
      <a href="#" onclick="scrollLegal('data')">Data Processing</a>
      <a href="#" onclick="scrollLegal('liability')">Liability</a>
    </div>
    <div class="lbody">
      <div id="ls-tos" class="ls"><h2>Terms of Service</h2><p>By accessing ZUVO, you agree to these Terms. If using on behalf of a school, you confirm you have authority to bind the organization.</p><h3>1. Acceptance</h3><p>By creating an account or using ZUVO, you confirm you are 18+, have legal authority, and agree to comply with these Terms.</p><h3>2. Service Description</h3><p>ZUVO provides school bus tracking, fleet management, admin dashboard, mobile apps for parents/drivers, and real-time GPS tracking.</p><h3>3. User Accounts</h3><p>You are responsible for securing your credentials. Notify us at support@zuvo.app of any unauthorized access.</p><h3>4. Acceptable Use</h3><p>You agree not to use the Service for unlawful purposes, attempt unauthorized access, or transmit harmful content.</p><h3>5. Payment</h3><p>Paid plans billed in advance monthly or annually via Razorpay in INR. GST invoices provided for all paid plans.</p><h3>6. Termination</h3><p>ZUVO may suspend accounts for Terms violations or non-payment. You may cancel anytime from Admin Dashboard.</p><h3>7. Changes</h3><p>We'll provide 30 days notice for material changes. Continued use constitutes acceptance.</p></div>
      <div id="ls-privacy" class="ls"><h2>Privacy Policy</h2><p>ZUVO Technologies Pvt. Ltd. is committed to protecting privacy of students, parents, admins, and drivers.</p><h3>1. Data We Collect</h3><p><strong>Account:</strong> Name, email, phone, school name, role.<br/><strong>Location:</strong> GPS from drivers only during active trips.<br/><strong>Student data:</strong> Name, grade, home location, parent contacts  provided by school admins.<br/><strong>Usage:</strong> App interactions and crash reports.</p><h3>2. How We Use It</h3><p>To provide the Service, send trip notifications, process payments, respond to support, and improve features.</p><h3>3. Data Sharing</h3><p>We do NOT sell your data. Shared only with service providers (Razorpay, AWS, Firebase) under strict agreements, or when legally required.</p><h3>4. Retention</h3><p>Personal data deleted within 30 days of account deletion. GPS logs within 90 days.</p><h3>5. Your Rights</h3><p>Access, correct, or delete your data at any time. Contact privacy@zuvo.app.</p></div>
      <div id="ls-cookies" class="ls"><h2>Cookie Policy</h2><p>We use cookies to enhance your experience. <strong>Essential cookies</strong> (authentication, security) cannot be disabled. <strong>Analytics cookies</strong> track usage and can be disabled. <strong>Preference cookies</strong> remember your settings. Manage via browser settings.</p></div>
      <div id="ls-data" class="ls"><h2>Data Processing Agreement</h2><p>For schools sharing student data with ZUVO, we act as a data processor. Your school is the data controller responsible for the legal basis to share this information. We process data per your instructions and in accordance with India's Digital Personal Data Protection Act, 2023.</p></div>
      <div id="ls-liability" class="ls"><h2>Limitation of Liability</h2><p>ZUVO's total liability shall not exceed the amount you paid us in the prior 12 months. We are not liable for indirect, incidental, or consequential damages. The Service is provided "as is"  we strive for 99.9% uptime. Contact: legal@zuvo.app</p></div>
    </div>
  </div></div></section>
  <footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none"><p>© 2026 ZUVO Technologies Pvt. Ltd.</p><p><a href="#" onclick="showPage('home');return false" style="color:#94a3b8">← Home</a></p></div></div></footer>
</div>

<!-- ======= REFUND PAGE ======= -->
<div class="page" id="page-refund">
  <section class="page-hero" style="padding:80px 0 50px"><div class="page-hero-glow"></div><div class="container"><div class="sec-badge" style="margin-bottom:16px">Refund Policy</div><h1 class="page-hero-title">Fair &amp; <span class="gradient-text">Transparent</span> Refunds</h1><p class="page-hero-sub">Last updated: September 25, 2026</p></div></section>
  <section class="section" style="padding-top:32px"><div class="container" style="max-width:820px">
    <div class="refund-hl" data-anim>
      <div class="rh"><span class="rhi">✅</span><strong>14-Day Guarantee</strong><p>Full refund within 14 days of first payment</p></div>
      <div class="rh"><span class="rhi">⚡</span><strong>Fast Processing</strong><p>5-7 business days to your account</p></div>
      <div class="rh"><span class="rhi">💳</span><strong>Original Method</strong><p>Refunds to your original payment method</p></div>
    </div>
    <div class="lbody" style="max-width:100%" data-anim>
      <div class="ls">
        <h2>Refund Policy</h2>
        <p>At ZUVO, we stand behind our product. If you're not satisfied, we want to make it right.</p>
        <h3>1. 14-Day Money-Back Guarantee</h3>
        <p>If you purchased a paid subscription and are unsatisfied, request a full refund within <strong>14 calendar days</strong> of your initial payment. No questions asked. Applies to first-time purchases only  not renewals.</p>
        <h3>2. Eligibility</h3>
        <p>Within 14 days of first payment, account in good standing, refund requested via billing@zuvo.app or Admin Dashboard.</p>
        <h3>3. Non-Refundable</h3>
        <ul class="legal-list"><li>Subscription renewals (cancel before renewal date)</li><li>Partial months beyond the 14-day window</li><li>Accounts terminated for Terms violations</li><li>Purchases older than 14 days</li><li>Free trial accounts</li></ul>
        <h3>4. How to Request</h3>
        <div class="refund-steps">
          <div class="rs"><div class="rsn">1</div><div><strong>Email billing@zuvo.app</strong><p>Subject: "Refund Request  [School Name]"</p></div></div>
          <div class="rs"><div class="rsn">2</div><div><strong>Include details</strong><p>Registered email, plan name, payment date, and reason (optional).</p></div></div>
          <div class="rs"><div class="rsn">3</div><div><strong>Confirmation in 24 hours</strong><p>Our billing team reviews and confirms eligibility.</p></div></div>
          <div class="rs"><div class="rsn">4</div><div><strong>Receive refund in 5-7 days</strong><p>To your original payment method (card, UPI, etc.).</p></div></div>
        </div>
        <h3>5. Cancellation</h3>
        <p>Cancel anytime from Admin Dashboard. Access continues until end of billing period. No refund after 14-day window.</p>
        <h3>6. Annual Plans</h3>
        <p>14-day guarantee applies from date of first payment. After 14 days, no refund but access continues until annual period ends.</p>
        <h3>7. Contact</h3>
        <p>📧 billing@zuvo.app &nbsp;&nbsp; 📞 +91 98765 43210 &nbsp;&nbsp; 💬 WhatsApp: +91 98765 43210</p>
      </div>
    </div>
  </div></section>
  <footer class="footer"><div class="container"><div class="footer-bottom" style="border-top:none"><p>© 2026 ZUVO Technologies Pvt. Ltd.</p><p><a href="#" onclick="showPage('home');return false" style="color:#94a3b8">← Home</a></p></div></div></footer>
</div>

<script src="script.js"></script>
</body>
</html>"""

with open(r"e:\Bus Tracking App\website\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
