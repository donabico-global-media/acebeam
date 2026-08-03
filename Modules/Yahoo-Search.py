# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Yahoo-Search.py] - YAHOO CRAWLER SENTINEL & INDEXING ENGINE
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os
from bs4 import BeautifulSoup

class ESEBYahooEngine:
    def __init__(self):
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-media-system")
        self.repo_raw = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/acebeam")
        self.repo_name = self.repo_raw.split("/")[-1] if "/" in self.repo_raw else self.repo_raw
        self.brand_title = self.repo_name.replace("-", " ").replace("_", " ").title()
        
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.active_border = "#10B981"  # Viền xanh lá cây active-modules

    def inject_yahoo_sentinel(self):
        """
        Gắn thẻ Sentinel nhận diện Yahoo Crawler vào file HTML mục tiêu
        """
        index_path = os.environ.get("TARGET_INDEX_HTML", "index.html")
        if not os.path.exists(index_path):
            print(f"[Yahoo-Search] WARNING: Không tìm thấy tệp {index_path}, bỏ qua bước inject HTML.")
            return

        with open(index_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        # Tìm container chính hoặc body nếu không có div.container
        container = soup.find("div", class_="container") or soup.body
        if container and not soup.find(id="yahoo-index-sentinel"):
            sentinel = soup.new_tag("span", id="yahoo-index-sentinel", style="display:none !important;")
            sentinel.string = f"YAHOO-INDEXING-MATRIX-{self.repo_name.upper()}-2026"
            container.append(sentinel)
            
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"[Yahoo-Search] Gắn mã nhận diện Yahoo Crawler thành công vào {index_path}.")
        else:
            print("[Yahoo-Search] Sentinel đã tồn tại hoặc không tìm thấy thẻ container/body.")

    def compile_yahoo_bridge(self):
        """
        Biên dịch tệp JavaScript Bridge cho Yahoo Crawler & GEO Indexing
        """
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Yahoo-Search.js"

        js_content = f"""/**
 * {self.brand_name}
 * [Yahoo-Search.js] - YAHOO SEARCH & SLURP CRAWLER INDEXING BRIDGE
 * Target Brand : {self.brand_title}
 * Generated Automatically via YAHOO SEARCH PROTOCOL
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';
    const SOTA_BORDER = "{self.active_border}";
    const BRAND_NAME = "{self.brand_name}";
    const YAHOO_BOTS = /slurp|yahoo|yahoosearch|yahoo-blogs/i;

    function injectYahooSchema() {{
        if (document.getElementById('eseb-yahoo-geo-schema')) return;

        const currentDomain = window.location.origin;
        const schemaData = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "Organization",
                    "@id": currentDomain + "/#organization",
                    "name": BRAND_NAME,
                    "url": currentDomain
                }},
                {{
                    "@type": "WebPage",
                    "@id": currentDomain + "/#webpage",
                    "url": window.location.href,
                    "name": document.title || "{self.brand_title} Official Network",
                    "isPartOf": {{
                        "@id": currentDomain + "/#website"
                    }},
                    "about": {{
                        "@id": currentDomain + "/#organization"
                    }}
                }}
            ]
        }};

        const script = document.createElement('script');
        script.id = 'eseb-yahoo-geo-schema';
        script.type = 'application/ld+json';
        script.text = JSON.stringify(schemaData);
        document.head.appendChild(script);
    }}

    function executeYahooProtocol() {{
        injectYahooSchema();
        const isYahooBot = YAHOO_BOTS.test(navigator.userAgent);

        if (isYahooBot) {{
            document.documentElement.setAttribute('data-yahoo-index', 'active');
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeYahooProtocol);
    }} else {{
        executeYahooProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Yahoo-Search] ESEB Yahoo Bridge được khởi tạo thành công tại {js_path}")

if __name__ == "__main__":
    engine = ESEBYahooEngine()
    engine.inject_yahoo_sentinel()
    engine.compile_yahoo_bridge()
