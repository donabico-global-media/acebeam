import os
import sys

def main():
    print("=== [ESEB CORE ENGINE] INITIALIZING GIT OPTIMIZATION BUILDER ===")
    
    # 1. Khởi tạo thư mục Bridges nếu chưa tồn tại
    bridge_dir = "Bridges"
    os.makedirs(bridge_dir, exist_ok=True)
    
    # 2. Tự động trích xuất thông tin Repository từ môi trường
    repo_slug = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/default-repo")
    repo_name = repo_slug.split("/")[-1]
    
    # 3. Biên dịch mã JS Client-side Telemetry & Clean-Up Bridge
    js_content = f"""/**
 * EATHESEN V3000-Ω / DONABICO GLOBAL MEDIA SYSTEM
 * MODULE: Git-Optimization Bridge (ESEB SOTA Standard)
 * REPOSITORY: {repo_slug}
 * ZERO-LOG & AUTO-SANITY CLIENT TELEMETRY
 */

(function() {{
    'use strict';
    
    const ESEB_GIT_CONFIG = {{
        repo: "{repo_name}",
        status: "CLEAN_OPTIMIZED",
        timestamp: new Date().toISOString()
    }};

    // Telemetry ping bảo toàn băng thông & dữ liệu bộ nhớ đệm client
    if (typeof window !== 'undefined') {{
        window.__ESEB_GIT_CACHE_SANITY__ = ESEB_GIT_CONFIG;
        
        // Dọn dẹp LocalStorage/SessionStorage rác nếu tồn tại
        try {{
            Object.keys(localStorage).forEach(key => {{
                if (key.startsWith('__eseb_tmp_')) {{
                    localStorage.removeItem(key);
                }}
            }});
        }} catch(e) {{}}
    }}
}})();
"""

    # 4. Xuất file Bridge và hoàn tất
    output_path = os.path.join(bridge_dir, "Git-Optimization.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"SUCCESS: Generated -> {output_path}")

if __name__ == "__main__":
    main()
