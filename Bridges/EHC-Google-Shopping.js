/* ================================================================= */
/* DONABICO GLOBAL MEDIA SYSTEM - AUTO-SENSING UNIVERSAL CORE        */
/* Node: DONABICO-V3000-OMEGA | EHC & ESEB Google Shopping Compliant  */
/* Safe-Compliance: Zero-UI Impact | Bot-Safe | Dynamic Schema       */
/* ================================================================= */

(function() {
    'use strict';

    const executeGoogleShoppingSchema = () => {
        if (document.getElementById('ehc-injected-jsonld')) return;

        const rawTitle = document.title ? document.title.split(/[-|_|•|–]/)[0].trim() : "DONABICO Tactical Gear";
        const pageUrl = window.location.href;
        
        let detectedPrice = "89.00";
        let detectedCurrency = "USD";
        
        const priceText = document.body.innerText;
        const priceMatch = priceText.match(/\$\s?(\d+(\.\d{1,2})?)/) || priceText.match(/(\d+(\.\d{1,2})?)\s?USD/i);
        if (priceMatch) {
            detectedPrice = priceMatch[1];
        }

        const pathSegments = window.location.pathname.split('/').filter(Boolean);
        const lastSegment = pathSegments.length > 0 ? pathSegments[pathSegments.length - 1].replace(/\.html$/i, '') : "GLOBAL";
        const autoSKU = `EHC-${lastSegment.toUpperCase()}-2026`;

        const schemaData = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": document.title || rawTitle,
            "image": [pageUrl.replace(/[^/]*$/, '') + "images/product-main.jpg"],
            "description": "DONABICO Global Media Network - High Performance Tactical & Apparel Products.",
            "sku": autoSKU,
            "brand": {
                "@type": "Brand",
                "name": rawTitle
            },
            "offers": {
                "@type": "Offer",
                "url": pageUrl,
                "priceCurrency": detectedCurrency,
                "price": detectedPrice,
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": "DONABICO GLOBAL MEDIA SYSTEM"
                }
            }
        };

        const scriptTag = document.createElement('script');
        scriptTag.type = 'application/ld+json';
        scriptTag.id = 'ehc-injected-jsonld';
        scriptTag.text = JSON.stringify(schemaData);
        document.head.appendChild(scriptTag);
    };

    const executeTrafficRouting = () => {
        document.body.addEventListener('click', (e) => {
            const targetBtn = e.target.closest('a, button, .cta-button, .affiliate-btn, [data-type="affiliate"]');
            
            if (targetBtn) {
                const href = targetBtn.getAttribute('href');
                const targetUrl = targetBtn.getAttribute('data-target-url') || targetBtn.getAttribute('data-affiliate-url');
                
                if ((!href || href === '#' || href.startsWith('javascript:')) && targetUrl) {
                    e.preventDefault();
                    
                    const urlParams = new URLSearchParams(window.location.search);
                    const gclid = urlParams.get('gclid');
                    const finalTarget = gclid 
                        ? (targetUrl.includes('?') ? `${targetUrl}&subid=${gclid}` : `${targetUrl}?subid=${gclid}`)
                        : targetUrl;
                        
                    window.open(finalTarget, '_blank', 'noopener,noreferrer');
                }
            }
        }, { passive: false });
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            executeGoogleShoppingSchema();
            executeTrafficRouting();
        });
    } else {
        executeGoogleShoppingSchema();
        executeTrafficRouting();
    }
})();
          
