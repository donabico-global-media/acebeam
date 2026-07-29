/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO-MEDIA-SYSTEM SHOPPING MATRIX
 * [Google-Shopping.js] - REAL GOOGLE SHOPPING FEED & ATTRIBUTION BRIDGE
 * Generated Automatically via GOOGLE SHOPPING PROTOCOL
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {
    'use strict';
    const SOTA_BORDER = "#10B981";
    const BRAND_NAME = "DONABICO GLOBAL MEDIA SYSTEM";
    const AFFILIATE_TARGET = "https://acebeamflashlight.sjv.io/donabio_global_media";
    const SHOPPING_BOTS = /googlebot|adsbot-google|google-merchant|googlebot-shopping/i;

    function injectMerchantSchema() {
        const schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": document.title || "Acebeam Tactical Gear",
            "image": ["https://www.acebeam.com/images/thumbs/000/0003503_defender-p16-tactical-flashlight.jpeg"],
            "description": "High-Performance Tactical Gear",
            "sku": "ACEBEAM-TAC-001",
            "brand": {
                "@type": "Brand",
                "name": "Acebeam"
            },
            "offers": {
                "@type": "Offer",
                "url": window.location.href,
                "priceCurrency": "USD",
                "price": "99.95",
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition"
            }
        };
        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-merchant-schema";
        script.text = JSON.stringify(schema);
        document.head.appendChild(script);
    }

    function executeShoppingProtocol() {
        injectMerchantSchema();
        const isBot = SHOPPING_BOTS.test(navigator.userAgent);

        if (isBot) {
            document.documentElement.setAttribute('data-merchant-status', 'active');
        } else {
            document.body.addEventListener('click', function(e) {
                const btn = e.target.closest('a, .action-link');
                if (btn) {
                    const href = btn.getAttribute('href');
                    if (!href || href === '#' || href === '') {
                        btn.setAttribute('href', AFFILIATE_TARGET);
                    }
                }
            }, { passive: true });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeShoppingProtocol);
    } else {
        executeShoppingProtocol();
    }
})();
