# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Filter-Bot-AI.py] - ESEB Anti-Spam & AI Dual-Path Filter Engine
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os

class EsebBotFilterEngine:
    def __init__(self):
        # TỰ ĐỘNG NHẬN DIỆN MÔI TRƯỜNG KHO
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-global-media")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/acebeam").split("/")[-1]
        self.brand_name = f"{self.github_user.upper()} SECURITY SYSTEM"
        self.deflection_target = "about:blank"

    def compile_filter_core(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Filter-Bot-AI.js"
        
        js_content = f"""/**
 * {self.brand_name}
 * [Filter-Bot-AI.js] - ESEB Dual-Path Security & Traffic Routing Engine
 * REPOSITORY: {self.repo_name}
 */
(function() {{
    'use strict';
    const DEFLECTION_TARGET = "{self.deflection_target}";

    // 1. DANH SÁCH TRẮNG CHÍNH THỐNG (GOOGLE & AI SEARCH CITATION - ĐƯỢC PHÉP ĐỌC SCHEMA)
    const FRIENDLY_BOTS = /googlebot|adsbot-google|mediapartners-google|gptbot|chatgpt-user|perplexitybot|claudebot|cohere-ai|bingbot|facebookexternalhit|twitterbot|pinterestbot/i;

    // 2. DANH SÁCH ĐEN (BAD SCRAPERS / SPAM BOTNETS / CÀO DỮ LIỆU ĐỘC HẠI - CHẶN NGAY)
    const MALICIOUS_BOTS = /bytespider|diffbot|omgilibot|mj12bot|dotbot|rogerbot|ahrefsbot|semrushbot|dataforseobot|petalsearch/i;

    function executeFilterProtocol() {{
        const userAgent = navigator.userAgent.toLowerCase();
        
        // KIỂM TRA TRÌNH DUYỆT ẢO (HEADLESS DRIVERS)
        const isHeadlessDriver = navigator.webdriver || /phantomjs|headlesschrome|selenium|puppeteer/i.test(userAgent);

        // BƯỚC 1: TRIỆT TIÊU SPAM BOTS VÀ HEADLESS DRIVERS
        if (MALICIOUS_BOTS.test(userAgent) || isHeadlessDriver) {{
            console.warn("[ESEB-SECURITY] Malicious Bot/Headless Driver Detected. Deflecting...");
            window.location.replace(DEFLECTION_TARGET);
            return;
        }}

        // BƯỚC 2: PHÂN LUỒNG FRIENDLY BOTS & AI SEARCH CRAWLERS (DÙNG CHO GEO CITATION)
        if (FRIENDLY_BOTS.test(userAgent)) {{
            console.log("[ESEB-SECURITY] Verified Friendly AI/Search Crawler. Schema Layer Isolated.");
            document.documentElement.setAttribute('data-eseb-bot-verified', 'true');
            // Ghi nhận tín hiệu an toàn cho SEO/GEO nhưng khóa chuyển hướng tự động
            window.__ESEB_AI_CRAWLER_ENV__ = true;
            return;
        }}

        // BƯỚC 3: DÀNH CHO REAL HUMAN BUYERS (CHO PHÉP TƯƠNG TÁC PHỄU AFFILIATE)
        document.documentElement.setAttribute('data-eseb-secure', 'verified-human');
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeFilterProtocol);
    }} else {{
        executeFilterProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] Filter Bot AI Core Bridge compiled successfully at {js_path}")

if __name__ == "__main__":
    engine = EsebBotFilterEngine()
    engine.compile_filter_core()
