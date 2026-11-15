/**
 * CS50x Anzali Hub - PJAX Smooth Transitions Engine (Barba.js + Alpine + HTMX)
 * Provides seamless app-like transitions across knowledge-base and dashboard.
 */
(function() {
  'use strict';

  // Check prefers-reduced-motion
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  // Ensure Barba is loaded
  if (typeof barba === 'undefined') {
    return;
  }

  try {
    barba.init({
      timeout: 5000,
      prevent: function({ el, href }) {
        if (!el || !href) return true;

        // Skip any link requesting prevent
        if (el.hasAttribute('data-barba-prevent') || el.closest('[data-barba-prevent]')) {
          return true;
        }

        // Skip HTMX links
        if (el.hasAttribute('hx-get') || el.hasAttribute('hx-post') || el.hasAttribute('hx-target')) {
          return true;
        }

        // Skip external, hash, or protocol links
        if (href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
          return true;
        }

        // Skip auth, admin, downloads, and practice runner
        const urlStr = String(href);
        if (
          urlStr.includes('/auth/') ||
          urlStr.includes('/admin/') ||
          urlStr.includes('/practice') ||
          urlStr.includes('/download') ||
          urlStr.includes('/api/') ||
          urlStr.includes('/static/')
        ) {
          return true;
        }

        // Skip if target="_blank" or download
        if (el.getAttribute('target') === '_blank' || el.hasAttribute('download')) {
          return true;
        }

        return false;
      },
      transitions: [{
        name: 'cs50-fade-transition',
        leave: function(data) {
          if (typeof gsap !== 'undefined') {
            return gsap.to(data.current.container, {
              opacity: 0,
              y: -8,
              duration: 0.18,
              ease: 'power1.in'
            });
          }
          data.current.container.style.opacity = '0';
          return Promise.resolve();
        },
        enter: function(data) {
          // Re-sync Document Title
          try {
            const raw = data.next.html;
            const match = raw.match(/<title>([^<]*)<\/title>/i);
            if (match && match[1]) {
              document.title = match[1];
            }
          } catch(e) {}

          // Re-initialize Alpine.js on the newly injected container
          if (window.Alpine && typeof Alpine.initTree === 'function') {
            try {
              Alpine.initTree(data.next.container);
            } catch(e) {
              console.warn('Alpine tree re-init notice:', e);
            }
          }

          // Re-process HTMX listeners on new container
          if (window.htmx && typeof htmx.process === 'function') {
            try {
              htmx.process(data.next.container);
            } catch(e) {}
          }

          // Scroll back to top smoothly or instantly
          if (window.lenis) {
            window.lenis.scrollTo(0, { immediate: true });
          } else {
            window.scrollTo(0, 0);
          }

          if (typeof gsap !== 'undefined') {
            return gsap.fromTo(data.next.container,
              { opacity: 0, y: 12 },
              { opacity: 1, y: 0, duration: 0.22, ease: 'power2.out' }
            );
          }
          data.next.container.style.opacity = '1';
          return Promise.resolve();
        }
      }]
    });
  } catch (err) {
    console.warn('Barba integration skipped:', err);
  }
})();
