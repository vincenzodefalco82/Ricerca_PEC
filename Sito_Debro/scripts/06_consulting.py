import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

ARCH = """<t t-name="custom.page_consulting">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- Hero -->
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:rgba(255,255,255,.7);">Consulting</span>
              <h1>La normativa non aspetta. Noi siamo già pronti.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Sistemi di gestione, compliance ACN e certificazioni ISO per aziende che non vogliono essere colte impreparate.</p>
              <div class="d-flex gap-3 flex-wrap">
                <a href="/contatti/?area=consulting" class="btn-dg-accent">Parliamo della tua situazione</a>
                <a href="#servizi" class="btn-dg-outline-white">I nostri servizi &#8594;</a>
              </div>
            </div>
            <div class="col-lg-5">
              <div class="d-flex flex-column gap-2">
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid #F5A623;">ISO 9001 · 27001 · 45001</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid rgba(255,255,255,.2);">Accreditamento ACN</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid rgba(255,255,255,.2);">D.Lgs. 36/2023</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid rgba(255,255,255,.2);">Piattaforme PAD</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Servizi -->
      <section class="dg-section-white" id="servizi">
        <div class="container">
          <span class="dg-label">Cosa facciamo</span>
          <h2>Trasformiamo la complessità normativa in vantaggio competitivo.</h2>
          <div class="row row-cols-1 row-cols-md-2 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>Sistemi di gestione</h3>
              <p>Progettiamo sistemi integrati (qualità, sicurezza, ambiente) adattati alla struttura reale dell&#39;organizzazione, non a template standard.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Accreditamento ACN</h3>
              <p>Percorso completo: analisi del gap, documentazione, affiancamento nei processi di verifica presso l&#39;Agenzia per la Cybersicurezza Nazionale.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Normative ISO</h3>
              <p>ISO 9001, 27001, 45001. Dalla gap analysis alla certificazione, fino al mantenimento nel tempo.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Codice Contratti &amp; PAD</h3>
              <p>Recepimento D.Lgs. 36/2023 e supporto adozione Piattaforme di Approvvigionamento Digitale per stazioni appaltanti e operatori economici.</p>
            </div></div>
          </div>
        </div>
      </section>

      <!-- Progetti -->
      <section class="dg-section-light">
        <div class="container">
          <span class="dg-label">Progetti realizzati</span>
          <h2>Tre casi concreti.</h2>
          <div class="d-flex flex-column gap-4 mt-4">
            <div class="dg-card-light">
              <h3>Supporto Università</h3>
              <p>Gestione documentale e processi di accreditamento per importanti atenei italiani, con digitalizzazione delle Scuole di Specializzazione.</p>
            </div>
            <div class="dg-card-light">
              <h3>Piattaforme PAD</h3>
              <p>Gestione adozione Piattaforme di Approvvigionamento Digitale per centrali di committenza con formazione e supervisione.</p>
            </div>
            <div class="dg-card-light">
              <h3>D.Lgs 36/2023</h3>
              <p>Consulenza per recepimento nuovo Codice Contratti Pubblici: procedure, modelli e strumenti di compliance.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- CTA -->
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Parliamo della tua situazione.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Prima call gratuita. Nessun impegno. Solo una conversazione concreta.</p>
          <a href="/contatti/?area=consulting" class="btn-dg-accent">Contattaci &#8594;</a>
        </div>
      </section>

    </div>
  </t>
</t>"""

existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/consulting/"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Pagina /consulting/ esiste (id={existing[0]['id']}) — aggiorno arch...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {
            "arch": ARCH,
            "website_meta_title": "Debro Consulting · ISO, ACN, Sistemi di Gestione",
            "website_meta_description": "Sistemi di gestione, accreditamento ACN e normative ISO per aziende che non vogliono essere colte impreparate.",
        }})
    print("Aggiornata.")
else:
    print("Creazione pagina Consulting...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Debro Consulting",
            "type":                     "qweb",
            "key":                      "custom.page_consulting",
            "url":                      "/consulting/",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          True,
            "website_meta_title":       "Debro Consulting · ISO, ACN, Sistemi di Gestione",
            "website_meta_description": "Sistemi di gestione, accreditamento ACN e normative ISO per aziende che non vogliono essere colte impreparate.",
            "arch":                     ARCH,
        }]})
    print(f"Consulting creata: id={ids[0] if isinstance(ids, list) else ids}")

print()
print("Task 6 completato.")
print("⚙️  Verifica: https://www.debro.it/consulting/")
