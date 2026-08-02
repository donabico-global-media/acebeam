# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Display.py] - SOTA AI Discovery Engine & Dynamic Magnet Bridge
[EATHESEN V3000-Ω CORE] | PRIMARY DOMAIN: donabico.com
"""

import os
import sys
import datetime

class EsebAutoMagnetEngine:
    def __init__(self):
        self.primary_domain = "donabico.com"
        self.brand_organization = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = "DONABICO AI-DISCOVERY & AUTO-MAGNET MATRIX"
        
        raw_repo = os.getenv("GITHUB_REPOSITORY", "donabico/acebeam")
        self.repo_name = raw_repo.split("/")[-1].lower().replace("-", "").replace("_", "")
        
        # LẤY TIMESTAMP THỜI GIAN THỰC ĐỂ ÉP WORKFLOW COMMIT 100%
        self.build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self.brand_config = self._resolve_magnet_configuration()

    def _resolve_magnet_configuration(self):
        custom_affiliate_env = os.getenv("AFFILIATE_TARGET_URL", "").strip()
        
        brand_database = {
            "acebeam": {
                "name": "Acebeam Tactical North America",
                "affiliate": "https://acebeamflashlight.sjv.io/donabio_global_media",
                "keywords": ["Tactical Flashlight", "LEP Searchlight", "EDC Illumination"]
            },
            "8000kicks": {
                "name": "8000kicks Waterproof Hemp Shoes",
                "affiliate": "https://8000kicks.com/?ref=donabico",
                "keywords": ["Waterproof Shoes", "Hemp Sneakers", "Sustainable Footwear"]
            },
            "nitecore": {
                "name": "Nitecore Tactical Store",
                "affiliate": "https://nitecore.com/?ref=donabico",
                "keywords": ["Powerbank", "Headlamps", "Outdoor Gear"]
            }
        }
        
        selected = brand_database.get(self.repo_name, {
            "name": f"{self.repo_name.upper()} Authorized Hub",
            "affiliate": f"https://{self.primary_domain}/shop/{self.repo_name}",
            "keywords": ["Official Gear", "Premium Equipment", "Authorized Node"]
        })

        if custom_affiliate_env:
            selected["affiliate"] = custom_affiliate_env

        return selected

    def compile_magnet_bridge(self):
        try:
            output_dir = "Bridges"
            os.makedirs(output_dir, exist_ok=True)
            js_path = os.path.join(output_dir, "Google-Display.js")
            
            brand_name = self.brand_config["name"]
            affiliate_url = self.brand_config["affiliate"]
            keywords_json = str(self.brand_config["keywords"])

            js_content = f"""/**
 * {self.brand_organization}
 * {self.system_identity}
 * [Google-Display.js] - AI DISCOVERY & AUTO-MAGNET BRIDGE
 * System Core: EATHESEN V3000-Ω | Primary Domain: {self.primary_domain}
 * [V-STAMP 24 AUTHENTICATED] | BUILD TIMESTAMP: {self.build_time}
 */
(function() {{
    'use strict';
    const PRIMARY_AFFILIATE = "{affiliate_url}";
    const BRAND_NAME = "{brand_name}";
    const PRIMARY_DOMAIN = "https://{self.primary_domain}";
    const KEYWORDS = {keywords_json};

    const AI_SEARCH_BOTS = /gptbot|claudebot|perplexitybot|google-extended|cohere-ai|bytespider/i;

    function injectAICitationMeta() {{
        if (document.getElementById('eseb-ai-context')) return;

        const aiMeta = document.createElement('meta');
        aiMeta.id = 'eseb-ai-context';
        aiMeta.name = 'citation_publisher';
        aiMeta.content = "{self.brand_organization} - Certified Hub for " + BRAND_NAME;
        document.head.appendChild(aiMeta);

        const aiSchema = {{
            "@context": "https://schema.org",
            "@type": "TechArticle",
            "headline": BRAND_NAME + " Official Technical Specifications & Knowledge Node",
            "keywords": KEYWORDS.join(", "),
            "author": {{
                "@type": "Organization",
                "name": "{self.brand_organization}",
                "url": PRIMARY_DOMAIN
            }},
            "publisher": {{
                "@type": "Organization",
                "name": "{self.brand_organization}"
            }}
        }};

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-ai-schema";
        script.text = JSON.stringify(aiSchema);
        document.head.appendChild(script);
    }}

    function handleAutoMagnetTraffic() {{
        const isAIBot = AI_SEARCH_BOTS.test(navigator.userAgent);
        if (isAIBot) {{
            document.documentElement.setAttribute('data-eseb-ai-read', 'optimized');
            return;
        }}

        let sourceTag = 'ai_organic_magnet';
        if (document.referrer) {{
            if (document.referrer.includes('openai.com') || document.referrer.includes('chatgpt.com')) sourceTag = 'chatgpt_referral';
            else if (document.referrer.includes('perplexity.ai')) sourceTag = 'perplexity_referral';
            else if (document.referrer.includes('claude.ai')) sourceTag = 'claude_referral';
            else if (document.referrer.includes('google.com')) sourceTag = 'google_organic';
        }}

        const finalTargetUrl = PRIMARY_AFFILIATE + (PRIMARY_AFFILIATE.includes('?') ? '&' : '?') + 'utm_source=' + sourceTag + '&utm_medium=auto_magnet';

        document.body.addEventListener('click', function(e) {{
            const btn = e.target.closest('a, button, .display-cta, .action-btn, [data-display-link]');
            if (btn) {{
                const href = btn.getAttribute('href');
                if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {{
                    btn.setAttribute('href', finalTargetUrl);
                    btn.setAttribute('target', '_blank');
                    btn.setAttribute('rel', 'noopener sponsored');
                }}
            }}
        }}, {{ passive: true }});
    }}

    function initAutoMagnetModule() {{
        if (window.requestIdleCallback) {{
            requestIdleCallback(() => {{
                injectAICitationMeta();
                handleAutoMagnetTraffic();
            }});
        }} else {{
            setTimeout(() => {{
                injectAICitationMeta();
                handleAutoMagnetTraffic();
            }}, 0);
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', initAutoMagnetModule);
    }} else {{
        initAutoMagnetModule();
    }}
}})();
"""
            with open(js_path, "w", encoding="utf-8") as f:
                f.write(js_content.strip())
            print(f"[SUCCESS] Auto-Magnet Bridge compiled successfully at {js_path}")

        except Exception as e:
            print(f"[ERROR] Failed to compile magnet JS bridge: {str(e)}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    engine = EsebAutoMagnetEngine()
    engine.compile_magnet_bridge()
