import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

# Navbar navy — fix leggibilità: rimuove rounded-pill bianco Odoo 19,
# forza background navy su nav.navbar, override navbar-light + o_colored_level.
# Script 02 aveva solo base CSS; questo aggiunge/sostituisce il blocco navbar.

NAVBAR_CSS = """
/* ── NAVBAR DEBRO ────────────────────────────────────── */
#top {
  background: var(--dg-navy) !important;
  box-shadow: 0 2px 20px rgba(10,20,40,.25);
  position: sticky;
  top: 0;
  z-index: 1000;
}
/* Rimuovi padding container Odoo e stile pill */
#top > div.container {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
#top nav.navbar {
  background: var(--dg-navy) !important;
  border-radius: 0 !important;
  border: none !important;
  box-shadow: none !important;
  min-height: 64px;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
  align-items: stretch;
}
/* Logo */
#top .navbar-brand {
  padding: 12px 0;
}
#top .navbar-brand img {
  max-height: 38px !important;
  filter: brightness(0) invert(1);
}
/* Nav links — override navbar-light + o_colored_level + span wrapper */
#top nav.navbar .nav-link,
#top nav.navbar .nav-link span,
#top .navbar-nav .nav-link,
#top .navbar-nav .nav-link span {
  color: rgba(255,255,255,.85) !important;
  font-weight: 600 !important;
  font-size: 13.5px !important;
  padding: 0 16px !important;
  line-height: 64px !important;
  border-bottom: 2px solid transparent !important;
  transition: color .15s ease, border-color .15s ease;
  text-decoration: none !important;
  background: transparent !important;
}
#top nav.navbar .nav-link:hover,
#top nav.navbar .nav-link:hover span {
  color: #fff !important;
  border-bottom-color: var(--dg-accent) !important;
}
#top nav.navbar .nav-link.active,
#top nav.navbar .nav-item.active > .nav-link,
#top nav.navbar .nav-item.active > .nav-link span {
  color: var(--dg-accent) !important;
  border-bottom-color: var(--dg-accent) !important;
}
/* Icone extra (cart, wishlist) */
#top .o_navlink_background,
#top .o_navlink_background i {
  color: rgba(255,255,255,.7) !important;
}
#top .o_navlink_background:hover,
#top .o_navlink_background:hover i {
  color: #fff !important;
}
/* Language switcher */
#top .o_lang_switcher_nav .nav-link,
#top .o_lang_switcher_nav .nav-link span,
#top .js_language_selector .btn,
#top .js_language_selector a {
  color: rgba(255,255,255,.6) !important;
  font-size: 12px !important;
  font-weight: 600 !important;
  border: 1px solid rgba(255,255,255,.25) !important;
  border-radius: 4px !important;
  padding: 4px 10px !important;
  line-height: normal !important;
  margin-left: 8px;
}
#top .o_lang_switcher_nav .nav-link:hover,
#top .js_language_selector .btn:hover {
  color: var(--dg-accent) !important;
  border-color: rgba(245,166,35,.5) !important;
  background: transparent !important;
}
/* Mobile hamburger */
#top .navbar-toggler {
  border-color: rgba(255,255,255,.3) !important;
  padding: 6px 10px;
}
#top .navbar-toggler-icon {
  filter: brightness(0) invert(1);
}
/* Mobile collapse */
@media (max-width: 991px) {
  #top nav.navbar {
    border-radius: 0 !important;
    flex-wrap: wrap;
    padding: 0 1rem !important;
  }
  #top .navbar-collapse {
    background: var(--dg-dark);
    padding: 8px 0 16px;
    border-top: 1px solid rgba(255,255,255,.08);
    width: 100%;
  }
  #top nav.navbar .nav-link,
  #top nav.navbar .nav-link span,
  #top .navbar-nav .nav-link,
  #top .navbar-nav .nav-link span {
    line-height: normal !important;
    padding: 10px 20px !important;
    border-bottom: none !important;
    border-left: 2px solid transparent !important;
  }
  #top nav.navbar .nav-link:hover {
    border-left-color: var(--dg-accent) !important;
    background: rgba(255,255,255,.04) !important;
  }
  #top nav.navbar .nav-link.active,
  #top nav.navbar .nav-item.active > .nav-link {
    border-left-color: var(--dg-accent) !important;
    color: var(--dg-accent) !important;
  }
}
/* Dropdown menu */
#top .dropdown-menu {
  border: none;
  border-radius: 8px;
  box-shadow: 0 8px 28px rgba(10,20,40,.18);
  padding: 8px 0;
  margin-top: 4px !important;
}
#top .dropdown-item {
  font-size: 14px;
  font-weight: 500;
  color: var(--dg-dark) !important;
  padding: 8px 20px;
}
#top .dropdown-item:hover {
  background: var(--dg-light);
  color: var(--dg-navy) !important;
}"""

print("Lettura custom_code_head attuale...")
site = odoo("website", "read", ids=[WEBSITE_ID], params={"fields": ["custom_code_head"]})
current = site[0].get("custom_code_head", "") or ""

# Sostituisce blocco navbar esistente o appende
start_marker = "/* ── NAVBAR DEBRO"
idx = current.find(start_marker)
if current.endswith("</style>"):
    base = current[:idx].rstrip() if idx != -1 else current[:-8].rstrip()
    new_css = base + "\n" + NAVBAR_CSS + "\n</style>"
else:
    new_css = current + "\n<style>" + NAVBAR_CSS + "\n</style>"

print(f"Iniezione CSS navbar ({len(new_css)} chars)...")
result = odoo("website", "write", ids=[WEBSITE_ID], params={"vals": {"custom_code_head": new_css}})
print(f"Risultato: {result}")

verify = odoo("website", "read", ids=[WEBSITE_ID], params={"fields": ["custom_code_head"]})
print(f"Verificato: {len(verify[0]['custom_code_head'])} chars in custom_code_head")
print("Task 13 completato. Verifica navbar su https://www.debro.it")
