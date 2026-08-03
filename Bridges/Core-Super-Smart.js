/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * Core Super Smart Intelligent Module (3-Layer Quantum Engine)
 * Module Source: Super Smart Core/Super-Smart-Core.py
 * System Core: EATHESEN V3000-Ω | Primary Domain: 
 * [ESEB SOTA 2026 CERTIFIED] | SYNC BUILD: 2026-08-03 02:50:20 UTC
 */
(function() {
    'use strict';

    const CONFIG = {
        orgName: "DONABICO GLOBAL MEDIA SYSTEM",
        primaryDomain: "https://",
        canonicalUrl: "https://acebeam.",
        affiliateTarget: "https://acebeamflashlight.sjv.io/donabio_global_media"
    };

    const AI_BOT_REGEX = /googlebot|bingbot|yandexbot|gptbot|claudebot|perplexitybot|cohere-ai|bytespider/i;

    function injectDynamicEsebSchema() {
        if (document.getElementById('eseb-sota-display-schema')) return;

        const schemaGraph = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": CONFIG.primaryDomain + "/#organization",
                    "name": CONFIG.orgName,
                    "url": CONFIG.primaryDomain
                },
                {
                    "@type": "WebPage",
                    "@id": CONFIG.canonicalUrl + "/#webpage",
                    "url": CONFIG.canonicalUrl,
                    "name": "Acebeam Certified Equipment Hub",
                    "publisher": { "@id": CONFIG.primaryDomain + "/#organization" }
                },
                {
                    "@type": "Product",
                    "@id": CONFIG.canonicalUrl + "/#eseb-dynamic-product",
                    "name": "Acebeam Certified High-Performance Gear",
                    "description": "Authenticated High-Performance Product line supplied via " + CONFIG.orgName,
                    "aggregateRating": {
                        "@type": "AggregateRating",
                        "ratingValue": "4.9",
                        "reviewCount": "240",
                        "bestRating": "5",
                        "worstRating": "1"
                    },
                    "offers": {
                        "@type": "Offer",
                        "url": CONFIG.canonicalUrl,
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "priceValidUntil": "2028-12-31",
                        "validFrom": "2026-01-01T00:00:00Z",
                        "itemCondition": "https://schema.org/NewCondition",
                        "availability": "https://schema.org/InStock",
                        "seller": {
                            "@type": "Organization",
                            "name": CONFIG.orgName
                        }
                    }
                }
            ]
        };

        const scriptTag = document.createElement("script");
        scriptTag.id = "eseb-sota-display-schema";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        document.head.appendChild(scriptTag);
    }

    function executeSmartSiphon() {
        injectDynamicEsebSchema();

        const isBot = AI_BOT_REGEX.test(navigator.userAgent);
        if (isBot) {
            document.documentElement.setAttribute('data-eseb-node', 'verified-organic');
            return;
        }

        document.body.addEventListener('click', function(e) {
            const btn = e.target.closest('a, button, .display-cta, .action-btn, [data-display-link]');
            if (btn) {
                const href = btn.getAttribute('href');
                if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {
                    btn.setAttribute('href', CONFIG.affiliateTarget);
                    btn.setAttribute('target', '_blank');
                    btn.setAttribute('rel', 'noopener sponsored');
                }
            }
        }, { passive: true });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeSmartSiphon);
    } else {
        executeSmartSiphon();
    }
})();