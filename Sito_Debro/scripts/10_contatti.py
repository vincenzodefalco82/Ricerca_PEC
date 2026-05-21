import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

# Imposta CRM default team = Website (id=2)
odoo("website", "write",
    ids=[WEBSITE_ID],
    params={"vals": {"crm_default_team_id": 2}})
print("CRM default team → Website (id=2)")

MAPS_URL = ("https://maps.google.com/maps"
            "?q=Via+Miguel+Cervantes+De+Saavedra,+55%2F5,+80133+Napoli+NA+Italy"
            "&amp;output=embed")

ARCH = f"""<t t-name="custom.page_contatti">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- Hero minimal -->
      <section class="dg-section-navy text-center" style="padding:60px 0 50px;">
        <div class="container">
          <h1 style="color:#fff;">Parliamo.</h1>
          <p class="mt-2 text-dg-muted">Scegli l&#39;area, raccontaci il tuo progetto.</p>
        </div>
      </section>

      <!-- Form + Info -->
      <section class="dg-section-white">
        <div class="container">
          <div class="row g-5">

            <!-- Form -->
            <div class="col-lg-7">
              <form action="/website_form/crm.lead"
                    method="post"
                    class="s_website_form"
                    data-success_page="/"
                    enctype="multipart/form-data">

                <div class="row g-3">
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Nome e Cognome *</label>
                    <input type="text" name="contact_name" class="form-control" required="required" placeholder="Mario Rossi"/>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Azienda</label>
                    <input type="text" name="partner_name" class="form-control" placeholder="Azienda Srl"/>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Email *</label>
                    <input type="email" name="email_from" class="form-control" required="required" placeholder="mario@azienda.it"/>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Telefono</label>
                    <input type="tel" name="phone" class="form-control" placeholder="+39 081 000000"/>
                  </div>
                  <div class="col-12">
                    <label class="form-label fw-bold">Area di interesse *</label>
                    <select name="name" class="form-select" required="required">
                      <option value="">Seleziona un&#39;area...</option>
                      <option value="Sito web — Consulting">Consulting</option>
                      <option value="Sito web — Software">Software</option>
                      <option value="Sito web — Formazione">Formazione</option>
                      <option value="Sito web — AI">AI</option>
                      <option value="Sito web — Altro">Altro</option>
                    </select>
                  </div>
                  <div class="col-12">
                    <label class="form-label fw-bold">Messaggio *</label>
                    <textarea name="description" class="form-control" rows="5" required="required" placeholder="Raccontaci il tuo progetto o la tua necessità..."></textarea>
                  </div>
                  <div class="col-12">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" id="privacy" name="check_privacy" required="required"/>
                      <label class="form-check-label" for="privacy">
                        Ho letto e accetto la <a href="/privacy-policy/" target="_blank">Privacy Policy</a> *
                      </label>
                    </div>
                  </div>
                  <div class="col-12 mt-2">
                    <button type="submit" class="btn-dg-accent">Invia messaggio</button>
                  </div>
                </div>
              </form>
            </div>

            <!-- Info -->
            <div class="col-lg-5">
              <h3>Dove siamo</h3>
              <p style="color:var(--dg-slate);">
                Debro S.r.l.<br/>
                Via Miguel Cervantes De Saavedra, 55/5<br/>
                80133 Napoli (NA)
              </p>
              <p class="mt-3">
                <a href="mailto:debro@debro.it" style="color:var(--dg-navy);font-weight:600;">debro@debro.it</a><br/>
                <a href="mailto:debrosrls@debro.it" style="color:var(--dg-navy);font-weight:600;">debrosrls@debro.it</a>
              </p>
              <div class="mt-4" style="border-radius:8px;overflow:hidden;">
                <iframe
                  src="{MAPS_URL}"
                  width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade">
                </iframe>
              </div>
            </div>

          </div>
        </div>
      </section>

    </div>
  </t>
</t>"""

existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/contatti/"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Pagina /contatti/ esiste (id={existing[0]['id']}) — aggiorno arch...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {
            "arch": ARCH,
            "website_meta_title": "Contatti · Debro Group",
            "website_meta_description": "Contatta Debro Group per consulenza, sviluppo software, formazione o AI. Prima call gratuita.",
        }})
    print("Aggiornata.")
else:
    print("Creazione pagina Contatti...")
    ids = odoo("website.page", "create",
        params={"vals_list": [{
            "name":                     "Contatti",
            "type":                     "qweb",
            "key":                      "custom.page_contatti",
            "url":                      "/contatti/",
            "website_id":               WEBSITE_ID,
            "is_published":             True,
            "website_indexed":          False,
            "website_meta_title":       "Contatti · Debro Group",
            "website_meta_description": "Contatta Debro Group per consulenza, sviluppo software, formazione o AI. Prima call gratuita.",
            "arch":                     ARCH,
        }]})
    print(f"Contatti creata: id={ids[0] if isinstance(ids, list) else ids}")

print()
print("Task 10 completato.")
print("⚙️  Verifica: https://www.debro.it/contatti/")
print("⚙️  SMTP: Settings → Technical → Outgoing Mail Servers → configura @debro.it")
print("⚙️  Test form: compila e invia → controlla CRM → Pipeline")
