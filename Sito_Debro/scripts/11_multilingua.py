import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

# ── IDs (verificati dal search_read) ──────────────────────
MENU_IDS = {
    "Home":       5,
    "Consulting": 10,
    "Software":   75,
    "Formazione": 7,
    "AI":         76,
    "Contatti":   77,
}

PAGE_IDS = {
    "/home":         25,
    "/consulting/":  26,
    "/software/":    27,
    "/formazione/":  28,
    "/ai/":          29,
    "/contatti/":    33,
}

MENU_EN = {
    5:  "Home",
    10: "Consulting",
    75: "Software",
    7:  "Training",
    76: "AI",
    77: "Contact",
}

PAGE_META_EN = {
    25: {
        "website_meta_title":       "Debro Group · Consulting, Software, Training and AI for SMBs",
        "website_meta_description": "Consulting, custom software, professional training and AI for Italian SMBs and public bodies. 10+ years, 15+ professionals, 40+ projects.",
    },
    26: {
        "website_meta_title":       "Debro Consulting · ISO, ACN, Management Systems",
        "website_meta_description": "Management systems, ACN accreditation and ISO standards for companies that cannot afford to be caught unprepared.",
    },
    27: {
        "website_meta_title":       "Debro Software · Custom Development and ICT Consulting",
        "website_meta_description": "End-to-end custom software and ICT consulting. From analysis to deployment, with people who know how to write code.",
    },
    28: {
        "website_meta_title":       "Debro Training · 81/08 Courses, ICT and Management",
        "website_meta_description": "D.Lgs. 81/08 courses, ICT & Digital Skills and Management. Mandatory training that actually teaches something.",
    },
    29: {
        "website_meta_title":       "Debro AI · Artificial Intelligence for SMBs",
        "website_meta_description": "Process automation, predictive analytics and custom AI assistants. Practical and measurable AI for Italian SMBs.",
    },
    33: {
        "website_meta_title":       "Contact · Debro Group",
        "website_meta_description": "Contact Debro Group for consulting, software development, training or AI. Free first call.",
    },
}

# ── Step 1: Traduci menu in EN ─────────────────────────────
print("Traduco menu items → EN...")
for menu_id, en_name in MENU_EN.items():
    odoo("website.menu", "write",
        ids=[menu_id],
        params={"vals": {"name": en_name}},
        context={"lang": "en_GB"})
    print(f"  ✓ menu id={menu_id} → '{en_name}'")

# ── Step 2: Meta tag EN per ogni pagina ────────────────────
print("\nImposto meta tag EN per le pagine...")
for page_id, meta in PAGE_META_EN.items():
    odoo("website.page", "write",
        ids=[page_id],
        params={"vals": meta},
        context={"lang": "en_GB"})
    print(f"  ✓ page id={page_id} → '{meta['website_meta_title'][:50]}'")

print()
print("Task 11 — automatizzato completato.")
print()
print("─" * 60)
print("⚙️  STEP MANUALI — contenuto pagine in EN")
print("─" * 60)
print()
print("Per ogni pagina: apri in Odoo Website → tasto 'Translate'")
print("(barra in alto) → traduci ogni campo di testo.")
print()
print("HOMEPAGE (/home):")
print("  H1: One group. Four specializations. Zero improvisation.")
print("  Sub: Consulting, custom software, training and AI")
print("       for Italian SMBs that mean business.")
print("  BU pills: Consulting / Software / Training / Debro AI")
print("  Numeri: years of experience / professionals / projects delivered")
print("  Sfide: 'Regulation that keeps changing.' → Debro Consulting")
print("         'Software that doesn't scale.' → Debro Software")
print("         'Skills that are missing.' → Debro Training + AI")
print("  CTA: 'Discover the Group' / 'Contact Us'")
print("  CTA finale: 'Let's talk about your project.'")
print()
print("CONSULTING (/consulting/):")
print("  H1: Regulation doesn't wait. We're already ready.")
print("  BU: Management Systems / ACN Accreditation / ISO Standards / Contracts Code")
print("  CTA: 'Let's talk about your situation'")
print()
print("SOFTWARE (/software/):")
print("  H1: Software that goes to production. Not just to demo.")
print("  CTA: 'Tell us about your project'")
print()
print("FORMAZIONE (/formazione/):")
print("  H1: Mandatory training. But not useless.")
print("  URL suggerito per EN: /en/training/")
print()
print("AI (/ai/):")
print("  H1: AI that works. In your processes.")
print("  CTA: 'Book a free call'")
print()
print("CONTATTI (/contatti/):")
print("  Dropdown: Consulting / Software / Training / AI / Other")
print("  Button: 'Send message'")
print()
print("⚙️  Language switcher: Website → Settings → verificare")
print("    che selettore IT/EN sia visibile in navbar.")
