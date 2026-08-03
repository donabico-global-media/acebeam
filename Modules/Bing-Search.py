# -*- coding: utf-8 -*-
import os
import datetime

def compile_bing_search_bridge():
    """
    ESEB Engine: Auto-detects repository context and compiles 
    the dynamic client-side JS bridge for Microsoft Bing & GEO optimization.
    """
    # 1. Tự động nhận diện ngữ cảnh Repository từ môi trường GitHub
    repo_raw = os.environ.get("GITHUB_REPOSITORY", "DONABICO/Universal-Store")
    repo_name = repo_raw.split("/")[-1] if "/" in repo_raw else repo_raw
    brand_title = repo_name.replace("-", " ").replace("_", " ").title()
    
    # 2. Đảm bảo thư mục Bridges/ tồn tại
    os.makedirs("Bridges", exist_ok=True)
    bridge_path = os.path.join("Bridges", "Bing-Search.js")
    
    # TimeStamp Freshness Signal
    build_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # 3. Biên dịch mã nguồn JavaScript (Client-side IIFE)
    js_content = f"""/**
 * [ESEB AUTO-GENERATED BRIDGE] - Bing Search & GEO Baiting Protocol
 * Organization : DONABICO GLOBAL MEDIA SYSTEM
 * Target Brand : {brand_title}
 * Build Stamp  : {build_time}
 * Security     : V-STAMP 24 AUTHENTICATED | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';

    // A. Dynamic Verification & Meta Injection (Bot Safe)
    function injectBingVerification() {{
        if (!document.querySelector('meta[name="msvalidate.01"]')) {{
            const meta = document.createElement('meta');
            meta.name = 'msvalidate.01';
            meta.content = 'BING-MATRIX-ACTIVE-2026';
            document.head.appendChild(meta);
        }}
    }}

    // B. GEO & Semantic Entity Injection (Microsoft IndexNow / BingBot Context)
    function injectBingSchema() {{
        if (document.getElementById('eseb-bing-geo-schema')) return;

        const currentDomain = window.location.origin;
        const schemaData = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "Organization",
                    "@id": currentDomain + "/#organization",
                    "name": "DONABICO GLOBAL MEDIA SYSTEM",
                    "url": currentDomain
                }},
                {{
                    "@type": "WebSite",
                    "@id": currentDomain + "/#website",
                    "url": currentDomain,
                    "name": "{brand_title} Official Network",
                    "publisher": {{
                        "@id": currentDomain + "/#organization"
                    }}
                }}
            ]
        }};

        const script = document.createElement('script');
        script.id = 'eseb-bing-geo-schema';
        script.type = 'application/ld+json';
        script.text = JSON.stringify(schemaData);
        document.head.appendChild(script);
    }}

    // C. Client Execution
    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', function() {{
            injectBingVerification();
            injectBingSchema();
        }});
    }} else {{
        injectBingVerification();
        injectBingSchema();
    }}
}})();
"""

    # 4. Ghi đè/Xuất bản tệp JS Bridge (Zero-Entropy)
    with open(bridge_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"[ESEB SUCCESS] Successfully compiled {bridge_path} for Brand: '{brand_title}'")

if __name__ == "__main__":
    compile_bing_search_bridge()
