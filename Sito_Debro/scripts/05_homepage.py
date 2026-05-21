import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

LOGO_BICOCCA    = "/web/image/5216/Universit__degli_Studi_di_Milano-Bicocca-logo-36B841D9FE-seeklogo.com.png"
LOGO_SIELTE     = "/web/image/5212/logo_sielte.png"
LOGO_MET        = "/web/image/5214/met%20italia.png"
LOGO_LEGAMBIENTE= "/web/image/5211/Legambiente_logo.png"
LOGO_UNIPV      = "/web/image/5213/unipv.png"
LOGO_UNIROMA2   = "/web/image/5215/uniroma2.png"
LOGO_BEON       = "/web/image/5217/beon.png"

ARCH = f"""<t t-name="custom.page_homepage">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- HERO -->
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-6">
              <div class="dg-accent-bar"></div>
              <h1>Un gruppo. Quattro specializzazioni. Zero improvvisazione.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Consulenza, software, formazione e AI per le PMI italiane che fanno sul serio.</p>
              <div class="d-flex gap-3 flex-wrap">
                <a href="#bu-section" class="btn-dg-accent">Scopri il Gruppo</a>
                <a href="/contatti/" class="btn-dg-outline-white">Contattaci</a>
              </div>
            </div>
            <div class="col-lg-6">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:16px;text-align:center;">
                  <div style="font-size:12px;font-weight:700;color:rgba(255,255,255,.9);margin-bottom:4px;">Consulting</div>
                  <div style="font-size:11px;color:rgba(255,255,255,.5);">ISO · ACN · Normative</div>
                </div>
                <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:16px;text-align:center;">
                  <div style="font-size:12px;font-weight:700;color:rgba(255,255,255,.9);margin-bottom:4px;">Software</div>
                  <div style="font-size:11px;color:rgba(255,255,255,.5);">Custom · ICT · Cloud</div>
                </div>
                <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:16px;text-align:center;">
                  <div style="font-size:12px;font-weight:700;color:rgba(255,255,255,.9);margin-bottom:4px;">Formazione</div>
                  <div style="font-size:11px;color:rgba(255,255,255,.5);">81/08 · ICT · Mgmt</div>
                </div>
                <div style="background:rgba(255,255,255,.12);border-radius:8px;padding:16px;text-align:center;border:1px solid rgba(245,166,35,.4);">
                  <div style="font-size:12px;font-weight:700;color:#F5A623;margin-bottom:4px;">Debro AI</div>
                  <div style="font-size:11px;color:rgba(255,255,255,.5);">Processi · Dati · PMI</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- CHI SIAMO -->
      <section class="dg-section-white">
        <div class="container">
          <div class="row align-items-center g-5">
            <div class="col-lg-7">
              <span class="dg-label">Chi siamo</span>
              <h2>Non siamo un&#39;agenzia tuttofare. Siamo un gruppo che sa cosa fa.</h2>
              <p class="mt-3">Debro è un ecosistema di competenze: consulenza organizzativa, sviluppo software, formazione professionale e AI applicata. Quattro realtà specializzate, un unico obiettivo — generare valore concreto per chi ci sceglie.</p>
            </div>
            <div class="col-lg-5">
              <div class="d-flex flex-column gap-3">
                <div style="background:var(--dg-light);border-radius:6px;padding:12px 16px;font-weight:600;color:var(--dg-dark);">&#10003; Competenze reali, non slide</div>
                <div style="background:var(--dg-light);border-radius:6px;padding:12px 16px;font-weight:600;color:var(--dg-dark);">&#10003; Un solo interlocutore per 4 aree</div>
                <div style="background:var(--dg-light);border-radius:6px;padding:12px 16px;font-weight:600;color:var(--dg-dark);">&#10003; Target: PMI e PA italiane</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 4 BU -->
      <section class="dg-section-light" id="bu-section">
        <div class="container">
          <span class="dg-label">Le nostre aree</span>
          <h2>Quattro specializzazioni. Un gruppo.</h2>
          <div class="row row-cols-1 row-cols-md-2 g-4 mt-3">
            <div class="col">
              <div class="dg-card-light">
                <span class="dg-label">Consulting</span>
                <h3>La normativa non aspetta.</h3>
                <p>ISO, ACN, sistemi di gestione, D.Lgs. 36/2023.</p>
                <a href="/consulting/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;">Scopri &#8594;</a>
              </div>
            </div>
            <div class="col">
              <div class="dg-card-dark">
                <span class="dg-label" style="color:rgba(255,255,255,.6);">Software</span>
                <h3>Codice che va in produzione.</h3>
                <p>Software custom, consulenza ICT, ARCASID.</p>
                <a href="/software/">Scopri &#8594;</a>
              </div>
            </div>
            <div class="col">
              <div class="dg-card-light">
                <span class="dg-label">Formazione</span>
                <h3>Formazione obbligatoria. Non inutile.</h3>
                <p>81/08, ICT &amp; Digital Skills, Management.</p>
                <a href="/formazione/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;">Scopri &#8594;</a>
              </div>
            </div>
            <div class="col">
              <div class="dg-card-ai">
                <span class="dg-label" style="color:#F5A623;">Debro AI</span>
                <h3 style="color:#fff;">L&#39;AI che lavora.<br/>Nei tuoi processi.</h3>
                <p style="color:rgba(255,255,255,.65);">Automazione, analisi e assistenti AI su misura. Nessuna demo. Solo risultati misurabili.</p>
                <a href="/ai/" style="color:#F5A623;font-weight:700;text-decoration:none;">Scopri &#8594;</a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- CLIENTI -->
      <section class="dg-section-white">
        <div class="container text-center">
          <span class="dg-label">Ci hanno scelto</span>
          <div class="d-flex flex-wrap gap-5 justify-content-center align-items-center mt-4">
            <div class="dg-client-logo"><img src="{LOGO_BICOCCA}" alt="Università Milano Bicocca"/></div>
            <div class="dg-client-logo"><img src="{LOGO_SIELTE}" alt="Sielte"/></div>
            <div class="dg-client-logo"><img src="{LOGO_MET}" alt="Met Italia"/></div>
            <div class="dg-client-logo"><img src="{LOGO_LEGAMBIENTE}" alt="Legambiente"/></div>
            <div class="dg-client-logo"><img src="{LOGO_UNIPV}" alt="Università di Pavia"/></div>
            <div class="dg-client-logo"><img src="{LOGO_UNIROMA2}" alt="Università Roma Tor Vergata"/></div>
            <div class="dg-client-logo"><img src="{LOGO_BEON}" alt="Beon"/></div>
          </div>
        </div>
      </section>

      <!-- CTA FINALE -->
      <section class="dg-section-light text-center">
        <div class="container">
          <h2>Parliamo del tuo progetto.</h2>
          <p class="mt-3 mb-4">Un&#39;analisi iniziale è gratuita e senza impegno. Scopri quale area Debro fa per te.</p>
          <a href="/contatti/" class="btn-dg-accent">Contattaci ora</a>
        </div>
      </section>

    </div>
  </t>
</t>"""

# Controlla se pagina esiste già
existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/home"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Pagina /home esiste (id={existing[0]['id']}) — aggiorno arch...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {"arch": ARCH,
                         "website_meta_title": "Debro Group · Consulting, Software, Formazione e AI per PMI",
                         "website_meta_description": "Debro è un gruppo di competenze specializzate: consulenza normativa, sviluppo software, formazione professionale e AI applicata per le PMI italiane."}})
    print("Aggiornata.")
else:
    print("Creazione Homepage...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Homepage",
            "type":                     "qweb",
            "key":                      "custom.page_homepage",
            "url":                      "/home",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          True,
            "website_meta_title":       "Debro Group · Consulting, Software, Formazione e AI per PMI",
            "website_meta_description": "Debro è un gruppo di competenze specializzate: consulenza normativa, sviluppo software, formazione professionale e AI applicata per le PMI italiane.",
            "arch":                     ARCH,
        }]})
    print(f"Homepage creata: id={ids[0]}")

print()
print("Task 5 completato.")
print("⚙️  STEP MANUALE: Website → Settings → Homepage → seleziona 'Homepage'")
print("    oppure aggiorna menu 'Home' (id=5) con url='/home'")
