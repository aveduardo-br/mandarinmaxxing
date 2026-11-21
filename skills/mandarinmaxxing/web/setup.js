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
    R + '{--soft:var(--text-secondary,color-mix(in srgb,currentColor 65%,transparent));--line:var(--border,color-mix(in srgb,currentColor 15%,transparent));--off:color-mix(in srgb,currentColor 10%,transparent);--offfg:color-mix(in srgb,currentColor 55%,transparent);padding:4px 0 20px}' +
    R + ' h2{font-size:16px;font-weight:500;margin:0 0 8px}' +
    R + ' p{margin:0 0 12px;font-size:15px;line-height:1.7}' +
    R + ' details{border-top:1px solid var(--line)}' +
    R + ' details:last-of-type{border-bottom:1px solid var(--line);margin-bottom:20px}' +
    R + ' summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;padding:10px 0;font-size:14px;font-weight:500;user-select:none}' +
    R + ' summary::-webkit-details-marker{display:none}' +
    R + ' summary:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:-2px}' +
    R + ' .mm-t{flex:none;display:grid;place-items:center;width:28px;height:28px;background:var(--off)}' +
    R + ' .mm-t svg{width:14px;height:12px;fill:var(--offfg)}' +
    R + ' summary:hover .mm-t:not(.on) svg{fill:currentColor}' +
    R + ' .mm-t.on{background:' + ORANGE + '}' +
    R + ' .mm-t.on svg{fill:' + INK + ';transform:scaleY(-1)}' +
    R + ' details>:not(summary){margin-left:40px;color:var(--soft);font-size:14px}' +
    R + ' details>:last-child{padding-bottom:6px}' +
    R + ' fieldset{border:0;padding:0;margin:0 0 16px;display:flex;flex-wrap:wrap;gap:2px;min-width:0}' +
    R + ' legend{padding:0;margin:0 0 6px;font-size:13px;line-height:20px;color:var(--soft)}' +
    // the host styles every button (border, radius, background) and wins over plain rules, so these are !important
    R + ' fieldset button{' + imp('box-sizing:border-box;cursor:pointer;width:auto;min-width:36px;height:36px;margin:0;padding:0 14px;display:inline-flex;flex-direction:row;align-items:baseline;justify-content:center;gap:7px;white-space:nowrap;font:inherit;font-size:14px;font-weight:500;line-height:36px;border:0;border-radius:0;box-shadow:none;transform:none;background:var(--off);color:var(--offfg);transition:background-color .12s ease,color .12s ease') + '}' +
    R + ' fieldset[data-square] button{' + imp('width:36px;padding:0') + '}' +
    R + ' fieldset button small{font-size:13px;font-weight:400;opacity:.7}' +
    R + ' fieldset button:hover{' + imp('background:color-mix(in srgb,' + ORANGE + ' 38%,transparent);color:inherit') + '}' +
    R + ' fieldset button:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:2px}' +
    R + ' fieldset button[aria-pressed="true"],' + R + ' fieldset button[aria-pressed="true"]:hover{' + imp('background:' + ORANGE + ';color:' + INK) + '}' +
    R + ' .mm-go{' + imp('box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;height:36px;margin:6px 0 0;padding:0 16px;font:inherit;font-size:14px;font-weight:500;border:0;border-radius:0;box-shadow:none;transform:none;background:' + ORANGE + ';color:' + INK) + '}' +
    R + ' .mm-go:focus-visible{outline:1px dashed currentColor;outline-offset:2px}' +
    R + ' .mm-out{margin:12px 0 0;font-size:13px;color:var(--soft)}';
  var style = document.createElement('style');
  style.textContent = css;
  root.appendChild(style);

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

  // The choices. State lives on the group, events are delegated from the document, and the colours are
  // also set inline, so a choice still works if the host re-renders the block or drops a style rule.
  var groups = [];
  function paint(g) {
    g.buttons().forEach(function (b) {
      var on = b === g.current();
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      var bg = on ? ORANGE : (b === hot ? 'color-mix(in srgb,' + ORANGE + ' 38%,transparent)' : '');
      if (bg) b.style.setProperty('background', bg, 'important'); else b.style.removeProperty('background');
      if (on) b.style.setProperty('color', INK, 'important'); else b.style.removeProperty('color');
    });
  }
  var hot = null;
  function live() { return document.getElementById('mandarinmaxxing-setup') || root; }
  Array.prototype.forEach.call(root.querySelectorAll('fieldset'), function (f, index) {
    var legend = f.querySelector('legend');
    var first = Array.prototype.slice.call(f.querySelectorAll('button'));
    if (!first.length) return;
    var start = first.indexOf(f.querySelector('button[data-on]'));
    var g = {
      name: legend ? legend.textContent.trim() : '',
      at: start < 0 ? 0 : start,
      el: function () { return live().querySelectorAll('fieldset')[index] || f; },
      buttons: function () { return Array.prototype.slice.call(g.el().querySelectorAll('button')); },
      current: function () { return g.buttons()[g.at]; },
      value: function () {
        var b = g.current();
        return (b.getAttribute('data-value') || b.textContent).trim().replace(/\s+/g, ' ');
      }
    };
    first.forEach(function (b) { b.type = 'button'; });
    groups.push(g);
    paint(g);
  });
  function groupOf(b) {
    for (var i = 0; i < groups.length; i++) if (groups[i].buttons().indexOf(b) > -1) return groups[i];
    return null;
  }
  function buttonAt(e) {
    var t = e.target && e.target.closest ? e.target.closest('#mandarinmaxxing-setup fieldset button') : null;
    return t;
  }
  var clicks = 0;
  document.addEventListener('click', function (e) {
    var b = buttonAt(e);
    if (b) {
      var g = groupOf(b);
      if (!g) return;
      clicks++;
      g.at = g.buttons().indexOf(b);
      paint(g);
      report();
      return;
    }
    var go = e.target && e.target.closest ? e.target.closest('#mandarinmaxxing-setup [data-start]') : null;
    if (!go) return;
    var text = groups.map(function (g) { return g.name + ': ' + g.value(); }).join('. ') + '.';
    if (live().hasAttribute('data-preview') || typeof sendPrompt !== 'function') { say(text); return; }
    sendPrompt(text);
  });
  document.addEventListener('mouseover', function (e) {
    var b = buttonAt(e);
    if (b === hot) return;
    hot = b;
    groups.forEach(paint);
  });

  var go = root.querySelector('[data-start]');
  if (go) { go.type = 'button'; go.classList.add('mm-go'); }
  function say(text) {
    var r = live(), out = r.querySelector('.mm-out');
    if (!out) { out = document.createElement('p'); out.className = 'mm-out'; r.appendChild(out); }
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
