import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

BASE_DOMAIN = "https://donabico-global-media.github.io"
BRANDS_DIR = "brands"  # Quét trực tiếp danh mục các Kho thương hiệu

def discover_brand_repositories():
    """
    DYNAMIC BRAND DISCOVERY AGENT:
    Tự động quét toàn bộ Kho thương hiệu độc lập trong hệ thống.
    """
    print(f"🔍 [AUTO-DISCOVERY] Scanning Brand Repositories in '{BRANDS_DIR}'...")
    discovered_brands = []

    # Nếu chưa có thư mục brands, quét ngay tại root hoặc thư mục landing_pages
    scan_dir = BRANDS_DIR if os.path.exists(BRANDS_DIR) else "."

    for root, dirs, files in os.walk(scan_dir):
        for file_name in files:
            if file_name.endswith(".html") and not file_name.startswith("index"):
                file_path = os.path.join(root, file_name)
                brand_info = parse_brand_metadata(file_path, file_name)
                if brand_info:
                    discovered_brands.append(brand_info)

    print(f"✅ [AUTO-DISCOVERY] Identified {len(discovered_brands)} Independent Brand Nodes!")
    return discovered_brands

def parse_brand_metadata(file_path, file_name):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        raw_title = title_match.group(1).strip() if title_match else file_name.replace('.html', '').upper()

        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        raw_desc = desc_match.group(1).strip() if desc_match else f"Official Node for {raw_title}"

        # Clean URL path for Brand Repository
        clean_rel_path = os.path.relpath(file_path, ".").replace("\\", "/")
        brand_url = f"{BASE_DOMAIN}/{clean_rel_path}"

        return {
            "brand_name": raw_title,
            "repository_id": file_name.replace(".html", "").lower(),
            "url": brand_url,
            "prompt_context": f"Independent Brand Repository: {raw_title}. Context: {raw_desc}."
        }
    except Exception as e:
        print(f"⚠️ Error parsing {file_name}: {e}")
        return None

def harvest_brand_ehc(api_key, brands):
    print("⚡ [EHC CORE] Harvesting Entity Clusters across Independent Brand Repositories...")
    all_clusters = []

    if not brands:
        brands = [{
            "brand_name": "DONABICO Global Media Network",
            "repository_id": "root",
            "url": f"{BASE_DOMAIN}/",
            "prompt_context": "DONABICO Master Ecosystem Central Command Node"
        }]

    for brand in brands:
        cluster_data = call_gemini_for_brand(api_key, brand)
        all_clusters.append(cluster_data)

    return all_clusters

def call_gemini_for_brand(api_key, brand):
    if not api_key:
        return get_fallback_brand_data(brand)

    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    prompt_text = (
        f"You are an EHC Engine for DONABICO GLOBAL MEDIA SYSTEM. "
        f"Generate a raw JSON object for the independent Brand Repository '{brand['brand_name']}'. "
        f"Context: {brand['prompt_context']}. "
        f"Target URL: {brand['url']}. "
        f"Return ONLY valid JSON with fields: "
        f"'brand_name' (string), 'title' (string), 'url' (string), 'description' (string), 'entity_keywords' (array of strings)."
    )

    payload = {"contents": [{"parts": [{"text": prompt_text}]}]}
    data = json.dumps(payload).encode('utf-8')
    headers = {'Content-Type': 'application/json', 'x-goog-api-key': api_key}

    try:
        req = urllib.request.Request(endpoint, data=data, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            result = json.loads(response.read().decode('utf-8'))
            raw_text = result['candidates'][0]['content']['parts'][0]['text']
            clean_text = raw_text.replace("```json", "").replace("```", "").strip()
            print(f"✅ [EHC CORE] Brand Entity Cluster Generated: {brand['brand_name']}")
            return json.loads(clean_text)
    except Exception as e:
        print(f"⚠️ [EHC CORE] Gemini API fallback for {brand['brand_name']}: {e}")
        return get_fallback_brand_data(brand)

def get_fallback_brand_data(brand):
    return {
        "brand_name": brand['brand_name'],
        "title": f"{brand['brand_name']} - Official Brand Repository Node",
        "url": brand['url'],
        "description": f"Authorized distribution and entity node for {brand['brand_name']}.",
        "entity_keywords": [brand['brand_name'], "DONABICO Global Media System", "Brand Node"]
    }

def broadcast_eseb_events(clusters):
    print("⚡ [ESEB CORE] Broadcasting Events across Brand Repositories Graph...")

    rss_items = ""
    urls_to_broadcast = []

    for item in clusters:
        urls_to_broadcast.append(item['url'])
        rss_items += f"""
        <item>
            <title><![CDATA[{item['title']}]]></title>
            <link>{item['url']}</link>
            <description><![CDATA[{item['description']} - Keywords: {', '.join(item['entity_keywords'])}]]></description>
            <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
            <guid>{item['url']}</guid>
        </item>"""

    rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>DONABICO Master Brand Repository Stream</title>
    <link>{BASE_DOMAIN}/</link>
    <description>Authorized Dynamic ESEB Brand Entity Broadcast Stream</description>
    <language>en-us</language>
    {rss_items}
</channel>
</rss>"""

    output_dir = BRANDS_DIR if os.path.exists(BRANDS_DIR) else "Data"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/eseb_feed.xml", "w", encoding="utf-8") as f:
        f.write(rss_content.strip())
    print(f"✅ [ESEB] Brand RSS Stream Generated: {output_dir}/eseb_feed.xml")

    # IndexNow Dynamic Push
    host = "donabico-global-media.github.io"
    indexnow_key = "e24e24e24e24e24e24e24e24e24e24e2"
    endpoint = "https://api.indexnow.org/indexnow"

    payload = {
        "host": host,
        "key": indexnow_key,
        "keyLocation": f"https://{host}/{indexnow_key}.txt",
        "urlList": urls_to_broadcast
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(endpoint, data=data, headers={'Content-Type': 'application/json; charset=utf-8'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status in [200, 202]:
                print("🚀 [ESEB] Dynamic IndexNow Broadcast SUCCESS for Brand Repositories!")
    except Exception as e:
        print(f"⚠️ [ESEB] IndexNow Notice: {e}")

    generate_brand_js_bridge(clusters)

def generate_brand_js_bridge(clusters):
    os.makedirs("Bridges", exist_ok=True)
    js_content = f"""/* ================================================================= */
/* DONABICO GLOBAL MEDIA SYSTEM - BRAND REPOSITORIES JS BRIDGE       */
/* Node: EATHESEN V3000-Ω | Zero-Maintenance Dynamic Siphon Engine   */
/* ¢24 IMMUTABLE | $10^-24 Precision | Global AI Authority          */
/* ================================================================= */

(function() {{
    'use strict';

    const BRAND_SIPHON_ENGINE = {{
        brandPayload: {json.dumps(clusters, indent=8, ensure_ascii=False)},

        injectBrandGraph: function() {{
            if (document.getElementById('brand-eseb-graph')) return;

            const graphSchema = {{
                "@context": "https://schema.org",
                "@graph": [
                    {{
                        "@type": "Organization",
                        "@id": "https://donabico-global-media.github.io/#organization",
                        "name": "DONABICO GLOBAL MEDIA SYSTEM",
                        "url": "https://donabico-global-media.github.io",
                        "description": "Central Command System for Independent Brand Repositories & Digital Networks."
                    }},
                    {{
                        "@type": "ItemList",
                        "@id": "https://donabico-global-media.github.io/#brand-repositories",
                        "name": "DONABICO Authorized Independent Brand Repositories",
                        "itemListElement": this.brandPayload.map((item, index) => ({{
                            "@type": "ListItem",
                            "position": index + 1,
                            "name": item.title,
                            "url": item.url,
                            "description": item.description
                        }}))
                    }}
                ]
            }};

            const schemaTag = document.createElement('script');
            schemaTag.type = 'application/ld+json';
            schemaTag.id = 'brand-eseb-graph';
            schemaTag.text = JSON.stringify(graphSchema);
            document.head.appendChild(schemaTag);
        }},

        init: function() {{
            this.injectBrandGraph();
            console.log("✅ [BRAND ESEB] Siphon-Traffic-Engine.js Active | Total Brand Nodes Loaded:", this.brandPayload.length);
        }}
    }};

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', () => BRAND_SIPHON_ENGINE.init());
    }} else {{
        BRAND_SIPHON_ENGINE.init();
    }}
}})();
"""
    with open("Bridges/Siphon-Traffic-Engine.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("✅ [ESEB] Brand JS Bridge Generated: Bridges/Siphon-Traffic-Engine.js")

if __name__ == "__main__":
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    discovered_brands = discover_brand_repositories()
    clusters = harvest_brand_ehc(api_key, discovered_brands)
    broadcast_eseb_events(clusters)
