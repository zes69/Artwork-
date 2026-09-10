/* Mock behaviour for the storefront design.
   No backend — placeholder art, filters, cart badge and a fake player. */

// --- placeholder artwork -----------------------------------------------
// Every [data-art] element gets a deterministic blue/green wash so the mock
// reads like a gallery before the real photography lands.
const PALETTES = [
  ['#0a232e', '#1f6b76', '#9dbcab'],
  ['#123a4a', '#3f7d63', '#c9a15b'],
  ['#1f6b76', '#9dbcab', '#f4f1e8'],
  ['#0d1f26', '#3f7d63', '#7fb3a3'],
  ['#123a4a', '#c9a15b', '#9dbcab'],
  ['#0a232e', '#2c5f6b', '#5f9c86'],
];

function seedOf(str) {
  let h = 0;
  for (let i = 0; i < str.length; i++) h = (h * 31 + str.charCodeAt(i)) >>> 0;
  return h;
}

function paintPlaceholder(el) {
  const seed = seedOf(el.dataset.art || el.textContent || 'artwork');
  const [a, b, c] = PALETTES[seed % PALETTES.length];
  const id = 'g' + seed.toString(36);
  const angle = 20 + (seed % 120);
  // insertAdjacentHTML, not innerHTML — the media box may already hold a tag.
  el.insertAdjacentHTML('afterbegin', `
    <svg viewBox="0 0 400 500" preserveAspectRatio="xMidYMid slice" role="img"
         aria-label="Placeholder artwork">
      <defs>
        <linearGradient id="${id}" gradientTransform="rotate(${angle} .5 .5)">
          <stop offset="0%" stop-color="${a}"/>
          <stop offset="55%" stop-color="${b}"/>
          <stop offset="100%" stop-color="${c}"/>
        </linearGradient>
        <radialGradient id="${id}h" cx="${30 + (seed % 40)}%" cy="${25 + (seed % 50)}%">
          <stop offset="0%" stop-color="#f4f1e8" stop-opacity=".42"/>
          <stop offset="100%" stop-color="#f4f1e8" stop-opacity="0"/>
        </radialGradient>
      </defs>
      <rect width="400" height="500" fill="url(#${id})"/>
      <rect width="400" height="500" fill="url(#${id}h)"/>
      <g fill="none" stroke="#f4f1e8" stroke-opacity=".22">
        ${[0, 1, 2, 3, 4].map(i => {
          const y = 90 + i * 78 + (seed >> (i + 1)) % 40;
          return `<path d="M-20 ${y} Q 100 ${y - 46} 200 ${y} T 420 ${y - 18}"/>`;
        }).join('')}
      </g>
      <circle cx="${120 + (seed % 180)}" cy="${110 + (seed % 130)}"
              r="${26 + (seed % 34)}" fill="#f4f1e8" fill-opacity=".14"/>
    </svg>`);
}

document.querySelectorAll('[data-art]').forEach(paintPlaceholder);

// --- mobile nav ---------------------------------------------------------
const toggle = document.querySelector('.nav-toggle');
if (toggle) {
  toggle.addEventListener('click', () => {
    const links = document.querySelector('.nav-links');
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
}

// --- gallery filters ----------------------------------------------------
const chips = document.querySelectorAll('.chip[data-filter]');
if (chips.length) {
  chips.forEach(chip => chip.addEventListener('click', () => {
    chips.forEach(c => c.setAttribute('aria-pressed', String(c === chip)));
    const want = chip.dataset.filter;
    document.querySelectorAll('[data-kind]').forEach(card => {
      card.hidden = want !== 'all' && card.dataset.kind !== want;
    });
  }));
}

// --- cart badge (mock) --------------------------------------------------
let items = 0;
const badge = document.querySelector('.cart b');
document.querySelectorAll('[data-add]').forEach(btn => {
  btn.addEventListener('click', e => {
    e.preventDefault();
    items += 1;
    if (badge) badge.textContent = items;
    const original = btn.textContent;
    btn.textContent = 'Added';
    setTimeout(() => { btn.textContent = original; }, 1400);
  });
});

// --- fake audio player --------------------------------------------------
document.querySelectorAll('.track button').forEach(btn => {
  btn.addEventListener('click', () => {
    const row = btn.closest('.track');
    const playing = row.dataset.playing === 'true';
    document.querySelectorAll('.track').forEach(t => {
      t.dataset.playing = 'false';
      t.querySelector('button').textContent = '▶';
    });
    if (!playing) {
      row.dataset.playing = 'true';
      btn.textContent = '❚❚';
      const now = document.querySelector('[data-now-playing]');
      if (now) now.textContent = row.dataset.title;
    }
  });
});

// --- mock form submits --------------------------------------------------
document.querySelectorAll('form[data-mock]').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const note = form.querySelector('[data-note]') || form;
    const msg = document.createElement('p');
    msg.textContent = form.dataset.mock;
    msg.style.cssText = 'margin:8px 0 0;font-size:.86rem;opacity:.85';
    form.querySelectorAll('[data-mock-msg]').forEach(n => n.remove());
    msg.setAttribute('data-mock-msg', '');
    note.appendChild(msg);
    form.reset();
  });
});
