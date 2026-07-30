/* ================================================================= */
/* DONABICO GLOBAL MEDIA SYSTEM - BOT HANDSHAKE TELEMETRY BRIDGE      */
/* Node: EATHESEN V3000-Ω | Universal Crawler Alliance Protocol     */
/* ¢24 IMMUTABLE | Zero-UI Impact | Google & Bing & Yahoo Compliant  */
/* ================================================================= */

(function() {
    'use strict';

    const BOT_HANDSHAKE_ENGINE = {
        botSignatures: [
            'googlebot', 'adsbot-google', 'mediapartners-google', 'feedfetcher-google',
            'bingbot', 'bingpreview', 'msnbot', 'slurp', 'yahoo! slurp',
            'duckduckbot', 'baiduspider', 'yandexbot', 'facebookexternalhit',
            'gptbot', 'claudebot', 'perplexbot', 'applebot'
        ],

        isFriendlyBot: function() {
            const ua = navigator.userAgent.toLowerCase();
            return this.botSignatures.some(bot => ua.includes(bot));
        },

        injectCanonicalAndMeta: function() {
            const currentUrl = window.location.href.split('?')[0];
            
            if (!document.querySelector("link[rel='canonical']")) {
                const canonicalLink = document.createElement('link');
                canonicalLink.rel = 'canonical';
                canonicalLink.href = currentUrl;
                document.head.appendChild(canonicalLink);
            }

            if (!document.querySelector("meta[name='robots']")) {
                const robotsMeta = document.createElement('meta');
                robotsMeta.name = 'robots';
                robotsMeta.content = 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1';
                document.head.appendChild(robotsMeta);
            }
        },

        injectEATKnowledgeGraph: function() {
            if (document.getElementById('ehc-bot-knowledge-graph')) return;

            const domain = window.location.hostname;
            const schemaGraph = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "Organization",
                        "@id": `https://${domain}/#organization`,
                        "name": "DONABICO GLOBAL MEDIA SYSTEM",
                        "url": `https://${domain}`,
                        "logo": `https://${domain}/images/logo.png`,
                        "knowsAbout": ["Tactical Gear", "Apparel", "Affiliate Marketing", "High-Performance Logistics"],
                        "sameAs": [
                            "https://x.com/donabico",
                            "https://facebook.com/donabico"
                        ]
                    },
                    {
                        "@type": "WebSite",
                        "@id": `https://${domain}/#website`,
                        "url": `https://${domain}`,
                        "name": document.title || "EATHESEN Global System",
                        "publisher": { "@id": `https://${domain}/#organization` }
                    }
                ]
            };

            const scriptTag = document.createElement('script');
            scriptTag.type = 'application/ld+json';
            scriptTag.id = 'ehc-bot-knowledge-graph';
            scriptTag.text = JSON.stringify(schemaGraph);
            document.head.appendChild(scriptTag);
        },

        triggerIndexNowTelemetry: function() {
            if (window.requestIdleCallback) {
                window.requestIdleCallback(() => this.sendPing());
            } else {
                setTimeout(() => this.sendPing(), 1000);
            }
        },

        sendPing: function() {
            const host = window.location.hostname;
            const url = window.location.href;
            
            const payload = {
                host: host,
                url: url,
                key: "eAthesen2026_c24_handshake",
                keyLocation: `https://${host}/eAthesen2026_c24_handshake.txt`
            };

            if (navigator.sendBeacon) {
                const blob = new Blob([JSON.stringify(payload)], { type: 'application/json' });
                navigator.sendBeacon('https://api.indexnow.org/indexnow', blob);
            }
        },

        init: function() {
            this.injectCanonicalAndMeta();
            this.injectEATKnowledgeGraph();
            this.triggerIndexNowTelemetry();
        }
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => BOT_HANDSHAKE_ENGINE.init());
    } else {
        BOT_HANDSHAKE_ENGINE.init();
    }
})();