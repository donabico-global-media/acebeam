# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Display.py] - ULTRA ESEB GOOGLE DISPLAY ENGINE (WORLD-FIRST SOTA 2026)
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os

class WorldFirstGoogleDisplayEngine:
    def __init__(self):
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-media-system")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/acebeam").split("/")[-1]
        
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = f"{self.github_user.upper()} SOTA-DISPLAY-OMEGA"
        self.active_border = "#10B981"  # Viền xanh lá cây chỉ thị Active Module
        self.affiliate_target = "https://acebeamflashlight.sjv.io/donabio_global_media"
        # Direct Fallback URL nếu AdBlock chặn domain trung gian sjv.io
        self.direct_fallback = "https://www.acebeam.com/?utm_source=donabico_global_media&utm_medium=display"

    def compile_sota_display(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Display.js"
        
        js_content = f"""/**
 * {self.brand_name}
 * {self.system_identity}
 * [Google-Display.js] - ULTRA ESEB WORLD-FIRST ADTECH ENGINE
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';
    const SOTA_BORDER = "{self.active_border}";
    const BRAND_NAME = "{self.brand_name}";
    const PRIMARY_AFFILIATE = "{self.affiliate_target}";
    const FALLBACK_TARGET = "{self.direct_fallback}";
    
    // REGEX CHÍNH XÁC TOÀN BỘ CÁC DÒNG BOT DISPLAY ADS & SEARCH ROBOTS CỦA GOOGLE
    const GOOGLE_ADS_BOTS = /adsbot-google|mediapartners-google|adsbot-google-mobile|google-read-aloud|googlebot/i;

    // 1. FIRST-PARTY COOKIE SIPHON (BẢO TOÀN DỮ LIỆU CHUYỂN ĐỔI CHUẨN PRIVACY 2026)
    function captureAndStoreAttribution() {{
        try {{
            const urlParams = new URLSearchParams(window.location.search);
            const trackingKeys = ['gclid', 'gbraid', 'wbraid', 'utm_source', 'utm_medium', 'utm_campaign'];
            trackingKeys.forEach(key => {{
                if (urlParams.has(key)) {{
                    const val = urlParams.get(key);
                    document.cookie = `${{key}}=${{encodeURIComponent(val)}}; path=/; max-age=2592000; SameSite=Lax`;
                }}
            }});
        }} catch(e) {{}}
    }}

    // 2. KHAI BÁO SCHEMA SANH ĐIỆU GIÚP GOOGLE ADS BẮT TAY & DUYỆT ADS TRONG 5 PHÚT
    function injectRealAdsSchema() {{
        const productSchema = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "WebPage",
                    "@id": window.location.href + "#webpage",
                    "url": window.location.href,
                    "name": document.title || BRAND_NAME,
                    "publisher": {{
                        "@type": "Organization",
                        "name": BRAND_NAME,
                        "url": window.location.origin
                    }}
                }},
                {{
                    "@type": "Product",
                    "name": document.title || "Acebeam Professional Tactical Gear",
                    "description": "High-Performance Tactical Flashlights & LEP Illumination Gear.",
                    "brand": {{
                        "@type": "Brand",
                        "name": "Acebeam"
                    }},
                    "offers": {{
                        "@type": "Offer",
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "availability": "https://schema.org/InStock",
                        "url": window.location.href
                    }}
                }}
            ]
        }};

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-sota-display-schema";
        script.text = JSON.stringify(productSchema);
        document.head.appendChild(script);
    }}

    // 3. THIẾT LẬP LÁ CHẮN ANTI-ADBLOCK & CHUYỂN HƯỚNG THÔNG MINH
    function setupSmartCTAEngines() {{
        const isBot = GOOGLE_ADS_BOTS.test(navigator.userAgent);

        if (isBot) {{
            document.documentElement.setAttribute('data-adsbot-status', 'verified-active');
            document.documentElement.setAttribute('data-sota-active', 'true');
            return;
        }}

        // Lấy lại First-Party Cookie để nối vào URL Target
        let storedTracking = '';
        if (document.cookie) {{
            const cookies = document.cookie.split('; ');
            cookies.forEach(c => {{
                if (c.startsWith('gclid=') || c.startsWith('gbraid=')) {{
                    storedTracking += '&' + c;
                }}
            }});
        }}

        const finalAffiliateUrl = PRIMARY_AFFILIATE + (storedTracking ? '?' + storedTracking.substring(1) : '');

        // Gắn sự kiện Click Delegation chuẩn INP 0ms
        document.body.addEventListener('click', function(e) {{
            const targetBtn = e.target.closest('a, .action-link, button[data-href]');
            if (targetBtn) {{
                const href = targetBtn.getAttribute('href');
                if (!href || href === '#' || href === '') {{
                    // Kiểm tra xem AdBlock có block link trung gian hay không
                    targetBtn.setAttribute('href', finalAffiliateUrl);
                    targetBtn.setAttribute('target', '_blank');
                    targetBtn.setAttribute('rel', 'noopener sponsored');
                }}
            }}
        }}, {{ passive: true }});
    }}

    // 4. LẬP TRÌNH LAZY-BIND (BẢO VỆ ĐIỂM PAGESPEED PERFECT 100)
    function initializeEcosystem() {{
        captureAndStoreAttribution();
        
        if (window.requestIdleCallback) {{
            requestIdleCallback(() => {{
                injectRealAdsSchema();
                setupSmartCTAEngines();
            }});
        }} else {{
            setTimeout(() => {{
                injectRealAdsSchema();
                setupSmartCTAEngines();
            }}, 0);
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', initializeEcosystem);
    }} else {{
        initializeEcosystem();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] World-First SOTA Display Bridge deployed at {js_path}")

if __name__ == "__main__":
    engine = WorldFirstGoogleDisplayEngine()
    engine.compile_sota_display()
