/* Markerer den sektion, man er i, i menuen øverst */
(function () {
  if (!('IntersectionObserver' in window)) return;
  var links = [].slice.call(document.querySelectorAll('.stops a'));
  var secs = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      links.forEach(function (a, i) { a.setAttribute('aria-current', secs[i] === e.target ? 'true' : 'false'); });
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  secs.forEach(function (s) { if (s) io.observe(s); });
})();
