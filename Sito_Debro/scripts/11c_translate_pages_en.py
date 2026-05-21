import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from helpers import odoo
from config import WEBSITE_ID

PAGES = {}

# ══════════════════════════════════════════════════════════
# CONSULTING (id=26)
# ══════════════════════════════════════════════════════════
PAGES[26] = """<t t-name="custom.page_consulting">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:rgba(255,255,255,.7);">Consulting</span>
              <h1>Regulation doesn&#39;t wait. We&#39;re already ready.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Management systems, ACN compliance and ISO certifications for companies that cannot afford to be caught unprepared.</p>
              <div class="d-flex gap-3 flex-wrap">
                <a href="/contatti/?area=consulting" class="btn-dg-accent">Let&#39;s talk about your situation</a>
                <a href="#servizi" class="btn-dg-outline-white">Our services &#8594;</a>
              </div>
            </div>
            <div class="col-lg-5">
              <div class="d-flex flex-column gap-2">
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid #F5A623;">ISO 9001 · 27001 · 45001</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid rgba(255,255,255,.2);">ACN Accreditation</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid rgba(255,255,255,.2);">D.Lgs. 36/2023</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,.85);border-left:2px solid rgba(255,255,255,.2);">PAD Platforms</div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-white" id="servizi">
        <div class="container">
          <span class="dg-label">What we do</span>
          <h2>We turn regulatory complexity into competitive advantage.</h2>
          <div class="row row-cols-1 row-cols-md-2 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>Management systems</h3>
              <p>We design integrated systems (quality, safety, environment) tailored to the real structure of the organisation, not standard templates.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>ACN Accreditation</h3>
              <p>Complete pathway: gap analysis, documentation, support throughout the verification process at the National Cybersecurity Agency.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>ISO Standards</h3>
              <p>ISO 9001, 27001, 45001. From gap analysis to certification, through to ongoing maintenance.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Contracts Code &amp; PAD</h3>
              <p>Implementation of D.Lgs. 36/2023 and support for adoption of Digital Procurement Platforms for contracting authorities and economic operators.</p>
            </div></div>
          </div>
        </div>
      </section>
      <section class="dg-section-light">
        <div class="container">
          <span class="dg-label">Projects delivered</span>
          <h2>Three concrete cases.</h2>
          <div class="d-flex flex-column gap-4 mt-4">
            <div class="dg-card-light"><h3>University Support</h3><p>Document management and accreditation processes for major Italian universities, including digitalisation of Specialisation Schools.</p></div>
            <div class="dg-card-light"><h3>PAD Platforms</h3><p>Management of Digital Procurement Platform adoption for central purchasing bodies, including training and supervision.</p></div>
            <div class="dg-card-light"><h3>D.Lgs 36/2023</h3><p>Consulting for implementation of the new Public Contracts Code: procedures, templates and compliance tools.</p></div>
          </div>
        </div>
      </section>
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Let&#39;s talk about your situation.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Free first call. No commitment. Just a concrete conversation.</p>
          <a href="/contatti/?area=consulting" class="btn-dg-accent">Contact us &#8594;</a>
        </div>
      </section>
    </div>
  </t>
</t>"""

# ══════════════════════════════════════════════════════════
# SOFTWARE (id=27)
# ══════════════════════════════════════════════════════════
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

PAGES[27] = f"""<t t-name="custom.page_software">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:rgba(255,255,255,.7);">Software</span>
              <h1>Software that goes to production. Not just to demo.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Custom development and ICT consulting for those who need solutions that actually work in the real environment.</p>
              <div class="d-flex gap-3 flex-wrap">
                <a href="/contatti/?area=software" class="btn-dg-accent">Tell us about your project</a>
                <a href="#progetti" class="btn-dg-outline-white">See the projects &#8594;</a>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-white">
        <div class="container">
          <span class="dg-label">How we work</span>
          <h2>We embed in teams. Understand processes. Write code.</h2>
          <div class="row row-cols-1 row-cols-md-2 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>Integrated consulting</h3>
              <p>Our professionals work alongside internal teams: cloud, microservices, application security, system integration. Real expertise, not slides.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>End-to-end development</h3>
              <p>Requirements analysis, design, iterative development, testing, deployment and post-release support. A complete cycle with no gaps in responsibility.</p>
            </div></div>
          </div>
        </div>
      </section>
      <section style="background:var(--dg-light);padding:60px 0;">
        <div class="container">
          <span class="dg-label">Tech stack</span>
          <div class="d-flex gap-2 flex-wrap mt-3">{stack_html}</div>
        </div>
      </section>
      <section class="dg-section-white" id="progetti">
        <div class="container">
          <span class="dg-label">Projects delivered</span>
          <h2>Live, not in demo.</h2>
          <div class="d-flex flex-column gap-4 mt-4">
            <div class="dg-card-light">
              <span style="background:#e8f5e9;color:#2e7d32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">Live</span>
              <h3 class="mt-2">ARCASID — Digital Logbook</h3>
              <p>The first digital system for university internships. Digital LogBook, intelligent secretariat, automatic Diploma Supplement. Integrated with ESSE3/Cineca, SPID and SSO (Shibboleth, Microsoft SAML).</p>
              <small style="color:var(--dg-slate);">Università degli Studi di Milano Bicocca · arcasid.it</small>
            </div>
            <div class="dg-card-light">
              <span style="background:#e3f2fd;color:#1565c0;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">In development</span>
              <h3 class="mt-2">BInclusion</h3>
              <p>Inclusion is not declared. It is measured. Platform for managing and monitoring inclusion pathways with operational tools and real data for decisions.</p>
            </div>
            <div class="dg-card-light">
              <span style="background:#e8f5e9;color:#2e7d32;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;">Live</span>
              <h3 class="mt-2">MedData — Clinical Research</h3>
              <p>Cloud platform for standardised clinical data collection: structured questionnaires, dashboards and statistics for scientific research.</p>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Tell us about your project.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Free first call. No commitment.</p>
          <a href="/contatti/?area=software" class="btn-dg-accent">Let&#39;s talk &#8594;</a>
        </div>
      </section>
    </div>
  </t>
</t>"""

# ══════════════════════════════════════════════════════════
# FORMAZIONE (id=28)
# ══════════════════════════════════════════════════════════
PAGES[28] = """<t t-name="custom.page_formazione">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:rgba(255,255,255,.7);">Training</span>
              <h1>Mandatory training. But not useless.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">D.Lgs. 81/08 courses, ICT and professional development — designed to leave something behind, not just a certificate.</p>
              <a href="/contatti/?area=formazione" class="btn-dg-accent">Request the catalogue</a>
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
                  <span style="font-size:13px;font-weight:700;color:rgba(255,255,255,.9);">Health &amp; Safety 81/08</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-white">
        <div class="container">
          <span class="dg-label">Our areas</span>
          <h2>Three areas. One concrete approach.</h2>
          <div class="row row-cols-1 row-cols-md-3 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>ICT &amp; Digital Skills</h3>
              <p>Python, Java, React, SQL, Cybersecurity, Cloud, AI/ML. Technical programmes for those who actually need to use the tools.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Management and Soft Skills</h3>
              <p>Agile, Scrum, PMI, Leadership, Communication, Coaching. For those who manage teams, projects or organisational change.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Health &amp; Safety 81/08</h3>
              <p>Courses for workers, supervisors, managers, RLS, RSPP, ASPP, fire safety, first aid. Mandatory and finally useful.</p>
            </div></div>
          </div>
        </div>
      </section>
      <section class="dg-section-light">
        <div class="container">
          <span class="dg-label">Course catalogue</span>
          <h2>What we offer.</h2>
          <div class="accordion mt-4" id="catalogoCorsi">
            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-navy)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#ict" style="font-weight:700;color:var(--dg-dark);">ICT &amp; Digital Skills</button>
              </h2>
              <div id="ict" class="accordion-collapse collapse show" data-bs-parent="#catalogoCorsi">
                <div class="accordion-body">
                  <ul class="list-unstyled">
                    <li class="mb-2">&#10003; Programming — Python, Java, JavaScript/React, SQL</li>
                    <li class="mb-2">&#10003; Cybersecurity &amp; Data Protection — GDPR, ISO/IEC 27001, OWASP</li>
                    <li class="mb-2">&#10003; Cloud &amp; DevOps — AWS, Azure, Kubernetes, Docker, CI/CD</li>
                    <li class="mb-2">&#10003; Business process digitalisation</li>
                    <li>&#10003; AI &amp; Machine Learning applied to business</li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-navy)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#mgmt" style="font-weight:700;color:var(--dg-dark);">Management and Soft Skills</button>
              </h2>
              <div id="mgmt" class="accordion-collapse collapse" data-bs-parent="#catalogoCorsi">
                <div class="accordion-body">
                  <ul class="list-unstyled">
                    <li class="mb-2">&#10003; Agile / Scrum / PMI Project Management</li>
                    <li class="mb-2">&#10003; Leadership and team management</li>
                    <li class="mb-2">&#10003; Effective communication and negotiation</li>
                    <li>&#10003; Coaching and soft skills development</li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="accordion-item border-0" style="border-left:3px solid var(--dg-navy)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#safety" style="font-weight:700;color:var(--dg-dark);">Health &amp; Safety D.Lgs. 81/08</button>
              </h2>
              <div id="safety" class="accordion-collapse collapse" data-bs-parent="#catalogoCorsi">
                <div class="accordion-body">
                  <ul class="list-unstyled">
                    <li class="mb-2">&#10003; Worker courses — low/medium/high risk + refreshers</li>
                    <li class="mb-2">&#10003; Courses for managers and employers</li>
                    <li class="mb-2">&#10003; RLS / RSPP / ASPP — modules A, B, C + refreshers</li>
                    <li class="mb-2">&#10003; Fire safety — levels 1, 2, 3 with practical exercises</li>
                    <li class="mb-2">&#10003; First Aid — groups A, B, C + BLSD</li>
                    <li class="mb-2">&#10003; Work at height + PPE category III</li>
                    <li>&#10003; PES / PAV / PEI — electrical safety</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Check your deadline.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Verify the status of your mandatory 81/08 obligations and request the full catalogue.</p>
          <a href="/contatti/?area=formazione" class="btn-dg-accent">Request the catalogue</a>
        </div>
      </section>
    </div>
  </t>
</t>"""

# ══════════════════════════════════════════════════════════
# AI (id=29)
# ══════════════════════════════════════════════════════════
PAGES[29] = """<t t-name="custom.page_ai">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <section class="dg-hero">
        <div class="container">
          <div class="row align-items-center g-5 py-4">
            <div class="col-lg-7">
              <div class="dg-accent-bar"></div>
              <span class="dg-label" style="color:#F5A623;">Debro AI</span>
              <h1>AI that works. In your processes.</h1>
              <p class="fs-5 mt-3 mb-4 text-dg-muted">Custom automation, analytics and AI assistants. No demos. Only measurable results.</p>
              <a href="/contatti/?area=ai" class="btn-dg-accent">Let&#39;s talk about your processes</a>
            </div>
            <div class="col-lg-5">
              <div class="d-flex flex-column gap-2 align-items-start">
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,.8);display:flex;align-items:center;gap:8px;">
                  <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>Manual process
                </div>
                <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,.3);">&#8595;</div>
                <div style="background:rgba(245,166,35,.15);border-radius:6px;padding:8px 14px;font-size:12px;color:#F5A623;font-weight:700;border:1px solid rgba(245,166,35,.3);display:flex;align-items:center;gap:8px;">
                  <span style="width:8px;height:8px;background:#F5A623;border-radius:50%;flex-shrink:0;"></span>Debro AI
                </div>
                <div style="margin-left:20px;font-size:18px;color:rgba(255,255,255,.3);">&#8595;</div>
                <div style="background:rgba(255,255,255,.08);border-radius:6px;padding:8px 14px;font-size:12px;color:rgba(255,255,255,.8);display:flex;align-items:center;gap:8px;">
                  <span style="width:8px;height:8px;background:#4caf50;border-radius:50%;flex-shrink:0;"></span>Measurable result
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-white">
        <div class="container">
          <span class="dg-label">What we do</span>
          <h2>Practical AI. Not theoretical.</h2>
          <div class="row row-cols-1 row-cols-md-3 g-4 mt-3">
            <div class="col"><div class="dg-card-light">
              <h3>Process automation</h3>
              <p>We identify repetitive flows — document, communication, management — and build automations that integrate with existing systems.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Analytics and decision support</h3>
              <p>Automated reports, predictive alerts, custom dashboards. Data that becomes useful information before you need it.</p>
            </div></div>
            <div class="col"><div class="dg-card-light">
              <h3>Custom AI assistants</h3>
              <p>We train models on your products, procedures and sector. Not a generic chatbot — a tool that knows your company.</p>
            </div></div>
          </div>
        </div>
      </section>
      <section class="dg-section-light">
        <div class="container">
          <span class="dg-label">FAQ</span>
          <h2>Is AI right for my company?</h2>
          <div class="accordion mt-4" id="faqAI">
            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header"><button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" style="font-weight:700;">We&#39;re an SMB with no internal IT team. Can we use AI?</button></h2>
              <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#faqAI">
                <div class="accordion-body">Yes. We design solutions that require no in-house data scientist. We start from the processes that already exist.</div>
              </div>
            </div>
            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" style="font-weight:700;">How long before we see results?</button></h2>
              <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                <div class="accordion-body">Depends on the process. Simpler automations are operational in 2-4 weeks. More complex projects follow an incremental plan with partial releases.</div>
              </div>
            </div>
            <div class="accordion-item border-0 mb-3" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" style="font-weight:700;">Is our data safe?</button></h2>
              <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                <div class="accordion-body">Yes. We design with GDPR compliance by design. Client data is never used to train general models.</div>
              </div>
            </div>
            <div class="accordion-item border-0" style="border-left:3px solid var(--dg-accent)!important;border-radius:8px;overflow:hidden;">
              <h2 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" style="font-weight:700;">What&#39;s the difference from ChatGPT or Copilot?</button></h2>
              <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#faqAI">
                <div class="accordion-body">Those are generic tools. We build solutions specific to your sector, your data and your processes.</div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section class="dg-section-navy text-center">
        <div class="container">
          <h2 style="color:#fff;">Let&#39;s talk about your processes.</h2>
          <p class="mt-3 mb-4 text-dg-muted">Free first call. No commitment.</p>
          <a href="/contatti/?area=ai" class="btn-dg-accent">Book a free call</a>
        </div>
      </section>
    </div>
  </t>
</t>"""

# ══════════════════════════════════════════════════════════
# CONTATTI (id=33)
# ══════════════════════════════════════════════════════════
MAPS_URL = ("https://maps.google.com/maps"
            "?q=Via+Miguel+Cervantes+De+Saavedra,+55%2F5,+80133+Napoli+NA+Italy"
            "&amp;output=embed")

PAGES[33] = f"""<t t-name="custom.page_contatti">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <section class="dg-section-navy text-center" style="padding:60px 0 50px;">
        <div class="container">
          <h1 style="color:#fff;">Let&#39;s talk.</h1>
          <p class="mt-2 text-dg-muted">Choose your area of interest and tell us about your project.</p>
        </div>
      </section>
      <section class="dg-section-white">
        <div class="container">
          <div class="row g-5">
            <div class="col-lg-7">
              <form action="/website_form/crm.lead" method="post" class="s_website_form" data-success_page="/" enctype="multipart/form-data">
                <div class="row g-3">
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Name and Surname *</label>
                    <input type="text" name="contact_name" class="form-control" required="required" placeholder="John Smith"/>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Company</label>
                    <input type="text" name="partner_name" class="form-control" placeholder="Company Ltd"/>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Email *</label>
                    <input type="email" name="email_from" class="form-control" required="required" placeholder="john@company.com"/>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label fw-bold">Phone</label>
                    <input type="tel" name="phone" class="form-control" placeholder="+39 081 000000"/>
                  </div>
                  <div class="col-12">
                    <label class="form-label fw-bold">Area of interest *</label>
                    <select name="name" class="form-select" required="required">
                      <option value="">Select an area...</option>
                      <option value="Sito web — Consulting">Consulting</option>
                      <option value="Sito web — Software">Software</option>
                      <option value="Sito web — Formazione">Training</option>
                      <option value="Sito web — AI">AI</option>
                      <option value="Sito web — Altro">Other</option>
                    </select>
                  </div>
                  <div class="col-12">
                    <label class="form-label fw-bold">Message *</label>
                    <textarea name="description" class="form-control" rows="5" required="required" placeholder="Tell us about your project or need..."></textarea>
                  </div>
                  <div class="col-12">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" id="privacy" name="check_privacy" required="required"/>
                      <label class="form-check-label" for="privacy">
                        I have read and accept the <a href="/privacy-policy/" target="_blank">Privacy Policy</a> *
                      </label>
                    </div>
                  </div>
                  <div class="col-12 mt-2">
                    <button type="submit" class="btn-dg-accent">Send message</button>
                  </div>
                </div>
              </form>
            </div>
            <div class="col-lg-5">
              <h3>Where to find us</h3>
              <p style="color:var(--dg-slate);">
                Debro S.r.l.<br/>
                Via Miguel Cervantes De Saavedra, 55/5<br/>
                80133 Naples (NA) — Italy
              </p>
              <p class="mt-3">
                <a href="mailto:debro@debro.it" style="color:var(--dg-navy);font-weight:600;">debro@debro.it</a><br/>
                <a href="mailto:debrosrls@debro.it" style="color:var(--dg-navy);font-weight:600;">debrosrls@debro.it</a>
              </p>
              <div class="mt-4" style="border-radius:8px;overflow:hidden;">
                <iframe src="{MAPS_URL}" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </t>
</t>"""

# ══════════════════════════════════════════════════════════
# DEPLOY
# ══════════════════════════════════════════════════════════
PAGE_NAMES = {26: "Consulting", 27: "Software", 28: "Formazione/Training",
              29: "AI", 33: "Contatti/Contact"}

for page_id, arch in PAGES.items():
    print(f"Scrivo EN — {PAGE_NAMES[page_id]} (id={page_id})...", end=" ")
    odoo("website.page", "write",
        ids=[page_id],
        params={"vals": {"arch": arch}},
        context={"lang": "en_GB"})
    print("✓")

print()
print("Tutte le traduzioni EN completate.")
print()
print("Verifica:")
for path in ["/en/consulting/", "/en/software/", "/en/formazione/", "/en/ai/", "/en/contatti/"]:
    print(f"  https://www.debro.it{path}")
