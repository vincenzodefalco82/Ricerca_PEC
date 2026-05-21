import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

CUSTOM_CSS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
body, h1, h2, h3, h4, p, a, button, input, textarea, select {
  font-family: 'Inter', sans-serif !important;
}
:root {
  --dg-navy:     #1A3A6B;
  --dg-blue:     #2A5298;
  --dg-dark:     #0D1F3C;
  --dg-slate:    #3A4A5C;
  --dg-light:    #E8EDF5;
  --dg-offwhite: #F8F9FC;
  --dg-accent:   #F5A623;
}
h1 { font-weight: 800; font-size: clamp(2rem, 4vw, 3rem); line-height: 1.15; color: var(--dg-dark); }
h2 { font-weight: 700; font-size: clamp(1.5rem, 3vw, 2rem); line-height: 1.25; color: var(--dg-navy); }
h3 { font-weight: 700; font-size: 1.25rem; color: var(--dg-dark); }
body { font-size: 17px; line-height: 1.6; color: var(--dg-slate); }

.dg-accent-bar { width: 32px; height: 3px; background: var(--dg-accent); border-radius: 2px; margin-bottom: 16px; }
.dg-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .5px; color: var(--dg-navy); margin-bottom: 8px; display: block; }
.dg-hero { background: linear-gradient(135deg, var(--dg-dark) 0%, var(--dg-navy) 100%); padding: 80px 0; }
.dg-hero h1, .dg-hero p { color: #fff; }
.dg-hero .dg-label { color: rgba(255,255,255,.7); }
.text-dg-muted { color: rgba(255,255,255,.65); }

.dg-card-light { background: #fff; border-left: 3px solid var(--dg-navy); border-radius: 8px; box-shadow: 0 2px 8px rgba(26,58,107,.07); padding: 1.5rem; height: 100%; }
.dg-card-dark  { background: var(--dg-navy); color: #fff; border-radius: 8px; box-shadow: 0 2px 12px rgba(26,58,107,.2); padding: 1.5rem; height: 100%; }
.dg-card-dark h3 { color: #fff; }
.dg-card-dark p  { color: rgba(255,255,255,.75); }
.dg-card-dark a  { color: var(--dg-accent); font-weight: 700; text-decoration: none; }
.dg-card-ai { background: linear-gradient(135deg, var(--dg-dark), var(--dg-navy)); border-radius: 8px; border: 1px solid rgba(245,166,35,.25); padding: 1.5rem; height: 100%; }

.btn-dg-accent        { background: var(--dg-accent) !important; color: #fff !important; border: none; border-radius: 4px; font-weight: 700; padding: 10px 24px; text-decoration: none; display: inline-block; }
.btn-dg-outline       { background: transparent !important; border: 2px solid var(--dg-navy) !important; color: var(--dg-navy) !important; border-radius: 4px; font-weight: 700; padding: 9px 22px; text-decoration: none; display: inline-block; }
.btn-dg-outline-white { background: transparent !important; border: 2px solid rgba(255,255,255,.6) !important; color: #fff !important; border-radius: 4px; font-weight: 700; padding: 9px 22px; text-decoration: none; display: inline-block; }

.dg-section-light { background: var(--dg-offwhite); padding: 80px 0; }
.dg-section-white { background: #fff; padding: 80px 0; }
.dg-section-navy  { background: var(--dg-navy); padding: 80px 0; }
.dg-section-navy h2 { color: #fff; }

.dg-client-logo img { filter: grayscale(1); opacity: .55; transition: opacity .2s; max-height: 40px; width: auto; }
.dg-client-logo img:hover { opacity: .85; }

.accordion-item { box-shadow: 0 1px 4px rgba(26,58,107,.06); }
.accordion-button:not(.collapsed) { background: var(--dg-offwhite); color: var(--dg-navy); box-shadow: none; }
.accordion-button:focus { box-shadow: none; }
</style>"""

print("Iniezione CSS globale in custom_code_head...")
result = odoo("website", "write",
    ids=[WEBSITE_ID],
    params={"vals": {"custom_code_head": CUSTOM_CSS}})
print(f"Risultato write: {result}")

# Verifica
site = odoo("website", "read",
    ids=[WEBSITE_ID],
    params={"fields": ["custom_code_head"]})
head = site[0].get("custom_code_head", "") or ""
print(f"CSS iniettato: {len(head)} caratteri")
print("Task 2 completato. Verifica su https://www.debro.it — font Inter attivo.")
