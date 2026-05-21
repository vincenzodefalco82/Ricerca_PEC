# Sito Debro Group — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Costruire il sito WordPress del Gruppo Debro — homepage scroll + 4 pagine BU + contatti, in IT e EN, con Elementor Pro + Astra.

**Architecture:** WordPress con Elementor Pro come page builder e Astra Pro come tema base. Ogni pagina BU segue un template condiviso costruito come Elementor Template. La multilingua è gestita da WPML con struttura URL `/en/` per la versione inglese.

**Tech Stack:** WordPress 6.x, Elementor Pro 3.x, Astra Pro, Yoast SEO, WP Rocket, WPML, Wordfence, WPForms, Cookie Law Info, Cloudflare CDN

**Design Spec:** `docs/superpowers/specs/2026-05-21-sito-debro-design.md`

**Copy IT approvato:** vedere sessione di brainstorming e memory agent copywriter

---

## Task 1: Hosting + WordPress install

**Checkpoint:** WordPress accessibile su dominio/staging, admin funzionante.

- [ ] **Step 1: Scegli hosting**

  Vai su SiteGround Business o Kinsta Starter. Crea account. Registra/trasferisci `debro.it` o usa sottodominio staging (es. `staging.debro.it`) per sviluppo.

- [ ] **Step 2: Installa WordPress**

  Dal pannello hosting usa il wizard one-click WordPress install. Impostazioni:
  - Site title: `Debro Group`
  - Admin email: `vincenzo.defalco@debro.it`
  - Username: non usare `admin` — scegli username personalizzato
  - Language: Italiano

- [ ] **Step 3: Configura impostazioni base WordPress**

  Vai in **Impostazioni → Generali**:
  - Titolo sito: `Debro Group`
  - Tagline: `Competenze reali. Risultati concreti.`
  - Timezone: `Rome`

  Vai in **Impostazioni → Permalink**:
  - Seleziona: `Nome articolo` (`/%postname%/`)
  - Salva

- [ ] **Step 4: Disabilita commenti globalmente**

  Vai in **Impostazioni → Discussione**:
  - Deseleziona tutto nella sezione "Impostazioni predefinite articolo"
  - Salva

- [ ] **Step 5: Elimina contenuto demo**

  Vai in **Articoli** → elimina "Hello World". Vai in **Pagine** → elimina "Sample Page".

- [ ] **Step 6: Verifica**

  Apri `debro.it` (o staging URL) nel browser. Vedi schermata WordPress base. Admin login funziona. ✓

- [ ] **Step 7: Checkpoint git**

  ```bash
  # Esporta settings WordPress come riferimento
  # In WP Admin: Strumenti → Esporta → Tutto il contenuto → Scarica file export
  # Salva in: docs/wp-exports/01-base-install.xml
  git add docs/wp-exports/01-base-install.xml
  git commit -m "chore: WordPress base install checkpoint"
  ```

---

## Task 2: Installa e configura plugin essenziali

**Checkpoint:** Tutti i plugin attivi, nessun conflitto, Elementor editor funzionante.

- [ ] **Step 1: Installa Astra Pro**

  Vai in **Aspetto → Temi → Aggiungi nuovo**. Cerca "Astra". Installa e attiva.
  
  Poi vai su [wpastra.com](https://wpastra.com) → Download Astra Pro plugin ZIP. Vai in **Plugin → Aggiungi nuovo → Carica plugin**. Carica ZIP. Attiva. Inserisci license key.

- [ ] **Step 2: Installa Elementor Pro**

  Vai su [elementor.com](https://elementor.com) → Download Elementor Pro ZIP. **Plugin → Aggiungi nuovo → Carica plugin**. Carica ZIP. Attiva. Inserisci license key e connetti sito.

- [ ] **Step 3: Installa plugin essenziali**

  Vai in **Plugin → Aggiungi nuovo**. Installa e attiva in sequenza:
  - `Yoast SEO` (cerca e installa)
  - `WP Rocket` (ZIP da account wprocket.me → carica manualmente)
  - `Wordfence Security` (cerca e installa)
  - `WPForms Lite` (cerca e installa — versione free sufficiente per form contatti)
  - `Cookie Law Info` (cerca "CookieYes" o "Cookie Law Info" → installa)

- [ ] **Step 4: Installa WPML**

  Vai su [wpml.org](https://wpml.org) → Download WPML Multilingual CMS ZIP. **Plugin → Carica**. Attiva. Wizard setup:
  - Lingua del sito: Italiano
  - Aggiungi lingua: English
  - Directory per traduzione EN: `/en/`

  Installa anche plugin companion: **WPML String Translation** e **WPML Translation Management** (inclusi nel download WPML).

- [ ] **Step 5: Verifica nessun conflitto**

  Vai in **Dashboard**. Nessun errore PHP. Elementor editor apribile: vai in **Pagine → Aggiungi nuova → Modifica con Elementor**. Editor carica. Chiudi senza salvare.

- [ ] **Step 6: Disabilita WP Rocket temporaneamente**

  Durante sviluppo il caching interferisce. Vai in **WP Rocket → Dashboard** → toggle OFF. Riattiverai a fine build.

- [ ] **Step 7: Checkpoint**

  ```bash
  git commit -m "chore: all plugins installed and verified"
  ```

---

## Task 3: Configura design system globale (Astra + Elementor)

**Checkpoint:** Palette, font e bottoni globali applicati. Qualsiasi nuova pagina eredita il sistema.

- [ ] **Step 1: Configura palette globale Elementor**

  Vai in **Elementor → Kit del sito → Impostazioni globali → Colori**. Aggiungi:
  
  | Nome | Hex |
  |---|---|
  | Navy Primary | `#1A3A6B` |
  | Blue Secondary | `#2A5298` |
  | Dark Text | `#0D1F3C` |
  | Slate Body | `#3A4A5C` |
  | Light BG | `#E8EDF5` |
  | Off White | `#F8F9FC` |
  | Accent CTA | `#F5A623` |

  Salva.

- [ ] **Step 2: Configura font globali Elementor**

  Vai in **Elementor → Kit del sito → Impostazioni globali → Font**. Imposta:
  - Primary font: `Inter` (Google Fonts)
  - Secondary font: `Inter`

  Vai in **Elementor → Kit del sito → Tipografia globale**:
  - Body: Inter 400, 17px, line-height 1.6, colore `#3A4A5C`
  - H1: Inter 800, 48px, line-height 1.15, colore `#0D1F3C`
  - H2: Inter 700, 32px, line-height 1.25, colore `#1A3A6B`
  - H3: Inter 700, 22px, colore `#0D1F3C`

  Salva.

- [ ] **Step 3: Configura bottoni globali**

  Vai in **Elementor → Kit del sito → Bottoni**:
  - Background: `#1A3A6B`
  - Testo: `#FFFFFF`
  - Border radius: `4px`
  - Padding: `10px 20px`
  - Typography: Inter 700, 14px

  Salva.

- [ ] **Step 4: Configura Astra — Header builder**

  Vai in **Aspetto → Personalizza → Intestazione**. Usa Astra Header Builder:
  - Riga 1: Logo SX | Menu principale CENTRO | [IT/EN language switcher] + [CTA button] DX
  - Background header: `#1A3A6B`
  - Logo: carica `Logo Società/Logo Colorato.png` — imposta altezza 40px
  - Header sticky: ON
  - Trasparenza: OFF

- [ ] **Step 5: Crea menu principale**

  Vai in **Aspetto → Menu → Crea nuovo menu** chiamato `Menu principale IT`.
  Aggiungi voci (pagine ancora da creare — aggiungile come link personalizzati per ora):
  - Consulting → `#`
  - Software → `#`
  - Formazione → `#`
  - AI → `#`

  Assegna al: `Primary Menu`. Salva.

- [ ] **Step 6: Configura Astra — Footer builder**

  Vai in **Aspetto → Personalizza → Piè di pagina**:
  - Background: `#0D1F3C`
  - Riga 1: Colonna SX (logo + P.IVA) | Colonna DX (2 menu widget: Servizi + Contatti)
  - Riga 2: Copyright centrato — testo: `© 2026 Debro Group. P.IVA [INSERIRE]. Privacy Policy · Cookie Policy`

- [ ] **Step 7: CSS custom globale**

  Vai in **Elementor → Kit del sito → CSS personalizzato**. Incolla:

  ```css
  /* Card BU — variante chiara */
  .card-bu-light {
    background: #ffffff;
    border-left: 3px solid #1A3A6B;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(26,58,107,0.07);
    padding: 1.5rem;
  }

  /* Card BU — variante scura */
  .card-bu-dark {
    background: #1A3A6B;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(26,58,107,0.2);
    padding: 1.5rem;
  }

  /* Bottone CTA accent */
  .btn-accent {
    background: #F5A623 !important;
    color: #ffffff !important;
    border-radius: 4px;
    font-weight: 700;
  }

  /* Bottone outline */
  .btn-outline {
    background: transparent !important;
    border: 2px solid #1A3A6B !important;
    color: #1A3A6B !important;
    border-radius: 4px;
    font-weight: 700;
  }

  /* Label BU uppercase */
  .label-bu {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #1A3A6B;
    margin-bottom: 8px;
    display: block;
  }

  /* Accent bar */
  .accent-bar {
    width: 32px;
    height: 3px;
    background: #F5A623;
    border-radius: 2px;
    margin-bottom: 16px;
  }

  /* Sezione clienti — loghi grayscale */
  .clients-logo img {
    filter: grayscale(1);
    opacity: 0.55;
    transition: opacity 0.2s;
    max-height: 40px;
    width: auto;
  }
  .clients-logo img:hover {
    opacity: 0.85;
  }
  ```

  Salva.

- [ ] **Step 8: Verifica design system**

  Apri qualsiasi pagina in Elementor. Aggiungi un widget Heading — verifica che il font sia Inter. Aggiungi un widget Button — verifica colore navy. Rimuovi e chiudi senza salvare.

- [ ] **Step 9: Checkpoint**

  ```bash
  git commit -m "feat: global design system configured (palette, typography, buttons, header, footer)"
  ```

---

## Task 4: Crea template BU (Elementor Template)

**Checkpoint:** Template riutilizzabile salvato in Elementor. Applicabile a tutte le pagine BU.

- [ ] **Step 1: Crea pagina "Template BU"**

  **Pagine → Aggiungi nuova**. Titolo: `[TEMPLATE] BU`. Pubblica. Apri con Elementor.

- [ ] **Step 2: Costruisci sezione Hero (Sezione 1)**

  Aggiungi nuova sezione. Layout: 2 colonne (60% / 40%).
  
  Colonna SX:
  - Widget HTML: `<div class="accent-bar"></div>`
  - Widget Text: classe CSS `label-bu` — testo: `[NOME BU]`
  - Widget Heading (H1): testo placeholder `[Headline BU]` — stile da globale
  - Widget Text: testo placeholder `[Sottotitolo]` — colore `rgba(255,255,255,0.65)`
  - Widget Button: testo `[CTA primaria]` — classe `btn-accent`
  - Widget Button: testo `[CTA secondaria]` — classe `btn-outline` — colore bordo/testo bianco
  
  Colonna DX:
  - Widget Inner Section (griglia 2x2) con 4 widget Text per card mini-BU
  
  Stile sezione: background gradiente da `#0D1F3C` a `#1A3A6B` (angolo 135°). Padding: 80px 0.

- [ ] **Step 3: Costruisci sezione Approccio (Sezione 2)**

  Aggiungi sezione. Layout: full width. Background: `#FFFFFF`. Padding: 80px 0.
  
  - Widget Text: classe `label-bu` — testo `[LABEL SEZIONE]`
  - Widget Heading (H2): testo `[Titolo approccio]`
  - Widget Inner Section 2 colonne:
    - Colonna SX: Inner Section con card (background `#F8F9FC`, border-top 3px `#1A3A6B`, radius 8px)
    - Colonna DX: stessa struttura

- [ ] **Step 4: Costruisci sezione Specifica (Sezione 3)**

  Aggiungi sezione placeholder. Background: `#E8EDF5`. Padding: 60px 0.
  - Nota: questa sezione va personalizzata per ogni BU (vedi spec sezione 5)
  - Placeholder: Widget Heading `[SEZIONE SPECIFICA BU]`

- [ ] **Step 5: Costruisci sezione Progetti (Sezione 4)**

  Aggiungi sezione. Background: `#F8F9FC`. Padding: 80px 0.
  
  - Widget Text: classe `label-bu`
  - Widget Heading (H2): `[Titolo progetti]`
  
  Per ogni card progetto (ripeti 3 volte):
  - Widget Inner Section: 2 colonne (icona 60px | contenuto)
    - Col SX: Widget Icon Box (icona quadrata navy 36px)
    - Col DX: Badge status (HTML widget) + Heading H3 + Text + Link

- [ ] **Step 6: Costruisci sezione CTA (Sezione 5)**

  Aggiungi sezione. Background: `#1A3A6B`. Padding: 80px 0. Allineamento: center.
  - Widget Heading (H2): colore `#FFFFFF`
  - Widget Text: colore `rgba(255,255,255,0.65)`
  - Widget Button: classe `btn-accent`

- [ ] **Step 7: Salva come Elementor Template**

  Click **Freccia accanto a "Pubblica"** → **Salva come template**. Nome: `BU Page Template`. Tipo: Pagina.

- [ ] **Step 8: Verifica template salvato**

  Vai in **Elementor → Modelli**. Vedi `BU Page Template` in lista. ✓

- [ ] **Step 9: Checkpoint**

  ```bash
  git commit -m "feat: Elementor BU page template created"
  ```

---

## Task 5: Homepage

**Checkpoint:** Homepage pubblicata con tutte le sezioni, navigazione funzionante.

- [ ] **Step 1: Crea pagina Homepage**

  **Pagine → Aggiungi nuova**. Titolo: `Homepage`. Attributi pagina → Template: `Elementor Canvas`. Pubblica. Apri con Elementor.

- [ ] **Step 2: Imposta come homepage**

  **Impostazioni → Lettura**:
  - La prima pagina mostra: Una pagina statica
  - Prima pagina: `Homepage`
  - Salva.

- [ ] **Step 3: Sezione 1 — Hero split**

  Sezione 2 colonne (50/50). Background gradiente `#0D1F3C → #1A3A6B` (135°). Min-height: 600px.
  
  Colonna SX (padding 60px):
  - HTML: `<div class="accent-bar"></div>`
  - Heading H1: `Un gruppo. Quattro specializzazioni. Zero improvvisazione.` — Inter 800, bianco
  - Text: `Consulenza, software, formazione e AI per le PMI italiane che fanno sul serio.` — rgba(255,255,255,0.65)
  - Button row (widget Button x2):
    - Button 1: `Scopri il Gruppo` — classe `btn-accent` — ancora `#bu-section`
    - Button 2: `Contattaci` — classe `btn-outline` — link `/contatti/`
  
  Colonna DX: Inner Section 2x2 con 4 mini-card semitrasparenti (HTML widget):
  ```html
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:20px;">
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:16px;text-align:center;">
      <div style="font-size:12px;font-weight:700;color:rgba(255,255,255,0.9);margin-bottom:4px;">Consulting</div>
      <div style="font-size:11px;color:rgba(255,255,255,0.5);">ISO · ACN · Normative</div>
    </div>
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:16px;text-align:center;">
      <div style="font-size:12px;font-weight:700;color:rgba(255,255,255,0.9);margin-bottom:4px;">Software</div>
      <div style="font-size:11px;color:rgba(255,255,255,0.5);">Custom · ICT · Cloud</div>
    </div>
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:16px;text-align:center;">
      <div style="font-size:12px;font-weight:700;color:rgba(255,255,255,0.9);margin-bottom:4px;">Formazione</div>
      <div style="font-size:11px;color:rgba(255,255,255,0.5);">81/08 · ICT · Mgmt</div>
    </div>
    <div style="background:rgba(255,255,255,0.12);border-radius:8px;padding:16px;text-align:center;border:1px solid rgba(245,166,35,0.4);">
      <div style="font-size:12px;font-weight:700;color:#F5A623;margin-bottom:4px;">Debro AI</div>
      <div style="font-size:11px;color:rgba(255,255,255,0.5);">Processi · Dati · PMI</div>
    </div>
  </div>
  ```

- [ ] **Step 4: Sezione 2 — Chi siamo**

  Sezione 2 colonne (60/40). Background: `#FFFFFF`. Padding: 80px 0.
  
  Colonna SX:
  - Text (classe `label-bu`): `Chi siamo`
  - Heading H2: `Non siamo un'agenzia tuttofare. Siamo un gruppo che sa cosa fa.`
  - Text: `Debro è un ecosistema di competenze: consulenza organizzativa, sviluppo software, formazione professionale e AI applicata. Quattro realtà specializzate, un unico obiettivo — generare valore concreto per chi ci sceglie.`
  
  Colonna DX: 3 widget Icon List con sfondo `#E8EDF5`, radius 6px, padding 10px:
  - `Competenze reali, non slide`
  - `Un solo interlocutore per 4 aree`
  - `Target: PMI e PA italiane`

- [ ] **Step 5: Sezione 3 — 4 BU cards**

  Sezione full width. Background: `#F8F9FC`. Padding: 80px 0. ID: `bu-section`.
  
  - Text (label): `Le nostre aree`
  - Heading H2: `Quattro specializzazioni. Un gruppo.`
  - Inner Section 2x2 grid (usa widget Inner Section anidato):

  Card Consulting (classe `card-bu-light`):
  - Text label: `Consulting`
  - Heading H3: `La normativa non aspetta.`
  - Text: `ISO, ACN, sistemi di gestione, D.Lgs. 36/2023.`
  - Link text: `Scopri →` → link `/consulting/`

  Card Software (classe `card-bu-dark`):
  - Text label (colore rgba(255,255,255,0.6)): `Software`
  - Heading H3 (bianco): `Codice che va in produzione.`
  - Text (rgba(255,255,255,0.7)): `Software custom, consulenza ICT, ARCASID.`
  - Link (colore `#F5A623`): `Scopri →` → link `/software/`

  Card Formazione (classe `card-bu-light`):
  - Text label: `Formazione`
  - Heading H3: `Formazione obbligatoria. Non inutile.`
  - Text: `81/08, ICT & Digital Skills, Management.`
  - Link: `Scopri →` → link `/formazione/`

  Card AI (HTML widget — card con bordo accent):
  ```html
  <div style="background:linear-gradient(135deg,#0D1F3C,#1A3A6B);border-radius:8px;padding:1.5rem;border:1px solid rgba(245,166,35,0.25);position:relative;overflow:hidden;">
    <span style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;color:#F5A623;display:block;margin-bottom:8px;">Debro AI</span>
    <h3 style="font-size:18px;font-weight:700;color:#fff;margin-bottom:8px;line-height:1.3;">L'AI che lavora.<br>Nei tuoi processi.</h3>
    <p style="font-size:14px;color:rgba(255,255,255,0.65);line-height:1.5;margin-bottom:12px;">Automazione, analisi e assistenti AI su misura. Nessuna demo. Solo risultati misurabili.</p>
    <a href="/ai/" style="font-size:13px;color:#F5A623;font-weight:700;text-decoration:none;">Scopri →</a>
  </div>
  ```

- [ ] **Step 6: Sezione 4 — Loghi clienti**

  Sezione full width. Background: `#FFFFFF`. Padding: 60px 0.
  
  - Text (label centrato): `Ci hanno scelto`
  - Image Gallery o riga di widget Image: carica tutti i loghi da `Logo Clienti/`. Per ogni immagine:
    - Classe CSS: `clients-logo`
    - Alt text: nome cliente
    - Link: nessuno
    - Dimensione: custom height 40px, width auto

  Loghi da caricare su WordPress Media Library: `logo-bicocca.png`, `logo-sielte.png`, `logo-met.png`, `logo-legambiente.png`, `logo-unipv.png`, `logo-uniroma2.png`, `logo-beon.png`

- [ ] **Step 7: Sezione 5 — CTA finale**

  Sezione full width. Background: `#F8F9FC`. Padding: 80px 0. Allineamento: center.
  - Heading H2: `Parliamo del tuo progetto.`
  - Text: `Un'analisi iniziale è gratuita e senza impegno. Scopri quale area Debro fa per te.`
  - Button: `Contattaci ora` — classe `btn-accent` — link `/contatti/`

- [ ] **Step 8: Pubblica e verifica**

  Click **Pubblica**. Apri `debro.it` nel browser. Verifica:
  - [ ] Hero visibile e testo corretto
  - [ ] 4 card BU cliccabili (link placeholder ok per ora)
  - [ ] Loghi clienti visibili in grayscale
  - [ ] CTA funzionante
  - [ ] Responsive mobile (DevTools → iPhone 12)

- [ ] **Step 9: Checkpoint**

  ```bash
  git commit -m "feat: homepage complete"
  ```

---

## Task 6: Pagina Debro Consulting

**Checkpoint:** Pagina `/consulting/` pubblicata con hero, 4 servizi, progetti, CTA.

- [ ] **Step 1: Crea pagina**

  **Pagine → Aggiungi nuova**. Titolo: `Consulting`. Slug: `consulting`. Template: `Elementor Canvas`. Pubblica. Apri con Elementor.

- [ ] **Step 2: Importa template BU**

  Click **icona cartella** (Aggiungi template) → **I miei template** → `BU Page Template` → Inserisci. Template importato.

- [ ] **Step 3: Personalizza Hero**

  - Label: `Consulting`
  - H1: `La normativa non aspetta. Noi siamo già pronti.`
  - Sottotitolo: `Sistemi di gestione, compliance ACN e certificazioni ISO per aziende che non vogliono essere colte impreparate.`
  - CTA primaria: `Parliamo della tua situazione` → link `/contatti/?area=consulting`
  - CTA secondaria: `I nostri servizi →` → ancora `#servizi`
  - Visual DX: 4 card con servizi (HTML):
  ```html
  <div style="display:flex;flex-direction:column;gap:8px;padding:20px;">
    <div style="background:rgba(255,255,255,0.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,0.85);border-left:2px solid #F5A623;">ISO 9001 · 27001 · 45001</div>
    <div style="background:rgba(255,255,255,0.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,0.85);border-left:2px solid rgba(255,255,255,0.2);">Accreditamento ACN</div>
    <div style="background:rgba(255,255,255,0.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,0.85);border-left:2px solid rgba(255,255,255,0.2);">D.Lgs. 36/2023</div>
    <div style="background:rgba(255,255,255,0.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,0.85);border-left:2px solid rgba(255,255,255,0.2);">Piattaforme PAD</div>
  </div>
  ```

- [ ] **Step 4: Personalizza Sezione Approccio → Sezione Servizi**

  ID sezione: `servizi`. Label: `Cosa facciamo`. H2: `Trasformiamo la complessità normativa in vantaggio competitivo.`
  
  4 card servizio (grid 2x2):
  - **Sistemi di gestione** — `Progettiamo sistemi integrati (qualità, sicurezza, ambiente) adattati alla struttura reale dell'organizzazione, non a template standard.`
  - **Accreditamento ACN** — `Percorso completo: analisi del gap, documentazione, affiancamento nei processi di verifica presso l'Agenzia per la Cybersicurezza Nazionale.`
  - **Normative ISO** — `ISO 9001, 27001, 45001. Dalla gap analysis alla certificazione, fino al mantenimento nel tempo.`
  - **Codice Contratti & PAD** — `Recepimento D.Lgs. 36/2023 e supporto adozione Piattaforme di Approvvigionamento Digitale per stazioni appaltanti e operatori economici.`

- [ ] **Step 5: Sostituisci Sezione Specifica → Sezione Progetti**

  Label: `Progetti realizzati`. H2: `Tre casi concreti.`
  
  3 card orizzontali:
  - **Supporto Università** — `Gestione documentale e processi di accreditamento per importanti atenei italiani, con digitalizzazione delle Scuole di Specializzazione.`
  - **Piattaforme PAD** — `Gestione adozione Piattaforme di Approvvigionamento Digitale per centrali di committenza con formazione e supervisione.`
  - **D.Lgs 36/2023** — `Consulenza per recepimento nuovo Codice Contratti Pubblici: procedure, modelli e strumenti di compliance.`

- [ ] **Step 6: CTA**

  H2: `Parliamo della tua situazione.`
  Text: `Prima call gratuita. Nessun impegno. Solo una conversazione concreta.`
  Button: `Contattaci →` → `/contatti/?area=consulting`

- [ ] **Step 7: Aggiorna menu**

  **Aspetto → Menu**. Modifica voce "Consulting" — cambia link placeholder con URL `/consulting/`. Salva.

- [ ] **Step 8: Verifica**

  Apri `debro.it/consulting/`. Tutte le sezioni visibili. Click CTA → va a `/contatti/` (pagina ancora da creare, 404 ok per ora). ✓

- [ ] **Step 9: Checkpoint**

  ```bash
  git commit -m "feat: Debro Consulting page complete"
  ```

---

## Task 7: Pagina Debro Software

**Checkpoint:** Pagina `/software/` pubblicata con hero, approccio, stack, 3 progetti, CTA.

- [ ] **Step 1: Crea pagina**

  Stessa procedura Task 6 Step 1. Titolo: `Software`. Slug: `software`.

- [ ] **Step 2: Importa template BU e personalizza Hero**

  - Label: `Software`
  - H1: `Software che va in produzione. Non solo in presentazione.`
  - Sottotitolo: `Sviluppo custom e consulenza ICT per chi ha bisogno di soluzioni che funzionano davvero nell'ambiente reale.`
  - CTA primaria: `Raccontaci il tuo progetto` → `/contatti/?area=software`
  - CTA secondaria: `Vedi i progetti →` → ancora `#progetti`
  - Visual DX: lista stack (HTML — vedi wireframe bu-template.html)

- [ ] **Step 3: Sezione Approccio**

  Label: `Come lavoriamo`. H2: `Entriamo nei team. Capiamo i processi. Scriviamo codice.`
  
  2 card:
  - **Consulenza integrata** — `I nostri professionisti si affiancano ai team interni: cloud, microservizi, sicurezza applicativa, integrazione sistemi. Competenze reali, non slide.`
  - **Sviluppo end-to-end** — `Analisi dei requisiti, progettazione, sviluppo iterativo, test, deployment e supporto post-rilascio. Un ciclo completo, senza buchi di responsabilità.`

- [ ] **Step 4: Sezione Stack tecnologico**

  Background: `#E8EDF5`. Label: `Stack tecnologico`. Usa widget HTML:
  ```html
  <div style="display:flex;gap:8px;flex-wrap:wrap;">
    <span style="background:#1A3A6B;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">React</span>
    <span style="background:#1A3A6B;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">Node.js</span>
    <span style="background:#1A3A6B;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">Python</span>
    <span style="background:#1A3A6B;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">Java Spring Boot</span>
    <span style="background:#2A5298;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">AWS</span>
    <span style="background:#2A5298;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">Azure</span>
    <span style="background:#2A5298;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">GCP</span>
    <span style="background:#2A5298;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">Docker</span>
    <span style="background:#455a7a;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">PostgreSQL</span>
    <span style="background:#455a7a;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">MongoDB</span>
    <span style="background:#455a7a;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">ChatGPT API</span>
    <span style="background:#455a7a;color:#fff;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;">GDPR · OWASP</span>
  </div>
  ```

- [ ] **Step 5: Sezione Progetti (ID: `progetti`)**

  Label: `Progetti realizzati`. H2: `In produzione, non in demo.`
  
  **ARCASID** (badge: "In produzione" — sfondo `#e8f5e9`, testo `#2e7d32`):
  - H3: `ARCASID — Digital Logbook`
  - Text: `Il primo sistema digitale per tirocini universitari. LogBook digitale, segreteria intelligente, Diploma Supplement automatico. Integrato con ESSE3/Cineca, SPID e SSO (Shibboleth, Microsoft SAML).`
  - Link: `Università degli Studi di Milano Bicocca · arcasid.it →`

  **BInclusion** (badge: "In sviluppo" — sfondo `#e3f2fd`, testo `#1565c0`):
  - H3: `BInclusion`
  - Text: `L'inclusione non si dichiara. Si misura. Piattaforma per gestione e monitoraggio dei percorsi di inclusione con strumenti operativi e dati reali per le decisioni.`
  - ⚠️ Validare contenuto con cliente prima pubblicazione

  **MedData** (badge: "In produzione"):
  - H3: `MedData — Ricerca Clinica`
  - Text: `Piattaforma cloud per raccolta dati clinici standardizzati: questionari strutturati, dashboard e statistiche per ricerca scientifica.`

- [ ] **Step 6: CTA + aggiorna menu + verifica + commit**

  CTA: `Raccontaci il tuo progetto.` / `Prima call gratuita. Nessun impegno.` / Button: `Parliamo →`
  
  Aggiorna menu voce "Software" → `/software/`. Verifica pagina. Commit:
  ```bash
  git commit -m "feat: Debro Software page complete"
  ```

---

## Task 8: Pagina Debro Formazione

**Checkpoint:** Pagina `/formazione/` con hero, 3 aree, catalogo accordion, CTA.

- [ ] **Step 1: Crea pagina e importa template**

  Titolo: `Formazione`. Slug: `formazione`. Importa template BU.

- [ ] **Step 2: Hero**

  - Label: `Formazione`
  - H1: `Formazione obbligatoria. Ma non inutile.`
  - Sottotitolo: `Corsi D.Lgs. 81/08, ICT e sviluppo professionale — progettati per lasciare qualcosa, non solo un attestato.`
  - CTA primaria: `Richiedi il catalogo` → `/contatti/?area=formazione`
  - Visual DX: 3 icone area (HTML con emoji o SVG semplici):
  ```html
  <div style="display:flex;flex-direction:column;gap:12px;padding:20px;">
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
      <span style="font-size:20px;">💻</span>
      <div style="font-size:13px;font-weight:700;color:rgba(255,255,255,0.9);">ICT & Digital Skills</div>
    </div>
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
      <span style="font-size:20px;">📊</span>
      <div style="font-size:13px;font-weight:700;color:rgba(255,255,255,0.9);">Management & Soft Skills</div>
    </div>
    <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;">
      <span style="font-size:20px;">⛑️</span>
      <div style="font-size:13px;font-weight:700;color:rgba(255,255,255,0.9);">Sicurezza D.Lgs. 81/08</div>
    </div>
  </div>
  ```

- [ ] **Step 3: Sezione 3 aree formative**

  Label: `Le nostre aree`. H2: `Tre aree. Un approccio concreto.`
  
  3 card (usa Inner Section 3 colonne):
  - **ICT & Digital Skills** — `Python, Java, React, SQL, Cybersecurity, Cloud, AI/ML. Programmi tecnici per chi deve davvero usare gli strumenti.`
  - **Management e Soft Skills** — `Agile, Scrum, PMI, Leadership, Comunicazione, Coaching. Per chi gestisce team, progetti o cambiamenti organizzativi e vuole farlo con metodo.`
  - **Salute e Sicurezza 81/08** — `La formazione sulla sicurezza non è facoltativa. Noi la rendiamo anche efficace. Corsi per lavoratori, preposti, dirigenti, RLS, RSPP, ASPP, antincendio, primo soccorso.`

- [ ] **Step 4: Catalogo corsi (accordion)**

  Usa widget **Toggle** o **Accordion** di Elementor Pro. 3 gruppi:
  
  **ICT & Digital Skills:**
  - Programmazione (Python, Java, JavaScript/React, SQL) — durata variabile — destinatari: sviluppatori, IT staff
  - Cybersecurity & Data Protection (GDPR, ISO/IEC 27001, OWASP) — destinatari: IT, responsabili dati
  - Cloud & DevOps (AWS, Azure, Kubernetes, Docker, CI/CD) — destinatari: DevOps, SysAdmin
  - Digitalizzazione processi aziendali — destinatari: PM, responsabili operativi
  - AI & Machine Learning applicata al business — destinatari: management, IT

  **Management e Soft Skills:**
  - Project Management Agile/Scrum/PMI standard
  - Leadership e gestione del team
  - Comunicazione efficace e negoziazione
  - Coaching e sviluppo soft skills

  **Salute e Sicurezza 81/08:**
  - Corsi per lavoratori (basso/medio/alto rischio) + aggiornamenti periodici
  - Corsi per dirigenti e datori di lavoro
  - RLS/RSPP/ASPP — moduli A, B, C + aggiornamenti
  - Antincendio — livelli 1, 2, 3 con prove pratiche
  - Primo Soccorso — gruppi A, B, C + BLSD
  - Lavori in quota + DPI III categoria
  - PES/PAV/PEI — sicurezza elettrica

- [ ] **Step 5: CTA**

  H2: `Verifica la tua scadenza.`
  Text: `Controlla lo stato dei tuoi obbligatori 81/08 e richiedi il catalogo completo.`
  Button: `Richiedi il catalogo` → `/contatti/?area=formazione`

- [ ] **Step 6: Aggiorna menu + verifica + commit**

  ```bash
  git commit -m "feat: Debro Formazione page complete"
  ```

---

## Task 9: Pagina Debro AI

**Checkpoint:** Pagina `/ai/` con hero, 3 servizi, sezione FAQ/casi, CTA.

- [ ] **Step 1: Crea pagina e importa template**

  Titolo: `AI`. Slug: `ai`. Importa template BU.

- [ ] **Step 2: Hero**

  - Label: `Debro AI`
  - H1: `L'AI che lavora. Nei tuoi processi.`
  - Sottotitolo: `Automazione, analisi e assistenti AI su misura. Nessuna demo. Solo risultati misurabili.`
  - CTA primaria: `Parliamo dei tuoi processi` → `/contatti/?area=ai`
  - Visual DX: diagramma astratto flusso (HTML):
  ```html
  <div style="padding:20px;display:flex;flex-direction:column;gap:8px;align-items:flex-start;">
    <div style="background:rgba(255,255,255,0.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,0.8);display:flex;align-items:center;gap:8px;">
      <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>Processo manuale
    </div>
    <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,0.3);">↓</div>
    <div style="background:rgba(245,166,35,0.15);border-radius:6px;padding:8px 14px;font-size:12px;color:#F5A623;font-weight:700;border:1px solid rgba(245,166,35,0.3);display:flex;align-items:center;gap:8px;">
      <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>AI Debro
    </div>
    <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,0.3);">↓</div>
    <div style="background:rgba(255,255,255,0.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,0.8);display:flex;align-items:center;gap:8px;">
      <span style="width:8px;height:8px;background:#4caf50;border-radius:50%;flex-shrink:0;"></span>Risultato misurabile
    </div>
  </div>
  ```

- [ ] **Step 3: Sezione 3 servizi**

  Label: `Cosa facciamo`. H2: `AI pratica. Non teorica.`
  
  3 card:
  - **Automazione dei processi** — `Identifichiamo i flussi ripetitivi — documentali, comunicativi, gestionali — e costruiamo automazioni che si integrano con i sistemi esistenti.`
  - **Analisi e supporto alle decisioni** — `Report automatici, alert predittivi, dashboard su misura. Dati che diventano informazioni utili prima che servano.`
  - **Assistenti AI su misura** — `Addestriamo modelli sui tuoi prodotti, procedure e settore. Non un chatbot generico — uno strumento che conosce la tua azienda.`

- [ ] **Step 4: Sezione FAQ (placeholder casi PMI)**

  Label: `Domande frequenti`. H2: `L'AI fa per la mia azienda?`
  
  Accordion con 4 domande:
  - **Siamo una PMI senza team IT interno. Possiamo usare l'AI?** — `Sì. Progettiamo soluzioni che non richiedono un data scientist interno. Partiamo dai processi che già esistono.`
  - **Quanto tempo ci vuole per vedere risultati?** — `Dipende dal processo. Le prime automazioni semplici sono operative in 2-4 settimane. Progetti più complessi seguono un piano incrementale con rilasci parziali.`
  - **I nostri dati restano al sicuro?** — `Sì. Progettiamo con GDPR compliance by design. I dati del cliente non vengono usati per addestrare modelli generali.`
  - **Che differenza c'è da ChatGPT o Copilot?** — `Quelli sono strumenti generici. Noi costruiamo soluzioni specifiche per il tuo settore, i tuoi dati e i tuoi processi.`
  
  ⚠️ Sostituire con casi PMI reali quando disponibili (vedi spec sezione 9).

- [ ] **Step 5: CTA + menu + verifica + commit**

  H2: `Parliamo dei tuoi processi.` / Button: `Prenota una call gratuita` → `/contatti/?area=ai`
  
  Aggiorna menu voce "AI" → `/ai/`.
  ```bash
  git commit -m "feat: Debro AI page complete"
  ```

---

## Task 10: Pagina Contatti

**Checkpoint:** Form funzionante, email in arrivo all'indirizzo corretto, mappa visibile.

- [ ] **Step 1: Crea pagina**

  Titolo: `Contatti`. Slug: `contatti`. Template: `Elementor Canvas`. Pubblica. Apri con Elementor.

- [ ] **Step 2: Crea form con WPForms**

  Vai in **WPForms → Aggiungi nuovo**. Scegli template "Simple Contact Form". Modifica:
  - Campo: Nome e Cognome (testo, obbligatorio)
  - Campo: Azienda (testo, opzionale)
  - Campo: Email (email, obbligatorio)
  - Campo: Telefono (testo, opzionale)
  - Campo: Area di interesse (dropdown, obbligatorio) — opzioni: `Consulting`, `Software`, `Formazione`, `AI`, `Altro`
  - Campo: Messaggio (textarea, obbligatorio)
  - Campo: Accetto la Privacy Policy (checkbox, obbligatorio) — testo: `Ho letto e accetto la [Privacy Policy](/privacy-policy/)`

  Vai in **Impostazioni → Notifiche**:
  - Invia a: `vincenzo.defalco@debro.it`
  - Oggetto: `[Debro] Nuovo contatto da {field_id="1"} — {field_id="4"}`
  - Messaggio: includi tutti i campi con smart tag `{all_fields}`

  Vai in **Impostazioni → Conferme**:
  - Tipo: Messaggio
  - Testo: `Grazie! Abbiamo ricevuto il tuo messaggio e ti risponderemo entro 24 ore lavorative.`

  Salva form.

- [ ] **Step 3: Configura SMTP**

  Installa plugin **WP Mail SMTP**. Configuralo con le credenziali SMTP dell'account `@debro.it` (o usa Brevo/SendGrid per deliverability migliore). Testa invio da **WP Mail SMTP → Strumenti → Test email**.

- [ ] **Step 4: Costruisci pagina Contatti in Elementor**

  Sezione 1 — Hero minimal:
  - Background: `#1A3A6B`. Padding 60px 0.
  - H1 (bianco): `Parliamo.`
  - Text (rgba bianco 65%): `Scegli l'area, raccontaci il tuo progetto.`

  Sezione 2 — Form + Info:
  - Layout 2 colonne (65% / 35%). Background: `#FFFFFF`. Padding: 80px 0.
  - Colonna SX: Widget **WPForms** → seleziona form creato
  - Colonna DX:
    - H3: `Dove siamo`
    - Text: indirizzo fisico Debro (da inserire)
    - Text: email cliccabile con mailto
    - Text: telefono cliccabile con tel
    - Widget Map (Elementor Pro) con indirizzo Debro — API key Google Maps necessaria

  Sezione 3 — CTA footer pagina:
  - Text centrato: `Oppure scrivici direttamente a [email]`

- [ ] **Step 5: Verifica form**

  Compila form con dati test. Invia. Verifica:
  - [ ] Email arriva a `vincenzo.defalco@debro.it` con tutti i campi
  - [ ] Messaggio di conferma appare sulla pagina
  - [ ] Checkbox Privacy obbligatoria funziona (blocca submit se non selezionata)

- [ ] **Step 6: Aggiorna CTA globale**

  Verifica che tutte le CTA su homepage e pagine BU che puntano a `/contatti/` carichino correttamente la pagina.

- [ ] **Step 7: Checkpoint**

  ```bash
  git commit -m "feat: contatti page with working form"
  ```

---

## Task 11: Multilingua IT/EN con WPML

**Checkpoint:** Versione EN accessibile su `/en/`, switcher navbar funzionante, contenuto tradotto.

- [ ] **Step 1: Configura WPML per le pagine esistenti**

  Vai in **WPML → Traduzione** → vedrà tutte le pagine create. Per ogni pagina (Homepage, Consulting, Software, Formazione, AI, Contatti):
  - Click **+** nella colonna EN → `Tradurre`
  - Si apre editor WPML — inserisci testo EN per ogni campo

- [ ] **Step 2: Traduci Homepage EN**

  Traduzione adattata (non letterale). Testi chiave:
  - H1: `One group. Four specializations. Zero improvisation.`
  - Chi siamo H2: `We're not a catch-all agency. We're a group that knows what it does.`
  - Chi siamo body: `Debro is an ecosystem of expertise: organizational consulting, software development, professional training and applied AI. Four specialized units, one goal — delivering real value to those who choose us.`
  - CTA: `Discover the Group` / `Contact Us`

- [ ] **Step 3: Traduci pagine BU EN**

  Per ogni BU tradurre: headline, sottotitolo, nomi servizi, descrizioni, CTA. Mantenere tono: diretto, B2B, niente hype. Stessa struttura IT.

- [ ] **Step 4: Configura language switcher navbar**

  Vai in **WPML → Lingue → Language Switcher**. Tipo: dropdown o flag + codice. Posizionalo nell'header Astra (Custom HTML widget in header builder con shortcode WPML: `[wpml_language_switcher]`).

- [ ] **Step 5: Configura hreflang**

  WPML aggiunge automaticamente hreflang se correttamente configurato. Verifica in **WPML → Impostazioni SEO multilingue** che sia attivo.

- [ ] **Step 6: Verifica**

  - Apri `debro.it/en/` — vedi homepage EN ✓
  - Click switcher → passa da IT a EN e viceversa ✓
  - `debro.it/en/consulting/` carica pagina EN ✓

- [ ] **Step 7: Checkpoint**

  ```bash
  git commit -m "feat: WPML multilingual IT/EN configured"
  ```

---

## Task 12: SEO, performance e lancio

**Checkpoint:** Lighthouse score ≥ 85 su mobile. Sitemap XML attiva. Cookie banner funzionante.

- [ ] **Step 1: Configura Yoast SEO**

  Vai in **Yoast SEO → Impostazioni → Generali**:
  - Nome sito: `Debro Group`
  - Separatore: `·`
  
  Vai in **Yoast SEO → Impostazioni → Sito web**:
  - Tipo organizzazione: Organizzazione
  - Nome: `Debro Group`
  - Logo: carica logo Debro

  Per ogni pagina, apri editor WordPress → pannello Yoast → compila:
  
  | Pagina | SEO Title | Meta Description |
  |---|---|---|
  | Homepage | `Debro Group · Consulting, Software, Formazione e AI per PMI` | `Debro è un gruppo di competenze specializzate: consulenza normativa, sviluppo software, formazione professionale e AI applicata per le PMI italiane.` |
  | Consulting | `Debro Consulting · ISO, ACN, Sistemi di Gestione` | `Sistemi di gestione, accreditamento ACN e normative ISO per aziende che non vogliono essere colte impreparate.` |
  | Software | `Debro Software · Sviluppo Custom e Consulenza ICT` | `Software custom e consulenza ICT end-to-end. Dall'analisi al deployment, con chi sa davvero scrivere codice.` |
  | Formazione | `Debro Formazione · Corsi 81/08, ICT e Management` | `Corsi D.Lgs. 81/08, ICT & Digital Skills e Management. Formazione obbligatoria e percorsi di sviluppo professionale.` |
  | AI | `Debro AI · Intelligenza Artificiale per PMI` | `Automazione processi, analisi predittiva e assistenti AI su misura. AI pratica e misurabile per le PMI italiane.` |
  | Contatti | `Contatti · Debro Group` | `Contatta Debro Group per consulenza, sviluppo software, formazione o AI. Prima call gratuita.` |

- [ ] **Step 2: Attiva WP Rocket**

  Vai in **WP Rocket → Dashboard** → toggle ON.
  
  Configura:
  - **Cache:** attiva page cache, cache mobile separata ON
  - **File Optimization:** minifica CSS e JS ON, carica JS in modo differito ON
  - **Immagini:** lazy load ON, WebP ON (se server supporta)
  - **CDN:** se usi Cloudflare, vai in tab CDN → inserisci URL CDN

- [ ] **Step 3: Ottimizza immagini**

  Installa **ShortPixel Image Optimizer** (piano gratuito: 100 immagini/mese). Vai in **ShortPixel → Bulk Optimize** → ottimizza tutte le immagini caricate (loghi clienti, logo Debro).

- [ ] **Step 4: Configura Cookie Banner**

  Vai in **CookieYes → Cookie Banner**:
  - Template: minimal, colori navy/bianco coerenti col sito
  - Lingua: IT (con versione EN per utenti /en/)
  - Categorie: Necessari (sempre ON) + Analitici (opt-in) + Marketing (opt-in)
  - Testo banner: `Utilizziamo cookie per migliorare la tua esperienza. Puoi accettare tutti i cookie o gestire le tue preferenze.`
  - Bottoni: `Accetta tutti` (accent amber) | `Gestisci preferenze`

  Crea pagina Privacy Policy e Cookie Policy (richieste legalmente). Usa generator IUBENDA o Termageddon.

- [ ] **Step 5: Configura Wordfence**

  Vai in **Wordfence → Gestione Firewall** → attiva firewall. Vai in **Wordfence → Scansione** → esegui prima scansione. Nessun malware. ✓

- [ ] **Step 6: Test Lighthouse**

  Apri Chrome DevTools su `debro.it`. Tab Lighthouse. Esegui audit su Mobile.
  
  Target minimo:
  - Performance: ≥ 85
  - Accessibility: ≥ 90
  - Best Practices: ≥ 90
  - SEO: ≥ 95
  
  Se Performance < 85: verificare immagini non ottimizzate, JS bloccante, WP Rocket non attivo.

- [ ] **Step 7: Test cross-browser**

  Verifica su:
  - [ ] Chrome (desktop + mobile)
  - [ ] Safari (desktop + iPhone)
  - [ ] Firefox (desktop)
  - [ ] Edge (desktop)

- [ ] **Step 8: Checklist pre-lancio**

  - [ ] Tutti i link interni funzionanti (nessun 404)
  - [ ] Form contatti testato e email arriva
  - [ ] Switcher IT/EN funzionante su tutte le pagine
  - [ ] Cookie banner appare alla prima visita
  - [ ] Privacy Policy e Cookie Policy pagine pubblicate
  - [ ] `robots.txt` accessibile su `debro.it/robots.txt`
  - [ ] Sitemap XML su `debro.it/sitemap_index.xml`
  - [ ] Google Search Console: verifica sito e invia sitemap
  - [ ] Analytics: installa Google Analytics 4 o Plausible (privacy-first)
  - [ ] SSL: certificato HTTPS attivo e forzato

- [ ] **Step 9: Lancio**

  Se sviluppato su staging: aggiorna il dominio principale in **Impostazioni → Generali**. Svuota cache WP Rocket. Svuota cache Cloudflare.

- [ ] **Step 10: Checkpoint finale**

  ```bash
  git commit -m "feat: SEO, performance e lancio completati — sito Debro Group live"
  ```

---

## Riepilogo task e dipendenze

```
Task 1: Hosting + WordPress install
Task 2: Plugin (dipende da 1)
Task 3: Design system globale (dipende da 2)
Task 4: Template BU Elementor (dipende da 3)
Task 5: Homepage (dipende da 3)
Task 6: Consulting (dipende da 4)
Task 7: Software (dipende da 4)
Task 8: Formazione (dipende da 4)
Task 9: AI (dipende da 4)
Task 10: Contatti (dipende da 3) — può procedere in parallelo con 6-9
Task 11: Multilingua (dipende da 5,6,7,8,9,10)
Task 12: SEO + lancio (dipende da 11)
```

**Task 6, 7, 8, 9 possono essere eseguiti in parallelo dopo Task 4.**
**Task 10 può essere eseguito in parallelo con 6-9.**
