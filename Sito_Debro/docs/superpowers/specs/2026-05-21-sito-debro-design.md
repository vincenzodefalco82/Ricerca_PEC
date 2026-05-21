# Sito Debro Group — Design Spec

**Data:** 2026-05-21  
**Stato:** Approvato  
**Piattaforma:** WordPress + Elementor Pro + tema Astra  
**Lingua:** IT + EN  
**Gestione dominio/DNS:** Odoo Online 19.0  
**Integrazione CRM:** Odoo Online 19.0 — XML-RPC (vedi sezione 10)  

---

## 1. Architettura

### Stack tecnico
- **CMS:** WordPress (ultima versione stabile)
- **Page builder:** Elementor Pro
- **Tema base:** Astra (versione Pro consigliata per header/footer builder)
- **Plugin essenziali:** Elementor Pro, Astra Pro, Yoast SEO, WP Rocket (caching), Wordfence (sicurezza), WPML o Polylang (multilingua IT/EN), WPForms (form contatti), Cookie Law Info (GDPR banner), WP Mail SMTP, Debro Odoo Bridge (custom)
- **Hosting:** VPS o hosting managed WordPress (es. Kinsta, WP Engine, SiteGround Business) — non hosting condiviso
- **CDN:** Cloudflare (piano gratuito sufficiente)
- **Gestione DNS:** Odoo Online 19.0 — DNS records gestiti dal pannello Odoo (`Settings → Domain Names → debro.it`). Opzione consigliata: delegare nameservers a Cloudflare per maggiore controllo e performance (vedi sezione 10)
- **CRM:** Odoo Online 19.0 — lead da form contatti inviati via XML-RPC (plugin custom `debro-odoo-bridge`)

### Struttura URL
```
debro.it/                    → Homepage
debro.it/consulting/         → Debro Consulting
debro.it/software/           → Debro Software
debro.it/formazione/         → Debro Formazione
debro.it/ai/                 → Debro AI
debro.it/contatti/           → Contatti

debro.it/en/                 → Homepage EN
debro.it/en/consulting/      → Consulting EN
... (struttura speculare)
```

### Multilingua
- Lingua primaria: italiano
- Lingua secondaria: inglese
- Switcher IT/EN nella navbar (lato destro, prima della CTA)
- Plugin raccomandato: WPML (più robusto per SEO multilingua) o Polylang (più economico)

---

## 2. Sitemap

```
Homepage (scroll)
├── Hero
├── Chi siamo
├── 4 card BU (teaser con link)
├── Ci hanno scelto (loghi clienti)
└── CTA finale

Debro Consulting (/consulting/)
├── Hero
├── Servizi (ISO, ACN, PAD, D.Lgs. 36/2023)
├── Progetti realizzati
└── CTA

Debro Software (/software/)
├── Hero
├── Approccio (Consulenza integrata + Sviluppo end-to-end)
├── Stack tecnologico
├── Progetti (ARCASID, BInclusion, MedData)
└── CTA

Debro Formazione (/formazione/)
├── Hero
├── 3 aree formative (ICT, Management, 81/08)
├── Catalogo corsi (accordion per area)
└── CTA

Debro AI (/ai/)
├── Hero
├── 3 servizi (Automazione, Analisi, Assistenti su misura)
├── Casi applicativi PMI (o mini-FAQ se casi non disponibili al lancio)
└── CTA

Contatti (/contatti/)
├── Form contatto
├── Mappa / indirizzo
└── Email + telefono

Globali
├── Navbar fissa (logo, menu BU, IT|EN, CTA Contatti)
├── Footer (link BU, social, P.IVA, Privacy, Cookie)
└── Cookie banner GDPR
```

---

## 3. Linguaggio visivo

### Palette colori
| Token | Valore | Uso |
|---|---|---|
| Navy Primary | `#1A3A6B` | Navbar, bottoni primari, bordi card, titoli sezione |
| Blue Secondary | `#2A5298` | Variazioni card, badge, tag stack |
| Dark Text | `#0D1F3C` | Headline H1/H2, body su sfondo chiaro |
| Slate Body | `#3A4A5C` | Testo corpo standard |
| Light BG | `#E8EDF5` | Sfondi sezione alternati, card highlight |
| Off-white | `#F8F9FC` | Sfondi sezione principali |
| White | `#FFFFFF` | Card, aree contenuto |
| Accent / CTA | `#F5A623` | Solo CTA primari, accenti grafici — usare con parsimonia |

### Tipografia
- **Font:** Inter (Google Fonts) — peso 400, 600, 700, 800
- **H1:** Inter 800, 40–48px, line-height 1.15, colore `#0D1F3C`
- **H2:** Inter 700, 28–32px, line-height 1.25, colore `#1A3A6B`
- **H3:** Inter 700, 20–22px, colore `#0D1F3C`
- **Body:** Inter 400, 16–18px, line-height 1.6, colore `#3A4A5C`
- **Label/Tag:** Inter 700, 11–12px, uppercase, letter-spacing 0.5px

### Bottoni
| Tipo | Stile |
|---|---|
| Primary | Background `#1A3A6B`, testo bianco, border-radius 4px, padding 10px 20px |
| CTA accent | Background `#F5A623`, testo bianco — solo per CTA principale di pagina |
| Outline | Border 2px `#1A3A6B`, testo navy — per azioni secondarie |

### Card BU
- Border-left 3px `#1A3A6B` su sfondo bianco (variante chiara)
- Background `#1A3A6B` testo bianco (variante scura — per highlight o alternanza)
- Border-radius 8px, box-shadow leggero
- Label BU uppercase + headline + body 2 righe max + link "Scopri →"

### Grafica decorativa
- Nessuna fotografia — solo grafica astratta (cerchi, linee, griglie geometriche)
- Sfere/cerchi con bordo semitrasparente su sfondi navy (hero)
- Badge tecnologie come pill/tag arrotondati
- Palette limitata: solo colori della palette definita, no gradienti creativi extra

---

## 4. Homepage — struttura sezioni

| # | Sezione | Sfondo | Note |
|---|---|---|---|
| 1 | Navbar fissa | `#1A3A6B` | Logo sx, menu centro, IT/EN + CTA dx |
| 2 | Hero split 50/50 | Gradiente `#0D1F3C→#1A3A6B` | Sx: headline + 2 CTA. Dx: 4 card mini-BU su sfondo semitrasparente |
| 3 | Chi siamo | `#FFFFFF` | Testo sx 60% + 3 bullet highlight dx 40% |
| 4 | Le 4 BU | `#F8F9FC` | Grid 2x2. Alternanza: card chiara/card navy. Card AI con bordo accent ambra |
| 5 | Ci hanno scelto | `#FFFFFF` | Logo clienti reali in grayscale opacity 55%. No didascalie |
| 6 | CTA finale | `#F8F9FC` | Headline centrata + testo + bottone accent |
| 7 | Footer | `#0D1F3C` | 2 colonne: brand + link BU + link utili |

**Loghi clienti disponibili:** Università Milano Bicocca, Sielte, Met Italia, Legambiente, UniPV, UniRoma2, Beon.

---

## 5. Template pagine BU

Struttura identica per tutte e 4 le BU. Contenuto diverso, schema uguale.

### Sezioni fisse
| # | Sezione | Note |
|---|---|---|
| 1 | Hero split | Breadcrumb + headline BU-specific + 2 CTA + visual dx |
| 2 | Approccio/Servizi | Label + H2 + 2 colonne (card con border-top navy) |
| 3 | Sezione specifica | Vedi variazioni sotto |
| 4 | Progetti/Catalogo | Card orizzontali con icona + badge stato + link |
| 5 | CTA pagina | Sfondo navy, headline + testo + bottone accent |

### Variazioni sezione [3] per BU

**Debro Consulting**
- 4 blocchi servizio: Sistemi di gestione, Accreditamento ACN, Normative ISO, Codice Contratti/PAD
- Nessuna sezione stack tecnologico
- Visual hero dx: 4 card semitrasparenti con nome servizio e norma di riferimento

**Debro Software**
- Stack tecnologico: tag/pill per categoria (Cloud & Infrastructure, Development, AI & Security)
- Sezione [4]: 3 progetti con badge "In produzione" / "In sviluppo"
- Visual hero dx: lista stack key con bordo accent (React, AWS, Docker, GDPR…)

**Debro Formazione**
- 3 aree formative con card (ICT & Digital Skills, Management e Soft Skills, Sicurezza 81/08)
- Sezione [4]: catalogo corsi in accordion per area — titolo corso + durata + destinatari. **Nessuna pagina dedicata per singolo corso** — tutto in accordion sulla pagina Formazione
- CTA: "Richiedi il catalogo" (porta a form contatto con campo "area di interesse" pre-selezionato)
- Visual hero dx: 3 icone area formativa su sfondo semitrasparente

**Debro AI**
- 3 servizi: Automazione processi, Analisi e supporto decisioni, Assistenti AI su misura
- Sezione [4]: casi PMI applicativi (se disponibili) o mini-FAQ (al lancio) — vedi sezione 9
- CTA: "Parliamo dei tuoi processi"
- Visual hero dx: diagramma astratto flusso dati (frecce + nodi geometrici)

---

## 6. Pagina Contatti

- Form: Nome, Azienda, Email, Telefono (opzionale), Area di interesse (dropdown: Consulting/Software/Formazione/AI/Altro), Messaggio
- Integrazione con email aziendale (SMTP o servizio dedicato es. Brevo)
- Indirizzo fisico + mappa Google Maps embed
- Link email + telefono cliccabili
- Privacy checkbox obbligatoria (GDPR)

---

## 7. SEO e performance

- Yoast SEO: meta title/description per ogni pagina, sitemap XML automatica
- Schema markup: Organization, LocalBusiness
- Core Web Vitals: WP Rocket per caching + Cloudflare CDN
- Immagini: formato WebP, lazy loading nativo WordPress
- Multilingua: hreflang tags gestiti da WPML/Polylang
- URL slug in italiano per versione IT, inglese per versione EN

---

## 8. Copy — stato al design freeze

Tutto il copy IT è prodotto e approvato. Include:
- Homepage: Hero, Chi siamo, 4 teaser BU (incluso Debro AI)
- Debro Consulting: Hero + 4 servizi
- Debro Software: Hero, Approccio, 3 progetti
- Debro Formazione: Hero + 3 aree
- Debro AI: Hero + 3 servizi + card homepage
- 5 varianti tagline di gruppo

**Ancora da produrre:**
- Copy EN (traduzione/adattamento da IT)
- Pagina Contatti (micro-copy form)
- Footer (testi link, payoff)
- Meta title/description SEO per ogni pagina

**Note critiche:**
- Card BInclusion: costruita su assunzioni — validare con il cliente prima della pubblicazione
- Headline card AI: variante raccomandata "L'AI che lavora. Nei tuoi processi." — alternativa disponibile "AI applicata. Non spiegata."
- Numeri eventuali (clienti, progetti): da validare con Debro prima di inserire nella sezione stats

---

## 9. Decisioni aperte

| Decisione | Stato | Note |
|---|---|---|
| Hosting provider | Da decidere | Raccomandato: Kinsta o SiteGround Business |
| Plugin multilingua | Da decidere | WPML (robusto, a pagamento) vs Polylang (gratuito, meno SEO features) |
| Dominio | ✓ Chiarito | debro.it gestito via Odoo Online 19 — nessun trasferimento necessario, solo aggiornamento record DNS |
| DNS management | Da eseguire | Opzione A: record A diretti in Odoo. Opzione B: delega nameservers a Cloudflare (raccomandato) |
| Copy EN | Da produrre | Dopo approvazione IT completo |
| Contenuto BInclusion | Da validare | Il copy attuale è basato su assunzioni |
| Casi PMI per Debro AI | Da raccogliere | Al lancio si può usare mini-FAQ come placeholder |

---

## 10. Integrazione Odoo Online 19.0

### Gestione DNS
Il dominio `debro.it` è registrato e gestito tramite Odoo Online 19.0.

**Durante sviluppo:** usare sottodominio staging (es. `staging.debro.it`) — aggiungere record A in Odoo DNS che punta al nuovo hosting. Non toccare il record A principale finché il sito WordPress non è pronto al lancio.

**Al lancio:** aggiornare record A principale in Odoo (`Settings → Domain Names → debro.it → DNS Records`) per puntare all'IP del hosting WordPress. Se si usa Cloudflare, delegare i nameservers prima.

### Integrazione CRM — form contatti → lead Odoo
- **Meccanismo:** plugin WordPress custom `debro-odoo-bridge` (vedi Task 13 del piano)
- **Protocollo:** XML-RPC → endpoint `/xmlrpc/2/common` (auth) + `/xmlrpc/2/object` (operazioni)
- **Autenticazione:** API Key Odoo (non password — più sicuro, revocabile)
- **Oggetto creato:** `crm.lead` con nome, azienda, email, telefono, area di interesse, messaggio
- **Limiti Odoo Online SaaS:** no moduli custom non approvati da Odoo App Store — solo API esposte utilizzabili

### API Odoo disponibili
| Endpoint | Uso |
|---|---|
| `POST /xmlrpc/2/common` → `authenticate` | Ottieni UID sessione |
| `POST /xmlrpc/2/object` → `execute_kw` | CRUD su qualsiasi modello Odoo |
| `POST /web/dataset/call_kw` | JSON-RPC alternativo |

### Credenziali necessarie (da raccogliere prima di Task 13)
- URL istanza: `https://[nome].odoo.com`
- Database name: Odoo → `Settings → Technical → Database Structure`
- Username: email account Odoo
- API Key: `Settings → Users → [utente] → API Keys → New`
