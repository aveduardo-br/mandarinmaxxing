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
  var css =
    R + '{--soft:var(--text-secondary,color-mix(in srgb,currentColor 65%,transparent));--line:var(--border,color-mix(in srgb,currentColor 15%,transparent));--off:color-mix(in srgb,currentColor 10%,transparent);--offfg:color-mix(in srgb,currentColor 55%,transparent);padding:4px 0 20px}' +
    R + ' h2{font-size:16px;font-weight:500;margin:0 0 8px}' +
    R + ' p{margin:0 0 12px;font-size:15px;line-height:1.7}' +
    R + ' details{border-top:1px solid var(--line)}' +
    R + ' details:last-of-type{border-bottom:1px solid var(--line);margin-bottom:24px}' +
    R + ' summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:14px;padding:12px 0;font-size:15px;font-weight:500;user-select:none}' +
    R + ' summary::-webkit-details-marker{display:none}' +
    R + ' summary:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:-2px}' +
    R + ' .mm-t{flex:none;display:grid;place-items:center;width:28px;height:28px;background:var(--off)}' +
    R + ' .mm-t svg{width:14px;height:12px;fill:var(--offfg)}' +
    R + ' summary:hover .mm-t:not(.on) svg{fill:currentColor}' +
    R + ' .mm-t.on{background:' + ORANGE + '}' +
    R + ' .mm-t.on svg{fill:' + INK + ';transform:scaleY(-1)}' +
    R + ' details>:not(summary){margin-left:42px;color:var(--soft);font-size:14px}' +
    R + ' details>:last-child{padding-bottom:6px}' +
    R + ' fieldset{border:0;padding:0;margin:0 0 18px;display:flex;flex-wrap:wrap;gap:2px}' +
    R + ' legend{padding:0;margin:0 0 8px;font-size:13px;color:var(--soft)}' +
    R + ' fieldset button{all:unset;box-sizing:border-box;cursor:pointer;width:112px;height:56px;padding:0 8px;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:13px;line-height:1.25;border-radius:0;background:var(--off);color:var(--soft);transition:background-color .12s ease,color .12s ease}' +
    R + ' fieldset[data-square] button{width:56px}' +
    R + ' fieldset button small{font-size:11px;opacity:.75}' +
    R + ' fieldset button:hover{background:color-mix(in srgb,' + ORANGE + ' 38%,transparent);color:inherit}' +
    R + ' fieldset button:focus-visible{outline:1px dashed ' + ORANGE + ';outline-offset:2px}' +
    R + ' fieldset button[aria-pressed="true"],' + R + ' fieldset button[aria-pressed="true"]:hover{background:' + ORANGE + ';color:' + INK + '}' +
    R + ' .mm-go{all:unset;box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;height:40px;padding:0 18px;border-radius:0;font-size:14px;font-weight:500;background:' + ORANGE + ';color:' + INK + '}' +
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

  var groups = [];
  root.querySelectorAll('fieldset').forEach(function (f) {
    var buttons = Array.prototype.slice.call(f.querySelectorAll('button'));
    if (!buttons.length) return;
    var legend = f.querySelector('legend');
    var group = { name: legend ? legend.textContent.trim() : '', value: '' };
    function pick(b) {
      buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      group.value = (b.getAttribute('data-value') || b.firstChild.textContent || b.textContent).trim().replace(/\s+/g, ' ');
    }
    buttons.forEach(function (b) {
      b.type = 'button';
      b.addEventListener('click', function () { pick(b); });
    });
    pick(f.querySelector('button[data-on]') || buttons[0]);
    groups.push(group);
  });

  var go = root.querySelector('[data-start]');
  if (go) {
    go.type = 'button';
    go.classList.add('mm-go');
    var out = document.createElement('p');
    out.className = 'mm-out';
    go.parentNode.insertBefore(out, go.nextSibling);
    go.addEventListener('click', function () {
      var text = groups.map(function (g) { return g.name + ': ' + g.value; }).join('. ') + '.';
      if (root.hasAttribute('data-preview') || typeof sendPrompt !== 'function') {
        out.textContent = text;
        return;
      }
      sendPrompt(text);
    });
  }
})();
