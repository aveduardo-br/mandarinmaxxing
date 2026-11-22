/* mandarinmaxxing vocabulary table: style, Hanzi font, stroke-order animation on hover, and the word's sound on click.
   Loaded by the table template in lesson-format.md. Without this file the table still reads as a plain table. */
(function () {
  var root = document.getElementById('mandarinmaxxing-vocab');
  if (!root || root.dataset.mm) return;
  root.dataset.mm = '1';
  var here = document.currentScript ? document.currentScript.src : '';
  var font = here.replace(/web\/vocab\.js.*$/, 'fonts/kaiti-hsk-1-6.woff');
  var css =
    '@font-face{font-family:"Mandarinmaxxing Kaiti";src:local("LXGW WenKai GB"),local("LXGW WenKai GB Lite"),url("' + font + '") format("woff");font-display:swap}' +
    '#mandarinmaxxing-vocab{--soft:var(--text-secondary,color-mix(in srgb,currentColor 65%,transparent));--line:var(--border,color-mix(in srgb,currentColor 15%,transparent));padding:4px 0 24px}' +
    '#mandarinmaxxing-vocab h2{font-size:16px;font-weight:500;margin:0 0 8px}' +
    '#mandarinmaxxing-vocab table{width:100%;border-collapse:collapse}' +
    '#mandarinmaxxing-vocab th,#mandarinmaxxing-vocab td{text-align:left;font-weight:400;padding:10px 64px 10px 0;border-bottom:1px solid var(--line);vertical-align:middle;user-select:text}' +
    '#mandarinmaxxing-vocab th{font-size:13px;font-weight:500;color:var(--soft)}' +
    '#mandarinmaxxing-vocab th:nth-child(-n+2),#mandarinmaxxing-vocab td:nth-child(-n+2){width:1%;white-space:nowrap}' +
    '#mandarinmaxxing-vocab td:nth-child(2){color:var(--soft)}' +
    '#mandarinmaxxing-vocab span[lang="zh-Hans"]{font-family:"Mandarinmaxxing Kaiti","Kaiti SC","STKaiti","KaiTi",serif;font-size:32px;line-height:1.2;font-synthesis:none;display:inline-flex;cursor:pointer;border-radius:4px}' +
    '#mandarinmaxxing-vocab span[lang="zh-Hans"]:focus-visible{outline:1px solid var(--soft);outline-offset:2px}' +
    '#mandarinmaxxing-vocab .mm-c{width:40px;height:40px;display:inline-flex;align-items:center;justify-content:center}' +
    '#mandarinmaxxing-vocab .mm-c svg{display:block}';
  var style = document.createElement('style');
  style.textContent = css;
  root.appendChild(style);

  // One recording per word lives in the mandarinmaxxing-audio repository, named with the word itself.
  // A click plays it; a word with no recording yet stays silent. When this address changes, update it here.
  var AUDIO = 'https://cdn.jsdelivr.net/gh/aveduardo-br/mandarinmaxxing-audio@cb005e4adfa852280b33fded8c27ae6edeae6d0e/audio/';
  // Words with two readings: the reading that has the plain file name. Any other reading is word_pinyin.
  var READINGS = {"还":"ha2i","好":"ha3o","看":"ka4n","只":"zhi1","啊":"a","长":"cha2ng","地":"de","得":"de","过":"guo4","头":"to2u","着":"zhe","地方":"di4fang","干":"ga4n","为":"we4i","行":"xi2ng","中":"zho1ng","种":"zho3ng","背":"be1i","重":"cho2ng","待":"da1i","当":"da1ng","倒":"da4o","结果":"jie2guo3","空":"ko1ng","量":"lia2ng","落":"luo4","数":"shu4","转":"zhua3n","冲":"cho1ng","处":"chu3","调":"dia4o","划":"hua2","系":"ji4","结":"jie2","扇":"sha1n","炸":"zha2","卷":"jua3n","露":"lo4u","散":"sa3n","吐":"tu3"};
  var TONE = { '\u0304': '1', '\u0301': '2', '\u030c': '3', '\u0300': '4' };
  function toneAscii(pinyin) {
    var out = [], text = (pinyin || '').split('/')[0].toLowerCase().normalize('NFD');
    for (var i = 0; i < text.length; i++) {
      var ch = text.charAt(i);
      if (TONE[ch]) out.push(TONE[ch]);
      else if (ch === '\u0308') out[out.length - 1] = 'v';
      else if (ch >= 'a' && ch <= 'z') out.push(ch);
    }
    return out.join('');
  }
  var player = null;
  function speak(word) {
    if (!word.sound || typeof Audio === 'undefined') return;
    if (player) { player.pause(); }
    player = new Audio(AUDIO + encodeURIComponent(word.sound) + '.mp3');
    player.onerror = function () { word.sound = ''; };  // no recording for this word: don't ask again
    var started = player.play();
    if (started && started.catch) started.catch(function () {});
  }

  var HAN = /[㐀-鿿]/;
  var words = [];
  root.querySelectorAll('span[lang="zh-Hans"]').forEach(function (w) {
    var text = w.textContent.trim();
    w.textContent = '';
    w.setAttribute('tabindex', '0');
    w.setAttribute('aria-label', text);
    var cells = [];
    Array.from(text).forEach(function (ch) {
      var c = document.createElement('span');
      c.className = 'mm-c';
      c.textContent = ch;
      c.setAttribute('aria-hidden', 'true');
      w.appendChild(c);
      if (HAN.test(ch)) cells.push({ el: c, ch: ch, writer: null });
    });
    var row = w.closest ? w.closest('tr') : null;
    var said = row && row.children[1] ? toneAscii(row.children[1].textContent) : '';
    var sound = READINGS[text] && said && READINGS[text] !== said ? text + '_' + said : text;
    var word = { el: w, cells: cells, busy: false, sound: HAN.test(text) ? sound : '' };
    words.push(word);
    w.addEventListener('click', function () { speak(word); });
  });

  function play(word) {
    var ready = word.cells.filter(function (c) { return c.writer; });
    if (word.busy || !ready.length) return;
    word.busy = true;
    var i = 0;
    (function next() {
      if (i >= ready.length) { word.busy = false; return; }
      var c = ready[i++];
      c.writer.updateColor('strokeColor', getComputedStyle(c.el).color, { duration: 0 });
      c.writer.animateCharacter({ onComplete: next });
    })();
  }

  function enhance() {
    if (typeof HanziWriter === 'undefined') return;
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    words.forEach(function (word) {
      word.cells.forEach(function (c) {
        var holder = document.createElement('span');
        holder.style.display = 'none';
        word.el.appendChild(holder);
        var writer = HanziWriter.create(holder, c.ch, {
          width: 40, height: 40, padding: 2, showOutline: false,
          strokeColor: getComputedStyle(c.el).color,
          strokeAnimationSpeed: 2, delayBetweenStrokes: 60,
          onLoadCharDataSuccess: function () {
            c.el.textContent = '';
            c.el.appendChild(holder.firstChild);
            holder.remove();
            c.writer = writer;
          },
          onLoadCharDataError: function () { holder.remove(); }
        });
      });
      if (!calm) word.el.addEventListener('mouseenter', function () { play(word); });
      word.el.addEventListener('click', function () { play(word); });
      word.el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); play(word); }
      });
    });
  }

  if (typeof HanziWriter !== 'undefined') return enhance();
  var lib = document.createElement('script');
  lib.src = 'https://cdn.jsdelivr.net/npm/hanzi-writer@3.5/dist/hanzi-writer.min.js';
  lib.onload = enhance;
  document.head.appendChild(lib);
})();
