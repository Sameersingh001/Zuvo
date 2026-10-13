// ==========================================================================
// ZUVO INTERACTIVE WEB APPLICATION SCRIPT (V2.5 ENHANCED)
// ==========================================================================

// Page switching logic
function showPage(name) {
  const pages = document.querySelectorAll('.page');
  const target = document.getElementById('page-' + name);

  if (!target) return;

  pages.forEach(p => {
    p.classList.remove('active');
  });

  target.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Update URL hash without jumping
  if (history.pushState) {
    history.pushState(null, null, '#' + name);
  }

  // Trigger hero animation inside active page
  setTimeout(() => {
    target.querySelectorAll('.anim').forEach(el => el.classList.add('visible'));
  }, 60);

  // Update active nav link
  document.querySelectorAll('.nav-link').forEach(link => {
    link.classList.remove('active');
    const onclickAttr = link.getAttribute('onclick') || '';
    if (onclickAttr.includes("'" + name + "'")) {
      link.classList.add('active');
    }
  });

  // Re-observe scroll animations for active page
  observeActivePage();
  closeMenu();
}

// Mobile Hamburger Menu
function toggleMenu() {
  const links = document.getElementById('navLinks');
  const btn = document.getElementById('hamburger');
  if (links) links.classList.toggle('open');
  if (btn) btn.classList.toggle('open');
}

function closeMenu() {
  const links = document.getElementById('navLinks');
  const btn = document.getElementById('hamburger');
  if (links) links.classList.remove('open');
  if (btn) btn.classList.remove('open');
}

// Close mobile menu on click outside
document.addEventListener('click', (e) => {
  const links = document.getElementById('navLinks');
  const btn = document.getElementById('hamburger');
  if (links && links.classList.contains('open')) {
    if (!links.contains(e.target) && (!btn || !btn.contains(e.target))) {
      closeMenu();
    }
  }
});

// Navbar scroll shadow
window.addEventListener('scroll', () => {
  const nav = document.getElementById('navbar');
  if (nav) {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  }
});

// Scroll-triggered animations with IntersectionObserver
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

function observeActivePage() {
  const activePage = document.querySelector('.page.active');
  if (activePage) {
    activePage.querySelectorAll('[data-anim]:not(.in-view)').forEach(el => {
      observer.observe(el);
    });
  }
}

// Interactive Toast Notification
function showToast(title, desc, type = 'blue') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'demo-toast';

  let iconSvg = '';
  if (type === 'green') {
    iconSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>';
  } else if (type === 'red') {
    iconSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/></svg>';
  } else {
    iconSvg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/></svg>';
  }

  toast.innerHTML = `
    <div class="toast-icon ${type}">${iconSvg}</div>
    <div class="toast-content">
      <div class="toast-title">${title}</div>
      <div class="toast-desc">${desc}</div>
    </div>
    <button class="toast-close" onclick="this.parentElement.remove()">✕</button>
  `;

  container.appendChild(toast);

  // Trigger enter animation
  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  // Auto remove after 4.5 seconds
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 4500);
}

// Hero Quick Bus Search Tracker
function handleHeroTrack(e) {
  e.preventDefault();
  const input = document.getElementById('heroBusInput');
  const busNum = input ? input.value.trim() : 'MH-04-E-2041';

  showToast('Live Vehicle Found', `Connecting to telemetry feed for <strong>${busNum}</strong>...`, 'blue');

  // Highlight visual card
  const card = document.getElementById('heroVisualCard');
  if (card) {
    card.style.transform = 'scale(1.03)';
    card.style.boxShadow = '0 0 40px rgba(37, 99, 235, 0.4)';
    setTimeout(() => {
      card.style.transform = '';
      card.style.boxShadow = '';
    }, 1200);
  }

  setTimeout(() => {
    showToast('GPS Stream Active', `${busNum} is on Route 12 • Speed: 39 km/h • ETA: 4 mins`, 'green');
  }, 900);
}

// Dual Audience Persona Switcher
function switchPersona(type) {
  const tabP = document.getElementById('tabParents');
  const tabS = document.getElementById('tabSchools');
  const viewP = document.getElementById('viewParents');
  const viewS = document.getElementById('viewSchools');

  if (type === 'schools') {
    tabP && tabP.classList.remove('active');
    tabS && tabS.classList.add('active');
    viewP && viewP.classList.remove('active');
    viewS && viewS.classList.add('active');
  } else {
    tabS && tabS.classList.remove('active');
    tabP && tabP.classList.add('active');
    viewS && viewS.classList.remove('active');
    viewP && viewP.classList.add('active');
  }
}

// Interactive Live Route Simulation
let isSimulating = false;
function runRouteSimulation() {
  if (isSimulating) return;
  isSimulating = true;

  const statusChip = document.getElementById('simStatusChip');
  const speedVal = document.getElementById('simSpeedVal');
  const etaVal = document.getElementById('simEtaVal');
  const stop3 = document.getElementById('simStop3');
  const stop4 = document.getElementById('simStop4');
  const routeLine = document.getElementById('simRouteLine');

  showToast('Route Simulation Started', 'Bus #07 is accelerating towards School Main Gate...', 'blue');

  if (statusChip) statusChip.innerHTML = '<span class="live-dot-green"></span> Simulating • Fast Transit';
  if (speedVal) speedVal.textContent = '48 km/h';
  if (etaVal) etaVal.textContent = '6 mins';

  // Step 1: In transit
  setTimeout(() => {
    if (speedVal) speedVal.textContent = '38 km/h';
    if (etaVal) etaVal.textContent = '3 mins';
    showToast('Approaching Stop', 'Geofence triggered: Bus entering School perimeter', 'green');
  }, 1600);

  // Step 2: Arrival at Campus
  setTimeout(() => {
    if (statusChip) statusChip.innerHTML = '<span class="live-dot-green"></span> Arrived At Campus';
    if (speedVal) speedVal.textContent = '0 km/h';
    if (etaVal) etaVal.textContent = '0 mins';

    if (stop3) {
      stop3.classList.remove('current');
      stop3.classList.add('passed');
      const circle = stop3.querySelector('.sv-node-circle');
      if (circle) circle.innerHTML = '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
    }

    if (stop4) {
      stop4.classList.add('current');
    }

    showToast('Safe Arrival Confirmed', 'Bus #07 safely docked at Campus Bay A. 36 students deboarded.', 'green');
  }, 3200);

  // Reset after 8 seconds
  setTimeout(() => {
    if (statusChip) statusChip.innerHTML = '<span class="live-dot-green"></span> En Route • On Time';
    if (speedVal) speedVal.textContent = '42 km/h';
    if (etaVal) etaVal.textContent = '10 mins';

    if (stop3) {
      stop3.classList.remove('passed');
      stop3.classList.add('current');
      const circle = stop3.querySelector('.sv-node-circle');
      if (circle) circle.textContent = '●';
    }

    if (stop4) {
      stop4.classList.remove('current');
    }

    isSimulating = false;
  }, 8500);
}

// School ROI Calculator
function updateRoi(busCount) {
  const count = parseInt(busCount) || 12;
  const countEl = document.getElementById('roiBusCount');
  const hoursEl = document.getElementById('roiHours');
  const fuelEl = document.getElementById('roiFuel');

  if (countEl) countEl.textContent = count + (count === 1 ? ' Bus' : ' Buses');

  const hoursSaved = count * 12; // ~12 hrs per bus/month
  const fuelSaved = count * 3800; // ~₹3,800 fuel saved per bus/month

  if (hoursEl) hoursEl.textContent = hoursSaved.toLocaleString('en-IN') + ' hrs/mo';
  if (fuelEl) fuelEl.textContent = '₹' + fuelSaved.toLocaleString('en-IN') + '/mo';
}

// FAQ Accordion
function toggleFaq(btn) {
  const item = btn.parentElement;
  const answer = item.querySelector('.fa');
  const icon = btn.querySelector('.fi');
  const isOpen = answer.classList.contains('open');

  document.querySelectorAll('.fa.open').forEach(a => a.classList.remove('open'));
  document.querySelectorAll('.fi.open').forEach(i => i.classList.remove('open'));

  if (!isOpen) {
    answer.classList.add('open');
    icon.classList.add('open');
  }
}

// Billing mode toggle (Monthly vs Annual)
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

  // Animate price numbers
  document.querySelectorAll('.pca').forEach(el => {
    const val = mode === 'y' ? el.dataset.y : el.dataset.m;
    if (val !== undefined) {
      el.style.transform = 'scale(0.85)';
      el.style.opacity = '0';
      setTimeout(() => {
        el.textContent = Number(val).toLocaleString('en-IN');
        el.style.transform = 'scale(1)';
        el.style.opacity = '1';
      }, 140);
      el.style.transition = 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)';
    }
  });

  // Update billing period labels (/ mo vs / yr)
  document.querySelectorAll('.pcp-cycle').forEach(el => {
    el.textContent = mode === 'y' ? '/ yr' : '/ mo';
  });

  // Toggle annual discount breakdown notes
  document.querySelectorAll('.pc-annual-note').forEach(el => {
    el.style.display = mode === 'y' ? 'flex' : 'none';
  });
}

// Contact form submission via WhatsApp
function handleContact(e) {
  e.preventDefault();

  const name = document.getElementById('cName')?.value?.trim() || '';
  const email = document.getElementById('cEmail')?.value?.trim() || '';
  const phone = document.getElementById('cPhone')?.value?.trim() || '';
  const school = document.getElementById('cSchool')?.value?.trim() || '';
  const inquiry = document.getElementById('cInquiry')?.value || '';
  const message = document.getElementById('cMsg')?.value?.trim() || '';

  const wpPhone = '919835051934';
  const text = `*New ZUVO Website Inquiry:*\n` +
    `• *Name:* ${name}\n` +
    `• *Phone:* ${phone}\n` +
    `• *Email:* ${email}\n` +
    `• *Institution:* ${school}\n` +
    `• *Inquiry Type:* ${inquiry}\n` +
    `• *Message:* ${message}`;

  const wpUrl = `https://wa.me/${wpPhone}?text=${encodeURIComponent(text)}`;

  const form = document.getElementById('contactForm');
  const success = document.getElementById('cSuccess');
  const wpLink = document.getElementById('cWpLink');

  if (wpLink) wpLink.href = wpUrl;
  if (form) form.style.display = 'none';
  if (success) success.style.display = 'block';

  // Open WhatsApp in new tab
  window.open(wpUrl, '_blank');
}

// Legal navigation scroll
function scrollLegal(id) {
  const el = document.getElementById('ls-' + id);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Live Simulated Telemetry Ticker (Brings page to life)
function initLiveTelemetryTicker() {
  const speedElem = document.getElementById('simSpeedVal');
  if (!speedElem) return;

  let baseSpeed = 42;
  setInterval(() => {
    if (isSimulating) return;
    const delta = (Math.random() * 4 - 2).toFixed(0);
    const newSpeed = Math.max(34, Math.min(46, baseSpeed + parseInt(delta)));
    if (speedElem) {
      speedElem.textContent = newSpeed + ' km/h';
    }
  }, 3500);
}

// Initialization on DOM ready
window.addEventListener('DOMContentLoaded', () => {
  const initialHash = window.location.hash.replace('#', '');
  if (initialHash && ['home', 'about', 'pricing', 'contact', 'legal', 'refund'].includes(initialHash)) {
    showPage(initialHash);
  } else {
    setTimeout(() => {
      document.querySelectorAll('#page-home .anim').forEach(el => el.classList.add('visible'));
    }, 80);
    observeActivePage();
  }

  initLiveTelemetryTicker();
  initCountdown();

  window.addEventListener('hashchange', () => {
    const currentHash = window.location.hash.replace('#', '');
    if (currentHash && ['home', 'about', 'pricing', 'contact', 'legal', 'refund'].includes(currentHash)) {
      showPage(currentHash);
    }
  });
});

// ==========================================================================
// PRE-LAUNCH WAITLIST FUNCTIONS
// ==========================================================================

// Backend API base URL (update to match your deployed backend)
const BACKEND_URL = 'http://localhost:5000/api/v1';

// Scroll to waitlist section
function scrollToWaitlist() {
  const el = document.getElementById('waitlist');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    // Focus first input
    setTimeout(() => {
      const inp = document.getElementById('wlName');
      if (inp) inp.focus();
    }, 600);
  }
}

// Countdown timer  set your target launch date here
function initCountdown() {
  // Set launch date: 60 days from now (or a fixed date like '2025-03-01T00:00:00+05:30')
  const launchDate = new Date();
  launchDate.setDate(launchDate.getDate() + 60);

  function tick() {
    const now = new Date();
    const diff = launchDate - now;

    if (diff <= 0) {
      document.getElementById('cdDays').textContent = '00';
      document.getElementById('cdHours').textContent = '00';
      document.getElementById('cdMins').textContent = '00';
      document.getElementById('cdSecs').textContent = '00';
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const secs = Math.floor((diff % (1000 * 60)) / 1000);

    const pad = (n) => String(n).padStart(2, '0');

    const dEl = document.getElementById('cdDays');
    const hEl = document.getElementById('cdHours');
    const mEl = document.getElementById('cdMins');
    const sEl = document.getElementById('cdSecs');

    if (dEl) dEl.textContent = pad(days);
    if (hEl) hEl.textContent = pad(hours);
    if (mEl) mEl.textContent = pad(mins);
    if (sEl) sEl.textContent = pad(secs);
  }

  tick();
  setInterval(tick, 1000);
}

// Waitlist form submission
async function handleWaitlistSubmit(e) {
  e.preventDefault();

  const name = document.getElementById('wlName')?.value?.trim();
  const email = document.getElementById('wlEmail')?.value?.trim();
  const phone = document.getElementById('wlPhone')?.value?.trim();
  const school = document.getElementById('wlSchool')?.value?.trim();
  const city = document.getElementById('wlCity')?.value?.trim();
  const busCount = document.getElementById('wlBuses')?.value;
  const role = document.getElementById('wlRole')?.value;
  const message = document.getElementById('wlMsg')?.value?.trim();

  if (!name || !email) {
    showToast('Missing Info', 'Please enter your name and email address.', 'red');
    return;
  }
  if (!/^\S+@\S+\.\S+$/.test(email)) {
    showToast('Invalid Email', 'Please enter a valid email address.', 'red');
    return;
  }

  // Show loading state
  const btn = document.getElementById('wlSubmitBtn');
  const btnText = document.getElementById('wlBtnText');
  const spinner = document.getElementById('wlSpinner');
  if (btn) btn.disabled = true;
  if (btnText) btnText.style.display = 'none';
  if (spinner) spinner.style.display = 'block';

  try {
    const response = await fetch(`${BACKEND_URL}/prelaunch/join`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, phone, schoolName: school, city, busCount, role, message }),
    });

    const data = await response.json();

    if (response.ok || response.status === 200) {
      // Show success state
      const form = document.getElementById('waitlistFormEl');
      const success = document.getElementById('wlSuccess');
      if (form) form.style.display = 'none';
      if (success) success.style.display = 'block';

      // Update lead count
      const countEl = document.getElementById('plLeadCount');
      if (countEl) {
        const current = parseInt(countEl.textContent) || 847;
        countEl.textContent = (current + 1).toLocaleString('en-IN');
      }

      showToast("You're on the list!", 'Check your email for next steps.', 'green');
    } else {
      throw new Error(data.message || 'Something went wrong');
    }
  } catch (err) {
    // If backend is not running, still show success (for demo/static hosting)
    if (err.name === 'TypeError' || err.message.includes('fetch')) {
      // Network error - backend not running, show demo success
      const form = document.getElementById('waitlistFormEl');
      const success = document.getElementById('wlSuccess');
      if (form) form.style.display = 'none';
      if (success) success.style.display = 'block';
      showToast('Waitlist Joined!', "We'll be in touch soon.", 'green');
    } else {
      // Restore button
      if (btn) btn.disabled = false;
      if (btnText) btnText.style.display = 'block';
      if (spinner) spinner.style.display = 'none';
      showToast('Error', err.message || 'Failed to join waitlist. Please try again.', 'red');
    }
  }
}

// Share waitlist
function shareWaitlist() {
  const text = "ZUVO — India's smartest school bus tracking platform is launching soon! Join the waitlist for exclusive early access: ";
  const url = window.location.href.split('#')[0] + '#waitlist';
  if (navigator.share) {
    navigator.share({ title: 'ZUVO School Bus Tracking  Join Waitlist', text, url });
  } else {
    navigator.clipboard.writeText(url).then(() => {
      showToast('Link Copied!', 'Share the ZUVO waitlist link with your network.', 'green');
    });
  }
}
