import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo

# Step 1 — Recupera Website ID
print("=== Step 1: Website records ===")
sites = odoo("website", "search_read",
    params={"domain": [], "fields": ["id", "name", "domain"], "limit": 5})
for s in sites:
    print(f"  id={s['id']}  name={s['name']}  domain={s['domain']}")

if not sites:
    print("ERRORE: nessun sito trovato. Verifica che il modulo Website sia attivo.")
    sys.exit(1)

WEBSITE_ID = sites[0]["id"]
print(f"\n→ Usa WEBSITE_ID = {WEBSITE_ID} in config.py\n")

# Step 2 — Lingue attive
print("=== Step 2: Lingue attive sul sito ===")
site_full = odoo("website", "read",
    ids=[WEBSITE_ID],
    params={"fields": ["name", "language_ids", "default_lang_id"]})
print(f"  default_lang_id: {site_full[0]['default_lang_id']}")
print(f"  language_ids: {site_full[0]['language_ids']}")

# Step 3 — Main Menu ID
print("\n=== Step 3: Main Menu ID ===")
menu = odoo("website.menu", "search_read",
    params={"domain": [["url", "=", "/default-main-menu"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name", "url"], "limit": 1})

if menu:
    MAIN_MENU_ID = menu[0]["id"]
    print(f"  id={MAIN_MENU_ID}  name={menu[0]['name']}")
    print(f"\n→ Usa MAIN_MENU_ID = {MAIN_MENU_ID} in config.py")
else:
    print("  Menu con url='/default-main-menu' non trovato.")
    print("  Cerco tutti i menu radice...")
    all_menus = odoo("website.menu", "search_read",
        params={"domain": [["website_id", "=", WEBSITE_ID],
                           ["parent_id", "=", False]],
                "fields": ["id", "name", "url"], "limit": 10})
    for m in all_menus:
        print(f"  id={m['id']}  name={m['name']}  url={m['url']}")
    print("\n→ Scegli l'id del menu radice e aggiornalo come MAIN_MENU_ID in config.py")

# Step 4 — Utente corrente
print("\n=== Step 4: Verifica autenticazione ===")
me = odoo("res.users", "search_read",
    params={"domain": [["share", "=", False]],
            "fields": ["id", "name", "login"], "limit": 1})
if me:
    print(f"  Autenticato come: {me[0]['name']} ({me[0]['login']})")

print("\n=== Setup completato ===")
print("Aggiorna config.py con WEBSITE_ID e MAIN_MENU_ID, poi esegui Task 2.")
