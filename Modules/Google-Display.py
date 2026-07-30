# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Display.py] - PURE GOOGLE DISPLAY ADTECH ENGINE (ISOLATED MODULE)
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os

class IsolatedGoogleDisplayEngine:
    def __init__(self):
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-global-media")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/acebeam").split("/")[-1]
        
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = f"{self.github_user.upper()} DISPLAY-ADTECH-MODULE"
        self.affiliate_target = "https://acebeamflashlight.sjv.io/donabio_global_media"
        self.direct_fallback = "https://www.acebeam.com/?utm_source=donabico_global_media&utm_medium=display"

    def compile_display_bridge(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Display.js"
        
        js_content = f"""/**
 * {self.brand_name}
 * {self.system_identity}
 * [Google-Display.js] - PURE ADTECH & BOT HANDSHAKE BRIDGE (ISOLATED FROM CORE)
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';
    const PRIMARY_AFFILIATE = "{self.affiliate_target}";
    const FALLBACK_TARGET = "{self.direct_fallback}";
    
    // BẮT BÓNG GOOGLE ADS BOTS CỤ THỂ
    const GOOGLE_ADS_BOTS = /adsbot-google|mediapartners-google|adsbot-google-mobile/i;

    // 1. FIRST-PARTY COOKIE ATTRIBUTION (BẢO TOÀN GCLID / GBRAID / UTMS)
    function captureGoogleAdsTracking() {{
        try {{
            const urlParams = new URLSearchParams(window.location.search);
            const adKeys = ['gclid', 'gbraid', 'wbraid', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content'];
            adKeys.forEach(key => {{
                if (urlParams.has(key)) {{
                    const val = urlParams.get(key);
                    document.cookie = `${{key}}=${{encodeURIComponent(val)}}; path=/; max-age=2592000; SameSite=Lax`;
                }}
            }});
        }} catch(e) {{}}
    }}

    // 2. KHAI BÁO SCHEMA WEBPAGE CHUẨN ADTECH (KHÔNG BỊ LỖI SEARCH CONSOLE)
    function injectGoogleAdsSchema() {{
        const displaySchema = {{
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": document.title || "Acebeam Professional Flashlight Series",
            "description": "High-Performance Tactical Flashlights & LEP Illumination Gear.",
            "url": window.location.href,
            "publisher": {{
                "@type": "Organization",
                "name": "{self.brand_name}",
                "url": window.location.origin
            }},
            "mainEntity": {{
                "@type": "Thing",
                "name": "Acebeam Tactical Illumination",
                "sameAs": "https://www.acebeam.com/"
            }}
        }};

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-display-ads-schema";
        script.text = JSON.stringify(displaySchema);
        document.head.appendChild(script);
    }}

    // 3. XỬ LÝ TRAFFIC VÀ BẮT TAY GOOGLE ADS BOT
    function handleDisplayTraffic() {{
        const isAdsBot = GOOGLE_ADS_BOTS.test(navigator.userAgent);

        if (isAdsBot) {{
            document.documentElement.setAttribute('data-adsbot-status', 'verified-active');
            return;
        }}

        // Gắn lại tham số GCLID/GBRAID đã lưu vào link đích
        let storedTracking = '';
        if (document.cookie) {{
            const cookies = document.cookie.split('; ');
            cookies.forEach(c => {{
                if (c.startsWith('gclid=') || c.startsWith('gbraid=') || c.startsWith('wbraid=')) {{
                    storedTracking += '&' + c;
                }}
            }});
        }}

        const finalTargetUrl = PRIMARY_AFFILIATE + (storedTracking ? '?' + storedTracking.substring(1) : '');

        document.body.addEventListener('click', function(e) {{
            const btn = e.target.closest('a.display-cta, button.display-cta, [data-display-link]');
            if (btn) {{
                const href = btn.getAttribute('href');
                if (!href || href === '#' || href === '') {{
                    btn.setAttribute('href', finalTargetUrl);
                    btn.setAttribute('target', '_blank');
                    btn.setAttribute('rel', 'noopener sponsored');
                }}
            }}
        }}, {{ passive: true }});
    }}

    // KHỜI CHẠY ĐỘC LẬP
    function initDisplayModule() {{
        captureGoogleAdsTracking();
        
        if (window.requestIdleCallback) {{
            requestIdleCallback(() => {{
                injectGoogleAdsSchema();
                handleDisplayTraffic();
            }});
        }} else {{
            setTimeout(() => {{
                injectGoogleAdsSchema();
                handleDisplayTraffic();
            }}, 0);
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', initDisplayModule);
    }} else {{
        initDisplayModule();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[SUCCESS] Google Display Bridge compiled at {js_path}")

if __name__ == "__main__":
    engine = IsolatedGoogleDisplayEngine()
    engine.compile_display_bridge()
