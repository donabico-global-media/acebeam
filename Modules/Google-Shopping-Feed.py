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
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-media-system")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/acebeam").split("/")[-1]
        
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = f"{self.github_user.upper()} SHOPPING MATRIX"
        self.domain = "https://acebeam.donabico.com"
        self.affiliate_target = "https://acebeamflashlight.sjv.io/donabio_global_media"
        self.active_border = "#10B981"  # Viền xanh lá cây active-modules

    def generate_shopping_xml(self):
        os.makedirs("Feeds", exist_ok=True)
        # ĐÃ ĐỔI TÊN THÀNH Shopping-Feed.xml (Chữ S và F viết hoa)
        xml_path = "Feeds/Shopping-Feed.xml"

        rss = ET.Element("rss", version="2.0")
        rss.set("xmlns:g", "http://base.google.com/ns/1.0")

        channel = ET.SubElement(rss, "channel")
        ET.SubElement(channel, "title").text = f"{self.brand_name} - Tactical Gear Feed"
        ET.SubElement(channel, "link").text = self.domain
        ET.SubElement(channel, "description").text = "Automated High-Performance Acebeam Tactical Gear Syndication Feed"

        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "g:id").text = "ACEBEAM-TAC-001"
        ET.SubElement(item, "title").text = "Acebeam Tactical Illumination Gear - Professional Series"
        ET.SubElement(item, "description").text = "High-Performance Tactical Flashlights, LEP Lights and Outdoor Search Gear."
        ET.SubElement(item, "link").text = self.domain
        
        # LINK ẢNH HỢP LỆ VỚI GOOGLE MERCHANT CENTER (ĐỊNH DẠNG JPEG)
        ET.SubElement(item, "g:image_link").text = "https://www.acebeam.com/images/thumbs/000/0003503_defender-p16-tactical-flashlight.jpeg"
        
        ET.SubElement(item, "g:availability").text = "in_stock"
        ET.SubElement(item, "g:price").text = "99.95 USD"
        ET.SubElement(item, "g:brand").text = "Acebeam"
        ET.SubElement(item, "g:condition").text = "new"
        ET.SubElement(item, "g:shipping_weight").text = "0.5 kg"

        tree = ET.ElementTree(rss)
        ET.indent(tree, space="  ", level=0)
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)
        print(f"[Success] Real Google Merchant XML Feed generated at {xml_path}")

    def compile_shopping_bridge(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Shopping.js"

        js_content = f"""/**
 * {self.brand_name}
 * {self.system_identity}
 * [Google-Shopping.js] - REAL GOOGLE SHOPPING FEED & ATTRIBUTION BRIDGE
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
            "name": document.title || "Acebeam Tactical Gear",
            "image": ["https://www.acebeam.com/images/thumbs/000/0003503_defender-p16-tactical-flashlight.jpeg"],
            "description": "High-Performance Tactical Gear",
            "sku": "ACEBEAM-TAC-001",
            "brand": {{
                "@type": "Brand",
                "name": "Acebeam"
            }},
            "offers": {{
                "@type": "Offer",
                "url": window.location.href,
                "priceCurrency": "USD",
                "price": "99.95",
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition"
            }}
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
        print(f"[Success] ESEB Shopping Bridge generated at {js_path}")

if __name__ == "__main__":
    engine = ESEBShoppingEngine()
    engine.generate_shopping_xml()
    engine.compile_shopping_bridge()
