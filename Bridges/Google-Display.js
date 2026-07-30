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
    
    // REGEX CHỈ BẮT BÓNG CÁC BOT QUẢNG CÁO CỦA GOOGLE ADS
    const GOOGLE_ADS_BOTS = /adsbot-google|mediapartners-google|adsbot-google-mobile/i;

    // 1. FIRST-PARTY COOKIE ATTRIBUTION (BẢO TOÀN GCLID / GBRAID / UTMS)
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

    // 2. KHAI BÁO SCHEMA CHUYÊN BIỆT DUYỆT ADS NHANH CHÓNG
    function injectGoogleAdsSchema() {
        const displaySchema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "@id": window.location.href + "#webpage",
                    "url": window.location.href,
                    "name": document.title || "DONABICO GLOBAL MEDIA SYSTEM",
                    "publisher": {
                        "@type": "Organization",
                        "name": "DONABICO GLOBAL MEDIA SYSTEM",
                        "url": window.location.origin
                    }
                },
                {
                    "@type": "Product",
                    "name": document.title || "Acebeam Professional Tactical Gear",
                    "description": "High-Performance Tactical Flashlights & LEP Illumination Gear.",
                    "brand": {
                        "@type": "Brand",
                        "name": "Acebeam"
                    },
                    "offers": {
                        "@type": "Offer",
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "availability": "https://schema.org/InStock",
                        "url": window.location.href
                    }
                }
            ]
        };

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-display-ads-schema";
        script.text = JSON.stringify(displaySchema);
        document.head.appendChild(script);
    }

    // 3. XỬ LÝ CHUYỂN HƯỚNG ADS & BẮT TAY BOT ADS
    function handleDisplayTraffic() {
        const isAdsBot = GOOGLE_ADS_BOTS.test(navigator.userAgent);

        if (isAdsBot) {
            document.documentElement.setAttribute('data-adsbot-status', 'verified-active');
            return;
        }

        // Trích xuất lại GCLID / GBRAID gắn vào URL Target
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

    // KHỞI CHẠY KHÔNG ẢNH HƯỞNG TỚI CORE
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
