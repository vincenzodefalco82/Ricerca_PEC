import base64
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

LOGO_DIR = os.path.join(os.path.dirname(__file__), "..", "Logo Clienti")
assets_map = {}

files = [f for f in os.listdir(LOGO_DIR)
         if f.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".webp"))]

print(f"Trovati {len(files)} loghi da caricare...\n")

for fname in files:
    fpath = os.path.join(LOGO_DIR, fname)
    ext = fname.rsplit(".", 1)[-1].lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "svg": "image/svg+xml", "webp": "image/webp"}.get(ext, "image/png")

    with open(fpath, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    att_ids = odoo("ir.attachment", "create",
        params={"vals_list": [{
            "name": fname,
            "type": "binary",
            "datas": data,
            "mimetype": mime,
            "public": True,
            "website_id": WEBSITE_ID,
        }]})
    att_id = att_ids[0]

    url = f"/web/image/{att_id}/{fname.replace(' ', '%20')}"
    assets_map[fname] = {"id": att_id, "url": url}
    print(f"  ✓ {fname} → id={att_id}  url={url}")

out_path = os.path.join(os.path.dirname(__file__), "assets_map.json")
with open(out_path, "w") as f:
    json.dump(assets_map, f, indent=2, ensure_ascii=False)

print(f"\nMappa salvata in scripts/assets_map.json")
print("Task 3 completato.")
