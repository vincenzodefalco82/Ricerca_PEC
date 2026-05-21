import requests


def odoo(model, method, args=None, kwargs=None):
    from config import ODOO_URL, API_KEY
    r = requests.post(
        f"{ODOO_URL}/json/2/{model}/{method}",
        headers={
            "Authorization": f"bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={"args": args or [], "kwargs": kwargs or {}},
        timeout=30,
    )
    r.raise_for_status()
    result = r.json()
    if "error" in result:
        raise Exception(f"Odoo error: {result['error']}")
    return result.get("result")
