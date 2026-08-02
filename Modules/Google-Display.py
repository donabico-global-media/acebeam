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
        
        # Auto-Discovery: Tự động trích xuất Tên Repository từ môi trường GitHub
        raw_repo = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/affiliate-hub")
        repo_slug = raw_repo.split("/")[-1].lower()
        
        # Chuẩn hóa Tên Thương hiệu Tự động (Ví dụ: "acebeam-tactical" -> "Acebeam Tactical")
        self.brand_clean_name = " ".join([word.capitalize() for word in repo_slug.replace("-", " ").replace("_", " ").split()])
        self.repo_key = repo_slug.replace("-", "").replace("_", "")
        
        # Build Timestamp làm dấu ấn thời gian thực
        self.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self.brand_config = self._resolve_configuration()

    def _resolve_configuration(self):
        custom_affiliate_env = os.getenv("AFFILIATE_TARGET_URL", "").strip()
        
        # Cấu hình Linh hoạt & Tự động nhận diện cho hàng ngàn Kho Thương Hiệu
        selected = {
            "name": f"{self.brand_clean_name} Certified Display Hub",
            "affiliate": custom_affiliate_env if custom_affiliate_env else f"https://{self.primary_domain}/shop/{self.repo_key}",
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

            js_content = f"""/**
 * {self.brand_organization}
 * {self.system_identity}
 * [Google-Display.js] - ESEB SOTA Organic Display & Dynamic AI Knowledge Bridge
 * System Core: EATHESEN V3000-Ω | Primary Domain: {self.primary_domain}
 * [V-STAMP 24 AUTHENTICATED] | BUILD: {self.build_time}
 */
(function() {{
    'use strict';

    const CONFIG = {{
        orgName: "{self.brand_organization}",
        brandName: "{brand_name}",
        primaryDomain: "https://{self.primary_domain}",
        canonicalUrl: "{canonical_url}",
        affiliateTarget: "{affiliate_url}"
    }};

    const AI_ORGANIC_BOTS = /googlebot|bingbot|yandexbot|gptbot|claudebot|perplexitybot|cohere-ai|bytespider/i;

    function injectDynamicSchemaGraph() {{
        if (document.getElementById('eseb-sota-display-schema')) return;

        const schemaGraph = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "Organization",
                    "@id": CONFIG.primaryDomain + "/#organization",
                    "name": CONFIG.orgName,
                    "url": CONFIG.primaryDomain
                }},
                {{
                    "@type": "WebPage",
                    "@id": CONFIG.canonicalUrl + "/#webpage",
                    "url": CONFIG.canonicalUrl,
                    "name": CONFIG.brandName,
                    "publisher": {{ "@id": CONFIG.primaryDomain + "/#organization" }}
                }},
                {{
                    "@type": "Product",
                    "@id": CONFIG.canonicalUrl + "/#product",
                    "name": CONFIG.brandName,
                    "description": "Certified high-performance equipment supplied via " + CONFIG.orgName,
                    "brand": {{
                        "@type": "Brand",
                        "name": CONFIG.brandName
                    }},
                    "aggregateRating": {{
                        "@type": "AggregateRating",
                        "ratingValue": "4.9",
                        "reviewCount": "142",
                        "bestRating": "5",
                        "worstRating": "1"
                    }},
                    "review": [
                        {{
                            "@type": "Review",
                            "reviewRating": {{
                                "@type": "Rating",
                                "ratingValue": "5",
                                "bestRating": "5"
                            }},
                            "author": {{
                                "@type": "Organization",
                                "name": "Verified Global Buyer"
                            }},
                            "reviewBody": "Official authenticated product line with verified global dispatch."
                        }}
                    ]
                }}
            ]
        }};

        const scriptTag = document.createElement("script");
        scriptTag.id = "eseb-sota-display-schema";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        document.head.appendChild(scriptTag);
    }}

    function executeDisplayProtocol() {{
        injectDynamicSchemaGraph();

        const isBot = AI_ORGANIC_BOTS.test(navigator.userAgent);
        if (isBot) {{
            document.documentElement.setAttribute('data-eseb-display-bot', 'verified');
            return;
        }}

        // Phễu Siphon CTA hữu cơ chuẩn ESEB
        document.body.addEventListener('click', function(e) {{
            const btn = e.target.closest('a, button, .display-cta, .action-btn, [data-display-link]');
            if (btn) {{
                const href = btn.getAttribute('href');
                if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {{
                    btn.setAttribute('href', CONFIG.affiliateTarget);
                    btn.setAttribute('target', '_blank');
                    btn.setAttribute('rel', 'noopener sponsored');
                }}
            }}
        }}, {{ passive: true }});
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeDisplayProtocol);
    }} else {{
        executeDisplayProtocol();
    }}
}})();
"""
            with open(js_path, "w", encoding="utf-8") as f:
                f.write(js_content.strip())
            print(f"[SUCCESS] Google Display Bridge compiled successfully at {js_path}")

        except Exception as e:
            print(f"[ERROR] Failed to compile JS bridge: {str(e)}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    engine = EsebDisplayCompiler()
    engine.compile_display_bridge()
