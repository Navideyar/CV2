// Service Worker برای وب‌سایت
const CACHE_NAME = 'cv2-cache-v1';
const urlsToCache = [
  '/',
  '/static/CACHE/js/output.8d126b85d939.js',
  '/static/fonts/IRANSans/IRANSansWeb(FaNum).woff',
  '/static/fonts/vazir/Vazir-Bold-FD.woff',
  '/static/vendor/font-awesome/webfonts/fa-solid-900.woff2',
  '/static/vendor/font-awesome/webfonts/fa-regular-400.woff2',
  '/static/vendor/font-awesome/webfonts/fa-brands-400.woff2',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
}); 