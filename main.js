/* ========================================
   MediLink — main.js
   Digital Hospital Management System
   ======================================== */

let curMod = null, curRec = null, curPat = null;

// ---- RENDER DOCTORS GRID ----
function renderDocs(list) {
  const g = document.getElementById('docsGrid');
  if (!list || !list.length) {
    g.innerHTML = '<div class="no-res"><p style="font-size:1rem;margin-bottom:.5rem">No doctors found</p><p style="font-size:.85rem">Try a different search term or clear filters</p></div>';
    return;
  }
  g.innerHTML = list.map(d => {
    const pct = Math.min(100, (d.exp / 20) * 100);
    return `<div class="doc-card" onclick="openMod(${d.id})">
      <div class="doc-top">
        <div class="doc-av" style="background:${d.bg}">${d.em}</div>
        <div>
          <div class="doc-name">${d.name}</div>
          <span class="doc-sp" style="background:${d.bg};color:${d.cl}">${d.spec}</span>
        </div>
      </div>
      <div class="doc-body">
        <div class="doc-row">
          <svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          ${d.loc}
        </div>
        <div class="doc-row">
          <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          ${d.clinic}
        </div>
        <div class="doc-row">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          ${d.avail}
        </div>
        <div style="margin-top:.6rem">
          <div style="display:flex;justify-content:space-between;font-size:.78rem;margin-bottom:.3rem">
            <span style="color:var(--gray)">Experience</span>
            <span style="color:var(--teal);font-weight:600">${d.exp} years</span>
          </div>
          <div class="exp-bar"><div class="exp-fill" style="width:${pct}%"></div></div>
        </div>
      </div>
      <div class="doc-foot">
        <button class="dbtn-bk" onclick="event.stopPropagation();bookDir(${d.id})">Book Now</button>
        <button class="dbtn-vw" onclick="event.stopPropagation();openMod(${d.id})">View Profile</button>
      </div>
    </div>`;
  }).join('');
}

// ---- FILTER DOCTORS ----
function filtDocs() {
  if (typeof docs === 'undefined') return;
  const s = document.getElementById('srchInput').value.toLowerCase();
  const f = document.getElementById('filtSpec').value;
  renderDocs(docs.filter(d =>
    (!f || d.spec === f) &&
    (!s || d.name.toLowerCase().includes(s) || d.loc.toLowerCase().includes(s) || d.spec.toLowerCase().includes(s))
  ));
}

document.addEventListener('DOMContentLoaded', function () {
  const srchInput = document.getElementById('srchInput');
  const filtSpec  = document.getElementById('filtSpec');
  if (srchInput) srchInput.addEventListener('input', filtDocs);
  if (filtSpec)  filtSpec.addEventListener('change', filtDocs);
});

// ---- DOCTOR MODAL ----
function openMod(id) {
  if (typeof docs === 'undefined') return;
  const d = docs.find(x => x.id === id);
  if (!d) return;
  curMod = d;
  document.getElementById('mAv').innerHTML = d.em;
  document.getElementById('mAv').style.background = d.bg;
  document.getElementById('mName').textContent = d.name;
  document.getElementById('mSp').textContent = d.spec;
  document.getElementById('mDets').innerHTML = [
    ['&#128205; Location', d.loc],
    ['&#127968; Clinic', d.clinic],
    ['&#9990;&#65039; Phone', d.phone],
    ['&#128336; Availability', d.avail],
    ['&#11088; Experience', d.exp + ' years']
  ].map(([k, v]) => `<div class="m-det"><span class="mk">${k}</span><strong>${v}</strong></div>`).join('');
  document.getElementById('docModal').classList.add('open');
}

function closeModal() {
  document.getElementById('docModal').classList.remove('open');
  curMod = null;
}

function bookFromModal() {
  closeModal();
  document.getElementById('patient').scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('docModal').addEventListener('click', e => {
  if (e.target === document.getElementById('docModal')) closeModal();
});

// ---- PATIENT FORM ----
function submitForm() {
  const n  = document.getElementById('pName').value.trim();
  const c  = document.getElementById('pCnic').value.trim();
  const e  = document.getElementById('pEmail').value.trim();
  const p  = document.getElementById('pPhone').value.trim();
  const di = document.getElementById('pDisease').value.trim();

  if (!n || !c || !e || !p || !di) { toast('Please fill in all required fields'); return; }
  if (!e.includes('@')) { toast('Please enter a valid email address'); return; }

  curPat = { n, c, e, p, di };
  const rec = recommend(di);
  curRec = rec;

  document.getElementById('recAv').innerHTML = rec.em;
  document.getElementById('recAv').style.background = rec.bg;
  document.getElementById('recName').textContent = rec.name;
  document.getElementById('recSpec').textContent = rec.spec + ' · ' + rec.exp + ' years experience';
  document.getElementById('recDets').innerHTML = [
    ['&#128205; Location', rec.loc],
    ['&#127968; Clinic', rec.clinic],
    ['&#9990;&#65039; Phone', rec.phone],
    ['&#128336; Available', rec.avail]
  ].map(([k, v]) => `<div class="rec-dr"><span class="rec-dk">${k}</span><span class="rec-dv">${v}</span></div>`).join('');

  const el = document.getElementById('recResult');
  el.style.display = 'block';
  el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function recommend(dis) {
  if (typeof docs === 'undefined') return null;
  const d = dis.toLowerCase();
  let sp = 'General Physician';
  for (const doc of docs) {
    if (doc.kw && doc.kw.some(k => d.includes(k))) { sp = doc.spec; break; }
  }
  const m = docs.filter(x => x.spec === sp).sort((a, b) => b.exp - a.exp);
  return m.length ? m[0] : docs[2];
}

function confirmAppt() {
  if (!curPat || !curRec) return;
  document.getElementById('confMsg').innerHTML =
    `Your appointment has been confirmed with <span class="cn">${curRec.name}</span> (${curRec.spec}) at <strong>${curRec.clinic}</strong>.<br><br>
     A confirmation will be sent to <strong>${curPat.e}</strong>. Please call <strong>${curRec.phone}</strong> to confirm your time slot.`;
  document.getElementById('confOv').classList.add('open');
}

function closeConf() {
  document.getElementById('confOv').classList.remove('open');
  resetForm();
  toast('Appointment booked successfully!');
}

function resetForm() {
  ['pName', 'pCnic', 'pEmail', 'pPhone', 'pDisease'].forEach(id => {
    document.getElementById(id).value = '';
  });
  document.getElementById('recResult').style.display = 'none';
  curPat = null;
  curRec = null;
}

function bookDir(id) {
  document.getElementById('patient').scrollIntoView({ behavior: 'smooth' });
  toast('Fill in your details below to book this doctor');
}

// ---- TOAST ----
function toast(msg) {
  const t = document.getElementById('toast');
  document.getElementById('toast-msg').textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3500);
}

// ---- MOBILE NAV ----
function toggleNav() {
  document.getElementById('navLinks').classList.toggle('open');
}
document.querySelectorAll('.nav-link').forEach(a =>
  a.addEventListener('click', () => document.getElementById('navLinks').classList.remove('open'))
);

// ---- SCROLL: nav shadow + active link ----
window.addEventListener('scroll', () => {
  document.getElementById('mainNav').classList.toggle('scrolled', scrollY > 20);
  const sections = ['hero', 'features', 'doctors', 'patient', 'about'];
  let act = 'hero';
  sections.forEach(s => {
    const el = document.getElementById(s);
    if (el && el.getBoundingClientRect().top <= 100) act = s;
  });
  document.querySelectorAll('.nav-link').forEach(a =>
    a.classList.toggle('active', a.getAttribute('href').replace('#', '') === act)
  );
});
