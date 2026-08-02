# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Display.py] - ESEB Organic Search & Display Bridge Compiler
System Core: EATHESEN V3000-Ω | Primary Domain: donabico.com
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os
import sys
import datetime

class EsebDisplayCompiler:
    def __init__(self):
        self.primary_domain = os.getenv("PRIMARY_DOMAIN", "donabico.com").strip()
        self.brand_organization = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = "DONABICO SEARCH & DISPLAY MATRIX"
        
        # Auto-Discovery từ môi trường GitHub Actions
        raw_repo = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/acebeam")
        repo_slug = raw_repo.split("/")[-1].lower()
        
        self.brand_clean_name = " ".join([word.capitalize() for word in repo_slug.replace("-", " ").replace("_", " ").split()])
        self.repo_key = repo_slug.replace("-", "").replace("_", "")
        self.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self.brand_config = self._resolve_configuration()

    def _resolve_configuration(self):
        custom_affiliate_env = os.getenv("AFFILIATE_TARGET_URL", "").strip()
        
        # Bảng ánh xạ Link Affiliate trực tiếp cho từng Thương hiệu (Mở rộng cho 1.000+ Kho)
        brand_affiliate_map = {
            "acebeam": "https://acebeamflashlight.sjv.io/donabio_global_media",
            "8000kicks": "https://8000kicks.com/?ref=donabico"
        }
        
        # Ưu tiên: 1. Biến môi trường Secret/Var -> 2. Link trực tiếp trong Map -> 3. Link fallback
        affiliate_target = custom_affiliate_env or brand_affiliate_map.get(
            self.repo_key, f"https://{self.primary_domain}/shop/{self.repo_key}"
        )

        selected = {
            "name": f"{self.brand_clean_name} Certified Display Hub",
            "affiliate": affiliate_target,
            "canonical": f"https://{self.repo_key}.{self.primary_domain}"
        }
        return selected

    def compile_display_bridge(self):
        try:
            output_dir = "Bridges"
            os.makedirs(output_dir, exist_ok=True)
            js_path = os.path.join(output_dir, "Google-Display.js")
            
            brand_name = self.brand_config["name"]
            affiliate_url = self.brand_config["affiliate"]
            canonical_url = self.brand_config["canonical"]
            current_year = datetime.datetime.now().year

            # Template JS an toàn, tránh đụng độ cú pháp F-string với JS
            template = """/**
 * __ORG_NAME__
 * __SYS_IDENTITY__
 * [Google-Display.js] - ESEB SOTA Organic Display & Dynamic AI Knowledge Bridge
 * System Core: EATHESEN V3000-Ω | Primary Domain: __PRIMARY_DOMAIN__
 * [V-STAMP 24 AUTHENTICATED] | BUILD: __BUILD_TIME__
 */
(function() {
    'use strict';

    const CONFIG = {
        orgName: "__ORG_NAME__",
        brandName: "__BRAND_NAME__",
        primaryDomain: "https://__PRIMARY_DOMAIN__",
        canonicalUrl: "__CANONICAL_URL__",
        affiliateTarget: "__AFFILIATE_URL__"
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
                    "name": CONFIG.brandName,
                    "publisher": { "@id": CONFIG.primaryDomain + "/#organization" }
                },
                {
                    "@type": "Product",
                    "@id": CONFIG.canonicalUrl + "/#eseb-dynamic-product",
                    "name": CONFIG.brandName,
                    "description": "Certified high-performance equipment supplied via " + CONFIG.orgName,
                    "aggregateRating": {
                        "@type": "AggregateRating",
                        "ratingValue": "4.9",
                        "reviewCount": "142",
                        "bestRating": "5",
                        "worstRating": "1"
                    },
                    "offers": {
                        "@type": "Offer",
                        "url": CONFIG.canonicalUrl,
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "priceValidUntil": "__PRICE_VALID_UNTIL__",
                        "validFrom": "__VALID_FROM__",
                        "itemCondition": "https://schema.org/NewCondition",
                        "availability": "https://schema.org/InStock",
                        "seller": {
                            "@type": "Organization",
                            "name": CONFIG.orgName
                        }
                    },
                    "review": [
                        {
                            "@type": "Review",
                            "reviewRating": {
                                "@type": "Rating",
                                "ratingValue": "5",
                                "bestRating": "5"
                            },
                            "author": {
                                "@type": "Organization",
                                "name": "Verified Global Buyer"
                            },
                            "reviewBody": "Official authenticated product line with verified global dispatch."
                        }
                    ]
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
"""

            # Điền các biến động an toàn
            js_content = template \
                .replace("__ORG_NAME__", self.brand_organization) \
                .replace("__SYS_IDENTITY__", self.system_identity) \
                .replace("__PRIMARY_DOMAIN__", self.primary_domain) \
                .replace("__BUILD_TIME__", self.build_time) \
                .replace("__BRAND_NAME__", brand_name) \
                .replace("__CANONICAL_URL__", canonical_url) \
                .replace("__AFFILIATE_URL__", affiliate_url) \
                .replace("__PRICE_VALID_UNTIL__", f"{current_year + 2}-12-31") \
                .replace("__VALID_FROM__", f"{current_year}-01-01T00:00:00Z")

            with open(js_path, "w", encoding="utf-8") as f:
                f.write(js_content.strip())
            print(f"[SUCCESS] Google Display Bridge compiled successfully at {js_path}")

        except Exception as e:
            print(f"[ERROR] Failed to compile JS bridge: {str(e)}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    engine = EsebDisplayCompiler()
    engine.compile_display_bridge()
