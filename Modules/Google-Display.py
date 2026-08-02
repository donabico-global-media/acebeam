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
        self.primary_domain = "donabico.com"
        self.brand_organization = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = "DONABICO SEARCH & DISPLAY MATRIX"
        
        # Nhận diện Repository Name
        raw_repo = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/acebeam")
        self.repo_name = raw_repo.split("/")[-1].lower().replace("-", "").replace("_", "")
        
        # Build Timestamp làm dấu ấn thời gian thực (Ép Git nhận diện thay đổi)
        self.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self.brand_config = self._resolve_configuration()

    def _resolve_configuration(self):
        custom_affiliate_env = os.getenv("AFFILIATE_TARGET_URL", "").strip()
        
        brand_database = {
            "acebeam": {
                "name": "Acebeam Tactical North America",
                "affiliate": "https://acebeamflashlight.sjv.io/donabio_global_media",
                "canonical": f"https://acebeam.{self.primary_domain}"
            },
            "8000kicks": {
                "name": "8000kicks Waterproof Hemp Shoes",
                "affiliate": "https://8000kicks.com/?ref=donabico",
                "canonical": f"https://8000kicks.{self.primary_domain}"
            }
        }
        
        selected = brand_database.get(self.repo_name, {
            "name": f"{self.repo_name.upper()} Authorized Hub",
            "affiliate": f"https://{self.primary_domain}/shop/{self.repo_name}",
            "canonical": f"https://{self.repo_name}.{self.primary_domain}"
        })

        if custom_affiliate_env:
            selected["affiliate"] = custom_affiliate_env

        return selected

    def compile_display_bridge(self):
        try:
            # Khởi tạo đúng thư mục Bridges theo cấu trúc hệ thống cũ
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
                    "name": CONFIG.brandName + " - Certified Display Hub",
                    "publisher": {{ "@id": CONFIG.primaryDomain + "/#organization" }}
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
