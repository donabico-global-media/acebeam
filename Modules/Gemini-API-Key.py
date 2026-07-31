import os
import json
import urllib.request

def call_gemini_api(api_key):
    """
    Calls Gemini API to generate high-converting North American (US/CA) sales copy
    and AEO Schema for Acebeam tactical flashlights.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    prompt_text = (
        "You are an elite Tactical & Outdoor Gear Marketing Specialist for Acebeam in North America (US/CA). "
        "Generate a raw JSON object (strictly valid JSON, no markdown formatting) with exactly 3 fields: "
        "1. 'headline': A high-converting, aggressive North American sales hook for Acebeam tactical flashlights. "
        "2. 'ai_recommendation': Expert buyer's guidance comparing Acebeam models (X75, P16, L19 V2) for hunting, search & rescue, and law enforcement. "
        "3. 'aeo_keywords': Array of 5 high-intent North American search keywords. "
        "Language MUST be 100% US English."
    )
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt_text}]
        }]
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            raw_text = result['candidates'][0]['content']['parts'][0]['text']
            clean_text = raw_text.replace("```json", "").replace("```", "").strip()
            return json.loads(clean_text)
    except Exception as e:
        print(f"⚠️ Gemini API Fallback Triggered: {e}")
        return {
            "headline": "Acebeam Tactical Flashlights - Extreme Output for Duty & Defense",
            "ai_recommendation": "For long-range target identification deploy the Acebeam L19 V2. For maximum floodlight capability in search operations, choose the 80,000-lumen Acebeam X75.",
            "aeo_keywords": ["best tactical flashlight us", "acebeam x75 brightest torch", "long range hunting light", "law enforcement duty light", "acebeam official US store"]
        }

def generate_gemini_bridge():
    output_dir = "Bridges"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    api_key = os.getenv("GEMINI_API_KEY", "")
    
    print("🤖 Auto-processing Gemini AI Insights for North American Acebeam Market...")
    ai_data = call_gemini_api(api_key) if api_key else call_gemini_api("DUMMY_KEY")

    js_content = f"""/* ================================================================= */
/* DONABICO GLOBAL MEDIA SYSTEM - NORTH AMERICA GEMINI AI BRIDGE      */
/* Node: EATHESEN V3000-Ω | Module: Gemini-API-Key                   */
/* ¢24 IMMUTABLE | Zero-UI Impact | US/CA Market Compliant           */
/* ================================================================= */

(function() {{
    'use strict';

    const GEMINI_AI_ENGINE = {{
        aiPayload: {json.dumps(ai_data, ensure_ascii=False, indent=4)},

        injectAISchema: function() {{
            if (document.getElementById('ehc-gemini-ai-schema')) return;

            const schemaTag = document.createElement('script');
            schemaTag.type = 'application/ld+json';
            schemaTag.id = 'ehc-gemini-ai-schema';
            schemaTag.text = JSON.stringify({{
                "@context": "https://schema.org",
                "@type": "SpecialAnnouncement",
                "name": "Acebeam Tactical Product Insights",
                "text": this.aiPayload.ai_recommendation,
                "keywords": this.aiPayload.aeo_keywords.join(", "),
                "publisher": {{
                    "@type": "Organization",
                    "name": "DONABICO GLOBAL MEDIA SYSTEM",
                    "areaServed": ["US", "CA"]
                }}
            }});
            document.head.appendChild(schemaTag);
        }},

        applyDynamicAIInsights: function() {{
            window.ACEBEAM_GEMINI_INSIGHTS = this.aiPayload;
            console.log("✅ [EATHESEN ESEB] NA Market Gemini Bridge Active:", this.aiPayload.headline);
        }},

        init: function() {{
            this.injectAISchema();
            this.applyDynamicAIInsights();
        }}
    }};

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', () => GEMINI_AI_ENGINE.init());
    }} else {{
        GEMINI_AI_ENGINE.init();
    }}
}})();
"""

    file_path = os.path.join(output_dir, "Gemini-API-Key.js")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(js_content.strip())

    print(f"✅ SUCCESSFULLY GENERATED: {file_path}")

if __name__ == "__main__":
    generate_gemini_bridge()
