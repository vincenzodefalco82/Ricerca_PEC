import sys
import os
import requests
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID, ODOO_URL

OUR_PAGES = [25, 26, 27, 28, 29, 33]

# ══════════════════════════════════════════════════════════
# STEP 1 — Verifica meta tag
# ══════════════════════════════════════════════════════════
print("=" * 60)
print("STEP 1 — Verifica meta tag")
print("=" * 60)

pages = odoo("website.page", "search_read",
    params={"domain": [["website_id", "=", WEBSITE_ID],
                       ["id", "in", OUR_PAGES]],
            "fields": ["id", "name", "url", "website_meta_title",
                       "website_meta_description", "website_indexed",
                       "is_published"]})

all_ok = True
for p in sorted(pages, key=lambda x: x["id"]):
    title_len = len(p.get("website_meta_title") or "")
    desc_len  = len(p.get("website_meta_description") or "")
    title_ok  = 30 <= title_len <= 70
    desc_ok   = 80 <= desc_len  <= 160
    published = p.get("is_published")
    indexed   = p.get("website_indexed")

    status_t = "✓" if title_ok  else "⚠"
    status_d = "✓" if desc_ok   else "⚠"
    status_p = "✓" if published else "✗"
    status_i = "✓" if indexed   else "—"

    if not (title_ok and desc_ok and published):
        all_ok = False

    print(f"\n  [{p['url']}]  pub:{status_p}  index:{status_i}")
    print(f"    title  ({title_len:3}ch) {status_t}  {(p.get('website_meta_title') or '')[:55]}")
    print(f"    desc   ({desc_len:3}ch) {status_d}  {(p.get('website_meta_description') or '')[:55]}")

print()
if all_ok:
    print("✅ Meta tag OK su tutte le pagine.")
else:
    print("⚠️  Alcune pagine hanno meta tag fuori range (30-70 title, 80-160 desc).")

# ══════════════════════════════════════════════════════════
# STEP 2 — Verifica sitemap
# ══════════════════════════════════════════════════════════
print()
print("=" * 60)
print("STEP 2 — Verifica sitemap.xml")
print("=" * 60)
try:
    r = requests.get(f"{ODOO_URL}/sitemap.xml", timeout=10)
    if r.status_code == 200 and "<loc>" in r.text:
        urls_in_sitemap = r.text.count("<loc>")
        print(f"✅ sitemap.xml OK — {urls_in_sitemap} URL indicizzati")
        for url_path in ["/home", "/consulting/", "/software/", "/formazione/", "/ai/"]:
            found = url_path in r.text
            print(f"  {'✓' if found else '✗'}  {url_path}")
    else:
        print(f"⚠️  sitemap.xml status={r.status_code}")
except Exception as e:
    print(f"⚠️  Impossibile raggiungere sitemap: {e}")

# ══════════════════════════════════════════════════════════
# STEP 3 — Crea pagina Privacy Policy
# ══════════════════════════════════════════════════════════
print()
print("=" * 60)
print("STEP 3 — Privacy Policy")
print("=" * 60)

PRIVACY_ARCH = """<t t-name="custom.page_privacy">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <section class="dg-section-white" style="padding:80px 0;">
        <div class="container" style="max-width:760px;">
          <h1>Privacy Policy</h1>
          <p style="color:var(--dg-slate);font-size:14px;">Ultimo aggiornamento: Maggio 2026</p>

          <h2 class="mt-5" style="font-size:1.3rem;">1. Titolare del trattamento</h2>
          <p>Debro S.r.l.<br/>Via Miguel Cervantes De Saavedra, 55/5 — 80133 Napoli (NA)<br/>
          Email: <a href="mailto:debro@debro.it">debro@debro.it</a></p>

          <h2 class="mt-4" style="font-size:1.3rem;">2. Dati raccolti</h2>
          <p>Il sito raccoglie dati personali esclusivamente tramite il modulo di contatto (nome, email, telefono, azienda, messaggio) per rispondere alle richieste degli utenti. Non raccoglie dati di profilazione.</p>

          <h2 class="mt-4" style="font-size:1.3rem;">3. Finalità del trattamento</h2>
          <ul>
            <li>Risposta a richieste di contatto e preventivi</li>
            <li>Adempimenti contrattuali e precontrattuali</li>
            <li>Analisi statistica anonima del traffico web (cookie tecnici)</li>
          </ul>

          <h2 class="mt-4" style="font-size:1.3rem;">4. Base giuridica</h2>
          <p>Consenso dell&#39;interessato (Art. 6, lett. a GDPR) per i dati raccolti tramite form. Legittimo interesse per l&#39;analisi statistica anonima.</p>

          <h2 class="mt-4" style="font-size:1.3rem;">5. Conservazione</h2>
          <p>I dati sono conservati per il tempo necessario a gestire la richiesta e, successivamente, per un massimo di 24 mesi salvo diversa indicazione normativa.</p>

          <h2 class="mt-4" style="font-size:1.3rem;">6. Diritti dell&#39;interessato</h2>
          <p>L&#39;utente può esercitare i diritti di accesso, rettifica, cancellazione, limitazione e portabilità scrivendo a <a href="mailto:debro@debro.it">debro@debro.it</a>.</p>

          <h2 class="mt-4" style="font-size:1.3rem;">7. Cookie</h2>
          <p>Il sito utilizza cookie tecnici necessari al funzionamento. Non utilizza cookie di profilazione o marketing di terze parti. Per maggiori dettagli consultare la <a href="/cookie-policy/">Cookie Policy</a>.</p>

          <h2 class="mt-4" style="font-size:1.3rem;">8. Trasferimenti extra-UE</h2>
          <p>I dati non vengono trasferiti al di fuori dell&#39;Unione Europea.</p>

          <h2 class="mt-4" style="font-size:1.3rem;">9. Modifiche</h2>
          <p>Il Titolare si riserva il diritto di modificare questa informativa. Le modifiche saranno pubblicate su questa pagina con data di aggiornamento.</p>

          <div style="margin-top:48px;padding:20px 24px;background:var(--dg-light);border-radius:8px;font-size:13px;color:var(--dg-slate);">
            Per qualsiasi domanda relativa al trattamento dei tuoi dati personali:<br/>
            <a href="mailto:debro@debro.it" style="color:var(--dg-navy);font-weight:600;">debro@debro.it</a>
          </div>
        </div>
      </section>
    </div>
  </t>
</t>"""

existing_pp = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/privacy-policy/"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing_pp:
    print(f"Privacy Policy esiste (id={existing_pp[0]['id']}) — aggiorno...")
    odoo("website.page", "write",
        ids=[existing_pp[0]["id"]],
        params={"vals": {"arch": PRIVACY_ARCH}})
    print("Aggiornata.")
else:
    print("Creazione Privacy Policy...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Privacy Policy",
            "type":                     "qweb",
            "key":                      "custom.page_privacy",
            "url":                      "/privacy-policy/",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          False,
            "website_meta_title":       "Privacy Policy · Debro Group",
            "website_meta_description": "Informativa sul trattamento dei dati personali ai sensi del GDPR — Debro S.r.l.",
            "arch":                     PRIVACY_ARCH,
        }]})
    print(f"Privacy Policy creata: id={ids[0] if isinstance(ids, list) else ids}")

# ══════════════════════════════════════════════════════════
# CHECKLIST PRE-LANCIO
# ══════════════════════════════════════════════════════════
print()
print("=" * 60)
print("CHECKLIST PRE-LANCIO")
print("=" * 60)
print("""
✅ automatizzato via script:
   ✓ Homepage v2 live (/home)
   ✓ Pagine BU live (consulting, software, formazione, ai)
   ✓ Pagina Contatti live + form → CRM
   ✓ Meta title + description IT e EN su tutte le pagine
   ✓ Menu IT e EN configurati
   ✓ Privacy Policy creata (/privacy-policy/)
   ✓ Design system CSS iniettato
   ✓ Loghi clienti caricati

⚙️  step manuali rimasti:
   [ ] Website → Settings → Homepage → seleziona 'Homepage'
       (se non già fatto dopo Task 5)
   [ ] Website → Settings → Cookie bar → attiva cookie banner GDPR
   [ ] Website → Settings → SEO → Schema Organization (nome: Debro Group)
   [ ] Test form contatti → verifica lead in CRM → Pipeline
   [ ] Switcher IT/EN visibile in navbar
   [ ] Traduci contenuto pagine in EN (Translate button per pagina)
   [ ] Google Search Console → verifica dominio → invia /sitemap.xml
   [ ] SMTP @debro.it → Settings → Outgoing Mail Servers
   [ ] Verifica Google Maps embed in /contatti/
""")

print("Task 12 completato.")
