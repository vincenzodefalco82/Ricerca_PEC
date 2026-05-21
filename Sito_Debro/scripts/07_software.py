import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

def pill(label, color="var(--dg-navy)"):
    return (f'<span style="background:{color};color:#fff;font-size:12px;'
            f'padding:4px 12px;border-radius:20px;font-weight:600;">{label}</span>')

stack_html = ""
for color, tags in [
    ("var(--dg-navy)", ["React", "Node.js", "Python", "Java Spring Boot"]),
    ("#2A5298",        ["AWS", "Azure", "GCP", "Docker"]),
    ("#455a7a",        ["PostgreSQL", "MongoDB", "ChatGPT API", "GDPR · OWASP"]),
]:
    for t in tags:
        stack_html += pill(t, color)

ARCH = f"""<t t-name="custom.page_software">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- Hero -->
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:rgba(255,255,255,.7);">Software</span>
              <h1>Software che va in produzione. Non solo in presentazione.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Sviluppo custom e consulenza ICT per chi ha bisogno di soluzioni che funzionano davvero nell&#39;ambiente reale.</p>
              <div class="d-flex gap-3 flex-wrap">
                <a href="/contatti/?area=software" class="btn-dg-accent">Raccontaci il tuo progetto</a>
                <a href="#progetti" class="btn-dg-outline-white">Vedi i progetti &#8594;</a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Come lavoriamo -->
      <section class="dg-section-white">
        <div class="container">
          <span class="dg-label">Come lavoriamo</span>
          <h2>Entriamo nei team. Capiamo i processi. Scriviamo codice.</h2>
          <div class="row row-cols-1 row-cols-md-2 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>Consulenza integrata</h3>
              <p>I nostri professionisti si affiancano ai team interni: cloud, microservizi, sicurezza applicativa, integrazione sistemi. Competenze reali, non slide.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Sviluppo end-to-end</h3>
              <p>Analisi dei requisiti, progettazione, sviluppo iterativo, test, deployment e supporto post-rilascio. Un ciclo completo, senza buchi di responsabilità.</p>
            </div></div>
          </div>
        </div>
      </section>

      <!-- Stack -->
      <section style="background:var(--dg-light);padding:60px 0;">
        <div class="container">
          <span class="dg-label">Stack tecnologico</span>
          <div class="d-flex gap-2 flex-wrap mt-3">{stack_html}</div>
        </div>
      </section>

      <!-- Progetti -->
      <section class="dg-section-white" id="progetti">
        <div class="container">
          <span class="dg-label">Progetti realizzati</span>
          <h2>In produzione, non in demo.</h2>
          <div class="d-flex flex-column gap-4 mt-4">

            <div class="dg-card-light">
              <span style="background:#e8f5e9;color:#2e7d32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In produzione</span>
              <h3 class="mt-2">ARCASID — Digital Logbook</h3>
              <p>Il primo sistema digitale per tirocini universitari. LogBook digitale, segreteria intelligente, Diploma Supplement automatico. Integrato con ESSE3/Cineca, SPID e SSO (Shibboleth, Microsoft SAML).</p>
              <small style="color:var(--dg-slate);">Università degli Studi di Milano Bicocca · arcasid.it</small>
            </div>

            <div class="dg-card-light">
              <span style="background:#e3f2fd;color:#1565c0;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In sviluppo</span>
              <h3 class="mt-2">BInclusion</h3>
              <p>L&#39;inclusione non si dichiara. Si misura. Piattaforma per gestione e monitoraggio dei percorsi di inclusione con strumenti operativi e dati reali per le decisioni.</p>
            </div>

            <div class="dg-card-light">
              <span style="background:#e8f5e9;color:#2e7d32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In produzione</span>
              <h3 class="mt-2">MedData — Ricerca Clinica</h3>
              <p>Piattaforma cloud per raccolta dati clinici standardizzati: questionari strutturati, dashboard e statistiche per ricerca scientifica.</p>
            </div>

          </div>
        </div>
      </section>

      <!-- CTA -->
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Raccontaci il tuo progetto.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Prima call gratuita. Nessun impegno.</p>
          <a href="/contatti/?area=software" class="btn-dg-accent">Parliamo &#8594;</a>
        </div>
      </section>

    </div>
  </t>
</t>"""

existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/software/"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Pagina /software/ esiste (id={existing[0]['id']}) — aggiorno arch...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {
            "arch": ARCH,
            "website_meta_title": "Debro Software · Sviluppo Custom e Consulenza ICT",
            "website_meta_description": "Software custom e consulenza ICT end-to-end. Dall'analisi al deployment, con chi sa davvero scrivere codice.",
        }})
    print("Aggiornata.")
else:
    print("Creazione pagina Software...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Debro Software",
            "type":                     "qweb",
            "key":                      "custom.page_software",
            "url":                      "/software/",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          True,
            "website_meta_title":       "Debro Software · Sviluppo Custom e Consulenza ICT",
            "website_meta_description": "Software custom e consulenza ICT end-to-end. Dall'analisi al deployment, con chi sa davvero scrivere codice.",
            "arch":                     ARCH,
        }]})
    print(f"Software creata: id={ids[0] if isinstance(ids, list) else ids}")

print()
print("Task 7 completato.")
print("⚙️  Verifica: https://www.debro.it/software/")
