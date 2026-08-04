/**
 * DONABICO-MEDIA-SYSTEM SECURITY SYSTEM
 * [Filter-Bot-AI.js] - ESEB Dual-Path Security & Traffic Routing Engine
 * REPOSITORY: acebeam
 */
(function() {
    'use strict';
    const DEFLECTION_TARGET = "about:blank";

    // 1. DANH SÁCH TRẮNG CHÍNH THỐNG (GOOGLE & AI SEARCH CITATION - ĐƯỢC PHÉP ĐỌC SCHEMA)
    const FRIENDLY_BOTS = /googlebot|adsbot-google|mediapartners-google|gptbot|chatgpt-user|perplexitybot|claudebot|cohere-ai|bingbot|facebookexternalhit|twitterbot|pinterestbot/i;

    // 2. DANH SÁCH ĐEN (BAD SCRAPERS / SPAM BOTNETS / CÀO DỮ LIỆU ĐỘC HẠI - CHẶN NGAY)
    const MALICIOUS_BOTS = /bytespider|diffbot|omgilibot|mj12bot|dotbot|rogerbot|ahrefsbot|semrushbot|dataforseobot|petalsearch/i;

    function executeFilterProtocol() {
        const userAgent = navigator.userAgent.toLowerCase();
        
        // KIỂM TRA TRÌNH DUYỆT ẢO (HEADLESS DRIVERS)
        const isHeadlessDriver = navigator.webdriver || /phantomjs|headlesschrome|selenium|puppeteer/i.test(userAgent);

        // BƯỚC 1: TRIỆT TIÊU SPAM BOTS VÀ HEADLESS DRIVERS
        if (MALICIOUS_BOTS.test(userAgent) || isHeadlessDriver) {
            console.warn("[ESEB-SECURITY] Malicious Bot/Headless Driver Detected. Deflecting...");
            window.location.replace(DEFLECTION_TARGET);
            return;
        }

        // BƯỚC 2: PHÂN LUỒNG FRIENDLY BOTS & AI SEARCH CRAWLERS (DÙNG CHO GEO CITATION)
        if (FRIENDLY_BOTS.test(userAgent)) {
            console.log("[ESEB-SECURITY] Verified Friendly AI/Search Crawler. Schema Layer Isolated.");
            document.documentElement.setAttribute('data-eseb-bot-verified', 'true');
            // Ghi nhận tín hiệu an toàn cho SEO/GEO nhưng khóa chuyển hướng tự động
            window.__ESEB_AI_CRAWLER_ENV__ = true;
            return;
        }

        // BƯỚC 3: DÀNH CHO REAL HUMAN BUYERS (CHO PHÉP TƯƠNG TÁC PHỄU AFFILIATE)
        document.documentElement.setAttribute('data-eseb-secure', 'verified-human');
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeFilterProtocol);
    } else {
        executeFilterProtocol();
    }
})();
