import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

ARCH = """<t t-name="custom.page_formazione">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- Hero -->
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:rgba(255,255,255,.7);">Formazione</span>
              <h1>Formazione obbligatoria. Ma non inutile.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Corsi D.Lgs. 81/08, ICT e sviluppo professionale — progettati per lasciare qualcosa, non solo un attestato.</p>
              <a href="/contatti/?area=formazione" class="btn-dg-accent">Richiedi il catalogo</a>
            </div>
            <div class="col-lg-5">
              <div class="d-flex flex-column gap-3">
                <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
                  <span style="font-size:20px;">&#128187;</span>
                  <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">ICT &amp; Digital Skills</span>
                </div>
                <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
                  <span style="font-size:20px;">&#128202;</span>
                  <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">Management &amp; Soft Skills</span>
                </div>
                <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
                  <span style="font-size:20px;">&#9937;</span>
                  <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">Sicurezza D.Lgs. 81/08</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Aree -->
      <section class="dg-section-white">
        <div class="container">
          <span class="dg-label">Le nostre aree</span>
          <h2>Tre aree. Un approccio concreto.</h2>
          <div class="row row-cols-1 row-cols-md-3 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>ICT &amp; Digital Skills</h3>
              <p>Python, Java, React, SQL, Cybersecurity, Cloud, AI/ML. Programmi tecnici per chi deve davvero usare gli strumenti.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Management e Soft Skills</h3>
              <p>Agile, Scrum, PMI, Leadership, Comunicazione, Coaching. Per chi gestisce team, progetti o cambiamenti organizzativi.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Salute e Sicurezza 81/08</h3>
              <p>Corsi per lavoratori, preposti, dirigenti, RLS, RSPP, ASPP, antincendio, primo soccorso. Obbligatori e finalmente utili.</p>
            </div></div>
          </div>
        </div>
      </section>

      <!-- Catalogo accordion -->
      <section class="dg-section-light">
        <div class="container">
          <span class="dg-label">Catalogo corsi</span>
          <h2>Cosa offriamo.</h2>
          <div class="accordion mt-4" id="catalogoCorsi">

            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-navy)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#ict" style="font-weight:700;color:var(--dg-dark);">ICT &amp; Digital Skills</button>
              </h2>
              <div id="ict" class="accordion-collapse collapse show" data-bs-parent="#catalogoCorsi">
                <div class="accordion-body">
                  <ul class="list-unstyled">
                    <li class="mb-2">&#10003; Programmazione — Python, Java, JavaScript/React, SQL</li>
                    <li class="mb-2">&#10003; Cybersecurity &amp; Data Protection — GDPR, ISO/IEC 27001, OWASP</li>
                    <li class="mb-2">&#10003; Cloud &amp; DevOps — AWS, Azure, Kubernetes, Docker, CI/CD</li>
                    <li class="mb-2">&#10003; Digitalizzazione processi aziendali</li>
                    <li>&#10003; AI &amp; Machine Learning applicata al business</li>
                  </ul>
                </div>
              </div>
            </div>

            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-navy)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#mgmt" style="font-weight:700;color:var(--dg-dark);">Management e Soft Skills</button>
              </h2>
              <div id="mgmt" class="accordion-collapse collapse" data-bs-parent="#catalogoCorsi">
                <div class="accordion-body">
                  <ul class="list-unstyled">
                    <li class="mb-2">&#10003; Project Management Agile / Scrum / PMI</li>
                    <li class="mb-2">&#10003; Leadership e gestione del team</li>
                    <li class="mb-2">&#10003; Comunicazione efficace e negoziazione</li>
                    <li>&#10003; Coaching e sviluppo soft skills</li>
                  </ul>
                </div>
              </div>
            </div>

            <div class="accordion-item border-0" style="border-left:3px solid var(--dg-navy)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#safety" style="font-weight:700;color:var(--dg-dark);">Salute e Sicurezza D.Lgs. 81/08</button>
              </h2>
              <div id="safety" class="accordion-collapse collapse" data-bs-parent="#catalogoCorsi">
                <div class="accordion-body">
                  <ul class="list-unstyled">
                    <li class="mb-2">&#10003; Corsi per lavoratori — basso/medio/alto rischio + aggiornamenti</li>
                    <li class="mb-2">&#10003; Corsi per dirigenti e datori di lavoro</li>
                    <li class="mb-2">&#10003; RLS / RSPP / ASPP — moduli A, B, C + aggiornamenti</li>
                    <li class="mb-2">&#10003; Antincendio — livelli 1, 2, 3 con prove pratiche</li>
                    <li class="mb-2">&#10003; Primo Soccorso — gruppi A, B, C + BLSD</li>
                    <li class="mb-2">&#10003; Lavori in quota + DPI III categoria</li>
                    <li>&#10003; PES / PAV / PEI — sicurezza elettrica</li>
                  </ul>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- CTA -->
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Verifica la tua scadenza.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Controlla lo stato dei tuoi obbligatori 81/08 e richiedi il catalogo completo.</p>
          <a href="/contatti/?area=formazione" class="btn-dg-accent">Richiedi il catalogo</a>
        </div>
      </section>

    </div>
  </t>
</t>"""

existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/formazione/"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Pagina /formazione/ esiste (id={existing[0]['id']}) — aggiorno arch...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {
            "arch": ARCH,
            "website_meta_title": "Debro Formazione · Corsi 81/08, ICT e Management",
            "website_meta_description": "Corsi D.Lgs. 81/08, ICT & Digital Skills e Management. Formazione obbligatoria e percorsi di sviluppo professionale.",
        }})
    print("Aggiornata.")
else:
    print("Creazione pagina Formazione...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Debro Formazione",
            "type":                     "qweb",
            "key":                      "custom.page_formazione",
            "url":                      "/formazione/",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          True,
            "website_meta_title":       "Debro Formazione · Corsi 81/08, ICT e Management",
            "website_meta_description": "Corsi D.Lgs. 81/08, ICT & Digital Skills e Management. Formazione obbligatoria e percorsi di sviluppo professionale.",
            "arch":                     ARCH,
        }]})
    print(f"Formazione creata: id={ids[0] if isinstance(ids, list) else ids}")

print()
print("Task 8 completato.")
print("⚙️  Verifica: https://www.debro.it/formazione/")
