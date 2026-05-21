import requests


def odoo(model, method, ids=(), params=None, context=None):
    """
    JSON-2 Odoo 19 — formato flat: tutti i parametri nel body direttamente.
    ids: lista di ID record (per metodi su recordset)
    params: dict di keyword arguments passati al metodo (es. domain, fields, limit)
    context: dict opzionale
    """
    from config import ODOO_URL, API_KEY
    body = dict(params or {})
    if ids:
        body["ids"] = list(ids)
    if context:
        body["context"] = context
    r = requests.post(
        f"{ODOO_URL}/json/2/{model}/{method}",
        headers={
            "Authorization": f"bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=30,
    )
    r.raise_for_status()
    result = r.json()
    # JSON-2 Odoo 19: risposta diretta (no wrapper {"result": ...})
    if isinstance(result, dict) and "name" in result and "message" in result:
        raise Exception(f"Odoo error [{result['name']}]: {result['message']}")
    return result
