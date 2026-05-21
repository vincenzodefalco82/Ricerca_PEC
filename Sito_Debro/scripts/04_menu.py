import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID, MAIN_MENU_ID

# Verifica menu esistenti per evitare duplicati
existing = odoo("website.menu", "search_read",
    params={"domain": [["website_id", "=", WEBSITE_ID],
                       ["parent_id", "=", MAIN_MENU_ID]],
            "fields": ["id", "name", "url"]})

print("Menu esistenti sotto Top Menu:")
for m in existing:
    print(f"  id={m['id']}  name={m['name']}  url={m['url']}")

existing_names = {m["name"].lower() for m in existing}

voci = [
    {"name": "Consulting",  "url": "/consulting/",  "sequence": 10},
    {"name": "Software",    "url": "/software/",    "sequence": 20},
    {"name": "Formazione",  "url": "/formazione/",  "sequence": 30},
    {"name": "AI",          "url": "/ai/",          "sequence": 40},
    {"name": "Contatti",    "url": "/contatti/",    "sequence": 50},
]

print("\nCreazione voci menu...")
for v in voci:
    if v["name"].lower() in existing_names:
        print(f"  SKIP {v['name']} — già esistente")
        continue
    ids = odoo("website.menu", "create",
        params={"vals_list": [{
            "name":      v["name"],
            "url":       v["url"],
            "parent_id": MAIN_MENU_ID,
            "website_id": WEBSITE_ID,
            "sequence":  v["sequence"],
        }]})
    print(f"  ✓ {v['name']} → id={ids[0]}  url={v['url']}")

print("\nTask 4 completato. Verifica menu su https://www.debro.it")
