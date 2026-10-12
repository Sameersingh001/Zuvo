
import os

base = r"e:\Bus Tracking App\website"

# ─── style.css ───────────────────────────────────────────────
css = r"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: 'Inter', sans-serif; background: #fff; color: #1e293b; line-height: 1.6; overflow-x: hidden; }
a { text-decoration: none; color: inherit; }
button { cursor: pointer; font-family: inherit; }
input, textarea, select { font-family: inherit; }

/* PAGES */
.page { display: none; }
.page.active { display: block; }

/* CONTAINER */
.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }

/* ─── NAVBAR ─── */
.nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.92); backdrop-filter: blur(20px); border-bottom: 1px solid #f1f5f9; transition: all 0.3s; }
.nav.scrolled { box-shadow: 0 4px 24px rgba(0,0,0,0.08); }
.nav-inner { display: flex; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 24px; height: 68px; gap: 40px; }
.nav-logo { display: flex; align-items: center; gap: 10px; font-weight: 800; font-size: 1.2rem; color: #0f172a; }
.nav-logo-icon { width: 36px; height: 36px; background: #2563eb; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #fff; flex-shrink: 0; }
.nav-logo-text { font-weight: 900; letter-spacing: -0.5px; }
.nav-links { display: flex; gap: 4px; flex: 1; }
.nav-link { padding: 7px 14px; border-radius: 8px; font-size: 0.9rem; font-weight: 500; color: #475569; transition: all 0.2s; }
.nav-link:hover { background: #f1f5f9; color: #0f172a; }
.nav-actions { display: flex; gap: 10px; align-items: center; margin-left: auto; }
.btn-ghost { padding: 8px 18px; border-radius: 9px; font-size: 0.875rem; font-weight: 600; color: #475569; border: 1.5px solid #e2e8f0; transition: all 0.2s; }
.btn-ghost:hover { border-color: #2563eb; color: #2563eb; }
.btn-primary { padding: 9px 20px; border-radius: 9px; font-size: 0.875rem; font-weight: 600; background: #2563eb; color: #fff; transition: all 0.2s; }
.btn-primary:hover { background: #1d4ed8; transform: translateY(-1px); box-shadow: 0 4px 14px rgba(37,99,235,0.35); }
.hamburger { display: none; flex-direction: column; gap: 5px; background: none; border: none; padding: 6px; }
.hamburger span { display: block; width: 22px; height: 2px; background: #334155; border-radius: 2px; transition: all 0.3s; }

/* ─── HERO ─── */
.hero { min-height: 100vh; padding: 120px 0 80px; position: relative; overflow: hidden; background: linear-gradient(135deg, #f8faff 0%, #f0f4ff 50%, #faf5ff 100%); display: flex; align-items: center; }
.hero-blob { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.35; pointer-events: none; }
.b1 { width: 600px; height: 600px; background: radial-gradient(circle, #bfdbfe, #ddd6fe); top: -100px; right: -100px; animation: blobFloat 8s ease-in-out infinite; }
.b2 { width: 500px; height: 500px; background: radial-gradient(circle, #bbf7d0, #bfdbfe); bottom: -100px; left: -100px; animation: blobFloat 10s ease-in-out infinite reverse; }
@keyframes blobFloat { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(30px,-30px) scale(1.05)} }
.hero-container { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; position: relative; z-index: 1; }
.hero-content { max-width: 560px; }
.hero-badge { display: inline-flex; align-items: center; gap: 8px; background: #fff; border: 1.5px solid #dbeafe; color: #2563eb; font-size: 0.82rem; font-weight: 600; padding: 7px 14px; border-radius: 99px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(37,99,235,0.1); }
.badge-dot { width: 8px; height: 8px; border-radius: 50%; background: #22c55e; animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.7;transform:scale(1.2)} }
.hero-title { font-size: clamp(2.5rem, 5vw, 3.8rem); font-weight: 900; color: #0f172a; line-height: 1.1; letter-spacing: -2px; margin-bottom: 24px; }
.gradient-text { background: linear-gradient(135deg, #2563eb, #7c3aed, #db2777); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-sub { font-size: 1.05rem; color: #475569; line-height: 1.75; margin-bottom: 36px; max-width: 460px; }
.hero-cta { display: flex; gap: 14px; margin-bottom: 48px; flex-wrap: wrap; }
.btn-hp { display: inline-flex; align-items: center; gap: 8px; padding: 14px 28px; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #fff; border-radius: 12px; font-weight: 700; font-size: 0.95rem; transition: all 0.3s; box-shadow: 0 6px 24px rgba(37,99,235,0.35); }
.btn-hp:hover { transform: translateY(-2px); box-shadow: 0 10px 32px rgba(37,99,235,0.45); }
.btn-hg { display: inline-flex; align-items: center; gap: 6px; padding: 14px 24px; color: #475569; border: 2px solid #e2e8f0; border-radius: 12px; font-weight: 600; font-size: 0.95rem; transition: all 0.2s; background: #fff; }
.btn-hg:hover { border-color: #2563eb; color: #2563eb; background: #eff6ff; }
.hero-trust { display: flex; align-items: center; gap: 24px; }
.ti { display: flex; flex-direction: column; }
.tn { font-size: 1.5rem; font-weight: 800; color: #0f172a; }
.ti span:last-child { font-size: 0.78rem; color: #94a3b8; font-weight: 500; }
.td { width: 1px; height: 36px; background: #e2e8f0; }

/* Hero Card */
.hero-card-wrap { position: relative; display: flex; justify-content: center; }
.hero-card { background: #fff; border-radius: 20px; box-shadow: 0 24px 80px rgba(15,23,42,0.15); padding: 20px; width: 320px; border: 1px solid rgba(255,255,255,0.8); }
.animate-float { animation: float 4s ease-in-out infinite; }
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
.hc-head { display: flex; align-items: center; gap: 8px; margin-bottom: 14px; font-size: 0.78rem; font-weight: 600; color: #334155; }
.hc-dot { width: 8px; height: 8px; border-radius: 50%; background: #22c55e; box-shadow: 0 0 0 3px rgba(34,197,94,0.2); animation: pulse 2s ease-in-out infinite; }
.hc-time { margin-left: auto; color: #94a3b8; font-weight: 400; }
.hc-map { height: 120px; background: linear-gradient(135deg, #f0f9ff, #e0f2fe); border-radius: 12px; position: relative; overflow: hidden; margin-bottom: 14px; }
.hc-road { position: absolute; background: rgba(148,163,184,0.3); border-radius: 2px; }
.hcr1 { width: 100%; height: 2px; top: 40%; left: 0; }
.hcr2 { width: 2px; height: 100%; left: 35%; top: 0; }
.hc-pin { position: absolute; display: flex; align-items: center; justify-content: center; border-radius: 50%; }
.bus-pin { width: 32px; height: 32px; background: #2563eb; top: 28%; left: 25%; box-shadow: 0 4px 14px rgba(37,99,235,0.4); animation: busMove 4s ease-in-out infinite; }
@keyframes busMove { 0%,100%{left:25%} 50%{left:45%} }
.dest-pin { font-size: 1.2rem; top: 20%; right: 15%; }
.hc-stats { display: flex; justify-content: space-around; margin-bottom: 12px; padding: 10px; background: #f8fafc; border-radius: 10px; }
.hc-s { display: flex; flex-direction: column; align-items: center; }
.hc-s span { font-size: 0.68rem; color: #94a3b8; margin-bottom: 2px; }
.hc-s strong { font-size: 0.82rem; color: #1e293b; font-weight: 700; }
.hc-alert { display: flex; align-items: center; gap: 8px; padding: 10px 12px; background: linear-gradient(135deg, #eff6ff, #f0fdf4); border-radius: 10px; font-size: 0.75rem; color: #334155; font-weight: 500; }

/* ─── SECTIONS ─── */
.section { padding: 96px 0; }
.steps-section { background: linear-gradient(135deg, #f8fafc, #f0f4ff); }
.sec-hd { text-align: center; margin-bottom: 64px; }
.sec-badge { display: inline-block; background: #eff6ff; color: #2563eb; font-size: 0.78rem; font-weight: 700; padding: 6px 16px; border-radius: 99px; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 16px; }
.sec-title { font-size: clamp(1.9rem, 4vw, 2.8rem); font-weight: 800; color: #0f172a; letter-spacing: -1.5px; line-height: 1.2; margin-bottom: 16px; }
.sec-sub { font-size: 1rem; color: #64748b; max-width: 520px; margin: 0 auto; }

/* Features Grid */
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.feat-card { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 16px; padding: 28px 24px; transition: all 0.3s; }
.feat-card:hover { transform: translateY(-6px); box-shadow: 0 20px 48px rgba(15,23,42,0.1); border-color: transparent; }
.feat-icon { width: 48px; height: 48px; border-radius: 12px; background: var(--cb); color: var(--c); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.feat-card h3 { font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
.feat-card p { font-size: 0.875rem; color: #64748b; line-height: 1.65; }

/* Steps */
.steps-wrap { display: flex; align-items: flex-start; gap: 0; justify-content: center; flex-wrap: wrap; }
.step-card { background: #fff; border-radius: 16px; padding: 28px 24px; text-align: center; width: 200px; box-shadow: 0 4px 20px rgba(15,23,42,0.06); border: 1.5px solid #f1f5f9; flex-shrink: 0; }
.step-num { font-size: 2.5rem; font-weight: 900; color: #dbeafe; letter-spacing: -2px; line-height: 1; margin-bottom: 12px; }
.step-card h3 { font-size: 0.95rem; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
.step-card p { font-size: 0.8rem; color: #94a3b8; line-height: 1.55; }
.step-arr { font-size: 1.5rem; color: #cbd5e1; align-self: center; padding: 0 12px; flex-shrink: 0; }

/* Testimonials */
.test-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.test-card { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 16px; padding: 28px; transition: all 0.3s; }
.test-card:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(15,23,42,0.09); }
.stars { color: #f59e0b; font-size: 1rem; margin-bottom: 14px; letter-spacing: 2px; }
.test-card p { font-size: 0.88rem; color: #475569; line-height: 1.7; margin-bottom: 20px; }
.test-author { display: flex; align-items: center; gap: 12px; }
.ta { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; flex-shrink: 0; }
.test-author strong { display: block; font-size: 0.875rem; font-weight: 700; color: #0f172a; }
.test-author span { display: block; font-size: 0.75rem; color: #94a3b8; }

/* CTA Section */
.cta-section { background: linear-gradient(135deg, #0f172a, #1e293b); padding: 96px 0; text-align: center; position: relative; overflow: hidden; }
.cta-glow { position: absolute; width: 600px; height: 600px; background: radial-gradient(circle, rgba(37,99,235,0.3), transparent); top: 50%; left: 50%; transform: translate(-50%,-50%); pointer-events: none; }
.cta-title { font-size: clamp(2rem, 4vw, 3rem); font-weight: 900; color: #fff; letter-spacing: -1.5px; margin-bottom: 16px; position: relative; }
.cta-sub { font-size: 1rem; color: #94a3b8; margin-bottom: 40px; position: relative; }
.cta-btns { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; position: relative; }
.btn-cta-p { padding: 15px 32px; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #fff; border-radius: 12px; font-weight: 700; font-size: 1rem; transition: all 0.3s; box-shadow: 0 8px 24px rgba(37,99,235,0.4); }
.btn-cta-p:hover { transform: translateY(-2px); box-shadow: 0 14px 36px rgba(37,99,235,0.5); }
.btn-cta-g { padding: 15px 28px; color: #94a3b8; border: 2px solid rgba(255,255,255,0.2); border-radius: 12px; font-weight: 600; font-size: 1rem; transition: all 0.2s; }
.btn-cta-g:hover { border-color: #fff; color: #fff; }

/* Footer */
.footer { background: #0f172a; padding: 72px 0 32px; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 48px; }
.footer-logo { display: flex; align-items: center; gap: 10px; font-weight: 900; color: #fff; font-size: 1.1rem; margin-bottom: 14px; }
.footer-logo svg { background: #2563eb; border-radius: 8px; padding: 4px; }
.footer-brand p { font-size: 0.875rem; color: #64748b; line-height: 1.65; max-width: 220px; }
.footer-social { display: flex; gap: 10px; margin-top: 20px; }
.footer-social a { width: 34px; height: 34px; border-radius: 8px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 0.8rem; color: #94a3b8; transition: all 0.2s; }
.footer-social a:hover { background: rgba(255,255,255,0.12); color: #fff; }
.footer-col h4 { font-size: 0.8rem; font-weight: 700; color: #cbd5e1; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 16px; }
.footer-col a { display: block; font-size: 0.875rem; color: #64748b; margin-bottom: 10px; transition: color 0.2s; }
.footer-col a:hover { color: #fff; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.06); padding-top: 28px; display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: #475569; flex-wrap: wrap; gap: 8px; }

/* ─── PAGE HERO ─── */
.page-hero { padding: 120px 0 80px; background: linear-gradient(135deg, #f8faff, #f0f4ff); position: relative; overflow: hidden; }
.page-hero-glow { position: absolute; width: 600px; height: 600px; background: radial-gradient(circle, rgba(37,99,235,0.12), transparent); top: 50%; left: 50%; transform: translate(-50%,-50%); pointer-events: none; }
.page-hero-title { font-size: clamp(2.2rem, 5vw, 3.5rem); font-weight: 900; color: #0f172a; letter-spacing: -2px; line-height: 1.15; margin-bottom: 16px; }
.page-hero-sub { font-size: 1rem; color: #64748b; max-width: 560px; }

/* ─── ABOUT ─── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
.about-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.asc { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 16px; padding: 24px; text-align: center; transition: all 0.3s; }
.asc:hover { transform: translateY(-4px); box-shadow: 0 12px 32px rgba(15,23,42,0.08); }
.asc-n { display: block; font-size: 2rem; font-weight: 900; letter-spacing: -1px; margin-bottom: 4px; }
.asc span:last-child { font-size: 0.8rem; color: #94a3b8; font-weight: 500; }
.values-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.val-card { background: #fff; border-radius: 16px; padding: 28px 20px; text-align: center; transition: all 0.3s; box-shadow: 0 2px 8px rgba(15,23,42,0.04); }
.val-card:hover { transform: translateY(-6px); box-shadow: 0 16px 40px rgba(15,23,42,0.1); }
.vi { font-size: 2.5rem; margin-bottom: 14px; }
.val-card h3 { font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
.val-card p { font-size: 0.85rem; color: #64748b; line-height: 1.65; }
.team-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.team-card { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 20px; padding: 32px 24px; text-align: center; transition: all 0.3s; }
.team-card:hover { transform: translateY(-6px); box-shadow: 0 20px 48px rgba(15,23,42,0.1); }
.team-av { width: 72px; height: 72px; border-radius: 50%; margin: 0 auto 18px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: 800; color: #fff; }
.team-card h3 { font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: 4px; }
.team-card span { display: block; font-size: 0.78rem; color: #2563eb; font-weight: 600; margin-bottom: 10px; }
.team-card p { font-size: 0.82rem; color: #64748b; line-height: 1.65; }

/* ─── PRICING ─── */
.billing-toggle { display: flex; align-items: center; gap: 14px; justify-content: center; margin-top: 32px; }
.btl { font-size: 0.9rem; font-weight: 600; color: #94a3b8; cursor: pointer; transition: color 0.2s; }
.btl.active { color: #0f172a; }
.bts { width: 44px; height: 24px; background: #e2e8f0; border-radius: 99px; position: relative; cursor: pointer; transition: background 0.3s; }
.bts.on { background: #2563eb; }
.btt { width: 18px; height: 18px; background: #fff; border-radius: 50%; position: absolute; top: 3px; left: 3px; transition: left 0.3s; box-shadow: 0 1px 4px rgba(0,0,0,0.2); }
.btt.on { left: 23px; }
.save-tag { background: #dcfce7; color: #16a34a; font-size: 0.7rem; padding: 2px 7px; border-radius: 99px; margin-left: 4px; font-weight: 700; }
.pricing-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 72px; }
.pc { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 20px; padding: 28px 24px; position: relative; transition: all 0.3s; }
.pc:hover { transform: translateY(-6px); box-shadow: 0 24px 56px rgba(15,23,42,0.12); }
.pc.popular { border-color: #2563eb; box-shadow: 0 8px 32px rgba(37,99,235,0.15); transform: scale(1.02); }
.pc.ent { border-color: #059669; }
.pop-tag { position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #2563eb; color: #fff; font-size: 0.72rem; font-weight: 700; padding: 4px 14px; border-radius: 99px; white-space: nowrap; }
.pc-ico { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.pc h3 { font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 8px; }
.pc-price { display: flex; align-items: baseline; gap: 2px; margin-bottom: 6px; }
.pcc { font-size: 1.2rem; font-weight: 700; color: #475569; }
.pca { font-size: 2.4rem; font-weight: 900; color: #0f172a; letter-spacing: -2px; line-height: 1; }
.pcp { font-size: 0.85rem; color: #94a3b8; margin-left: 2px; }
.pcd { font-size: 0.82rem; color: #64748b; margin-bottom: 20px; min-height: 38px; }
.pcf { list-style: none; margin-bottom: 24px; display: flex; flex-direction: column; gap: 9px; }
.pcf li { display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #334155; }
.fy { color: #22c55e; font-weight: 700; font-size: 0.9rem; }
.fn { color: #e2e8f0; font-weight: 700; }
.pc-btn { display: block; text-align: center; padding: 12px; border-radius: 10px; font-weight: 700; font-size: 0.875rem; transition: all 0.2s; margin-top: auto; }
.pc-btn.ghost { border: 2px solid #e2e8f0; color: #475569; }
.pc-btn.ghost:hover { border-color: #2563eb; color: #2563eb; }
.pc-btn.primary { background: linear-gradient(135deg, #2563eb, #3b82f6); color: #fff; box-shadow: 0 4px 14px rgba(37,99,235,0.3); }
.pc-btn.primary:hover { box-shadow: 0 8px 24px rgba(37,99,235,0.45); }
.pc-btn.purple { background: linear-gradient(135deg, #7c3aed, #8b5cf6); color: #fff; box-shadow: 0 4px 14px rgba(124,58,237,0.3); }
.pc-btn.purple:hover { box-shadow: 0 8px 24px rgba(124,58,237,0.45); }
.pc-btn.green { background: linear-gradient(135deg, #059669, #10b981); color: #fff; box-shadow: 0 4px 14px rgba(5,150,105,0.3); }
.pc-btn.green:hover { box-shadow: 0 8px 24px rgba(5,150,105,0.45); }

/* FAQ */
.faq-sec { max-width: 720px; margin: 0 auto; }
.faq-list { display: flex; flex-direction: column; gap: 12px; }
.faq-item { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 12px; overflow: hidden; }
.fq { display: flex; justify-content: space-between; align-items: center; padding: 18px 20px; font-weight: 600; font-size: 0.9rem; color: #1e293b; background: none; border: none; width: 100%; text-align: left; transition: all 0.2s; }
.fq:hover { background: #f8fafc; }
.fi { font-size: 1.3rem; color: #94a3b8; transition: transform 0.2s; flex-shrink: 0; }
.fa { padding: 0 20px 18px; font-size: 0.875rem; color: #64748b; line-height: 1.7; display: none; }
.fa.open { display: block; }
.fi.open { transform: rotate(45deg); }

/* ─── CONTACT ─── */
.contact-grid { display: grid; grid-template-columns: 3fr 2fr; gap: 48px; align-items: start; }
.cfc { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 20px; padding: 36px 32px; }
.cfc h2 { font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-bottom: 8px; }
.cf-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.cfg { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }
.cfg label { font-size: 0.8rem; font-weight: 600; color: #334155; }
.cfg input, .cfg select, .cfg textarea { padding: 11px 14px; border: 1.5px solid #e2e8f0; border-radius: 10px; font-size: 0.875rem; color: #1e293b; outline: none; transition: all 0.2s; background: #fff; resize: vertical; }
.cfg input:focus, .cfg select:focus, .cfg textarea:focus { border-color: #2563eb; box-shadow: 0 0 0 3px rgba(37,99,235,0.1); }
.btn-submit { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #fff; border: none; border-radius: 12px; font-weight: 700; font-size: 0.95rem; cursor: pointer; transition: all 0.3s; box-shadow: 0 6px 20px rgba(37,99,235,0.3); }
.btn-submit:hover { transform: translateY(-1px); box-shadow: 0 10px 28px rgba(37,99,235,0.4); }
.success-msg { text-align: center; padding: 32px; }
.success-msg h3 { font-size: 1.3rem; font-weight: 800; color: #0f172a; margin-bottom: 8px; }
.success-msg p { color: #64748b; }
.cic { display: flex; flex-direction: column; gap: 16px; }
.ci-card { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 14px; padding: 18px 20px; display: flex; align-items: center; gap: 14px; transition: all 0.2s; }
.ci-card:hover { transform: translateX(4px); border-color: #dbeafe; }
.ci-i { font-size: 1.5rem; flex-shrink: 0; }
.ci-card h4 { font-size: 0.85rem; font-weight: 700; color: #0f172a; margin-bottom: 2px; }
.ci-card p { font-size: 0.875rem; color: #334155; font-weight: 600; }
.ci-card span { font-size: 0.75rem; color: #94a3b8; }
.help-links h3 { font-size: 0.9rem; font-weight: 700; color: #334155; margin-bottom: 12px; }
.help-links { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 14px; padding: 20px; }
.hl { display: flex; align-items: center; gap: 12px; padding: 10px; border-radius: 10px; transition: all 0.2s; margin-bottom: 4px; }
.hl:hover { background: #f8fafc; }
.hl span { font-size: 1.2rem; flex-shrink: 0; }
.hl strong { display: block; font-size: 0.82rem; font-weight: 700; color: #0f172a; }
.hl small { display: block; font-size: 0.75rem; color: #94a3b8; }

/* ─── LEGAL ─── */
.legal-layout { display: grid; grid-template-columns: 220px 1fr; gap: 48px; align-items: start; }
.ltoc { position: sticky; top: 90px; background: #fff; border: 1.5px solid #f1f5f9; border-radius: 16px; padding: 24px; }
.ltoc h4 { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #94a3b8; margin-bottom: 14px; }
.ltoc a { display: block; font-size: 0.875rem; color: #475569; padding: 8px 10px; border-radius: 8px; transition: all 0.2s; margin-bottom: 2px; }
.ltoc a:hover { background: #eff6ff; color: #2563eb; }
.lbody { display: flex; flex-direction: column; gap: 0; }
.ls { margin-bottom: 48px; padding-bottom: 48px; border-bottom: 1px solid #f1f5f9; scroll-margin-top: 90px; }
.ls:last-child { border-bottom: none; }
.ls h2 { font-size: 1.6rem; font-weight: 800; color: #0f172a; margin-bottom: 16px; letter-spacing: -0.5px; }
.ls h3 { font-size: 1rem; font-weight: 700; color: #1e293b; margin: 20px 0 8px; }
.ls p { font-size: 0.9rem; color: #475569; line-height: 1.8; margin-bottom: 12px; }
.legal-list { list-style: disc; padding-left: 24px; margin: 12px 0; color: #475569; line-height: 2.1; font-size: 0.9rem; }

/* ─── REFUND ─── */
.refund-hl { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 48px; }
.rh { background: #fff; border: 1.5px solid #f1f5f9; border-radius: 16px; padding: 28px 24px; text-align: center; }
.rhi { display: block; font-size: 2.5rem; margin-bottom: 12px; }
.rh strong { display: block; font-size: 0.95rem; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
.rh p { font-size: 0.82rem; color: #64748b; }
.refund-steps { display: flex; flex-direction: column; gap: 20px; margin: 20px 0 28px; }
.rs { display: flex; align-items: flex-start; gap: 16px; }
.rsn { width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.875rem; flex-shrink: 0; }
.rs strong { display: block; font-size: 0.9rem; font-weight: 700; color: #0f172a; margin-bottom: 4px; }
.rs p { font-size: 0.85rem; color: #64748b; line-height: 1.6; margin: 0; }

/* ─── ANIMATIONS ─── */
.anim { opacity: 0; transform: translateY(24px); }
.anim.visible { animation: fadeUp 0.7s ease forwards; }
.a1 { animation-delay: 0.05s !important; }
.a2 { animation-delay: 0.15s !important; }
.a3 { animation-delay: 0.25s !important; }
.a4 { animation-delay: 0.35s !important; }
.a5 { animation-delay: 0.45s !important; }
@keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
[data-anim] { opacity: 0; transform: translateY(32px); transition: opacity 0.6s ease, transform 0.6s ease; }
[data-anim].in-view { opacity: 1; transform: translateY(0); }

/* ─── RESPONSIVE ─── */
@media (max-width: 1024px) {
  .features-grid { grid-template-columns: repeat(2, 1fr); }
  .pricing-grid { grid-template-columns: repeat(2, 1fr); }
  .pc.popular { transform: scale(1); }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .values-grid { grid-template-columns: repeat(2, 1fr); }
  .about-grid { grid-template-columns: 1fr; }
  .contact-grid { grid-template-columns: 1fr; }
  .legal-layout { grid-template-columns: 1fr; }
  .ltoc { position: static; }
}
@media (max-width: 768px) {
  .hero-container { grid-template-columns: 1fr; gap: 40px; }
  .hero-card-wrap { justify-content: center; }
  .nav-links { display: none; flex-direction: column; gap: 4px; position: fixed; top: 68px; left: 0; right: 0; background: #fff; padding: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.1); z-index: 999; }
  .nav-links.open { display: flex; }
  .nav-actions { display: none; }
  .hamburger { display: flex; }
  .features-grid { grid-template-columns: 1fr; }
  .test-grid { grid-template-columns: 1fr; }
  .team-grid { grid-template-columns: 1fr; }
  .pricing-grid { grid-template-columns: 1fr; }
  .refund-hl { grid-template-columns: 1fr; }
  .steps-wrap { flex-direction: column; align-items: center; }
  .step-arr { transform: rotate(90deg); }
  .footer-grid { grid-template-columns: 1fr; }
  .cf-row { grid-template-columns: 1fr; }
  .hero-trust { flex-wrap: wrap; gap: 16px; }
  .values-grid { grid-template-columns: repeat(2, 1fr); }
}
"""

# ─── script.js ───────────────────────────────────────────────
js = r"""
// Page switching
function showPage(name) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  const target = document.getElementById('page-' + name);
  if (target) {
    target.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    // Trigger hero anims
    setTimeout(() => {
      target.querySelectorAll('.anim').forEach(el => el.classList.add('visible'));
    }, 80);
    // Update active nav link
    document.querySelectorAll('.nav-link').forEach(a => a.classList.remove('active'));
    document.querySelectorAll('.nav-link').forEach(a => {
      if (a.getAttribute('onclick') && a.getAttribute('onclick').includes("'" + name + "'")) {
        a.classList.add('active');
      }
    });
  }
  closeMenu();
}

// Hamburger menu
function toggleMenu() {
  const links = document.getElementById('navLinks');
  links.classList.toggle('open');
}
function closeMenu() {
  const links = document.getElementById('navLinks');
  links && links.classList.remove('open');
}

// Navbar scroll effect
window.addEventListener('scroll', () => {
  const nav = document.getElementById('navbar');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 20);
});

// Scroll-triggered animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('in-view'), i * 80);
    }
  });
}, { threshold: 0.15 });

function initAnimations() {
  document.querySelectorAll('.page.active [data-anim]').forEach(el => observer.observe(el));
}

// FAQ toggle
function toggleFaq(btn) {
  const item = btn.parentElement;
  const answer = item.querySelector('.fa');
  const icon = btn.querySelector('.fi');
  const isOpen = answer.classList.contains('open');
  // Close all
  document.querySelectorAll('.fa.open').forEach(a => a.classList.remove('open'));
  document.querySelectorAll('.fi.open').forEach(i => i.classList.remove('open'));
  if (!isOpen) {
    answer.classList.add('open');
    icon.classList.add('open');
  }
}

// Pricing toggle
let billingMode = 'm';
function toggleBilling() {
  setBilling(billingMode === 'm' ? 'y' : 'm');
}
function setBilling(mode) {
  billingMode = mode;
  const btt = document.getElementById('btt');
  const bts = document.querySelector('.bts');
  const mLabel = document.getElementById('btl-m');
  const yLabel = document.getElementById('btl-y');
  if (mode === 'y') {
    btt && btt.classList.add('on');
    bts && bts.classList.add('on');
    mLabel && mLabel.classList.remove('active');
    yLabel && yLabel.classList.add('active');
  } else {
    btt && btt.classList.remove('on');
    bts && bts.classList.remove('on');
    mLabel && mLabel.classList.add('active');
    yLabel && yLabel.classList.remove('active');
  }
  // Update prices with animation
  document.querySelectorAll('.pca').forEach(el => {
    const val = mode === 'y' ? el.dataset.y : el.dataset.m;
    if (val !== undefined) {
      el.style.transform = 'scale(0.8)';
      el.style.opacity = '0';
      setTimeout(() => {
        el.textContent = Number(val).toLocaleString('en-IN');
        el.style.transform = 'scale(1)';
        el.style.opacity = '1';
      }, 150);
      el.style.transition = 'all 0.2s ease';
    }
  });
}

// Contact form
function handleContact(e) {
  e.preventDefault();
  const form = document.getElementById('contactForm');
  const success = document.getElementById('cSuccess');
  if (form && success) {
    form.style.display = 'none';
    success.style.display = 'block';
  }
}

// Legal scroll
function scrollLegal(id) {
  const el = document.getElementById('ls-' + id);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Init on load
window.addEventListener('DOMContentLoaded', () => {
  // Trigger hero anims for home
  setTimeout(() => {
    document.querySelectorAll('#page-home .anim').forEach(el => el.classList.add('visible'));
  }, 100);

  // Observe all animations on currently active page
  initAnimations();

  // Re-observe when page changes
  const pagesObserver = new MutationObserver(() => {
    document.querySelectorAll('.page.active [data-anim]:not(.in-view)').forEach(el => observer.observe(el));
  });
  document.querySelectorAll('.page').forEach(p => {
    pagesObserver.observe(p, { attributes: true, attributeFilter: ['class'] });
  });
});
"""

# Write files
with open(os.path.join(base, 'style.css'), 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css written:", len(css), "bytes")

with open(os.path.join(base, 'script.js'), 'w', encoding='utf-8') as f:
    f.write(js)
print("script.js written:", len(js), "bytes")
print("Done!")
