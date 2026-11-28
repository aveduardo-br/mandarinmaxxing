/* mandarinmaxxing setup card: an introduction, collapsible topics with the site's tiles, and the course
   choices as tile buttons. Loaded by the setup template in setup.md. The start button sends the learner's
   choices to the chat. Without this file the block still reads: native details and plain buttons. */
(function () {
  var root = document.getElementById('mandarinmaxxing-setup');
  if (!root || root.dataset.mm) return;
  root.dataset.mm = '1';
  var ORANGE = '#F07A42', INK = '#161616', DUR = 190;
  var CLOSE = 'cubic-bezier(.6,0,.8,.3)', OPEN = 'cubic-bezier(.2,.7,.2,1)';
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var R = '#mandarinmaxxing-setup';
  function imp(d) { return d.split(';').join(' !important;') + ' !important'; }
  var css =
    R + '{--soft:var(--text-secondary,color-mix(in srgb,currentColor 65%,transparent));--line:var(--border,color-mix(in srgb,currentColor 15%,transparent));--off:color-mix(in srgb,currentColor 10%,transparent);--offfg:color-mix(in srgb,currentColor 55%,transparent);--onoff:color-mix(in srgb,currentColor 88%,transparent);padding:4px 0 20px}' +
    // three levels: the card's title, a small label over each section, and the name of each choice
    R + ' h2{font-size:20px;font-weight:600;line-height:28px;margin:0 0 6px}' +
    R + ' h3{font-size:11px;font-weight:600;line-height:16px;letter-spacing:.08em;text-transform:uppercase;color:var(--offfg);margin:36px 0 14px}' +
    R + ' p b{font-weight:600;color:var(--text-primary,currentColor)}' +
    R + ' p{margin:0 0 12px;font-size:15px;line-height:1.7}' +
    R + ' details:last-of-type{margin-bottom:0}' +
    R + '[data-home] details:first-of-type{margin-top:28px}' +
    R + '[data-home] details:last-of-type{margin-bottom:0}' +
    R + ' summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;padding:6px 0;font-size:14px;font-weight:600;user-select:none}' +
    R + ' summary::-webkit-details-marker{display:none}' +
    R + ' summary:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:-2px}' +
    R + ' .mm-t{flex:none;display:grid;place-items:center;width:28px;height:28px;background:var(--off)}' +
    R + ' .mm-t svg{width:14px;height:12px;fill:var(--offfg)}' +
    R + ' summary:hover .mm-t:not(.on) svg{fill:currentColor}' +
    R + ' .mm-t.on{background:' + ORANGE + '}' +
    R + ' .mm-t.on svg{fill:' + INK + ';transform:scaleY(-1)}' +
    R + ' details>:not(summary){margin:0 0 0 40px;color:var(--soft);font-size:14px}' +
    R + ' details>:last-child{padding-bottom:6px}' +
    R + ' fieldset{border:0;padding:0;margin:0 0 22px;display:flex;flex-wrap:wrap;gap:4px 24px;min-width:0}' +
    R + ' legend{padding:0;margin:0 0 4px;font-size:14px;font-weight:600;line-height:22px;color:var(--text-primary,inherit)}' +
    R + ' legend small{font-size:13px;font-weight:400;margin-left:8px;color:var(--soft)}' +
    // the host styles every button (border, radius, background) and wins over plain rules, so these are !important
    // a choice is plain text with a small tile in front of it; the tile of the chosen one is orange
    R + ' fieldset button{' + imp('box-sizing:border-box;cursor:pointer;width:auto;height:28px;margin:0;padding:0;display:inline-flex;align-items:center;gap:8px;white-space:nowrap;font:inherit;font-size:14px;font-weight:500;line-height:28px;border:0;border-radius:0;box-shadow:none;transform:none;background:transparent;color:var(--soft);transition:color .12s ease') + '}' +
    R + ' fieldset button small{font-size:13px;font-weight:400;margin-left:-2px;opacity:.85}' +
    R + ' fieldset button:hover,' + R + ' fieldset button[aria-pressed="true"]{' + imp('color:inherit') + '}' +
    R + ' fieldset button:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:3px}' +
    R + ' .mm-m{flex:none;width:10px;height:10px;background:color-mix(in srgb,currentColor 24%,transparent);transition:background-color .12s ease}' +
    R + ' fieldset button:hover .mm-m{background:color-mix(in srgb,' + ORANGE + ' 45%,transparent)}' +
    R + ' fieldset button[data-note] .mm-m,' + R + ' fieldset button[disabled] .mm-m{background:transparent;outline:1px dashed var(--offfg);outline-offset:-1px}' +
    R + ' fieldset button[aria-pressed="true"] .mm-m{background:' + ORANGE + ';outline:0}' +
    R + ' fieldset button[disabled]{' + imp('cursor:default;color:var(--offfg)') + '}' +
    R + ' .mm-note{flex-basis:100%;margin:6px 0 0;font-size:13px;line-height:20px;color:var(--soft)}' +
    // one filled button per card: the main action. The other actions are plain text
    R + ' .mm-go,' + R + ' nav button[data-primary]{' + imp('box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;height:36px;margin:6px 0 0;padding:0 16px;font:inherit;font-size:14px;font-weight:600;line-height:36px;border:0;border-radius:0;box-shadow:none;transform:none;background:' + ORANGE + ';color:' + INK) + '}' +
    R + ' .mm-go:focus-visible,' + R + ' nav button:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:3px}' +
    R + ' nav{display:flex;flex-wrap:wrap;align-items:center;gap:8px 24px;margin:16px 0 0}' +
    R + ' nav button{' + imp('box-sizing:border-box;cursor:pointer;height:36px;margin:0;padding:0;display:inline-flex;align-items:center;white-space:nowrap;font:inherit;font-size:14px;font-weight:500;line-height:36px;border:0;border-radius:0;box-shadow:none;transform:none;background:transparent;color:var(--soft);transition:color .12s ease') + '}' +
    R + ' nav button:hover{' + imp('color:inherit') + '}' +
    R + ' nav button[data-primary]{' + imp('margin:0') + '}' +
    R + ' nav button[data-primary]:hover{' + imp('color:' + INK) + '}' +
    R + ' [data-progress]{margin:0;font-size:14px;line-height:22px;color:var(--soft)}' +
    R + ' [data-progress] strong{font-weight:600;color:var(--text-primary,currentColor);margin-right:8px}' +
    R + '[data-home] .mm-go[hidden]{' + imp('display:none') + '}' +
    R + ' .mm-w{margin:4px 0 28px;max-width:440px}' +
    R + ' .mm-w svg{display:block;width:100%;height:auto;overflow:visible}' +
    R + ' .mm-w rect{fill:currentColor;opacity:.3}' +
    R + ' .mm-w .x rect{fill:' + ORANGE + ';opacity:1}' +
    R + ' .mm-w text{fill:' + INK + ';font-size:2px;font-weight:700;text-anchor:middle}' +
    R + ' .mm-w pre{margin:0;padding:0;border:0;background:none;overflow:hidden;font-family:ui-monospace,"SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace;font-size:8.6px;line-height:1.18;letter-spacing:0;white-space:pre;color:' + ORANGE + '}' +
    R + ' .mm-w.a{max-width:none}' +
    R + ' .mm-w span{display:block;margin-top:10px;font-size:12px;line-height:16px;letter-spacing:.04em;color:var(--offfg)}' +
    R + ' .mm-out{margin:12px 0 0;font-size:13px;color:var(--soft)}';
  var style = document.createElement('style');
  style.textContent = css;
  root.appendChild(style);

  // The wordmark: MANDARIN in the tiles of the site's hero, MAXXING in seven tiles over its bottom edge.
  // An element with data-wordmark gets it drawn above its own text, which stays as the caption.
  var MARK = [
    '.............................###########......##..............................',
    '.....................####....#############....##....########..................',
    '................#....####....#############...####...#########.###.............',
    '..........##...####..#####...######...####..######..################..........',
    '.........###..######.#####...######....############.###....#########..........',
    '###.....####.#############...######....#######..#######....###########.....###',
    '####...#########.###########.######....######....######....############...####',
    '######.########....#########.######....######....######....############.######',
    '###############....#####.###.######....########..#############################',
    '########..#####...######.##########....######################.######.#########',
    '###.####..##############..#########...##############################..####.###',
    '###..##...##############..###################....######....#########...#...###',
    '###.......##############..###############.###....######....#########.......###',
    '###.......#####....#####....############..###....######....#########.......###',
    '###.......#####....####..............................##....#########.......###',
    '###.......####................................................######.......###',
    '###.......##......................................................##.......###',
    '###........................................................................###',
    '##.........................................................................###'
  ];
  // data-wordmark="ascii" draws the name as a terminal banner instead
  var BANNER = [
    "███╗   ███╗ █████╗ ███╗   ██╗██████╗  █████╗ ██████╗ ██╗███╗   ██╗███╗   ███╗ █████╗ ██╗  ██╗██╗  ██╗██╗███╗   ██╗ ██████╗",
    "████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║████╗ ████║██╔══██╗╚██╗██╔╝╚██╗██╔╝██║████╗  ██║██╔════╝",
    "██╔████╔██║███████║██╔██╗ ██║██║  ██║███████║██████╔╝██║██╔██╗ ██║██╔████╔██║███████║ ╚███╔╝  ╚███╔╝ ██║██╔██╗ ██║██║  ███╗",
    "██║╚██╔╝██║██╔══██║██║╚██╗██║██║  ██║██╔══██║██╔══██╗██║██║╚██╗██║██║╚██╔╝██║██╔══██║ ██╔██╗  ██╔██╗ ██║██║╚██╗██║██║   ██║",
    "██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝██║  ██║██║  ██║██║██║ ╚████║██║ ╚═╝ ██║██║  ██║██╔╝ ██╗██╔╝ ██╗██║██║ ╚████║╚██████╔╝",
    "╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝"
  ];
  var mark = root.querySelector('[data-wordmark]');
  if (mark && mark.getAttribute('data-wordmark') === 'ascii') {
    var line = mark.textContent.trim();
    mark.className = 'mm-w a';
    mark.innerHTML = '<pre role="img" aria-label="mandarinmaxxing"></pre>' + (line ? '<span></span>' : '');
    mark.querySelector('pre').textContent = BANNER.join('\n');
    if (line) mark.querySelector('span').textContent = line;
    // the banner is 123 characters wide: its font shrinks until the whole line fits the card
    var pre = mark.querySelector('pre');
    var fit = function () {
      var size = 9;
      pre.style.fontSize = size + 'px';
      while (size > 4 && pre.scrollWidth > pre.clientWidth + 1) { size -= 0.2; pre.style.fontSize = size + 'px'; }
    };
    fit();
    window.addEventListener('resize', fit);
  } else if (mark) {
    var caption = mark.textContent.trim(), out = '', NS = ' xmlns="http://www.w3.org/2000/svg"';
    MARK.forEach(function (row, y) {
      for (var x = 0; x < row.length; x++) if (row.charAt(x) === '#') out += '<rect x="' + x + '" y="' + y + '" width=".84" height=".84"/>';
    });
    var size = 3, gap = 0.3, left = (MARK[0].length - (7 * size + 6 * gap)) / 2, top = MARK.length - 3.4;
    out += '<g class="x">';
    'MAXXING'.split('').forEach(function (ch, i) {
      var x = left + i * (size + gap);
      out += '<rect x="' + x.toFixed(2) + '" y="' + top + '" width="' + size + '" height="' + size + '"/>' +
        '<text x="' + (x + size / 2).toFixed(2) + '" y="' + (top + 2.2).toFixed(2) + '">' + ch + '</text>';
    });
    out += '</g>';
    mark.className = 'mm-w';
    mark.innerHTML = '<svg' + NS + ' viewBox="0 0 ' + MARK[0].length + ' ' + (top + size).toFixed(2) + '" role="img" aria-label="mandarinmaxxing">' + out + '</svg>' +
      (caption ? '<span></span>' : '');
    if (caption) mark.querySelector('span').textContent = caption;
  }

  var ARROW = '<svg viewBox="0 0 7 6" shape-rendering="crispEdges" aria-hidden="true"><path d="M3 0h1v3h-1zM1 3h1v1h-1zM5 3h1v1h-1zM2 4h3v1h-3zM3 3h1v3h-1z"/></svg>';
  function flip(tile, on) {
    if (calm || !tile.animate) { tile.classList.toggle('on', on); return; }
    var a = tile.animate([{ transform: 'scaleY(1)' }, { transform: 'scaleY(0)' }], { duration: DUR, easing: CLOSE, fill: 'forwards' });
    a.onfinish = function () {
      a.cancel();
      tile.classList.toggle('on', on);
      tile.animate([{ transform: 'scaleY(0)' }, { transform: 'scaleY(1)' }], { duration: DUR, easing: OPEN });
    };
  }
  root.querySelectorAll('details').forEach(function (d) {
    var s = d.querySelector('summary');
    if (!s) return;
    var tile = document.createElement('span');
    tile.className = 'mm-t' + (d.open ? ' on' : '');
    tile.innerHTML = ARROW;
    s.insertBefore(tile, s.firstChild);
    d.addEventListener('toggle', function () { flip(tile, d.open); });
  });

  // "14/57" on a line puts the share done, as a percentage, in front of it
  var prog = root.querySelector('[data-progress]');
  if (prog) {
    var nums = (prog.getAttribute('data-progress') || '').split('/');
    var done = parseInt(nums[0], 10) || 0, total = parseInt(nums[1], 10) || 0;
    if (total) {
      var pct = document.createElement('strong');
      pct.textContent = Math.round(100 * done / total) + '%';
      prog.insertBefore(pct, prog.firstChild);
    }
  }
  Array.prototype.forEach.call(root.querySelectorAll('nav button'), function (b) { b.type = 'button'; });

  // The choices. State lives on the group, events are delegated from the document, and the colours are
  // also set inline, so a choice still works if the host re-renders the block or drops a style rule.
  var groups = [];
  function paint(g) {
    if (g.busy) return;
    g.buttons().forEach(function (b) {
      var on = b === g.current();
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      var m = b.querySelector('.mm-m');
      if (m) m.style.background = on ? ORANGE : '';
    });
    // a choice can carry a note, shown under its group while it is the one chosen
    var el = g.el(), note = el.querySelector('.mm-note'), text = g.current() ? g.current().getAttribute('data-note') : null;
    if (text && !note) { note = document.createElement('p'); note.className = 'mm-note'; el.appendChild(note); }
    if (note) { note.textContent = text || ''; note.style.display = text ? '' : 'none'; }
  }
  // a choice turns like every tile: the old and the new one close, change colour, and open again
  function turn(g, pair) {
    if (calm || !pair[0].animate) { paint(g); return; }
    g.busy = true;
    var left = pair.length;
    pair.forEach(function (button) {
      var b = button.querySelector('.mm-m') || button;
      var a = b.animate([{ transform: 'scaleY(1)' }, { transform: 'scaleY(0)' }], { duration: DUR, easing: CLOSE, fill: 'forwards' });
      a.onfinish = function () {
        a.cancel();
        if (--left === 0) { g.busy = false; paint(g); }
        b.animate([{ transform: 'scaleY(0)' }, { transform: 'scaleY(1)' }], { duration: DUR, easing: OPEN });
      };
    });
  }
  function live() { return document.getElementById('mandarinmaxxing-setup') || root; }
  Array.prototype.forEach.call(root.querySelectorAll('fieldset'), function (f, index) {
    var legend = f.querySelector('legend');
    var first = Array.prototype.slice.call(f.querySelectorAll('button'));
    if (!first.length) return;
    var start = first.indexOf(f.querySelector('button[data-on]'));
    var g = {
      name: legend ? (legend.firstChild && legend.firstChild.nodeType === 3 ? legend.firstChild.textContent : legend.textContent).trim() : '',
      at: start,  // -1: no choice marked, as with a pace that is none of the three
      el: function () { return live().querySelectorAll('fieldset')[index] || f; },
      buttons: function () { return Array.prototype.slice.call(g.el().querySelectorAll('button')); },
      current: function () { return g.buttons()[g.at]; },
      value: function () {
        var b = g.current();
        if (!b) return '';
        var small = b.querySelector('small');
        var label = '';
        for (var k = 0; k < b.childNodes.length; k++) if (b.childNodes[k].nodeType === 3) label += b.childNodes[k].textContent;
        label = label.trim();
        var text = b.getAttribute('data-value') || (small ? label + ' (' + small.textContent.trim() + ')' : label);
        return text.replace(/\s+/g, ' ');
      }
    };
    first.forEach(function (b) {
      b.type = 'button';
      var m = document.createElement('span');
      m.className = 'mm-m';
      m.setAttribute('aria-hidden', 'true');
      b.insertBefore(m, b.firstChild);
    });
    groups.push(g);
    paint(g);
  });
  var initial = groups.map(function (g) { return g.value() ? g.name + ': ' + g.value() : ''; });
  function groupOf(b) {
    for (var i = 0; i < groups.length; i++) if (groups[i].buttons().indexOf(b) > -1) return groups[i];
    return null;
  }
  function buttonAt(e) {
    var t = e.target && e.target.closest ? e.target.closest('#mandarinmaxxing-setup fieldset button:not([disabled])') : null;
    return t;
  }
  var clicks = 0;
  document.addEventListener('click', function (e) {
    var b = buttonAt(e);
    if (b) {
      var g = groupOf(b);
      if (!g) return;
      clicks++;
      var prev = g.current();
      if (prev === b) return;
      g.at = g.buttons().indexOf(b);
      turn(g, prev ? [prev, b] : [b]);
      showSave();
      report();
      return;
    }
    var cut = e.target && e.target.closest ? e.target.closest('#mandarinmaxxing-setup nav button') : null;
    if (cut) { send(cut.getAttribute('data-send') || cut.textContent.trim()); return; }
    var go = e.target && e.target.closest ? e.target.closest('#mandarinmaxxing-setup [data-start]') : null;
    if (!go) return;
    var now = groups.map(function (g) { return g.value() ? g.name + ': ' + g.value() : ''; });
    // at home only what changed is sent, and nothing is sent when nothing changed
    if (live().hasAttribute('data-home')) {
      now = now.filter(function (line, i) { return line && line !== initial[i]; });
      if (!now.length) { say(go.getAttribute('data-same') || ''); return; }
    }
    var lead = go.getAttribute('data-lead');
    send((lead ? lead + ' ' : '') + now.filter(Boolean).join('. ') + '.');
  });
  function send(text) {
    if (live().hasAttribute('data-preview') || typeof sendPrompt !== 'function') { say(text); return; }
    sendPrompt(text);
  }
  var go = root.querySelector('[data-start]');
  if (go) { go.type = 'button'; go.classList.add('mm-go'); }
  function changed() {
    return groups.some(function (g, i) { return (g.value() ? g.name + ': ' + g.value() : '') !== initial[i]; });
  }
  function showSave() {
    var r = live(), b = r.querySelector('[data-start]');
    if (b && r.hasAttribute('data-home')) b.hidden = !changed();
  }
  showSave();
  function say(text) {
    var r = live(), out = r.querySelector('.mm-out');
    if (!out) {
      out = document.createElement('p');
      out.className = 'mm-out';
      var after = r.querySelector('[data-start]');
      if (after) after.parentNode.insertBefore(out, after.nextSibling); else r.appendChild(out);
    }
    out.textContent = text;
  }
  // In a preview, one line under the card says what the script sees, to debug a host that swallows events.
  function report() {
    var r = live();
    if (!r.hasAttribute('data-debug')) return;
    var b = r.querySelector('fieldset button');
    var box = b.getBoundingClientRect();
    var top = document.elementFromPoint(box.left + box.width / 2, box.top + box.height / 2);
    say('debug · clicks ' + clicks + ' · same block ' + (r === root) + ' · style ' + !!r.querySelector('style') +
      ' · pressed ' + r.querySelectorAll('button[aria-pressed="true"]').length +
      ' · on top ' + (top ? top.tagName.toLowerCase() : 'none') +
      ' · bg ' + getComputedStyle(b).backgroundColor);
  }
  report();
  setTimeout(report, 1500);
})();
