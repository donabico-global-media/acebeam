# -*- coding: utf-8 -*-
# [EATHESEN-SYSTEM-IDENTITY]: ESEB CORE GENERATOR (PURE TELEMETRY - NO UI)
# [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE

import os
import json
import time

def build_eseb_js_bridge():
    """Biên dịch Bridges/Super-Core-Affiliate.js CHỈ phát tín hiệu Telemetry ngầm"""
    output_dir = "Bridges"
    os.makedirs(output_dir, exist_ok=True)
    
    config_path = "Protocols/eseb_global_config.json"
    default_target = "https://donabico-global-media.github.io/shop/8000kicks.html"
    indexnow_key = "aeth24e38f9024240000000000000000"
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                default_target = cfg.get("affiliate_link", default_target)
                indexnow_key = cfg.get("indexnow_key", indexnow_key)
        except Exception:
            pass

    current_timestamp = int(time.time())

    # Mã JS IIFE CHỈ BƠM TÍN HIỆU TELEMETRY (KHÔNG CHÈN HTML/CSS VÀO TRANG)
    js_payload = f"""/**
 * ESEB AUTO-GENERATED JS BRIDGE - PURE BACKGROUND TELEMETRY
 * SYSTEM: DONABICO GLOBAL MEDIA SYSTEM
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 * TIMESTAMP: {current_timestamp}
 */
(function() {{
    'use strict';
    const CONFIG = {{
        targetUrl: "{default_target}",
        indexKey: "{indexnow_key}"
    }};

    function dispatchGlobalBigTechTelemetry() {{
        const host = window.location.hostname;
        if (!host || host.includes("localhost") || host.includes("127.0.0.1")) return;

        const currentUrl = window.location.href;
        const encodedUrl = encodeURIComponent(currentUrl);

        // 1. CỔNG INDEXNOW DIRECT REST API (Bing, Yandex, IndexNow, Seznam)
        const indexNowPayload = {{
            host: host,
            key: CONFIG.indexKey,
            keyLocation: `https://${{host}}/${{CONFIG.indexKey}}.txt`,
            urlList: [currentUrl, `https://${{host}}/index.html`]
        }};

        const indexNowEndpoints = [
            "https://api.indexnow.org/indexnow",
            "https://bing.com/indexnow",
            "https://yandex.com/indexnow",
            "https://search.seznam.cz/indexnow"
        ];

        indexNowEndpoints.forEach(ep => {{
            try {{
                fetch(ep, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json; charset=utf-8' }},
                    body: JSON.stringify(indexNowPayload),
                    mode: 'no-cors'
                }}).catch(() => {{}});
            }} catch(e) {{}}
        }});

        // 2. CỔNG PING BEACON (Google, Baidu, Yahoo)
        const pingEndpoints = [
            `https://www.google.com/ping?sitemap=${{encodedUrl}}`,
            `https://www.bing.com/ping?sitemap=${{encodedUrl}}`,
            `https://www.baidu.com/ping?sitemap=${{encodedUrl}}`,
            `https://search.yahoo.com/ping?sitemap=${{encodedUrl}}`
        ];

        pingEndpoints.forEach(url => {{
            try {{
                if (navigator.sendBeacon) {{
                    navigator.sendBeacon(url);
                }} else {{
                    const img = new Image();
                    img.src = url;
                }}
            }} catch(e) {{}}
        }});

        // 3. CỔNG SOCIAL CRAWLER CACHE (Facebook, Twitter, LinkedIn, Pinterest)
        const crawlerEndpoints = [
            `https://graph.facebook.com/?id=${{encodedUrl}}&scrape=true`,
            `https://cards-dev.twitter.com/validator?url=${{encodedUrl}}`,
            `https://www.linkedin.com/count/serv/count?url=${{encodedUrl}}`,
            `https://widgets.pinterest.com/v1/urls/count.json?url=${{encodedUrl}}`
        ];

        crawlerEndpoints.forEach(ep => {{
            try {{
                fetch(ep, {{ mode: 'no-cors' }}).catch(() => {{}});
            }} catch(e) {{}}
        }});
    }}

    // CHẠY NGẦM THẦM LẶNG - KHÔNG CHÈN HTML THỪA
    if (document.readyState === "loading") {{
        document.addEventListener("DOMContentLoaded", dispatchGlobalBigTechTelemetry);
    }} else {{
        dispatchGlobalBigTechTelemetry();
    }}
}})();"""

    target_file = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_payload.strip())
        
    print(f"[SUCCESS] ESEB Engine compiled PURE TELEMETRY: {target_file}")

if __name__ == "__main__":
    build_eseb_js_bridge()
