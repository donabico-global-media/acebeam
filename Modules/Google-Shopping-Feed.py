# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Shopping-Feed.py] - GOOGLE SHOPPING COMPLIANT FEED & BRIDGE ENGINE
[V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
"""

import os
import xml.etree.ElementTree as ET

class ESEBShoppingEngine:
    def __init__(self):
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-media-system")
        self.repo_raw = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/acebeam")
        self.repo_name = self.repo_raw.split("/")[-1] if "/" in self.repo_raw else self.repo_raw
        
        self.brand_title = self.repo_name.replace("-", " ").replace("_", " ").title()
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = f"{self.github_user.upper()} SHOPPING MATRIX"
        
        # Domain chính thức chứa Landing Page minh bạch
        self.domain = f"https://{self.repo_name}.donabico.com"
        # Đường dẫn trực tiếp tới sản phẩm thực tế và ảnh thật
        self.product_url = f"{self.domain}/landing_pages/landing_pages_affiliate.html"
        self.product_image = f"{self.domain}/assets/images/product-main.jpg"
        
        self.affiliate_target = f"https://{self.repo_name}.sjv.io/donabio_global_media"
        self.active_border = "#10B981"

    def generate_shopping_xml(self):
        os.makedirs("Feeds", exist_ok=True)
        xml_path = "Feeds/Shopping-Feed.xml"

        rss = ET.Element("rss", version="2.0")
        rss.set("xmlns:g", "http://base.google.com/ns/1.0")

        channel = ET.SubElement(rss, "channel")
        ET.SubElement(channel, "title").text = f"{self.brand_name} - {self.brand_title} Official Store"
        ET.SubElement(channel, "link").text = self.domain
        ET.SubElement(channel, "description").text = f"Official High-Performance {self.brand_title} Tactical Equipment & Outdoor Gear"

        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "g:id").text = f"{self.repo_name.upper()}-TAC-001"
        ET.SubElement(item, "title").text = f"{self.brand_title} Tactical Illumination Flashlight Series"
        ET.SubElement(item, "description").text = f"Professional-grade {self.brand_title} Tactical Illumination Equipment with ultra-durable aircraft aluminum casing and high-lumen output."
        # SỬA LỖI: Trỏ link sản phẩm và ảnh sản phẩm thực tế, tuyệt đối không dùng favicon
        ET.SubElement(item, "link").text = self.product_url
        ET.SubElement(item, "g:image_link").text = self.product_image
        ET.SubElement(item, "g:availability").text = "in_stock"
        ET.SubElement(item, "g:price").text = "99.95 USD"
        ET.SubElement(item, "g:brand").text = self.brand_title
        ET.SubElement(item, "g:condition").text = "new"
        ET.SubElement(item, "g:shipping_weight").text = "0.5 kg"

        tree = ET.ElementTree(rss)
        ET.indent(tree, space="  ", level=0)
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)
        print(f"[Success] Compliant Google Merchant XML Feed generated at {xml_path}")

    def compile_shopping_bridge(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Shopping.js"

        # SỬA LỖI: Loại bỏ logic kiểm tra userAgent BOT để tránh bị quy lỗi Cloaking / Trình bày sai
        js_content = f"""/**
 * {self.brand_name}
 * {self.system_identity}
 * [Google-Shopping.js] - COMPLIANT MERCHANT SCHEMA BRIDGE
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 */
(function() {{
    'use strict';

    function injectMerchantSchema() {{
        const schema = {{
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "{self.brand_title} Tactical Illumination Flashlight Series",
            "image": ["{self.product_image}"],
            "description": "Professional-grade {self.brand_title} Tactical Illumination Equipment.",
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
            }}
        }};
        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.id = "eseb-merchant-schema";
        script.text = JSON.stringify(schema);
        document.head.appendChild(script);
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', injectMerchantSchema);
    }} else {{
        injectMerchantSchema();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] Merchant Schema Bridge generated at {js_path}")

if __name__ == "__main__":
    engine = ESEBShoppingEngine()
    engine.generate_shopping_xml()
    engine.compile_shopping_bridge()
