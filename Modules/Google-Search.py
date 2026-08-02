# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Search.py] - SOTA Universal Organic Search & Dynamic Schema Inception Engine
[EATHESEN V3000-Ω CORE] | ¢24 IMMUTABLE | PRIMARY DOMAIN: donabico.com
[V-STAMP 24 AUTHENTICATED]
"""

import os

class EsebSearchMatrixEngine:
    def __init__(self):
        # 1. ĐỊNH DANH THỰC THỂ CỐT LÕI (IMMUTABLE ANCHOR)
        self.primary_domain = "donabico.com"
        self.brand_organization = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = "DONABICO SEARCH MATRIX"
        
        # 2. TỰ ĐỘNG KHÁM PHÁ MÔI TRƯỜNG REPOSITORY (UBARP PROTOCOL)
        raw_repo = os.getenv("GITHUB_REPOSITORY", "donabico/acebeam")
        self.repo_name = raw_repo.split("/")[-1].lower().replace("-", "").replace("_", "")
        
        # 3. MA TRẬN DỮ LIỆU THƯƠNG HIỆU TỰ ĐỘNG
        self.brand_config = self._resolve_brand_configuration()

    def _resolve_brand_configuration(self):
        """
        Giao thức tự động tra cứu thương hiệu theo Repo Name.
        Hỗ trợ biến môi trường AFFILIATE_TARGET_URL để ghi đè link linh hoạt.
        """
        custom_affiliate_env = os.getenv("AFFILIATE_TARGET_URL", "").strip()
        
        brand_database = {
            "acebeam": {
                "name": "Acebeam Tactical North America",
                "affiliate": "https://acebeamflashlight.sjv.io/donabio_global_media",
                "subdomain": f"https://acebeam.{self.primary_domain}",
                "currency": "USD",
                "price": "99.95"
            },
            "8000kicks": {
                "name": "8000kicks Waterproof Hemp Shoes",
                "affiliate": "https://8000kicks.com/?ref=donabico",
                "subdomain": f"https://8000kicks.{self.primary_domain}",
                "currency": "USD",
                "price": "135.00"
            },
            "nitecore": {
                "name": "Nitecore Tactical Store",
                "affiliate": "https://nitecore.com/?ref=donabico",
                "subdomain": f"https://nitecore.{self.primary_domain}",
                "currency": "USD",
                "price": "89.90"
            }
        }
        
        # Cơ chế Fallback tự động khởi tạo dữ liệu chuẩn cho kho mới chưa khai báo
        selected = brand_database.get(self.repo_name, {
            "name": f"{self.repo_name.upper()} Official Authorized Hub",
            "affiliate": f"https://{self.primary_domain}/shop/{self.repo_name}",
            "subdomain": f"https://{self.repo_name}.{self.primary_domain}",
            "currency": "USD",
            "price": "49.99"
        })

        if custom_affiliate_env:
            selected["affiliate"] = custom_affiliate_env

        return selected

    def compile_search_core(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Search.js"
        
        brand_name = self.brand_config["name"]
        affiliate_url = self.brand_config["affiliate"]
        subdomain_url = self.brand_config["subdomain"]
        currency = self.brand_config["currency"]
        price = self.brand_config["price"]

        js_content = f"""/**
 * {self.brand_organization}
 * {self.system_identity}
 * [Google-Search.js] - ESEB SOTA Organic Search & Merchant Schema Bridge
 * System Core: EATHESEN V3000-Ω | Primary Domain: {self.primary_domain}
 * Generated Automatically via GOOGLE SEARCH PROTOCOL
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';

    const CONFIG = {{
        orgName: "{self.brand_organization}",
        brandName: "{brand_name}",
        primaryDomain: "https://{self.primary_domain}",
        subDomain: "{subdomain_url}",
        affiliateTarget: "{affiliate_url}",
        price: "{price}",
        currency: "{currency}"
    }};

    // SOTA Bot Detection Matrix (Crawler & AI Search Engine Bots)
    const SEARCH_BOTS = /googlebot|bingbot|yandexbot|baiduspider|duckduckbot|gptbot|claudebot|perplexitybot/i;

    function injectDynamicSchemaGraph() {{
        if (document.getElementById('eseb-sota-schema-graph')) return;

        const currentOrigin = window.location.origin;

        const schemaGraph = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "Organization",
                    "@id": CONFIG.primaryDomain + "/#organization",
                    "name": CONFIG.orgName,
                    "url": CONFIG.primaryDomain,
                    "logo": CONFIG.primaryDomain + "/assets/logo.png",
                    "sameAs": [
                        "https://x.com/donabico",
                        "https://facebook.com/donabico"
                    ]
                }},
                {{
                    "@type": "WebSite",
                    "@id": currentOrigin + "/#website",
                    "url": currentOrigin,
                    "name": CONFIG.brandName,
                    "publisher": {{ "@id": CONFIG.primaryDomain + "/#organization" }},
                    "potentialAction": {{
                        "@type": "SearchAction",
                        "target": currentOrigin + "/?s={{search_term_string}}",
                        "query-input": "required name=search_term_string"
                    }}
                }},
                {{
                    "@type": "Product",
                    "@id": currentOrigin + "/#primary-product",
                    "name": CONFIG.brandName,
                    "image": CONFIG.primaryDomain + "/assets/product-hero.png",
                    "description": CONFIG.brandName + " - Official Authorized Node under DONABICO GLOBAL MEDIA SYSTEM.",
                    "brand": {{
                        "@type": "Brand",
                        "name": CONFIG.brandName
                    }},
                    "offers": {{
                        "@type": "Offer",
                        "url": CONFIG.affiliateTarget,
                        "priceCurrency": CONFIG.currency,
                        "price": CONFIG.price,
                        "priceValidUntil": "2028-12-31",
                        "itemCondition": "https://schema.org/NewCondition",
                        "availability": "https://schema.org/InStock",
                        "seller": {{ "@id": CONFIG.primaryDomain + "/#organization" }},
                        "shippingDetails": {{
                            "@type": "OfferShippingDetails",
                            "shippingRate": {{
                                "@type": "MonetaryAmount",
                                "value": "0.00",
                                "currency": CONFIG.currency
                            }},
                            "shippingDestination": [
                                {{ "@type": "DefinedRegion", "addressCountry": "US" }},
                                {{ "@type": "DefinedRegion", "addressCountry": "CA" }}
                            ],
                            "deliveryTime": {{
                                "@type": "ShippingDeliveryTime",
                                "handlingTime": {{
                                    "@type": "QuantitativeValue",
                                    "minValue": 1,
                                    "maxValue": 2,
                                    "unitCode": "DAY"
                                }},
                                "transitTime": {{
                                    "@type": "QuantitativeValue",
                                    "minValue": 3,
                                    "maxValue": 5,
                                    "unitCode": "DAY"
                                }}
                            }}
                        }},
                        "hasMerchantReturnPolicy": {{
                            "@type": "MerchantReturnPolicy",
                            "applicableCountry": ["US", "CA"],
                            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
                            "merchantReturnDays": 30,
                            "returnMethod": "https://schema.org/ReturnByMail",
                            "returnFees": "https://schema.org/FreeReturn"
                        }}
                    }}
                }},
                {{
                    "@type": "FAQPage",
                    "mainEntity": [
                        {{
                            "@type": "Question",
                            "name": "How does DONABICO verify " + CONFIG.brandName + " products?",
                            "acceptedAnswer": {{
                                "@type": "Answer",
                                "text": "DONABICO GLOBAL MEDIA SYSTEM operates an authenticated digital node ensuring direct manufacturer redirection and global warranty routing."
                            }}
                        }}
                    ]
                }}
            ]
        }};

        const scriptTag = document.createElement("script");
        scriptTag.id = "eseb-sota-schema-graph";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        document.head.appendChild(scriptTag);
    }}

    function executeInceptionProtocol() {{
        injectDynamicSchemaGraph();

        const isBot = SEARCH_BOTS.test(navigator.userAgent);
        
        if (isBot) {{
            document.documentElement.setAttribute('data-eseb-sota-bot', 'verified');
        }} else {{
            // Phễu Siphon Organic Users về Link Affiliate Đích
            const ctaElements = document.querySelectorAll('a, button, .action-btn, .cta-link');
            ctaElements.forEach(element => {{
                const href = element.getAttribute('href');
                if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {{
                    element.setAttribute('href', CONFIG.affiliateTarget);
                    element.setAttribute('target', '_blank');
                    element.setAttribute('rel', 'noopener sponsored');
                }}
            }});
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeInceptionProtocol);
    }} else {{
        executeInceptionProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
            
        print(f"✅ [SOTA_SUCCESS] Core Bridge Generated: {js_path}")
        print(f"   ├─ Primary Domain Locked: {self.primary_domain}")
        print(f"   ├─ Target Repo Node: {self.repo_name}")
        print(f"   └─ Resolved Brand: {brand_name}")

if __name__ == "__main__":
    engine = EsebSearchMatrixEngine()
    engine.compile_search_core()
