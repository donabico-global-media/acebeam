# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Shopping-Feed.py] - ULTRA ESEB SHOPPING FEED & BRIDGE ENGINE
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os
import xml.etree.ElementTree as ET

class ESEBShoppingEngine:
    def __init__(self):
        # Tự động bóc tách tên User/Org và Repo từ biến môi trường GitHub Actions
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-media-system")
        self.repo_raw = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/acebeam")
        self.repo_name = self.repo_raw.split("/")[-1] if "/" in self.repo_raw else self.repo_raw
        
        # Biến đổi tên Brand động (Ví dụ: "acebeam" -> "Acebeam", "8000kicks" -> "8000kicks")
        self.brand_title = self.repo_name.replace("-", " ").replace("_", " ").title()
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = f"{self.github_user.upper()} SHOPPING MATRIX"
        
        # Domain & Link Affiliate tự động biến đổi theo repo
        self.domain = f"https://{self.repo_name}.donabico.com"
        self.affiliate_target = f"https://{self.repo_name}.sjv.io/donabio_global_media"
        self.active_border = "#10B981"  # Viền xanh lá cây active-modules

    def generate_shopping_xml(self):
        os.makedirs("Feeds", exist_ok=True)
        xml_path = "Feeds/Shopping-Feed.xml"

        rss = ET.Element("rss", version="2.0")
        rss.set("xmlns:g", "http://base.google.com/ns/1.0")

        channel = ET.SubElement(rss, "channel")
        ET.SubElement(channel, "title").text = f"{self.brand_name} - {self.brand_title} Feed"
        ET.SubElement(channel, "link").text = self.domain
        ET.SubElement(channel, "description").text = f"Automated High-Performance {self.brand_title} Gear Syndication Feed"

        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "g:id").text = f"{self.repo_name.upper()}-TAC-001"
        ET.SubElement(item, "title").text = f"{self.brand_title} Tactical Illumination Gear - Professional Series"
        ET.SubElement(item, "description").text = f"High-Performance {self.brand_title} Tactical Equipment, Search & Outdoor Gear."
        ET.SubElement(item, "link").text = self.domain
        ET.SubElement(item, "g:image_link").text = f"{self.domain}/favicon.ico"
        ET.SubElement(item, "g:availability").text = "in_stock"
        ET.SubElement(item, "g:price").text = "99.95 USD"
        ET.SubElement(item, "g:brand").text = self.brand_title
        ET.SubElement(item, "g:condition").text = "new"
        ET.SubElement(item, "g:shipping_weight").text = "0.5 kg"

        tree = ET.ElementTree(rss)
        ET.indent(tree, space="  ", level=0)
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)
        print(f"[Success] Dynamic Google Merchant XML Feed generated at {xml_path} for '{self.brand_title}'")

    def compile_shopping_bridge(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Shopping.js"

        js_content = f"""/**
 * {self.brand_name}
 * {self.system_identity}
 * [Google-Shopping.js] - REAL GOOGLE SHOPPING FEED & ATTRIBUTION BRIDGE
 * Target Brand : {self.brand_title}
 * Generated Automatically via GOOGLE SHOPPING PROTOCOL
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';
    const SOTA_BORDER = "{self.active_border}";
    const BRAND_NAME = "{self.brand_name}";
    const AFFILIATE_TARGET = "{self.affiliate_target}";
    const SHOPPING_BOTS = /googlebot|adsbot-google|google-merchant|googlebot-shopping/i;

    function injectMerchantSchema() {{
        const schema = {{
            "@context": "https://schema.org",
            "@type": "Product",
            "name": document.title || "{self.brand_title} Tactical Gear",
            "image": [window.location.origin + "/favicon.ico"],
            "description": "High-Performance {self.brand_title} Equipment & Gear Network",
            "sku": "{self.repo_name.upper()}-TAC-001",
            "brand": {{
                "@type": "Brand",
                "name": "{self.brand_title}"
            }},
            "offers": {{
                "@type": "Offer",
                "url": window.location.href,
                "priceCurrency": "USD",
                "price": "99.95",
                "priceValidUntil": "2027-12-31",
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition"
            }},
            "aggregateRating": {{
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "reviewCount": "128",
                "bestRating": "5",
                "worstRating": "1"
            }},
            "review": [
                {{
                    "@type": "Review",
                    "reviewRating": {{
                        "@type": "Rating",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "worstRating": "1"
                    }},
                    "author": {{
                        "@type": "Person",
                        "name": "Tactical Gear Reviewer"
                    }},
                    "reviewBody": "Exceptional brightness, rugged durability and outstanding battery efficiency."
                }}
            ]
        }};
        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-merchant-schema";
        script.text = JSON.stringify(schema);
        document.head.appendChild(script);
    }}

    function executeShoppingProtocol() {{
        injectMerchantSchema();
        const isBot = SHOPPING_BOTS.test(navigator.userAgent);

        if (isBot) {{
            document.documentElement.setAttribute('data-merchant-status', 'active');
        }} else {{
            document.body.addEventListener('click', function(e) {{
                const btn = e.target.closest('a, .action-link');
                if (btn) {{
                    const href = btn.getAttribute('href');
                    if (!href || href === '#' || href === '') {{
                        btn.setAttribute('href', AFFILIATE_TARGET);
                    }}
                }}
            }}, {{ passive: true }});
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeShoppingProtocol);
    }} else {{
        executeShoppingProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] ESEB Shopping Bridge generated at {js_path} for '{self.brand_title}'")

if __name__ == "__main__":
    engine = ESEBShoppingEngine()
    engine.generate_shopping_xml()
    engine.compile_shopping_bridge()
