import json
import os

FILE = "shopping.json"

def load_list():
    """
    Nolasa produktus no JSON faila.

    Ja fails neeksistē, atgriež tukšu sarakstu [].

    Piemērs:
    >>> load_list()
    [{"name": "Maize", "price": 1.20}]
    """
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    """
    Saglabā produktu sarakstu JSON failā.

    Parametri:
    items (list): saraksts ar produktiem

    Piemērs:
    >>> save_list([{"name": "Maize", "price": 1.20}])
    """
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)