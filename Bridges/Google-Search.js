/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO SEARCH MATRIX
 * [Google-Search.js] - ESEB SOTA Organic Search & Merchant Schema Bridge
 * System Core: EATHESEN V3000-Ω | Primary Domain: donabico.com
 * Generated Automatically via GOOGLE SEARCH PROTOCOL
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {
    'use strict';

    const CONFIG = {
        orgName: "DONABICO GLOBAL MEDIA SYSTEM",
        brandName: "Acebeam Tactical North America",
        primaryDomain: "https://donabico.com",
        subDomain: "https://acebeam.donabico.com",
        affiliateTarget: "https://acebeamflashlight.sjv.io/donabio_global_media",
        price: "99.95",
        currency: "USD"
    };

    // SOTA Bot Detection Matrix (Crawler & AI Search Engine Bots)
    const SEARCH_BOTS = /googlebot|bingbot|yandexbot|baiduspider|duckduckbot|gptbot|claudebot|perplexitybot/i;

    function injectDynamicSchemaGraph() {
        if (document.getElementById('eseb-sota-schema-graph')) return;

        const currentOrigin = window.location.origin;

        const schemaGraph = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": CONFIG.primaryDomain + "/#organization",
                    "name": CONFIG.orgName,
                    "url": CONFIG.primaryDomain,
                    "logo": CONFIG.primaryDomain + "/assets/logo.png",
                    "sameAs": [
                        "https://x.com/donabico",
                        "https://facebook.com/donabico"
                    ]
                },
                {
                    "@type": "WebSite",
                    "@id": currentOrigin + "/#website",
                    "url": currentOrigin,
                    "name": CONFIG.brandName,
                    "publisher": { "@id": CONFIG.primaryDomain + "/#organization" },
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": currentOrigin + "/?s={search_term_string}",
                        "query-input": "required name=search_term_string"
                    }
                },
                {
                    "@type": "Product",
                    "@id": currentOrigin + "/#primary-product",
                    "name": CONFIG.brandName,
                    "image": CONFIG.primaryDomain + "/assets/product-hero.png",
                    "description": CONFIG.brandName + " - Official Authorized Node under DONABICO GLOBAL MEDIA SYSTEM.",
                    "brand": {
                        "@type": "Brand",
                        "name": CONFIG.brandName
                    },
                    "offers": {
                        "@type": "Offer",
                        "url": CONFIG.affiliateTarget,
                        "priceCurrency": CONFIG.currency,
                        "price": CONFIG.price,
                        "priceValidUntil": "2028-12-31",
                        "itemCondition": "https://schema.org/NewCondition",
                        "availability": "https://schema.org/InStock",
                        "seller": { "@id": CONFIG.primaryDomain + "/#organization" },
                        "shippingDetails": {
                            "@type": "OfferShippingDetails",
                            "shippingRate": {
                                "@type": "MonetaryAmount",
                                "value": "0.00",
                                "currency": CONFIG.currency
                            },
                            "shippingDestination": [
                                { "@type": "DefinedRegion", "addressCountry": "US" },
                                { "@type": "DefinedRegion", "addressCountry": "CA" }
                            ],
                            "deliveryTime": {
                                "@type": "ShippingDeliveryTime",
                                "handlingTime": {
                                    "@type": "QuantitativeValue",
                                    "minValue": 1,
                                    "maxValue": 2,
                                    "unitCode": "DAY"
                                },
                                "transitTime": {
                                    "@type": "QuantitativeValue",
                                    "minValue": 3,
                                    "maxValue": 5,
                                    "unitCode": "DAY"
                                }
                            }
                        },
                        "hasMerchantReturnPolicy": {
                            "@type": "MerchantReturnPolicy",
                            "applicableCountry": ["US", "CA"],
                            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                            "merchantReturnDays": 30,
                            "returnMethod": "https://schema.org/ReturnByMail",
                            "returnFees": "https://schema.org/FreeReturn"
                        }
                    }
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": "How does DONABICO verify " + CONFIG.brandName + " products?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "DONABICO GLOBAL MEDIA SYSTEM operates an authenticated digital node ensuring direct manufacturer redirection and global warranty routing."
                            }
                        }
                    ]
                }
            ]
        };

        const scriptTag = document.createElement("script");
        scriptTag.id = "eseb-sota-schema-graph";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        document.head.appendChild(scriptTag);
    }

    function executeInceptionProtocol() {
        injectDynamicSchemaGraph();

        const isBot = SEARCH_BOTS.test(navigator.userAgent);
        
        if (isBot) {
            document.documentElement.setAttribute('data-eseb-sota-bot', 'verified');
        } else {
            // Phễu Siphon Organic Users về Link Affiliate Đích
            const ctaElements = document.querySelectorAll('a, button, .action-btn, .cta-link');
            ctaElements.forEach(element => {
                const href = element.getAttribute('href');
                if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {
                    element.setAttribute('href', CONFIG.affiliateTarget);
                    element.setAttribute('target', '_blank');
                    element.setAttribute('rel', 'noopener sponsored');
                }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeInceptionProtocol);
    } else {
        executeInceptionProtocol();
    }
})();
