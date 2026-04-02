import json
import os

# Nosaka mapes ceļu, kur atrodas šis Python fails
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Izveido pilnu ceļu uz JSON failu (droši strādā jebkurā vidē)
FILE = os.path.join(BASE_DIR, "expenses.json")

def load_expenses():
    """
    Nolasa izdevumus no JSON faila.

    Ja fails neeksistē, ir tukšs vai bojāts, tiek izveidots tukšs fails
    un atgriezts tukšs saraksts.

    Returns:
        list: Saraksts ar izdevumu ierakstiem (dict).

    Example:
    >>> load_expenses()
    [
        {
            "date": "2025-02-15",
            "amount": 12.50,
            "category": "Ēdiens",
            "description": "Pusdienas kafejnīcā"
        }
    ]
    """
    # Ja fails vēl neeksistē, izveido tukšu failu un atgriež tukšu sarakstu
    if not os.path.exists(FILE):
        save_expenses([])
        return []
    try:
        # Atver failu ar utf-8-sig, lai būtu saderība ar Excel
        with open(FILE, "r", encoding="utf-8-sig") as f:
            
            # Ielādē JSON datus Python struktūrā
            data = json.load(f)

            # Pārliecinās, ka dati ir saraksts (drošībai)
            if isinstance(data, list):
                return data
            else:
                return []

    # Ja fails ir bojāts vai rodas lasīšanas kļūda
    except (json.JSONDecodeError, OSError):
        return []

def save_expenses(items):
    """
    Saglabā izdevumu sarakstu JSON failā ar atkāpēm un LV simbboliem.

    Args:
        items (list): Saraksts ar izdevumu ierakstiem.
            Katrs ieraksts ir vārdnīca ar laukiem:
            - date (str): Datums formātā YYYY-MM-DD
            - amount (float): Summa
            - category (str): Izdevumu kategorija
            - description (str): Apraksts
    
    Raises:
        OSError: Ja rodas kļūda rakstot failā.

    Example:
    >>> save_expenses([
            {
                "date": "2025-02-15",
                "amount": 12.50,
                "category": "Ēdiens",
                "description": "Pusdienas kafejnīcā"
            }
        ])
    """
    try:
        # Atver failu rakstīšanai (pārraksta visu saturu)
        with open(FILE, "w", encoding="utf-8-sig") as f:
            
            # Saglabā datus JSON formātā:
            # indent=2 → skaists, salasāms formāts
            # ensure_ascii=False → saglabā latviešu simbolus
            json.dump(items, f, indent=2, ensure_ascii=False)

    # Ja rodas kļūda saglabājot failu
    except OSError as e:
        print(f"Kļūda saglabājot datus: {e}")