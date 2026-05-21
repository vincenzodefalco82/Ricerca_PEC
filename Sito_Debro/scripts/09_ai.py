import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

ARCH = """<t t-name="custom.page_ai">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- Hero -->
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:#F5A623;">Debro AI</span>
              <h1>L&#39;AI che lavora. Nei tuoi processi.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Automazione, analisi e assistenti AI su misura. Nessuna demo. Solo risultati misurabili.</p>
              <a href="/contatti/?area=ai" class="btn-dg-accent">Parliamo dei tuoi processi</a>
            </div>
            <div class="col-lg-5">
              <div class="d-flex flex-column gap-2 align-items-start">
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,.8);display:flex;align-items:center;gap:8px;">
                  <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>Processo manuale
                </div>
                <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,.3);">&#8595;</div>
                <div style="background:rgba(245,166,35,.15);border-radius:6px;padding:8px 14px;font-size:12px;color:#F5A623;font-weight:700;border:1px solid rgba(245,166,35,.3);display:flex;align-items:center;gap:8px;">
                  <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>AI Debro
                </div>
                <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,.3);">&#8595;</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,.8);display:flex;align-items:center;gap:8px;">
                  <span style="width:8px;height:8px;background:#4caf50;border-radius:50%;flex-shrink:0;"></span>Risultato misurabile
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Servizi -->
      <section class="dg-section-white">
        <div class="container">
          <span class="dg-label">Cosa facciamo</span>
          <h2>AI pratica. Non teorica.</h2>
          <div class="row row-cols-1 row-cols-md-3 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>Automazione dei processi</h3>
              <p>Identifichiamo i flussi ripetitivi — documentali, comunicativi, gestionali — e costruiamo automazioni che si integrano con i sistemi esistenti.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Analisi e supporto alle decisioni</h3>
              <p>Report automatici, alert predittivi, dashboard su misura. Dati che diventano informazioni utili prima che servano.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Assistenti AI su misura</h3>
              <p>Addestriamo modelli sui tuoi prodotti, procedure e settore. Non un chatbot generico — uno strumento che conosce la tua azienda.</p>
            </div></div>
          </div>
        </div>
      </section>

      <!-- FAQ accordion -->
      <section class="dg-section-light">
        <div class="container">
          <span class="dg-label">Domande frequenti</span>
          <h2>L&#39;AI fa per la mia azienda?</h2>
          <div class="accordion mt-4" id="faqAI">

            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" style="font-weight:700;">Siamo una PMI senza team IT interno. Possiamo usare l&#39;AI?</button>
              </h2>
              <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#faqAI">
                <div class="accordion-body">Sì. Progettiamo soluzioni che non richiedono un data scientist interno. Partiamo dai processi che già esistono.</div>
              </div>
            </div>

            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" style="font-weight:700;">Quanto tempo ci vuole per vedere risultati?</button>
              </h2>
              <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                <div class="accordion-body">Dipende dal processo. Le prime automazioni semplici sono operative in 2-4 settimane. Progetti più complessi seguono un piano incrementale con rilasci parziali.</div>
              </div>
            </div>

            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" style="font-weight:700;">I nostri dati restano al sicuro?</button>
              </h2>
              <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                <div class="accordion-body">Sì. Progettiamo con GDPR compliance by design. I dati del cliente non vengono usati per addestrare modelli generali.</div>
              </div>
            </div>

            <div class="accordion-item border-0" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" style="font-weight:700;">Che differenza c&#39;è da ChatGPT o Copilot?</button>
              </h2>
              <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                <div class="accordion-body">Quelli sono strumenti generici. Noi costruiamo soluzioni specifiche per il tuo settore, i tuoi dati e i tuoi processi.</div>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- CTA -->
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Parliamo dei tuoi processi.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Prima call gratuita. Nessun impegno.</p>
          <a href="/contatti/?area=ai" class="btn-dg-accent">Prenota una call gratuita</a>
        </div>
      </section>

    </div>
  </t>
</t>"""

existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/ai/"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Pagina /ai/ esiste (id={existing[0]['id']}) — aggiorno arch...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {
            "arch": ARCH,
            "website_meta_title": "Debro AI · Intelligenza Artificiale per PMI",
            "website_meta_description": "Automazione processi, analisi predittiva e assistenti AI su misura. AI pratica e misurabile per le PMI italiane.",
        }})
    print("Aggiornata.")
else:
    print("Creazione pagina AI...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Debro AI",
            "type":                     "qweb",
            "key":                      "custom.page_ai",
            "url":                      "/ai/",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          True,
            "website_meta_title":       "Debro AI · Intelligenza Artificiale per PMI",
            "website_meta_description": "Automazione processi, analisi predittiva e assistenti AI su misura. AI pratica e misurabile per le PMI italiane.",
            "arch":                     ARCH,
        }]})
    print(f"AI creata: id={ids[0] if isinstance(ids, list) else ids}")

print()
print("Task 9 completato.")
print("⚙️  Verifica: https://www.debro.it/ai/")
