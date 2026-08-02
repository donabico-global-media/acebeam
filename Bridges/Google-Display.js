/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO SEARCH & DISPLAY MATRIX
 * [Google-Display.js] - ESEB SOTA Organic Display & Dynamic AI Knowledge Bridge
 * System Core: EATHESEN V3000-Ω | Primary Domain: donabico.com
 * [V-STAMP 24 AUTHENTICATED] | BUILD: 2026-08-02 17:02:19 UTC
 */
(function() {
    'use strict';

    const CONFIG = {
        orgName: "DONABICO GLOBAL MEDIA SYSTEM",
        brandName: "Acebeam Tactical North America",
        primaryDomain: "https://donabico.com",
        canonicalUrl: "https://acebeam.donabico.com",
        affiliateTarget: "https://acebeamflashlight.sjv.io/donabio_global_media"
    };

    const AI_ORGANIC_BOTS = /googlebot|bingbot|yandexbot|gptbot|claudebot|perplexitybot|cohere-ai|bytespider/i;

    function injectDynamicSchemaGraph() {
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
                    "name": CONFIG.brandName + " - Certified Display Hub",
                    "publisher": { "@id": CONFIG.primaryDomain + "/#organization" }
                }
            ]
        };

        const scriptTag = document.createElement("script");
        scriptTag.id = "eseb-sota-display-schema";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        document.head.appendChild(scriptTag);
    }

    function executeDisplayProtocol() {
        injectDynamicSchemaGraph();

        const isBot = AI_ORGANIC_BOTS.test(navigator.userAgent);
        if (isBot) {
            document.documentElement.setAttribute('data-eseb-display-bot', 'verified');
            return;
        }

        // Phễu Siphon CTA hữu cơ chuẩn ESEB
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
        document.addEventListener('DOMContentLoaded', executeDisplayProtocol);
    } else {
        executeDisplayProtocol();
    }
})();