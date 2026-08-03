/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * [Yahoo-Search.js] - YAHOO SEARCH & SLURP CRAWLER INDEXING BRIDGE
 * Target Brand : Acebeam
 * Generated Automatically via YAHOO SEARCH PROTOCOL
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {
    'use strict';
    const SOTA_BORDER = "#10B981";
    const BRAND_NAME = "DONABICO GLOBAL MEDIA SYSTEM";
    const YAHOO_BOTS = /slurp|yahoo|yahoosearch|yahoo-blogs/i;

    function injectYahooSchema() {
        if (document.getElementById('eseb-yahoo-geo-schema')) return;

        const currentDomain = window.location.origin;
        const schemaData = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": currentDomain + "/#organization",
                    "name": BRAND_NAME,
                    "url": currentDomain
                },
                {
                    "@type": "WebPage",
                    "@id": currentDomain + "/#webpage",
                    "url": window.location.href,
                    "name": document.title || "Acebeam Official Network",
                    "isPartOf": {
                        "@id": currentDomain + "/#website"
                    },
                    "about": {
                        "@id": currentDomain + "/#organization"
                    }
                }
            ]
        };

        const script = document.createElement('script');
        script.id = 'eseb-yahoo-geo-schema';
        script.type = 'application/ld+json';
        script.text = JSON.stringify(schemaData);
        document.head.appendChild(script);
    }

    function executeYahooProtocol() {
        injectYahooSchema();
        const isYahooBot = YAHOO_BOTS.test(navigator.userAgent);

        if (isYahooBot) {
            document.documentElement.setAttribute('data-yahoo-index', 'active');
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeYahooProtocol);
    } else {
        executeYahooProtocol();
    }
})();
