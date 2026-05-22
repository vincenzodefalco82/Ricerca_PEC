import sys
import os
import re
sys.path.insert(0, os.path.dirname(__file__))

from helpers import odoo

# Ripristina contenuto IT come source e aggiunge EN via t-if request.lang.code.
# Necessario perché JSON-2 API Odoo 19 ignora lang context su write di arch
# (sovrascrive sempre il source invece di salvare la traduzione separata).
# Soluzione: arch unico con t-if/t-else per IT e EN, QWeb sceglie al render.

LOGO_BICOCCA     = "/web/image/5216/Universit__degli_Studi_di_Milano-Bicocca-logo-36B841D9FE-seeklogo.com.png"
LOGO_SIELTE      = "/web/image/5212/logo_sielte.png"
LOGO_MET         = "/web/image/5214/met%20italia.png"
LOGO_LEGAMBIENTE = "/web/image/5211/Legambiente_logo.png"
LOGO_UNIPV       = "/web/image/5213/unipv.png"
LOGO_UNIROMA2    = "/web/image/5215/uniroma2.png"
LOGO_BEON        = "/web/image/5217/beon.png"

def load_arch_from_script(script_path, var_name="ARCH"):
    with open(script_path) as f:
        code = f.read()
    safe = code.replace(
        "import sys\nimport os\nsys.path.insert(0, os.path.dirname(__file__))\n\nfrom helpers import odoo\nfrom config import WEBSITE_ID",
        "WEBSITE_ID=1\nodoo=lambda *a,**k:None",
    ).replace(
        "import sys, os\nsys.path.insert(0, os.path.dirname(__file__))\nfrom helpers import odoo\nfrom config import WEBSITE_ID",
        "WEBSITE_ID=1\nodoo=lambda *a,**k:None",
    )
    ns = {"__builtins__": __builtins__, "__file__": script_path}
    exec(compile(safe, script_path, "exec"), ns)
    return ns.get(var_name, "")

def extract_inner(arch):
    m = re.search(r'<div id="wrap"[^>]*>(.*?)</div>\s*</t>\s*</t>', arch, re.DOTALL)
    return m.group(1).strip() if m else arch

def make_bilingual(t_name, inner_it, inner_en):
    return f"""<t t-name="{t_name}">
  <t t-call="website.layout">
    <div id="wrap" class="oe_structure">
      <t t-if="request.lang.code == 'en_GB'">
{inner_en}
      </t>
      <t t-else="">
{inner_it}
      </t>
    </div>
  </t>
</t>"""

base = os.path.dirname(__file__)

# --- HOMEPAGE (view 6486) ---
print("Homepage...")
arch_it_home = load_arch_from_script(os.path.join(base, "05_homepage_v2.py"))
arch_en_home = load_arch_from_script(os.path.join(base, "11b_translate_homepage_en.py"), "ARCH_EN")
merged_home = make_bilingual(
    "custom.page_homepage",
    extract_inner(arch_it_home),
    extract_inner(arch_en_home),
)
odoo("ir.ui.view", "write", ids=[6486], params={"vals": {"arch": merged_home}})
print("  ✓ Homepage")

# --- PAGINE BU (11c ha PAGES dict per id) ---
pages_en_dict = {}
with open(os.path.join(base, "11c_translate_pages_en.py")) as f:
    code = f.read()
safe = code.replace(
    "import sys, os\nsys.path.insert(0, os.path.dirname(__file__))\nfrom helpers import odoo\nfrom config import WEBSITE_ID",
    "WEBSITE_ID=1\nodoo=lambda *a,**k:None",
)
ns_11c = {"__builtins__": __builtins__, "__file__": os.path.join(base, "11c_translate_pages_en.py"), "PAGES": {}}
exec(compile(safe, "11c", "exec"), ns_11c)
pages_en_dict = ns_11c.get("PAGES", {})

bu_pages = [
    (26, os.path.join(base, "06_consulting.py"), 6487, "custom.page_consulting"),
    (27, os.path.join(base, "07_software.py"),   6488, "custom.page_software"),
    (28, os.path.join(base, "08_formazione.py"), 6489, "custom.page_formazione"),
    (29, os.path.join(base, "09_ai.py"),          6490, "custom.page_ai"),
    (33, os.path.join(base, "10_contatti.py"),    6494, "custom.page_contatti"),
]

for page_id, script_it, view_id, t_name in bu_pages:
    print(f"{t_name}...")
    arch_it = load_arch_from_script(script_it)
    arch_en = pages_en_dict.get(page_id, "")
    if not arch_en:
        print(f"  ✗ EN arch mancante per page_id={page_id}")
        continue
    merged = make_bilingual(t_name, extract_inner(arch_it), extract_inner(arch_en))
    odoo("ir.ui.view", "write", ids=[view_id], params={"vals": {"arch": merged}})
    print(f"  ✓ {t_name}")

print("\nTask 14 completato.")
print("IT: /home /consulting/ /software/ /formazione/ /ai/ /contatti/")
print("EN: /en/home /en/consulting/ /en/software/ /en/formazione/ /en/ai/ /en/contatti/")
