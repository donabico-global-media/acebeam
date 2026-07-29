# -*- coding: utf-8 -*-
# [EATHESEN-SYSTEM-IDENTITY]: ESEB CORE GENERATOR
# [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE

import os
import json
import time

def build_eseb_js_bridge():
    """Thực thi biên dịch tự động và ghi đè tệp Bridges/Super-Core-Affiliate.js"""
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

    # Mã JS tự thực thi (IIFE) phát tín hiệu Telemetry & Tự động Render UI nếu DOM rỗng
    js_payload = f"""/**
 * ESEB AUTO-GENERATED JS BRIDGE - ZERO-DOM EXTENSION
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

    function dispatchEdgeTelemetry() {{
        const host = window.location.hostname;
        if (!host || host.includes("localhost") || host.includes("127.0.0.1")) return;

        const payload = {{
            host: host,
            key: CONFIG.indexKey,
            keyLocation: `https://${{host}}/${{CONFIG.indexKey}}.txt`,
            urlList: [window.location.href, `https://${{host}}/index.html`]
        }};

        const endpoints = [
            "https://api.indexnow.org/indexnow",
            "https://bing.com/indexnow",
            "https://yandex.com/indexnow"
        ];

        endpoints.forEach(ep => {{
            try {{
                fetch(ep, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json; charset=utf-8' }},
                    body: JSON.stringify(payload),
                    mode: 'no-cors'
                }}).catch(() => {{}});
            }} catch(e) {{}}
        }});
    }}

    function injectDynamicUI() {{
        if (document.getElementById("eseb-core-root")) return;

        const style = document.createElement("style");
        style.textContent = `
            :root {{ --bg: #0d1117; --card: #161b22; --border: #30363d; --text: #c9d1d9; --accent: #2ea043; }}
            body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; justify-content: center; padding: 40px 20px; margin: 0; }}
            .eseb-card {{ max-width: 800px; width: 100%; background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 30px; box-sizing: border-box; }}
            .eseb-h1 {{ color: #fff; font-size: 22px; border-bottom: 1px solid var(--border); padding-bottom: 12px; margin-top: 0; }}
            .eseb-btn {{ display: block; width: 100%; background: var(--accent); color: #fff; text-align: center; padding: 14px 0; text-decoration: none; font-weight: bold; border-radius: 6px; margin-top: 25px; box-sizing: border-box; }}
            .eseb-ft {{ margin-top: 30px; font-size: 11px; color: #8b949e; text-align: right; border-top: 1px solid var(--border); padding-top: 12px; }}
        `;
        document.head.appendChild(style);

        const container = document.createElement("div");
        container.id = "eseb-core-root";
        container.className = "eseb-card";
        container.innerHTML = `
            <h1 class="eseb-h1">DONABICO GLOBAL MEDIA SYSTEM</h1>
            <p>Hệ thống phân phối nội dung tự động hóa & bơm tín hiệu Indexation trên hạ tầng CDN ngoại biên.</p>
            <a href="${{CONFIG.targetUrl}}" target="_blank" rel="noopener noreferrer sponsored" class="eseb-btn">XEM DỰ ÁN CHI TIẾT</a>
            <div class="eseb-ft">DONABICO GLOBAL MEDIA SYSTEM | [ V-STAMP 24 AUTHENTICATED ]</div>
        `;
        document.body.appendChild(container);
    }}

    document.addEventListener("DOMContentLoaded", function() {{
        dispatchEdgeTelemetry();
        injectDynamicUI();
    }});
}})();"""

    target_file = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(js_payload.strip())
        
    print(f"[SUCCESS] ESEB Engine compiled: {target_file}")

if __name__ == "__main__":
    build_eseb_js_bridge()
