# Sito Debro Group — Design Spec

**Data:** 2026-05-21
**Aggiornata:** 2026-05-21 (migrazione stack WordPress → Odoo)
**Stato:** Approvato
**Piattaforma:** Odoo Online 19.0 — Website module
**Lingua:** IT + EN
**Gestione dominio/DNS:** Odoo Online 19.0
**CRM:** Odoo CRM nativo (form → lead, zero bridge)

---

## 1. Architettura

### Stack tecnico

| Componente | Tecnologia | Note |
|---|---|---|
| CMS / Website builder | Odoo Online 19.0 — Website module | Piano Custom — API esterna attiva |
| Templating | QWeb (XML) + Bootstrap 5 | Struttura pagine via API |
| Automazione build | Python 3.x + JSON-2 API (`/json/2/`) | Script per ogni task |
| Autenticazione API | Bearer API Key (`Authorization: bearer <key>`) | Generata in Settings → Users → API Keys |
| CSS globale | `website.custom_code_head` — writable via API | Inter font + CSS custom properties + componenti |
| Palette colori (SCSS) | Manuale — Odoo Website Editor | Non accessibile via API esterna |
| CRM | Odoo CRM — `website_crm` module | Form contatti → `crm.lead` nativo |
| Multilingua | Odoo Translate nativo | `website.language_ids` + editor traduzioni |
| DNS | Odoo Domain Names (`Settings → Domain Names`) | Nessun hosting separato necessario |
| SEO | Odoo SEO nativo | `website_meta_title`, `website_meta_description` per pagina via API |

### Struttura URL

```
debro.it/                    → Homepage
debro.it/consulting/         → Debro Consulting
debro.it/software/           → Debro Software
debro.it/formazione/         → Debro Formazione
debro.it/ai/                 → Debro AI
debro.it/contatti/           → Contatti (form → CRM nativo)

debro.it/en/                 → Homepage EN
debro.it/en/consulting/      → Consulting EN
... (struttura speculare — gestita da Odoo router automaticamente)
```

### API JSON-2 — formato chiamate

```python
import requests

ODOO_URL = "https://debro.odoo.com"
API_KEY  = "your_api_key"

def odoo(model, method, args=None, kwargs=None):
    r = requests.post(
        f"{ODOO_URL}/json/2/{model}/{method}",
        headers={"Authorization": f"bearer {API_KEY}",
                 "Content-Type": "application/json"},
        json={"args": args or [], "kwargs": kwargs or {}}
    )
    r.raise_for_status()
    return r.json()
```

### Limiti Odoo Online SaaS

| Operazione | Disponibile |
|---|---|
| Crea/scrivi `ir.ui.view`, `website.page`, `website.menu` | ✓ via API |
| Upload immagini `ir.attachment` | ✓ via API |
| CSS globale via `website.custom_code_head` | ✓ via API |
| Palette SCSS (`make_scss_customization`) | ✗ solo UI |
| Selezione font SCSS | ✗ workaround: CSS vars via `custom_code_head` |
| Form contatti → CRM | ✓ nativo (zero codice custom) |
| Moduli custom non approvati Odoo | ✗ Odoo Online SaaS blocca |

---

## 2. Sitemap

```
Homepage (/)
├── Hero split
├── Chi siamo
├── 4 card BU (link alle BU)
├── Ci hanno scelto (loghi clienti)
└── CTA finale

Debro Consulting (/consulting/)
├── Hero
├── 4 servizi (Sistemi gestione, ACN, ISO, Codice Contratti)
├── 3 progetti realizzati
└── CTA

Debro Software (/software/)
├── Hero
├── Approccio (Consulenza integrata + Sviluppo end-to-end)
├── Stack tecnologico (tag Bootstrap pill)
├── 3 progetti (ARCASID, BInclusion, MedData)
└── CTA

Debro Formazione (/formazione/)
├── Hero
├── 3 aree formative (ICT, Management, 81/08)
├── Catalogo corsi (accordion Bootstrap)
└── CTA

Debro AI (/ai/)
├── Hero
├── 3 servizi (Automazione, Analisi, Assistenti)
├── FAQ accordion
└── CTA

Contatti (/contatti/)
├── Hero minimal
├── Form nativo Odoo → crm.lead
├── Indirizzo + mappa embed
└── Email + telefono

Globali
├── Navbar (logo sx, menu BU centro, IT/EN + CTA dx)
├── Footer (link BU, P.IVA, Privacy, Cookie)
└── Cookie banner GDPR (Odoo built-in)
```

---

## 3. Linguaggio visivo

### Palette colori

| Token | Hex | Uso |
|---|---|---|
| Navy Primary | `#1A3A6B` | Navbar, bottoni primari, bordi card, sezioni hero |
| Blue Secondary | `#2A5298` | Variazioni card, badge, tag stack |
| Dark Text | `#0D1F3C` | Headline H1/H2, body su sfondo chiaro |
| Slate Body | `#3A4A5C` | Testo corpo standard |
| Light BG | `#E8EDF5` | Sfondi sezione alternati |
| Off-white | `#F8F9FC` | Sfondi sezione principali |
| White | `#FFFFFF` | Card, aree contenuto |
| Accent / CTA | `#F5A623` | Solo CTA primari, accenti grafici — usare con parsimonia |

**Nota implementazione:** la palette Bootstrap SCSS (primary, secondary) va impostata manualmente nell'editor Odoo (Customize → Colors). Le variabili CSS custom sotto vengono iniettate via `custom_code_head` e sovrascrivono dove Elementor non interviene.

### CSS custom properties (iniettate via API)

```css
:root {
  --dg-navy:    #1A3A6B;
  --dg-blue:    #2A5298;
  --dg-dark:    #0D1F3C;
  --dg-slate:   #3A4A5C;
  --dg-light:   #E8EDF5;
  --dg-offwhite:#F8F9FC;
  --dg-accent:  #F5A623;
}
```

### Tipografia

- **Font:** Inter (Google Fonts) — inject via `custom_code_head`
- **H1:** Inter 800, 40–48px, line-height 1.15, colore `#0D1F3C`
- **H2:** Inter 700, 28–32px, line-height 1.25, colore `#1A3A6B`
- **H3:** Inter 700, 20–22px, colore `#0D1F3C`
- **Body:** Inter 400, 16–17px, line-height 1.6, colore `#3A4A5C`
- **Label/Tag:** Inter 700, 11–12px, uppercase, letter-spacing 0.5px

### Componenti CSS (iniettati via `custom_code_head`)

```css
/* Accent bar decorativa */
.dg-accent-bar {
  width: 32px; height: 3px;
  background: var(--dg-accent);
  border-radius: 2px; margin-bottom: 16px;
}

/* Label BU */
.dg-label {
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.5px;
  color: var(--dg-navy); margin-bottom: 8px; display: block;
}

/* Card BU chiara */
.dg-card-light {
  background: #fff; border-left: 3px solid var(--dg-navy);
  border-radius: 8px; box-shadow: 0 2px 8px rgba(26,58,107,.07);
  padding: 1.5rem;
}

/* Card BU scura */
.dg-card-dark {
  background: var(--dg-navy); color: #fff;
  border-radius: 8px; box-shadow: 0 2px 12px rgba(26,58,107,.2);
  padding: 1.5rem;
}

/* Bottone accent */
.btn-dg-accent {
  background: var(--dg-accent) !important; color: #fff !important;
  border: none; border-radius: 4px; font-weight: 700;
  padding: 10px 20px;
}

/* Bottone outline */
.btn-dg-outline {
  background: transparent !important;
  border: 2px solid var(--dg-navy) !important;
  color: var(--dg-navy) !important;
  border-radius: 4px; font-weight: 700; padding: 10px 20px;
}

/* Bottone outline bianco (su sfondi navy) */
.btn-dg-outline-white {
  background: transparent !important;
  border: 2px solid rgba(255,255,255,.6) !important;
  color: #fff !important;
  border-radius: 4px; font-weight: 700; padding: 10px 20px;
}

/* Hero gradient */
.dg-hero {
  background: linear-gradient(135deg, var(--dg-dark) 0%, var(--dg-navy) 100%);
  padding: 80px 0;
}

/* Loghi clienti grayscale */
.dg-client-logo img {
  filter: grayscale(1); opacity: .55;
  transition: opacity .2s; max-height: 40px; width: auto;
}
.dg-client-logo img:hover { opacity: .85; }
```

### QWeb template base pagina

```xml
<t t-name="custom.page_NOME">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">

      <!-- SEZIONI QUI -->

    </div>
  </t>
</t>
```

Ogni `<section>` usa classi Bootstrap + classi `dg-*` custom. Attributo `data-snippet` opzionale (abilita editing visuale nel builder Odoo).

---

## 4. Homepage — struttura sezioni

| # | Sezione | Sfondo | Struttura Bootstrap |
|---|---|---|---|
| 1 | Hero split | `dg-hero` (gradiente navy) | `row` 2 × `col-lg-6` |
| 2 | Chi siamo | `#FFFFFF` | `row col-lg-7 + col-lg-5` |
| 3 | Le 4 BU | `#F8F9FC` | `row row-cols-1 row-cols-md-2 g-4` |
| 4 | Ci hanno scelto | `#FFFFFF` | `d-flex flex-wrap gap-4 justify-content-center align-items-center` |
| 5 | CTA finale | `#F8F9FC` | `text-center` |

---

## 5. Template pagine BU

Struttura identica per tutte e 4 le BU.

| # | Sezione | Note |
|---|---|---|
| 1 | Hero | Breadcrumb + H1 BU-specific + 2 CTA + visual DX |
| 2 | Servizi / Approccio | Label + H2 + grid 2 card |
| 3 | Sezione specifica | Vedi variazioni sotto |
| 4 | Progetti / Catalogo | Card orizzontali o accordion |
| 5 | CTA pagina | Sfondo navy, headline + bottone accent |

### Variazioni sezione [3]

**Consulting:** 4 blocchi servizio (Sistemi gestione, ACN, ISO, Codice Contratti)
**Software:** Stack tecnologico — tag pill Bootstrap (`badge rounded-pill bg-dg-navy`)
**Formazione:** Catalogo accordion Bootstrap per area (ICT, Management, 81/08)
**AI:** FAQ accordion — 4 domande PMI

---

## 6. Pagina Contatti

- Form nativo Odoo (`website_crm`) — nessun plugin custom necessario
- Campi: Nome, Azienda, Email, Telefono (opt), Area interesse (dropdown), Messaggio, Privacy checkbox
- Routing automatico → `crm.lead` tramite `data-model_name="crm.lead"` nel template
- Default team/salesperson configurabile via API su record `website`
- Mappa: Google Maps embed HTML nel template QWeb
- SMTP: configurato in Odoo (`Settings → Technical → Outgoing Mail Servers`)

---

## 7. SEO

- `website_meta_title` e `website_meta_description` settabili via API su `website.page`
- Sitemap XML: generata automaticamente da Odoo (`/sitemap.xml`)
- hreflang: gestito automaticamente da Odoo router per multilingua
- Schema Organization: configurabile in `Website → Settings → SEO`

---

## 8. Copy — stato

**Prodotto e approvato (IT):**
- Homepage: Hero, Chi siamo, 4 teaser BU
- Debro Consulting: Hero + 4 servizi + 3 progetti
- Debro Software: Hero, Approccio, stack, 3 progetti
- Debro Formazione: Hero + 3 aree + catalogo
- Debro AI: Hero + 3 servizi + FAQ
- 5 varianti tagline di gruppo

**Da produrre:**
- Copy EN (traduzione/adattamento)
- Micro-copy form contatti (label, placeholder, conferma)
- Footer (testi link, payoff)
- Meta title/description SEO

**Note critiche:**
- BInclusion: validare contenuto con cliente prima pubblicazione
- Headline AI: variante raccomandata `L'AI che lavora. Nei tuoi processi.`
- Numeri stats: da validare con Debro prima di inserire

---

## 9. Decisioni aperte

| Decisione | Stato | Note |
|---|---|---|
| Hosting | ✓ Risolto | Odoo Online — nessun hosting separato |
| DNS | ✓ Risolto | Gestito in Odoo (`Settings → Domain Names`) |
| Plugin multilingua | ✓ Risolto | Odoo Translate nativo |
| CRM bridge | ✓ Risolto | `website_crm` nativo — zero codice custom |
| Palette SCSS colori | Da fare manuale | Odoo Website Editor → Customize → Colors |
| Copy EN | Da produrre | Dopo approvazione IT completo |
| Contenuto BInclusion | Da validare | Copy attuale basato su assunzioni |
| Casi PMI per Debro AI | Da raccogliere | Placeholder FAQ al lancio |
| Google Maps API key | Da procurare | Per embed mappa in pagina Contatti |

---

## 10. Credenziali API necessarie

Da raccogliere prima di eseguire Task 1:

| Parametro | Dove trovarlo | Variabile script |
|---|---|---|
| URL istanza | `https://[nome].odoo.com` | `ODOO_URL` |
| API Key | `Settings → Users → [utente] → API Keys → New` | `API_KEY` |
| Website ID | Recuperato da script (search su `website` model) | `WEBSITE_ID` |
| Main menu ID | Recuperato da script (search `url='/default-main-menu'`) | `MAIN_MENU_ID` |
