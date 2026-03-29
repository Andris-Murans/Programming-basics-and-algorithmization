import json
import os

FILE = "shopping.json"
PRICES_FILE = "prices.json"

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

def load_prices():
    """
    Nolasa cenas no JSON faila. 
    
    Ja fails neeksistē, atgriež tukšu vārdnīcu {}.

    Piemērs:
    >>> load_prices()
    {
        "Maize": 1.20,
        "Piens": 1.50,
        "Sviests": 2.30
    }
    """
    if not os.path.exists(PRICES_FILE):
        return {}

    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_prices(prices):
    """
    Saglabā cenu vārdnīcu JSON failā.

    Parametri:
    prices (dict): vārdnīca ar produktu cenām

    Piemērs:
    >>> save_prices({
        "Maize": 1.20,
        "Piens": 1.50,
        "Sviests": 2.30
    })
    """
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)

def get_price(name):
    """
    Atgriež produkta cenu vai None.

    Funkcija nolasa prices.json failu un mēģina atrast cenu
    pēc produkta nosaukuma.
    
    Parametri:
    name (str): produkta nosaukums

    Atgriež:
    float | None: produkta cena, ja atrasta, citādi None

    Piemēri:
    >>> get_price("Maize")
    1.20

    >>> get_price("Avokado")
    None
    """
    prices = load_prices()
    return prices.get(name)

def set_price(name, price):
    """
    Saglabā vai atjaunina cenu.

    Ja produkts jau eksistē, cena tiek atjaunināta.
    Ja neeksistē — tiek pievienots jauns ieraksts.

    Parametri:
    name(str): produkta nosaukums
    price(float): produkta cena

    Piemēri:
    >>> set_price("Avokado", 1.80)   # pievieno jaunu produktu
    >>> set_price("Maize", 1.20)
    >>> set_price("Maize", 1.35)     # atjaunina esošu cenu
    """
    prices = load_prices()
    prices[name] = price
    save_prices(prices)