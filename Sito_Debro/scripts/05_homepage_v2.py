import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo
from config import WEBSITE_ID

LOGO_BICOCCA     = "/web/image/5216/Universit__degli_Studi_di_Milano-Bicocca-logo-36B841D9FE-seeklogo.com.png"
LOGO_SIELTE      = "/web/image/5212/logo_sielte.png"
LOGO_MET         = "/web/image/5214/met%20italia.png"
LOGO_LEGAMBIENTE = "/web/image/5211/Legambiente_logo.png"
LOGO_UNIPV       = "/web/image/5213/unipv.png"
LOGO_UNIROMA2    = "/web/image/5215/uniroma2.png"
LOGO_BEON        = "/web/image/5217/beon.png"

ARCH = f"""<t t-name="custom.page_homepage">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- ═══════════════════════════════════════
           HERO — centrato, headline enorme
      ═══════════════════════════════════════ -->
      <section class="dg-hero" style="padding:100px 0 80px;text-align:center;">
        <div class="container" style="max-width:860px;">
          <div class="dg-accent-bar" style="margin:0 auto 24px;"></div>
          <h1 style="font-size:clamp(2.4rem,5.5vw,4.2rem);line-height:1.08;font-weight:800;letter-spacing:-.02em;color:#fff;">
            Un gruppo.<br/>Quattro competenze.<br/>Zero improvvisazione.
          </h1>
          <p class="text-dg-muted" style="font-size:1.2rem;margin:28px auto 40px;max-width:600px;line-height:1.6;">
            Consulenza normativa, software custom, formazione professionale e AI applicata.<br/>
            Per le PMI e PA italiane che fanno sul serio.
          </p>
          <div class="d-flex gap-3 justify-content-center flex-wrap">
            <a href="#aree" class="btn-dg-accent" style="font-size:1rem;padding:14px 32px;">Scopri il Gruppo</a>
            <a href="/contatti/" class="btn-dg-outline-white" style="font-size:1rem;padding:14px 32px;">Contattaci</a>
          </div>

          <!-- 4 pill BU -->
          <div class="d-flex gap-2 justify-content-center flex-wrap" style="margin-top:56px;">
            <a href="/consulting/" style="background:rgba(255,255,255,.10);color:rgba(255,255,255,.9);text-decoration:none;border-radius:40px;padding:8px 20px;font-size:13px;font-weight:700;border:1px solid rgba(255,255,255,.15);transition:background .2s;" onmouseover="this.style.background='rgba(255,255,255,.18)'" onmouseout="this.style.background='rgba(255,255,255,.10)'">
              Consulting <span style="opacity:.5;font-weight:400;margin-left:4px;">ISO · ACN</span>
            </a>
            <a href="/software/" style="background:rgba(255,255,255,.10);color:rgba(255,255,255,.9);text-decoration:none;border-radius:40px;padding:8px 20px;font-size:13px;font-weight:700;border:1px solid rgba(255,255,255,.15);" onmouseover="this.style.background='rgba(255,255,255,.18)'" onmouseout="this.style.background='rgba(255,255,255,.10)'">
              Software <span style="opacity:.5;font-weight:400;margin-left:4px;">Custom · ICT</span>
            </a>
            <a href="/formazione/" style="background:rgba(255,255,255,.10);color:rgba(255,255,255,.9);text-decoration:none;border-radius:40px;padding:8px 20px;font-size:13px;font-weight:700;border:1px solid rgba(255,255,255,.15);" onmouseover="this.style.background='rgba(255,255,255,.18)'" onmouseout="this.style.background='rgba(255,255,255,.10)'">
              Formazione <span style="opacity:.5;font-weight:400;margin-left:4px;">81/08 · ICT</span>
            </a>
            <a href="/ai/" style="background:rgba(245,166,35,.18);color:#F5A623;text-decoration:none;border-radius:40px;padding:8px 20px;font-size:13px;font-weight:700;border:1px solid rgba(245,166,35,.35);" onmouseover="this.style.background='rgba(245,166,35,.28)'" onmouseout="this.style.background='rgba(245,166,35,.18)'">
              Debro AI <span style="opacity:.7;font-weight:400;margin-left:4px;">Processi · Dati</span>
            </a>
          </div>
        </div>
      </section>

      <!-- ═══════════════════════════════════════
           NUMERI — credibilità immediata
      ═══════════════════════════════════════ -->
      <section style="background:#fff;border-bottom:1px solid #eef0f4;">
        <div class="container-fluid" style="max-width:1100px;margin:0 auto;">
          <div class="row g-0 text-center">
            <div class="col-6 col-md-3" style="padding:52px 16px;border-right:1px solid #eef0f4;">
              <div style="font-size:3.2rem;font-weight:800;color:var(--dg-navy);line-height:1;letter-spacing:-.03em;">10+</div>
              <div style="font-size:13px;color:var(--dg-slate);margin-top:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;">anni di esperienza</div>
            </div>
            <div class="col-6 col-md-3" style="padding:52px 16px;border-right:1px solid #eef0f4;">
              <div style="font-size:3.2rem;font-weight:800;color:var(--dg-navy);line-height:1;letter-spacing:-.03em;">15+</div>
              <div style="font-size:13px;color:var(--dg-slate);margin-top:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;">professionisti</div>
            </div>
            <div class="col-6 col-md-3" style="padding:52px 16px;border-right:1px solid #eef0f4;">
              <div style="font-size:3.2rem;font-weight:800;color:var(--dg-navy);line-height:1;letter-spacing:-.03em;">40+</div>
              <div style="font-size:13px;color:var(--dg-slate);margin-top:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;">progetti consegnati</div>
            </div>
            <div class="col-6 col-md-3" style="padding:52px 16px;">
              <div style="font-size:3.2rem;font-weight:800;color:var(--dg-navy);line-height:1;letter-spacing:-.03em;">4</div>
              <div style="font-size:13px;color:var(--dg-slate);margin-top:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;">aree di competenza</div>
            </div>
          </div>
        </div>
      </section>

      <!-- ═══════════════════════════════════════
           PROBLEMA → SOLUZIONE
      ═══════════════════════════════════════ -->
      <section class="dg-section-light">
        <div class="container">
          <div class="text-center mb-5">
            <span class="dg-label">Perché scegliere Debro</span>
            <h2 style="margin-top:12px;">Tre sfide reali. Un gruppo che le risolve.</h2>
          </div>
          <div class="row g-4">

            <div class="col-md-4">
              <div style="background:#fff;border-radius:12px;padding:36px 28px;height:100%;border-top:3px solid var(--dg-accent);box-shadow:0 2px 12px rgba(26,58,107,.06);">
                <div style="font-size:11px;color:var(--dg-slate);font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px;">La sfida</div>
                <h3 style="font-size:1.15rem;font-weight:700;color:var(--dg-dark);">Normativa che cambia. Continuamente.</h3>
                <p style="color:var(--dg-slate);font-size:14px;line-height:1.6;margin-top:10px;">ISO, ACN, D.Lgs. 36/2023. Stare al passo richiede esperti dedicati, non consulenti generici.</p>
                <div style="margin-top:24px;padding-top:20px;border-top:1px solid #eef0f4;">
                  <div style="font-size:11px;color:var(--dg-navy);font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;">La risposta</div>
                  <a href="/consulting/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;font-size:15px;">Debro Consulting &#8594;</a>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <div style="background:#fff;border-radius:12px;padding:36px 28px;height:100%;border-top:3px solid var(--dg-navy);box-shadow:0 2px 12px rgba(26,58,107,.06);">
                <div style="font-size:11px;color:var(--dg-slate);font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px;">La sfida</div>
                <h3 style="font-size:1.15rem;font-weight:700;color:var(--dg-dark);">Software che non scala. O non esiste ancora.</h3>
                <p style="color:var(--dg-slate);font-size:14px;line-height:1.6;margin-top:10px;">Soluzioni custom, integrazione sistemi, consulenza ICT. Serve chi sa scrivere codice e capisce il business.</p>
                <div style="margin-top:24px;padding-top:20px;border-top:1px solid #eef0f4;">
                  <div style="font-size:11px;color:var(--dg-navy);font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;">La risposta</div>
                  <a href="/software/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;font-size:15px;">Debro Software &#8594;</a>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <div style="background:#fff;border-radius:12px;padding:36px 28px;height:100%;border-top:3px solid #2A5298;box-shadow:0 2px 12px rgba(26,58,107,.06);">
                <div style="font-size:11px;color:var(--dg-slate);font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px;">La sfida</div>
                <h3 style="font-size:1.15rem;font-weight:700;color:var(--dg-dark);">Competenze che mancano. O restano inutilizzate.</h3>
                <p style="color:var(--dg-slate);font-size:14px;line-height:1.6;margin-top:10px;">Formazione 81/08, digital skills, AI applicata. Non corsi standard — percorsi su misura.</p>
                <div style="margin-top:24px;padding-top:20px;border-top:1px solid #eef0f4;">
                  <div style="font-size:11px;color:var(--dg-navy);font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;">La risposta</div>
                  <a href="/formazione/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;font-size:15px;">Debro Formazione + AI &#8594;</a>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- ═══════════════════════════════════════
           4 BU — LAYOUT ALTERNATO FULL-WIDTH
      ═══════════════════════════════════════ -->
      <div id="aree">

        <!-- Consulting — navy -->
        <section style="background:var(--dg-navy);padding:72px 0;">
          <div class="container">
            <div class="row align-items-center g-5">
              <div class="col-lg-6">
                <span class="dg-label" style="color:rgba(255,255,255,.6);">Consulting</span>
                <h2 style="color:#fff;font-size:2rem;font-weight:800;margin-top:12px;line-height:1.2;">La normativa non aspetta.<br/>Noi siamo già pronti.</h2>
                <p style="color:rgba(255,255,255,.65);margin-top:16px;line-height:1.7;">Sistemi di gestione, accreditamento ACN, ISO 9001/27001/45001 e D.Lgs. 36/2023. Affiancamento reale, non template.</p>
                <a href="/consulting/" class="btn-dg-accent" style="margin-top:28px;display:inline-block;">Scopri Consulting &#8594;</a>
              </div>
              <div class="col-lg-6">
                <div class="d-flex flex-column gap-3">
                  <div style="background:rgba(255,255,255,.07);border-radius:8px;padding:14px 18px;display:flex;align-items:center;gap:12px;">
                    <div style="width:6px;height:6px;background:#F5A623;border-radius:50%;flex-shrink:0;"></div>
                    <span style="color:rgba(255,255,255,.85);font-size:14px;font-weight:600;">Sistemi di gestione integrati (qualità, sicurezza, ambiente)</span>
                  </div>
                  <div style="background:rgba(255,255,255,.07);border-radius:8px;padding:14px 18px;display:flex;align-items:center;gap:12px;">
                    <div style="width:6px;height:6px;background:#F5A623;border-radius:50%;flex-shrink:0;"></div>
                    <span style="color:rgba(255,255,255,.85);font-size:14px;font-weight:600;">Accreditamento ACN — percorso completo</span>
                  </div>
                  <div style="background:rgba(255,255,255,.07);border-radius:8px;padding:14px 18px;display:flex;align-items:center;gap:12px;">
                    <div style="width:6px;height:6px;background:#F5A623;border-radius:50%;flex-shrink:0;"></div>
                    <span style="color:rgba(255,255,255,.85);font-size:14px;font-weight:600;">ISO 9001 · 27001 · 45001</span>
                  </div>
                  <div style="background:rgba(255,255,255,.07);border-radius:8px;padding:14px 18px;display:flex;align-items:center;gap:12px;">
                    <div style="width:6px;height:6px;background:#F5A623;border-radius:50%;flex-shrink:0;"></div>
                    <span style="color:rgba(255,255,255,.85);font-size:14px;font-weight:600;">Codice Contratti D.Lgs. 36/2023 e PAD</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Software — white -->
        <section style="background:#fff;padding:72px 0;">
          <div class="container">
            <div class="row align-items-center g-5 flex-lg-row-reverse">
              <div class="col-lg-6">
                <span class="dg-label">Software</span>
                <h2 style="color:var(--dg-dark);font-size:2rem;font-weight:800;margin-top:12px;line-height:1.2;">Codice che va in produzione.<br/>Non solo in demo.</h2>
                <p style="color:var(--dg-slate);margin-top:16px;line-height:1.7;">Sviluppo custom end-to-end, consulenza ICT, integrazione sistemi. ARCASID già in produzione in importanti atenei italiani.</p>
                <a href="/software/" style="margin-top:28px;display:inline-block;background:var(--dg-navy);color:#fff;padding:12px 28px;border-radius:4px;text-decoration:none;font-weight:700;">Scopri Software &#8594;</a>
              </div>
              <div class="col-lg-6">
                <div class="d-flex flex-column gap-3">
                  <div style="border:1px solid #eef0f4;border-radius:10px;padding:20px 22px;">
                    <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                      <span style="background:#e8f5e9;color:#2e7d32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In produzione</span>
                      <span style="font-size:13px;font-weight:700;color:var(--dg-dark);">ARCASID</span>
                    </div>
                    <p style="font-size:13px;color:var(--dg-slate);margin:0;line-height:1.5;">Digital logbook universitario — ESSE3, SPID, SSO integrati.</p>
                  </div>
                  <div style="border:1px solid #eef0f4;border-radius:10px;padding:20px 22px;">
                    <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                      <span style="background:#e3f2fd;color:#1565c0;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In sviluppo</span>
                      <span style="font-size:13px;font-weight:700;color:var(--dg-dark);">BInclusion</span>
                    </div>
                    <p style="font-size:13px;color:var(--dg-slate);margin:0;line-height:1.5;">Piattaforma inclusione scolastica con dati misurabili.</p>
                  </div>
                  <div style="border:1px solid #eef0f4;border-radius:10px;padding:20px 22px;">
                    <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                      <span style="background:#e8f5e9;color:#2e7d32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In produzione</span>
                      <span style="font-size:13px;font-weight:700;color:var(--dg-dark);">MedData</span>
                    </div>
                    <p style="font-size:13px;color:var(--dg-slate);margin:0;line-height:1.5;">Raccolta dati clinici cloud per ricerca scientifica.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Formazione — light -->
        <section style="background:var(--dg-light);padding:72px 0;">
          <div class="container">
            <div class="row align-items-center g-5">
              <div class="col-lg-6">
                <span class="dg-label">Formazione</span>
                <h2 style="color:var(--dg-dark);font-size:2rem;font-weight:800;margin-top:12px;line-height:1.2;">Formazione obbligatoria.<br/>Ma non inutile.</h2>
                <p style="color:var(--dg-slate);margin-top:16px;line-height:1.7;">D.Lgs. 81/08, ICT &amp; Digital Skills, Management. Percorsi progettati per lasciare qualcosa — non solo un attestato.</p>
                <a href="/formazione/" style="margin-top:28px;display:inline-block;background:var(--dg-navy);color:#fff;padding:12px 28px;border-radius:4px;text-decoration:none;font-weight:700;">Scopri Formazione &#8594;</a>
              </div>
              <div class="col-lg-6">
                <div class="row g-3">
                  <div class="col-6">
                    <div style="background:#fff;border-radius:10px;padding:24px 20px;text-align:center;box-shadow:0 1px 6px rgba(26,58,107,.06);">
                      <div style="font-size:24px;margin-bottom:8px;">&#128187;</div>
                      <div style="font-size:13px;font-weight:700;color:var(--dg-dark);">ICT &amp; Digital</div>
                      <div style="font-size:12px;color:var(--dg-slate);margin-top:4px;">Python · Cloud · AI/ML</div>
                    </div>
                  </div>
                  <div class="col-6">
                    <div style="background:#fff;border-radius:10px;padding:24px 20px;text-align:center;box-shadow:0 1px 6px rgba(26,58,107,.06);">
                      <div style="font-size:24px;margin-bottom:8px;">&#128202;</div>
                      <div style="font-size:13px;font-weight:700;color:var(--dg-dark);">Management</div>
                      <div style="font-size:12px;color:var(--dg-slate);margin-top:4px;">Agile · PMI · Coaching</div>
                    </div>
                  </div>
                  <div class="col-12">
                    <div style="background:#fff;border-radius:10px;padding:20px;display:flex;align-items:center;gap:16px;box-shadow:0 1px 6px rgba(26,58,107,.06);">
                      <div style="font-size:28px;">&#9937;</div>
                      <div>
                        <div style="font-size:13px;font-weight:700;color:var(--dg-dark);">Salute e Sicurezza 81/08</div>
                        <div style="font-size:12px;color:var(--dg-slate);margin-top:2px;">Lavoratori · RSPP · Antincendio · Primo Soccorso</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Debro AI — dark -->
        <section style="background:linear-gradient(135deg,#0d1b35 0%,#1a3a6b 60%,#0d2040 100%);padding:72px 0;">
          <div class="container">
            <div class="row align-items-center g-5 flex-lg-row-reverse">
              <div class="col-lg-6">
                <span class="dg-label" style="color:#F5A623;">Debro AI</span>
                <h2 style="color:#fff;font-size:2rem;font-weight:800;margin-top:12px;line-height:1.2;">L&#39;AI che lavora.<br/>Nei tuoi processi.</h2>
                <p style="color:rgba(255,255,255,.65);margin-top:16px;line-height:1.7;">Automazione, analisi predittiva e assistenti AI addestrati sulla tua azienda. Nessuna demo. Solo risultati misurabili.</p>
                <a href="/ai/" style="margin-top:28px;display:inline-block;background:#F5A623;color:#1A3A6B;padding:12px 28px;border-radius:4px;text-decoration:none;font-weight:800;">Scopri Debro AI &#8594;</a>
              </div>
              <div class="col-lg-6">
                <div class="d-flex flex-column gap-3">
                  <div style="background:rgba(255,255,255,.06);border:1px solid rgba(245,166,35,.2);border-radius:10px;padding:20px 22px;">
                    <div style="font-size:13px;font-weight:700;color:#F5A623;margin-bottom:6px;">Automazione dei processi</div>
                    <p style="font-size:13px;color:rgba(255,255,255,.6);margin:0;line-height:1.5;">Flussi documentali, comunicativi e gestionali — integrati nei sistemi esistenti.</p>
                  </div>
                  <div style="background:rgba(255,255,255,.06);border:1px solid rgba(245,166,35,.2);border-radius:10px;padding:20px 22px;">
                    <div style="font-size:13px;font-weight:700;color:#F5A623;margin-bottom:6px;">Analisi e supporto alle decisioni</div>
                    <p style="font-size:13px;color:rgba(255,255,255,.6);margin:0;line-height:1.5;">Dashboard su misura, alert predittivi, report automatici.</p>
                  </div>
                  <div style="background:rgba(255,255,255,.06);border:1px solid rgba(245,166,35,.2);border-radius:10px;padding:20px 22px;">
                    <div style="font-size:13px;font-weight:700;color:#F5A623;margin-bottom:6px;">Assistenti AI su misura</div>
                    <p style="font-size:13px;color:rgba(255,255,255,.6);margin:0;line-height:1.5;">Addestrati sui tuoi prodotti, procedure e settore. Non un chatbot generico.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

      </div>

      <!-- ═══════════════════════════════════════
           CLIENTI — headline forte
      ═══════════════════════════════════════ -->
      <section class="dg-section-white" style="padding:80px 0;">
        <div class="container text-center">
          <span class="dg-label">Ci hanno scelto</span>
          <h2 style="margin-top:12px;max-width:600px;margin-left:auto;margin-right:auto;">Università, enti e aziende che non possono permettersi di sbagliare.</h2>
          <div class="d-flex flex-wrap gap-5 justify-content-center align-items-center mt-5">
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

      <!-- ═══════════════════════════════════════
           CTA FINALE
      ═══════════════════════════════════════ -->
      <section class="dg-section-navy text-center" style="padding:96px 0;">
        <div class="container" style="max-width:700px;">
          <h2 style="color:#fff;font-size:2.4rem;font-weight:800;line-height:1.15;">Parliamo del tuo progetto.</h2>
          <p class="text-dg-muted" style="margin-top:20px;margin-bottom:40px;font-size:1.1rem;line-height:1.6;">
            Prima analisi gratuita. Nessun impegno.<br/>Scopri quale area Debro fa per te.
          </p>
          <a href="/contatti/" class="btn-dg-accent" style="font-size:1.05rem;padding:16px 40px;">Contattaci ora &#8594;</a>
        </div>
      </section>

    </div>
  </t>
</t>"""

existing = odoo("website.page", "search_read",
    params={"domain": [["url", "=", "/home"],
                       ["website_id", "=", WEBSITE_ID]],
            "fields": ["id", "name"], "limit": 1})

if existing:
    print(f"Homepage esiste (id={existing[0]['id']}) — aggiorno...")
    odoo("website.page", "write",
        ids=[existing[0]["id"]],
        params={"vals": {
            "arch": ARCH,
            "website_meta_title":       "Debro Group · Consulting, Software, Formazione e AI per PMI",
            "website_meta_description": "Consulenza normativa, software custom, formazione e AI per le PMI e PA italiane. 10+ anni, 15+ professionisti, 40+ progetti.",
        }})
    print("Homepage aggiornata.")
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
            "website_meta_description": "Consulenza normativa, software custom, formazione e AI per le PMI e PA italiane.",
            "arch":                     ARCH,
        }]})
    print(f"Homepage creata: id={ids[0] if isinstance(ids, list) else ids}")

print()
print("Homepage v2 completata.")
print("⚙️  Verifica: https://www.debro.it/home")
