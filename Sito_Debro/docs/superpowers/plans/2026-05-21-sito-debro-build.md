# Sito Debro Group — Implementation Plan

> **Stack:** Odoo Online 19.0 — Website module. Automazione via JSON-2 API (Python).
> **Design Spec:** `docs/superpowers/specs/2026-05-21-sito-debro-design.md`
> **API Research:** `docs/research/odoo-website-api.md`

**Goal:** Homepage + 4 pagine BU + Contatti, IT e EN, interamente su Odoo.
**Automazione:** ~80% via script Python JSON-2. Passi manuali esplicitamente marcati ⚙️.

---

## Setup — Configurazione environment

Prima di ogni task, crea `scripts/config.py`:

```python
# scripts/config.py
ODOO_URL  = "https://INSERISCI.odoo.com"   # sostituisci
API_KEY   = "INSERISCI_API_KEY"             # Settings → Users → API Keys
WEBSITE_ID = None   # recuperato in Task 1 Step 1
MAIN_MENU_ID = None # recuperato in Task 1 Step 3
```

Aggiungi `scripts/config.py` a `.gitignore` — contiene credenziali.

Helper comune (incolla in ogni script o importa):

```python
import requests, json

def odoo(model, method, args=None, kwargs=None):
    from config import ODOO_URL, API_KEY
    r = requests.post(
        f"{ODOO_URL}/json/2/{model}/{method}",
        headers={"Authorization": f"bearer {API_KEY}",
                 "Content-Type": "application/json"},
        json={"args": args or [], "kwargs": kwargs or {}}
    )
    r.raise_for_status()
    result = r.json()
    if "error" in result:
        raise Exception(result["error"])
    return result.get("result")
```

---

## Task 1: Configurazione base Odoo Website

**Checkpoint:** Website ID noto, lingua EN attiva, logo caricato, API funzionante.

- [ ] **Step 1: Recupera Website ID e verifica API**

  ```python
  # scripts/01_setup.py
  from helpers import odoo

  sites = odoo("website", "search_read",
      kwargs={"domain": [], "fields": ["id", "name", "domain"], "limit": 5})
  print(sites)
  # Nota il valore "id" del sito Debro → WEBSITE_ID in config.py
  ```

- [ ] **Step 2: Verifica permessi utente API**

  In Odoo: **Settings → Users → [tuo utente]**.
  Verifica che abbia gruppo: `Website / Editor` (o `Website / Designer`).
  Se mancante: aggiungi manualmente. ⚙️

- [ ] **Step 3: Recupera Main Menu ID**

  ```python
  menu = odoo("website.menu", "search_read",
      kwargs={"domain": [["url", "=", "/default-main-menu"],
                         ["website_id", "=", WEBSITE_ID]],
              "fields": ["id", "name"], "limit": 1})
  print(menu)
  # Nota "id" → MAIN_MENU_ID in config.py
  ```

- [ ] **Step 4: Aggiungi lingua EN** ⚙️

  In Odoo: **Website → Settings → Languages** → aggiungi `English`.
  Oppure via API:

  ```python
  # Trova ID lingua EN
  lang = odoo("res.lang", "search_read",
      kwargs={"domain": [["code", "=", "en_US"]],
              "fields": ["id", "name"]})
  lang_id = lang[0]["id"]

  # Aggiorna website con EN
  odoo("website", "write",
      args=[[WEBSITE_ID], {"language_ids": [[4, lang_id]]}])
  ```

- [ ] **Step 5: Carica logo Debro**

  ```python
  import base64

  with open("Logo Società/Logo Colorato.png", "rb") as f:
      logo_b64 = base64.b64encode(f.read()).decode()

  odoo("website", "write",
      args=[[WEBSITE_ID], {"logo": logo_b64}])
  ```

- [ ] **Step 6: Checkpoint**

  ```bash
  git add scripts/
  git commit -m "chore: add Odoo API scripts — Task 1 setup"
  ```

---

## Task 2: Design system — CSS globale via API

**Checkpoint:** Inter font attivo, CSS custom properties e componenti dg-* iniettati globalmente.

- [ ] **Step 1: Imposta palette SCSS** ⚙️

  In Odoo Website Editor: **Customize → Colors**.
  Imposta Primary: `#1A3A6B`, Secondary: `#2A5298`.
  Salva. Questo è l'unico step non automatable via API.

- [ ] **Step 2: Inietta CSS globale via API**

  ```python
  # scripts/02_design_system.py
  from helpers import odoo
  from config import WEBSITE_ID

  CUSTOM_CSS = """
  <!-- Inter font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
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
  .dg-card-light { background: #fff; border-left: 3px solid var(--dg-navy); border-radius: 8px; box-shadow: 0 2px 8px rgba(26,58,107,.07); padding: 1.5rem; height: 100%; }
  .dg-card-dark { background: var(--dg-navy); color: #fff; border-radius: 8px; box-shadow: 0 2px 12px rgba(26,58,107,.2); padding: 1.5rem; height: 100%; }
  .dg-card-dark h3 { color: #fff; }
  .dg-card-dark p { color: rgba(255,255,255,.75); }
  .dg-card-dark a { color: var(--dg-accent); font-weight: 700; text-decoration: none; }
  .dg-card-ai { background: linear-gradient(135deg, var(--dg-dark), var(--dg-navy)); border-radius: 8px; border: 1px solid rgba(245,166,35,.25); padding: 1.5rem; height: 100%; }
  .btn-dg-accent { background: var(--dg-accent) !important; color: #fff !important; border: none; border-radius: 4px; font-weight: 700; padding: 10px 24px; text-decoration: none; display: inline-block; }
  .btn-dg-outline { background: transparent !important; border: 2px solid var(--dg-navy) !important; color: var(--dg-navy) !important; border-radius: 4px; font-weight: 700; padding: 9px 22px; text-decoration: none; display: inline-block; }
  .btn-dg-outline-white { background: transparent !important; border: 2px solid rgba(255,255,255,.6) !important; color: #fff !important; border-radius: 4px; font-weight: 700; padding: 9px 22px; text-decoration: none; display: inline-block; }
  .dg-client-logo img { filter: grayscale(1); opacity: .55; transition: opacity .2s; max-height: 40px; width: auto; }
  .dg-client-logo img:hover { opacity: .85; }
  .dg-section-light { background: var(--dg-offwhite); padding: 80px 0; }
  .dg-section-white { background: #fff; padding: 80px 0; }
  .dg-section-navy { background: var(--dg-navy); padding: 80px 0; }
  .dg-section-navy h2, .dg-section-navy p { color: #fff; }
  .dg-section-navy h2 { color: #fff; }
  .text-dg-muted { color: rgba(255,255,255,.65); }
  </style>
  """

  odoo("website", "write",
      args=[[WEBSITE_ID], {"custom_code_head": CUSTOM_CSS}])
  print("Design system iniettato.")
  ```

  ```bash
  python scripts/02_design_system.py
  ```

- [ ] **Step 3: Verifica visiva** ⚙️

  Apri `debro.it` nel browser. Font Inter attivo. Nessun errore console.

- [ ] **Step 4: Checkpoint**

  ```bash
  git add scripts/02_design_system.py
  git commit -m "feat: global design system — Inter font, CSS vars, dg-* components"
  ```

---

## Task 3: Upload asset (loghi)

**Checkpoint:** Logo Debro e tutti i loghi clienti caricati. Mapping URL salvato in `scripts/assets_map.json`.

- [ ] **Step 1: Carica loghi clienti**

  ```python
  # scripts/03_upload_assets.py
  import base64, json, os
  from helpers import odoo
  from config import WEBSITE_ID

  LOGO_DIR = "Logo Clienti"
  assets_map = {}

  for fname in os.listdir(LOGO_DIR):
      if not fname.lower().endswith((".png", ".jpg", ".svg", ".webp")):
          continue
      fpath = os.path.join(LOGO_DIR, fname)
      with open(fpath, "rb") as f:
          data = base64.b64encode(f.read()).decode()
      mime = "image/svg+xml" if fname.endswith(".svg") else f"image/{'jpeg' if fname.endswith('.jpg') else fname.split('.')[-1]}"
      att_id = odoo("ir.attachment", "create", args=[{
          "name": fname,
          "type": "binary",
          "datas": data,
          "mimetype": mime,
          "public": True,
          "website_id": WEBSITE_ID,
      }])
      att = odoo("ir.attachment", "read", args=[[att_id]], kwargs={"fields": ["id", "name"]})
      url = f"/web/image/{att_id}/{fname}"
      assets_map[fname] = url
      print(f"Caricato: {fname} → {url}")

  with open("scripts/assets_map.json", "w") as f:
      json.dump(assets_map, f, indent=2)
  print("Mappa salvata in scripts/assets_map.json")
  ```

  ```bash
  python scripts/03_upload_assets.py
  ```

- [ ] **Step 2: Checkpoint**

  ```bash
  git add scripts/03_upload_assets.py scripts/assets_map.json
  git commit -m "chore: upload client logos to Odoo media library"
  ```

---

## Task 4: Menu principale

**Checkpoint:** Menu con 4 voci BU + Contatti creato. Visibile nella navbar Odoo.

- [ ] **Step 1: Crea menu** (le pagine non esistono ancora — URL placeholder, aggiornati in seguito)

  ```python
  # scripts/04_menu.py
  from helpers import odoo
  from config import WEBSITE_ID, MAIN_MENU_ID

  voci = [
      {"name": "Consulting",  "url": "/consulting/",  "sequence": 10},
      {"name": "Software",    "url": "/software/",    "sequence": 20},
      {"name": "Formazione",  "url": "/formazione/",  "sequence": 30},
      {"name": "AI",          "url": "/ai/",          "sequence": 40},
      {"name": "Contatti",    "url": "/contatti/",    "sequence": 50},
  ]

  for v in voci:
      mid = odoo("website.menu", "create", args=[{
          **v,
          "parent_id": MAIN_MENU_ID,
          "website_id": WEBSITE_ID,
      }])
      print(f"Menu creato: {v['name']} (id {mid})")
  ```

  ```bash
  python scripts/04_menu.py
  ```

- [ ] **Step 2: Checkpoint**

  ```bash
  git add scripts/04_menu.py
  git commit -m "feat: main menu structure created via API"
  ```

---

## Task 5: Homepage

**Checkpoint:** `debro.it/` pubblica con tutte le 5 sezioni, responsive.

- [ ] **Step 1: Crea pagina Homepage**

  ```python
  # scripts/05_homepage.py
  import json
  from helpers import odoo
  from config import WEBSITE_ID

  with open("scripts/assets_map.json") as f:
      assets = json.load(f)

  ARCH = """<t t-name="custom.page_homepage">
    <t t-call="website.layout">
      <div id="wrap" class="oe_structure">

        <!-- SEZIONE 1: Hero -->
        <section class="dg-hero">
          <div class="container">
            <div class="row align-items-center g-5">
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

        <!-- SEZIONE 2: Chi siamo -->
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
                  <div style="background:var(--dg-light);border-radius:6px;padding:12px 16px;font-weight:600;color:var(--dg-dark);">✓ Competenze reali, non slide</div>
                  <div style="background:var(--dg-light);border-radius:6px;padding:12px 16px;font-weight:600;color:var(--dg-dark);">✓ Un solo interlocutore per 4 aree</div>
                  <div style="background:var(--dg-light);border-radius:6px;padding:12px 16px;font-weight:600;color:var(--dg-dark);">✓ Target: PMI e PA italiane</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- SEZIONE 3: Le 4 BU -->
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
                  <a href="/consulting/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;">Scopri →</a>
                </div>
              </div>
              <div class="col">
                <div class="dg-card-dark">
                  <span class="dg-label" style="color:rgba(255,255,255,.6);">Software</span>
                  <h3>Codice che va in produzione.</h3>
                  <p>Software custom, consulenza ICT, ARCASID.</p>
                  <a href="/software/">Scopri →</a>
                </div>
              </div>
              <div class="col">
                <div class="dg-card-light">
                  <span class="dg-label">Formazione</span>
                  <h3>Formazione obbligatoria. Non inutile.</h3>
                  <p>81/08, ICT &amp; Digital Skills, Management.</p>
                  <a href="/formazione/" style="color:var(--dg-navy);font-weight:700;text-decoration:none;">Scopri →</a>
                </div>
              </div>
              <div class="col">
                <div class="dg-card-ai">
                  <span class="dg-label" style="color:#F5A623;">Debro AI</span>
                  <h3 style="color:#fff;">L&#39;AI che lavora.<br/>Nei tuoi processi.</h3>
                  <p style="color:rgba(255,255,255,.65);">Automazione, analisi e assistenti AI su misura. Nessuna demo. Solo risultati misurabili.</p>
                  <a href="/ai/" style="color:#F5A623;font-weight:700;text-decoration:none;">Scopri →</a>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- SEZIONE 4: Clienti -->
        <section class="dg-section-white">
          <div class="container text-center">
            <span class="dg-label">Ci hanno scelto</span>
            <div class="d-flex flex-wrap gap-5 justify-content-center align-items-center mt-4">
              <div class="dg-client-logo"><img src="/web/image/LOGO_BICOCCA_ID/logo-bicocca.png" alt="Università Milano Bicocca"/></div>
              <div class="dg-client-logo"><img src="/web/image/LOGO_SIELTE_ID/logo-sielte.png" alt="Sielte"/></div>
              <div class="dg-client-logo"><img src="/web/image/LOGO_MET_ID/logo-met.png" alt="Met Italia"/></div>
              <div class="dg-client-logo"><img src="/web/image/LOGO_LEGAMBIENTE_ID/logo-legambiente.png" alt="Legambiente"/></div>
              <div class="dg-client-logo"><img src="/web/image/LOGO_UNIPV_ID/logo-unipv.png" alt="Università di Pavia"/></div>
              <div class="dg-client-logo"><img src="/web/image/LOGO_UNIROMA2_ID/logo-uniroma2.png" alt="Università Roma Tor Vergata"/></div>
              <div class="dg-client-logo"><img src="/web/image/LOGO_BEON_ID/logo-beon.png" alt="Beon"/></div>
            </div>
          </div>
        </section>

        <!-- SEZIONE 5: CTA finale -->
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

  page_id = odoo("website.page", "create", args=[{
      "name": "Homepage",
      "type": "qweb",
      "key": "custom.page_homepage",
      "url": "/homepage-debro",   # Odoo riserva "/" — verrà impostato come homepage dalle impostazioni
      "website_id": WEBSITE_ID,
      "is_published": True,
      "website_indexed": True,
      "website_meta_title": "Debro Group · Consulting, Software, Formazione e AI per PMI",
      "website_meta_description": "Debro è un gruppo di competenze specializzate: consulenza normativa, sviluppo software, formazione professionale e AI applicata per le PMI italiane.",
      "arch": ARCH,
  }])
  print(f"Homepage creata: id {page_id}")
  ```

  > **Nota URL homepage:** Odoo gestisce `/` come homepage dal modulo website. Dopo la creazione:
  > ⚙️ Vai in **Website → Settings → Homepage** e seleziona questa pagina.

- [ ] **Step 2: Sostituisci URL loghi clienti**

  Apri `scripts/assets_map.json`. Per ogni logo cliente, sostituisci i placeholder `LOGO_*_ID` nel template con gli ID reali restituiti da Task 3.

- [ ] **Step 3: Esegui script**

  ```bash
  cd scripts && python 05_homepage.py
  ```

- [ ] **Step 4: Verifica** ⚙️

  Apri `debro.it` nel browser. Tutte le 5 sezioni visibili. Mobile responsive (DevTools → iPhone 12).

- [ ] **Step 5: Checkpoint**

  ```bash
  git add scripts/05_homepage.py
  git commit -m "feat: homepage created via Odoo API"
  ```

---

## Task 6: Pagina Debro Consulting

**Checkpoint:** `/consulting/` pubblica con hero, 4 servizi, 3 progetti, CTA.

- [ ] **Step 1: Crea pagina**

  ```python
  # scripts/06_consulting.py
  from helpers import odoo
  from config import WEBSITE_ID

  ARCH = """<t t-name="custom.page_consulting">
    <t t-call="website.layout">
      <div id="wrap" class="oe_structure">

        <!-- Hero -->
        <section class="dg-hero">
          <div class="container">
            <div class="row align-items-center g-5">
              <div class="col-lg-7">
                <div class="dg-accent-bar"></div>
                <span class="dg-label" style="color:rgba(255,255,255,.7);">Consulting</span>
                <h1>La normativa non aspetta. Noi siamo già pronti.</h1>
                <p class="fs-5 mt-3 mb-4 text-dg-muted">Sistemi di gestione, compliance ACN e certificazioni ISO per aziende che non vogliono essere colte impreparate.</p>
                <div class="d-flex gap-3 flex-wrap">
                  <a href="/contatti/?area=consulting" class="btn-dg-accent">Parliamo della tua situazione</a>
                  <a href="#servizi" class="btn-dg-outline-white">I nostri servizi →</a>
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
              <div class="dg-card-light"><h3>Supporto Università</h3><p>Gestione documentale e processi di accreditamento per importanti atenei italiani, con digitalizzazione delle Scuole di Specializzazione.</p></div>
              <div class="dg-card-light"><h3>Piattaforme PAD</h3><p>Gestione adozione Piattaforme di Approvvigionamento Digitale per centrali di committenza con formazione e supervisione.</p></div>
              <div class="dg-card-light"><h3>D.Lgs 36/2023</h3><p>Consulenza per recepimento nuovo Codice Contratti Pubblici: procedure, modelli e strumenti di compliance.</p></div>
            </div>
          </div>
        </section>

        <!-- CTA -->
        <section class="dg-section-navy text-center">
          <div class="container">
            <h2 style="color:#fff;">Parliamo della tua situazione.</h2>
            <p class="mt-3 mb-4 text-dg-muted">Prima call gratuita. Nessun impegno. Solo una conversazione concreta.</p>
            <a href="/contatti/?area=consulting" class="btn-dg-accent">Contattaci →</a>
          </div>
        </section>

      </div>
    </t>
  </t>"""

  page_id = odoo("website.page", "create", args=[{
      "name": "Debro Consulting",
      "type": "qweb",
      "key": "custom.page_consulting",
      "url": "/consulting/",
      "website_id": WEBSITE_ID,
      "is_published": True,
      "website_indexed": True,
      "website_meta_title": "Debro Consulting · ISO, ACN, Sistemi di Gestione",
      "website_meta_description": "Sistemi di gestione, accreditamento ACN e normative ISO per aziende che non vogliono essere colte impreparate.",
      "arch": ARCH,
  }])
  print(f"Consulting creata: id {page_id}")
  ```

  ```bash
  python scripts/06_consulting.py
  ```

- [ ] **Step 2: Verifica** ⚙️ — apri `debro.it/consulting/`, tutte le sezioni visibili.

- [ ] **Step 3: Checkpoint**

  ```bash
  git add scripts/06_consulting.py
  git commit -m "feat: Debro Consulting page via Odoo API"
  ```

---

## Task 7: Pagina Debro Software

**Checkpoint:** `/software/` con hero, approccio, stack pill, 3 progetti con badge.

- [ ] **Step 1: Crea pagina**

  ```python
  # scripts/07_software.py
  from helpers import odoo
  from config import WEBSITE_ID

  STACK_TAGS = ["React","Node.js","Python","Java Spring Boot","AWS","Azure","GCP","Docker","PostgreSQL","MongoDB","ChatGPT API","GDPR · OWASP"]

  def pill(label, color="var(--dg-navy)"):
      return f'<span style="background:{color};color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">{label}</span>'

  stack_html = "".join(pill(t) for t in STACK_TAGS)

  colors = {"var(--dg-navy)": STACK_TAGS[:4], "#2A5298": STACK_TAGS[4:8], "#455a7a": STACK_TAGS[8:]}
  stack_html = ""
  for color, tags in [("var(--dg-navy)", STACK_TAGS[:4]), ("#2A5298", STACK_TAGS[4:8]), ("#455a7a", STACK_TAGS[8:])]:
      for t in tags:
          stack_html += pill(t, color)

  ARCH = f"""<t t-name="custom.page_software">
    <t t-call="website.layout">
      <div id="wrap" class="oe_structure">

        <section class="dg-hero">
          <div class="container">
            <div class="row align-items-center g-5">
              <div class="col-lg-7">
                <div class="dg-accent-bar"></div>
                <span class="dg-label" style="color:rgba(255,255,255,.7);">Software</span>
                <h1>Software che va in produzione. Non solo in presentazione.</h1>
                <p class="fs-5 mt-3 mb-4 text-dg-muted">Sviluppo custom e consulenza ICT per chi ha bisogno di soluzioni che funzionano davvero nell&#39;ambiente reale.</p>
                <div class="d-flex gap-3 flex-wrap">
                  <a href="/contatti/?area=software" class="btn-dg-accent">Raccontaci il tuo progetto</a>
                  <a href="#progetti" class="btn-dg-outline-white">Vedi i progetti →</a>
                </div>
              </div>
            </div>
          </div>
        </section>

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

        <section style="background:var(--dg-light);padding:60px 0;">
          <div class="container">
            <span class="dg-label">Stack tecnologico</span>
            <div class="d-flex gap-2 flex-wrap mt-3">{stack_html}</div>
          </div>
        </section>

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

        <section class="dg-section-navy text-center">
          <div class="container">
            <h2 style="color:#fff;">Raccontaci il tuo progetto.</h2>
            <p class="mt-3 mb-4 text-dg-muted">Prima call gratuita. Nessun impegno.</p>
            <a href="/contatti/?area=software" class="btn-dg-accent">Parliamo →</a>
          </div>
        </section>

      </div>
    </t>
  </t>"""

  page_id = odoo("website.page", "create", args=[{
      "name": "Debro Software",
      "type": "qweb",
      "key": "custom.page_software",
      "url": "/software/",
      "website_id": WEBSITE_ID,
      "is_published": True,
      "website_indexed": True,
      "website_meta_title": "Debro Software · Sviluppo Custom e Consulenza ICT",
      "website_meta_description": "Software custom e consulenza ICT end-to-end. Dall&#39;analisi al deployment, con chi sa davvero scrivere codice.",
      "arch": ARCH,
  }])
  print(f"Software creata: id {page_id}")
  ```

  ```bash
  python scripts/07_software.py
  ```

- [ ] **Step 2: Verifica + Checkpoint**

  ```bash
  git add scripts/07_software.py
  git commit -m "feat: Debro Software page via Odoo API"
  ```

---

## Task 8: Pagina Debro Formazione

**Checkpoint:** `/formazione/` con hero, 3 aree, catalogo accordion Bootstrap, CTA.

- [ ] **Step 1: Crea pagina**

  ```python
  # scripts/08_formazione.py
  from helpers import odoo
  from config import WEBSITE_ID

  ARCH = """<t t-name="custom.page_formazione">
    <t t-call="website.layout">
      <div id="wrap" class="oe_structure">

        <section class="dg-hero">
          <div class="container">
            <div class="row align-items-center g-5">
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
                    <span style="font-size:20px;">💻</span>
                    <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">ICT &amp; Digital Skills</span>
                  </div>
                  <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
                    <span style="font-size:20px;">📊</span>
                    <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">Management &amp; Soft Skills</span>
                  </div>
                  <div style="background:rgba(255,255,255,.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
                    <span style="font-size:20px;">⛑️</span>
                    <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">Sicurezza D.Lgs. 81/08</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

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
                      <li class="mb-2">✓ Programmazione — Python, Java, JavaScript/React, SQL</li>
                      <li class="mb-2">✓ Cybersecurity &amp; Data Protection — GDPR, ISO/IEC 27001, OWASP</li>
                      <li class="mb-2">✓ Cloud &amp; DevOps — AWS, Azure, Kubernetes, Docker, CI/CD</li>
                      <li class="mb-2">✓ Digitalizzazione processi aziendali</li>
                      <li>✓ AI &amp; Machine Learning applicata al business</li>
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
                      <li class="mb-2">✓ Project Management Agile / Scrum / PMI</li>
                      <li class="mb-2">✓ Leadership e gestione del team</li>
                      <li class="mb-2">✓ Comunicazione efficace e negoziazione</li>
                      <li>✓ Coaching e sviluppo soft skills</li>
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
                      <li class="mb-2">✓ Corsi per lavoratori — basso/medio/alto rischio + aggiornamenti</li>
                      <li class="mb-2">✓ Corsi per dirigenti e datori di lavoro</li>
                      <li class="mb-2">✓ RLS / RSPP / ASPP — moduli A, B, C + aggiornamenti</li>
                      <li class="mb-2">✓ Antincendio — livelli 1, 2, 3 con prove pratiche</li>
                      <li class="mb-2">✓ Primo Soccorso — gruppi A, B, C + BLSD</li>
                      <li class="mb-2">✓ Lavori in quota + DPI III categoria</li>
                      <li>✓ PES / PAV / PEI — sicurezza elettrica</li>
                    </ul>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </section>

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

  page_id = odoo("website.page", "create", args=[{
      "name": "Debro Formazione",
      "type": "qweb",
      "key": "custom.page_formazione",
      "url": "/formazione/",
      "website_id": WEBSITE_ID,
      "is_published": True,
      "website_indexed": True,
      "website_meta_title": "Debro Formazione · Corsi 81/08, ICT e Management",
      "website_meta_description": "Corsi D.Lgs. 81/08, ICT & Digital Skills e Management. Formazione obbligatoria e percorsi di sviluppo professionale.",
      "arch": ARCH,
  }])
  print(f"Formazione creata: id {page_id}")
  ```

  ```bash
  python scripts/08_formazione.py
  git add scripts/08_formazione.py
  git commit -m "feat: Debro Formazione page via Odoo API"
  ```

---

## Task 9: Pagina Debro AI

**Checkpoint:** `/ai/` con hero, 3 servizi, FAQ accordion, CTA.

- [ ] **Step 1: Crea pagina**

  ```python
  # scripts/09_ai.py
  from helpers import odoo
  from config import WEBSITE_ID

  ARCH = """<t t-name="custom.page_ai">
    <t t-call="website.layout">
      <div id="wrap" class="oe_structure">

        <section class="dg-hero">
          <div class="container">
            <div class="row align-items-center g-5">
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
                  <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,.3);">↓</div>
                  <div style="background:rgba(245,166,35,.15);border-radius:6px;padding:8px 14px;font-size:12px;color:#F5A623;font-weight:700;border:1px solid rgba(245,166,35,.3);display:flex;align-items:center;gap:8px;">
                    <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>AI Debro
                  </div>
                  <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,.3);">↓</div>
                  <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,.8);display:flex;align-items:center;gap:8px;">
                    <span style="width:8px;height:8px;background:#4caf50;border-radius:50%;flex-shrink:0;"></span>Risultato misurabile
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

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

        <section class="dg-section-light">
          <div class="container">
            <span class="dg-label">Domande frequenti</span>
            <h2>L&#39;AI fa per la mia azienda?</h2>
            <div class="accordion mt-4" id="faqAI">
              <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
                <h2 class="accordion-header"><button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" style="font-weight:700;">Siamo una PMI senza team IT interno. Possiamo usare l&#39;AI?</button></h2>
                <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#faqAI">
                  <div class="accordion-body">Sì. Progettiamo soluzioni che non richiedono un data scientist interno. Partiamo dai processi che già esistono.</div>
                </div>
              </div>
              <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
                <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" style="font-weight:700;">Quanto tempo ci vuole per vedere risultati?</button></h2>
                <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                  <div class="accordion-body">Dipende dal processo. Le prime automazioni semplici sono operative in 2-4 settimane. Progetti più complessi seguono un piano incrementale con rilasci parziali.</div>
                </div>
              </div>
              <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
                <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" style="font-weight:700;">I nostri dati restano al sicuro?</button></h2>
                <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                  <div class="accordion-body">Sì. Progettiamo con GDPR compliance by design. I dati del cliente non vengono usati per addestrare modelli generali.</div>
                </div>
              </div>
              <div class="accordion-item border-0" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
                <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" style="font-weight:700;">Che differenza c&#39;è da ChatGPT o Copilot?</button></h2>
                <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                  <div class="accordion-body">Quelli sono strumenti generici. Noi costruiamo soluzioni specifiche per il tuo settore, i tuoi dati e i tuoi processi.</div>
                </div>
              </div>
            </div>
          </div>
        </section>

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

  page_id = odoo("website.page", "create", args=[{
      "name": "Debro AI",
      "type": "qweb",
      "key": "custom.page_ai",
      "url": "/ai/",
      "website_id": WEBSITE_ID,
      "is_published": True,
      "website_indexed": True,
      "website_meta_title": "Debro AI · Intelligenza Artificiale per PMI",
      "website_meta_description": "Automazione processi, analisi predittiva e assistenti AI su misura. AI pratica e misurabile per le PMI italiane.",
      "arch": ARCH,
  }])
  print(f"AI creata: id {page_id}")
  ```

  ```bash
  python scripts/09_ai.py
  git add scripts/09_ai.py
  git commit -m "feat: Debro AI page via Odoo API"
  ```

---

## Task 10: Pagina Contatti (form → CRM nativo)

**Checkpoint:** Form funzionante, lead visibile in Odoo CRM → Pipeline. Privacy checkbox obbligatoria.

- [ ] **Step 1: Configura CRM defaults via API**

  ```python
  # scripts/10_contatti.py (prima parte)
  from helpers import odoo
  from config import WEBSITE_ID

  # Trova team CRM di default (o usa ID 1)
  teams = odoo("crm.team", "search_read",
      kwargs={"domain": [], "fields": ["id", "name"], "limit": 5})
  print(teams)  # nota ID team da assegnare come default

  TEAM_ID = teams[0]["id"]  # aggiusta se necessario

  odoo("website", "write",
      args=[[WEBSITE_ID], {"crm_default_team_id": TEAM_ID}])
  print("CRM default team configurato.")
  ```

- [ ] **Step 2: Crea pagina Contatti**

  ```python
  # continua in scripts/10_contatti.py

  ARCH = """<t t-name="custom.page_contatti">
    <t t-call="website.layout">
      <div id="wrap" class="oe_structure">

        <!-- Hero minimal -->
        <section class="dg-section-navy text-center" style="padding:60px 0;">
          <div class="container">
            <h1 style="color:#fff;">Parliamo.</h1>
            <p class="mt-2 text-dg-muted">Scegli l&#39;area, raccontaci il tuo progetto.</p>
          </div>
        </section>

        <!-- Form + Info -->
        <section class="dg-section-white">
          <div class="container">
            <div class="row g-5">

              <div class="col-lg-7">
                <form action="/web/dataset/call_kw" method="post"
                      data-model_name="crm.lead"
                      data-success_page="/grazie/"
                      class="s_website_form"
                      enctype="multipart/form-data">

                  <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>

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
                      <input type="tel" name="phone" class="form-control" placeholder="+39 02 123456"/>
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
                        <input class="form-check-input" type="checkbox" id="privacy" required="required"/>
                        <label class="form-check-label" for="privacy">
                          Ho letto e accetto la <a href="/privacy-policy/" target="_blank">Privacy Policy</a> *
                        </label>
                      </div>
                    </div>
                    <div class="col-12">
                      <button type="submit" class="btn-dg-accent">Invia messaggio</button>
                    </div>
                  </div>
                </form>
              </div>

              <div class="col-lg-5">
                <h3>Dove siamo</h3>
                <p style="color:var(--dg-slate);">[INDIRIZZO DA INSERIRE]<br/>[CAP Città (Prov.)]</p>
                <p><a href="mailto:info@debro.it" style="color:var(--dg-navy);font-weight:600;">info@debro.it</a></p>
                <p><a href="tel:+39XXXXXXXXXX" style="color:var(--dg-navy);font-weight:600;">[TELEFONO]</a></p>
                <div class="mt-4" style="border-radius:8px;overflow:hidden;">
                  <iframe
                    src="https://www.google.com/maps/embed?pb=INSERISCI_EMBED_URL"
                    width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy">
                  </iframe>
                </div>
              </div>

            </div>
          </div>
        </section>

      </div>
    </t>
  </t>"""

  page_id = odoo("website.page", "create", args=[{
      "name": "Contatti",
      "type": "qweb",
      "key": "custom.page_contatti",
      "url": "/contatti/",
      "website_id": WEBSITE_ID,
      "is_published": True,
      "website_indexed": False,
      "website_meta_title": "Contatti · Debro Group",
      "website_meta_description": "Contatta Debro Group per consulenza, sviluppo software, formazione o AI. Prima call gratuita.",
      "arch": ARCH,
  }])
  print(f"Contatti creata: id {page_id}")
  ```

  > ⚠️ Sostituisci `[INDIRIZZO]`, `[TELEFONO]`, e l'URL embed Google Maps prima di pubblicare.
  > ⚙️ Per Google Maps embed: vai su maps.google.com → cerca indirizzo → Condividi → Incorpora una mappa → copia URL src.

- [ ] **Step 3: Configura SMTP Odoo** ⚙️

  **Settings → Technical → Outgoing Mail Servers** → aggiungi server SMTP `@debro.it`. Testa invio.

- [ ] **Step 4: Verifica lead CRM**

  Compila e invia il form. Vai in **CRM → Pipeline** — verifica che il lead appaia con area e messaggio.

- [ ] **Step 5: Checkpoint**

  ```bash
  git add scripts/10_contatti.py
  git commit -m "feat: contatti page with native Odoo CRM form"
  ```

---

## Task 11: Multilingua IT/EN

**Checkpoint:** `debro.it/en/` accessibile, switcher lingua in navbar, pagine IT tradotte in EN.

- [ ] **Step 1: Verifica lingua EN attiva** — già fatto in Task 1 Step 4.

- [ ] **Step 2: Traduci pagine in Odoo** ⚙️

  In Odoo Website: apri ogni pagina → click **Translate** (bottone in alto) → traduzione campo per campo.

  Testi chiave EN da tradurre:
  - H1 Homepage: `One group. Four specializations. Zero improvisation.`
  - Chi siamo H2: `We're not a catch-all agency. We're a group that knows what it does.`
  - CTA: `Discover the Group` / `Contact Us`
  - BU pages: headline + sottotitolo + CTA (stesso tono diretto IT)

  Alternativa API (avanzata):

  ```python
  # Aggiorna nome menu in EN
  odoo("website.menu", "write",
      args=[[MENU_ID], {"name": "Consulting"}],
      kwargs={"context": {"lang": "en_US"}})
  ```

- [ ] **Step 3: Verifica switcher lingua** ⚙️

  Il switcher IT/EN appare automaticamente nella navbar Odoo quando più lingue sono attive.
  Stile: **Website → Settings → Language Selector** → scegli formato (dropdown, inline, flag).

- [ ] **Step 4: Checkpoint**

  ```bash
  git commit -m "feat: IT/EN multilingual configured"
  ```

---

## Task 12: SEO e lancio

**Checkpoint:** Sitemap attiva, meta tag corretti per ogni pagina, cookie banner GDPR configurato, sito live su `debro.it`.

- [ ] **Step 1: Verifica meta tag via API**

  Meta title e description già settati nei Task 5–10. Verifica:

  ```python
  # scripts/12_seo_check.py
  from helpers import odoo
  from config import WEBSITE_ID

  pages = odoo("website.page", "search_read",
      kwargs={"domain": [["website_id", "=", WEBSITE_ID]],
              "fields": ["name", "url", "website_meta_title", "website_meta_description"]})
  for p in pages:
      print(f"{p['url']}: title={len(p.get('website_meta_title','') or '')}ch  desc={len(p.get('website_meta_description','') or '')}ch")
  ```

- [ ] **Step 2: Schema Organization** ⚙️

  **Website → Settings → SEO**:
  - Tipo organizzazione: `Organization`
  - Nome: `Debro Group`
  - Logo: già caricato in Task 1

- [ ] **Step 3: Sitemap XML**

  Odoo genera automaticamente `/sitemap.xml`. Verifica: apri `debro.it/sitemap.xml`. Tutte le pagine IT + EN presenti. ✓

- [ ] **Step 4: Cookie banner GDPR** ⚙️

  **Website → Settings → Privacy Policy** → attiva cookie bar nativa Odoo.
  Crea pagina Privacy Policy: **Website → New Page** → `/privacy-policy/`.

- [ ] **Step 5: Homepage come pagina principale** ⚙️

  **Website → Settings → Homepage** → seleziona la pagina Homepage creata in Task 5.

- [ ] **Step 6: Checklist pre-lancio**

  - [ ] Tutti i link interni funzionanti (nessun 404)
  - [ ] Form contatti testato — lead arriva in CRM
  - [ ] Switcher IT/EN funzionante su tutte le pagine
  - [ ] Cookie banner appare alla prima visita
  - [ ] Privacy Policy pagina pubblicata
  - [ ] `debro.it/sitemap.xml` accessibile e completa
  - [ ] Google Search Console: verifica sito e invia sitemap
  - [ ] SSL attivo (Odoo Online gestisce HTTPS automaticamente)
  - [ ] Indirizzo e telefono in pagina Contatti aggiornati
  - [ ] Google Maps embed funzionante

- [ ] **Step 7: Checkpoint finale**

  ```bash
  git add scripts/12_seo_check.py
  git commit -m "feat: SEO verified, pre-launch checklist complete"
  ```

---

## Riepilogo task e dipendenze

```
Task 1:  Setup base Odoo Website (prerequisito tutto)
Task 2:  Design system CSS globale (dipende da 1)
Task 3:  Upload asset / loghi (dipende da 1) — parallelo con 2
Task 4:  Menu principale (dipende da 1)
Task 5:  Homepage (dipende da 2, 3)
Task 6:  Consulting (dipende da 2)   ┐
Task 7:  Software (dipende da 2)     │ eseguibili in parallelo
Task 8:  Formazione (dipende da 2)   │ dopo Task 2
Task 9:  AI (dipende da 2)           ┘
Task 10: Contatti (dipende da 2) — parallelo con 6-9
Task 11: Multilingua (dipende da 5,6,7,8,9,10)
Task 12: SEO + lancio (dipende da 11)
```

**Task 2 e 3 paralleli.**
**Task 6, 7, 8, 9, 10 paralleli dopo Task 2.**
**~80% automatable via script Python. Step manuali marcati ⚙️.**
