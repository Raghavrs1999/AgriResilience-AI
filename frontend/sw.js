/**
 * AgriResilience AI — Progressive Web App Service Worker
 * Ensures offline resilience for smallholder farmers in remote agricultural fields.
 */

const CACHE_NAME = 'agriresilience-v3.2.0';
const STATIC_ASSETS = [
  './',
  './index.html',
  './styles.css',
  './app.js',
  './manifest.json',
  './pitch_deck.html',
  './assets/images/cotton_blight.jpg',
  './assets/images/rice_blast.jpg',
  './assets/images/cassava_mosaic.jpg',
  './assets/images/maize_blight_pest.jpg',
  './assets/images/sugarcane_red_rot.jpg',
  './assets/images/wheat_yellow_rust.jpg',
  './assets/images/soybean_asian_rust.jpg',
  './assets/images/sunscorch_control.jpg',
  './assets/images/mechanical_injury.jpg',
  './assets/audio/cotton_blight_mr_16k.mp3',
  './assets/audio/rice_blast_bn_16k.mp3',
  './assets/audio/cassava_cmd_id_16k.mp3',
  './assets/audio/maize_blight_te_16k.mp3',
  './assets/audio/sugarcane_redrot_ta_16k.mp3',
  './assets/audio/wheat_rust_hi_16k.mp3',
  './assets/audio/soybean_rust_vi_16k.mp3',
  './assets/audio/rx_cotton_blight_mr.mp3',
  './assets/audio/rx_rice_blast_bn.mp3',
  './assets/audio/rx_cassava_cmd_id.mp3',
  './assets/audio/rx_maize_blight_te.mp3',
  './assets/audio/rx_sugarcane_redrot_ta.mp3',
  './assets/audio/rx_wheat_rust_hi.mp3',
  './assets/audio/rx_soybean_rust_vi.mp3'
];

// Install Event: Pre-cache core application shell
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Pre-caching offline application shell v2.1.0');
      return cache.addAll(STATIC_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activate Event: Cleanup stale caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[ServiceWorker] Removing obsolete cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event: Cache-First with Network Fallback strategy
self.addEventListener('fetch', (event) => {
  // Pass-through live API requests directly to backend or fallback gracefully
  if (event.request.url.includes('/api/')) {
    event.respondWith(
      fetch(event.request).catch(() => {
        return new Response(
          JSON.stringify({
            offline: true,
            message: 'Offline mode active. Using cached field telemetry.'
          }),
          { headers: { 'Content-Type': 'application/json' } }
        );
      })
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        // Cache new static resources dynamically
        if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      }).catch(() => {
        if (event.request.headers.get('accept').includes('text/html')) {
          return caches.match('./index.html');
        }
      });
    })
  );
});
