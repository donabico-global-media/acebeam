/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO-MEDIA-SYSTEM DISPLAY-ADTECH-MODULE
 * [Google-Display.js] - PURE ADTECH & BOT HANDSHAKE BRIDGE (ISOLATED FROM CORE)
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {
    'use strict';
    const PRIMARY_AFFILIATE = "https://acebeamflashlight.sjv.io/donabio_global_media";
    const FALLBACK_TARGET = "https://www.acebeam.com/?utm_source=donabico_global_media&utm_medium=display";
    const GOOGLE_ADS_BOTS = /adsbot-google|mediapartners-google|adsbot-google-mobile/i;

    function captureGoogleAdsTracking() {
        try {
            const urlParams = new URLSearchParams(window.location.search);
            const adKeys = ['gclid', 'gbraid', 'wbraid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
            adKeys.forEach(key => {
                if (urlParams.has(key)) {
                    const val = urlParams.get(key);
                    document.cookie = `${key}=${encodeURIComponent(val)}; path=/; max-age=2592000; SameSite=Lax`;
                }
            });
        } catch(e) {}
    }

    function injectGoogleAdsSchema() {
        const displaySchema = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": document.title || "Acebeam Professional Flashlight Series",
            "description": "High-Performance Tactical Flashlights & LEP Illumination Gear.",
            "url": window.location.href,
            "publisher": {
                "@type": "Organization",
                "name": "DONABICO GLOBAL MEDIA SYSTEM",
                "url": window.location.origin
            },
            "mainEntity": {
                "@type": "Thing",
                "name": "Acebeam Tactical Illumination",
                "sameAs": "https://www.acebeam.com/"
            }
        };

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-display-ads-schema";
        script.text = JSON.stringify(displaySchema);
        document.head.appendChild(script);
    }

    function handleDisplayTraffic() {
        const isAdsBot = GOOGLE_ADS_BOTS.test(navigator.userAgent);
        if (isAdsBot) {
            document.documentElement.setAttribute('data-adsbot-status', 'verified-active');
            return;
        }

        let storedTracking = '';
        if (document.cookie) {
            const cookies = document.cookie.split('; ');
            cookies.forEach(c => {
                if (c.startsWith('gclid=') || c.startsWith('gbraid=') || c.startsWith('wbraid=')) {
                    storedTracking += '&' + c;
                }
            });
        }

        const finalTargetUrl = PRIMARY_AFFILIATE + (storedTracking ? '?' + storedTracking.substring(1) : '');

        document.body.addEventListener('click', function(e) {
            const btn = e.target.closest('a.display-cta, button.display-cta, [data-display-link]');
            if (btn) {
                const href = btn.getAttribute('href');
                if (!href || href === '#' || href === '') {
                    btn.setAttribute('href', finalTargetUrl);
                    btn.setAttribute('target', '_blank');
                    btn.setAttribute('rel', 'noopener sponsored');
                }
            }
        }, { passive: true });
    }

    function initDisplayModule() {
        captureGoogleAdsTracking();
        if (window.requestIdleCallback) {
            requestIdleCallback(() => {
                injectGoogleAdsSchema();
                handleDisplayTraffic();
            });
        } else {
            setTimeout(() => {
                injectGoogleAdsSchema();
                handleDisplayTraffic();
            }, 0);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDisplayModule);
    } else {
        initDisplayModule();
    }
})();