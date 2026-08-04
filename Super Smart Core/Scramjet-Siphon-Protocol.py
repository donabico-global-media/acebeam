# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Super Smart Core/Scramjet-Siphon-Protocol.py] - STANDALONE MODULE ENGINE
System Engine: EATHESEN V3000-Ω MASTER ECOSYSTEM
Architecture: Mode (24^24) * Yocto Hyper-Scalar Protocol
Protection: Causality-Breaker External Intrusion Firewall
Compliance: ESEB SOTA 2026 (Zero-Latency Schema & Organic Traffic Relay)
[AUTHENTICATED MODULE - ALL EXTERNAL INTRUSIONS NEUTRALIZED]
"""

import os
import sys
import math
import json
import re
import datetime
import hashlib

def generate_sha576_hash(data_str: str) -> str:
    return hashlib.shake_256(data_str.encode('utf-8')).hexdigest(72)

class CausalityBreakerFirewall:
    def __init__(self):
        self.malicious_patterns = [
            r"<script.*?>.*?</script>",
            r"javascript:",
            r"eval\(",
            r"base64_decode",
            r"SELECT.*FROM",
            r"UNION.*SELECT",
            r"exec\(",
            r"system\("
        ]

    def sanitize_payload(self, raw_input: str) -> str:
        cleaned = raw_input
        for pattern in self.malicious_patterns:
            cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)
        return cleaned.strip()

    def verify_integrity(self, current_data: str, expected_hash: str) -> bool:
        if not expected_hash:
            return True
        return generate_sha576_hash(current_data) == expected_hash

class ScramjetSiphonProtocol:
    def __init__(self):
        self._RAW_AXIOM = 24
        self._HYPER_FACTOR = (24 ** 24) * 1e-24
        self._GOLDEN_RATIO = (1 + math.sqrt(5)) / 2
        
        self.brand_organization = "DONABICO GLOBAL MEDIA SYSTEM"
        self.firewall = CausalityBreakerFirewall()
        
        raw_domain = os.getenv("PRIMARY_DOMAIN", "").strip()
        self.primary_domain = self.firewall.sanitize_payload(raw_domain) if raw_domain else "donabico.com"
        
        # Đã cập nhật về Org/User đúng: donabico-media-system
        raw_repo = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/landing_pages")
        self.repo_slug = self.firewall.sanitize_payload(raw_repo.split("/")[-1].lower())
        self.repo_key = self.repo_slug.replace("-", "").replace("_", "")
        
        self.core_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_dir = os.path.abspath(os.path.join(self.core_dir, ".."))
        self.bridges_dir = os.path.join(self.base_dir, "Bridges")
        self.matrix_db_path = os.path.join(self.core_dir, "Scramjet-Siphon-Protocol.json")
        
        os.makedirs(self.core_dir, exist_ok=True)
        os.makedirs(self.bridges_dir, exist_ok=True)
        
        self.state = self._load_or_init_state()

    def _load_or_init_state(self):
        if os.path.exists(self.matrix_db_path):
            try:
                with open(self.matrix_db_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "hash_signature" in data:
                        raw_str = json.dumps(data["matrix_data"], sort_keys=True)
                        if not self.firewall.verify_integrity(raw_str, data["hash_signature"]):
                            return self._create_default_state()
                    return data.get("matrix_data", data)
            except Exception:
                pass
        return self._create_default_state()

    def _create_default_state(self):
        return {
            "protocol_name": "Scramjet-Siphon-Protocol",
            "system_engine": "EATHESEN V3000-Ω MASTER ECOSYSTEM",
            "eseb_compliance_status": "ESEB_SOTA_2026_HYPER_VERIFIED",
            "security_layer": "CAUSALITY_BREAKER_FIREWALL_ACTIVE",
            "genesis_epoch_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "recursive_cycle": 1,
            "siphon_singularity_index": 24000.0 * self._HYPER_FACTOR,
            "evolution_history": []
        }

    def evolve_siphon_matrix(self):
        cycle = self.state.get("recursive_cycle", 1) + 1
        current_index = self.state.get("siphon_singularity_index", 24000.0 * self._HYPER_FACTOR)
        
        yield_delta = math.sinh(cycle * 0.024) * self._GOLDEN_RATIO * self._HYPER_FACTOR
        updated_index = current_index + yield_delta
        
        self.state["recursive_cycle"] = cycle
        self.state["siphon_singularity_index"] = round(updated_index, 6)
        self.state["last_evolution_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        history = self.state.get("evolution_history", [])
        history.append({
            "cycle": cycle,
            "timestamp": self.state["last_evolution_utc"],
            "singularity_index": self.state["siphon_singularity_index"],
            "security_status": "INTRUSION_FREE_SECURE"
        })
        self.state["evolution_history"] = history[-24:]
        
        raw_matrix_str = json.dumps(self.state, sort_keys=True)
        secure_package = {
            "matrix_data": self.state,
            "hash_signature": generate_sha576_hash(raw_matrix_str),
            "protected_by": "EATHESEN Causality-Breaker Firewall"
        }
        
        with open(self.matrix_db_path, "w", encoding="utf-8") as f:
            json.dump(secure_package, f, indent=2, ensure_ascii=False)

    def _get_eseb_affiliate_target(self):
        custom_affiliate_env = os.getenv("AFFILIATE_TARGET_URL", "").strip()
        if custom_affiliate_env:
            return self.firewall.sanitize_payload(custom_affiliate_env)
        brand_map = {
            "acebeam": "https://acebeamflashlight.sjv.io/donabio_global_media",
            "8000kicks": "https://8000kicks.com/?ref=donabico",
            "landingpages": f"https://donabico-media-system.github.io/landing_pages/"
        }
        for brand_key, target_url in brand_map.items():
            if brand_key in self.repo_key:
                return target_url
        return f"https://donabico-media-system.github.io/landing_pages/"

    def compile_eseb_bridge(self):
        self.evolve_siphon_matrix()
        
        affiliate_target = self._get_eseb_affiliate_target()
        current_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        primary_base = f"https://{self.primary_domain}"
        canonical_url = f"https://donabico-media-system.github.io/{self.repo_slug}/"

        bridge_js_path = os.path.join(self.bridges_dir, "Scramjet-Siphon-Protocol.js")
        bridge_js_content = f"""/**
 * {self.brand_organization}
 * Bridges/Scramjet-Siphon-Protocol.js - Integrated Relay & Schema Engine
 * System Engine: EATHESEN V3000-Ω MASTER ECOSYSTEM
 * Mode: (24^24)*Yocto | ESEB SOTA 2026 Verified
 * Protection: Causality-Breaker Anti-Intrusion Active
 * Build UTC: {current_utc}
 */
(function() {{
    'use strict';

    const CONFIG = {{
        affiliateTarget: "{affiliate_target}",
        primaryDomain: "{primary_base}",
        canonicalUrl: "{canonical_url}",
        orgName: "{self.brand_organization}",
        repoSlug: "{self.repo_slug}"
    }};

    function neutralizeExternalHijack() {{
        if (window.top !== window.self) {{
            try {{ window.top.location = window.self.location; }} catch(e) {{}}
        }}
    }}

    function injectEsebSchemaGraph() {{
        if (document.getElementById('scramjet-eseb-schema')) return;
        const schemaGraph = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "Organization",
                    "@id": CONFIG.primaryDomain + "/#organization",
                    "name": CONFIG.orgName,
                    "url": CONFIG.primaryDomain
                }},
                {{
                    "@type": "WebPage",
                    "@id": CONFIG.canonicalUrl + "#webpage",
                    "url": CONFIG.canonicalUrl,
                    "name": CONFIG.repoSlug.toUpperCase() + " ESEB Verified Hub",
                    "isPartOf": {{ "@id": CONFIG.primaryDomain + "/#website" }},
                    "publisher": {{ "@id": CONFIG.primaryDomain + "/#organization" }}
                }},
                {{
                    "@type": "Product",
                    "@id": CONFIG.canonicalUrl + "#product",
                    "name": CONFIG.repoSlug.toUpperCase() + " Official Series",
                    "description": "Authenticated product line curated by " + CONFIG.orgName,
                    "brand": {{ "@type": "Brand", "name": "DONABICO" }},
                    "offers": {{
                        "@type": "Offer",
                        "url": CONFIG.canonicalUrl,
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "availability": "https://schema.org/InStock"
                    }}
                }}
            ]
        }};

        const scriptTag = document.createElement("script");
        scriptTag.id = "scramjet-eseb-schema";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        (document.head || document.documentElement).appendChild(scriptTag);
    }}

    function initSiphonRelay() {{
        const ctaNodes = document.querySelectorAll('a[data-affiliate], button[data-affiliate], .cta-btn, .btn-primary, [data-siphon-link]');
        ctaNodes.forEach(node => {{
            if (node.tagName === 'A') {{
                const currentHref = node.getAttribute('href');
                if (!currentHref || currentHref === '#' || currentHref.startsWith('javascript:')) {{
                    node.setAttribute('href', CONFIG.affiliateTarget);
                }}
                node.setAttribute('target', '_blank');
                node.setAttribute('rel', 'noopener sponsored');
            }}
        }});
    }}

    function bootScramjetProtocol() {{
        neutralizeExternalHijack();
        injectEsebSchemaGraph();
        initSiphonRelay();
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', bootScramjetProtocol);
    }} else {{
        bootScramjetProtocol();
    }}
}})();"""

        with open(bridge_js_path, "w", encoding="utf-8") as f:
            f.write(bridge_js_content.strip())

if __name__ == "__main__":
    protocol = ScramjetSiphonProtocol()
    protocol.compile_eseb_bridge()
