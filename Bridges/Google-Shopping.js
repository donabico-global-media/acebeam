/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO-MEDIA-SYSTEM SHOPPING MATRIX
 * [Google-Shopping.js] - COMPLIANT MERCHANT SCHEMA BRIDGE
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {
    'use strict';

    function injectMerchantSchema() {
        const schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "Acebeam Tactical Illumination Flashlight Series",
            "image": ["https://acebeam.donabico.com/assets/images/product-main.jpg"],
            "description": "Professional-grade Acebeam Tactical Illumination Equipment.",
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
                "priceValidUntil": "2027-12-31",
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

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectMerchantSchema);
    } else {
        injectMerchantSchema();
    }
})();
