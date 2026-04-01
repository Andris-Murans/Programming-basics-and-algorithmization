from datetime import datetime

def sum_total(expenses):
    """
    Aprēķina visu sarakstā esošo izdevumu kopējo summu.
    
    Args:
    expenses (list): saraksts ar izdevumu ierakstiem (dict)
    
    Returns:
    float: noapaļota kopsumma (2 zīmes aiz komata)

    Examples:
    >>> sum_total([
            {
                "date": "2025-02-15",
                "amount": 12.50,
                "category": "Ēdiens",
                "description": "Pusdienas kafejnīcā"
            },
            {
                "date": "2025-02-16",
                "amount": 7.25,
                "category": "Transports",
                "description": "Autobusa biļete"
            }
        ])
    19.75
    """
    total = 0   # Mainīgais kopējās summas uzkrāšanai
    for expense in expenses:
        # Pieskaita katra izdevuma "amount" vērtību kopējai summai
        total += expense["amount"]
    
    # Atgriežam noapaļotu rezultātu, lai izvairītos no float precizitātes kļūdām 
    return round(total, 2)

def filter_by_month(expenses, year, month):
    """
    Atgriež izdevumus, kas atbilst norādītajam gadam un mēnesim.

    Args:
        expenses (list): Saraksts ar izdevumu ierakstiem (dict).
        year (int): Gads (piemēram, 2026).
        month (int): Mēnesis (1–12).

    Returns:
        list: Saraksts ar filtrētajiem izdevumiem.

    Examples:
        >>> filter_by_month([
                {"date": "2026-03-31", "amount": 12.50, "category": "Ēdiens", "description": "Pusdienas"},
                {"date": "2026-02-15", "amount": 5.00, "category": "Transports", "description": "Biļete"}
            ], 2026, 3)
        [{'date': '2026-03-31', 'amount': 12.5, 'category': 'Ēdiens', 'description': 'Pusdienas'}]
    """
    result = []     # Saraksts filtrētajiem rezultātiem
    for expense in expenses:
        # Pārvērš datuma tekstu (string) par datetime objektu
        d = datetime.strptime(expense["date"], "%Y-%m-%d")

        # Pārbauda vai gads un mēnesis sakrīt ar meklēto
        if d.year == year and d.month == month:
            # Ja sakrīt → pievieno rezultātu sarakstam
            result.append(expense)

    # Atgriež visus atbilstošos izdevumus
    return result

def sum_by_category(expenses):
    """
    Aprēķina kopējo izdevumu summu katrai kategorijai.

    Args:
        expenses (list): Saraksts ar izdevumu ierakstiem (dict).

    Returns:
        dict: Vārdnīca ar formātu {kategorija: summa}.

    Examples:
        >>> sum_by_category([
                {"date": "2026-03-31", "amount": 10.00, "category": "Ēdiens", "description": ""},
                {"date": "2026-03-31", "amount": 5.00, "category": "Ēdiens", "description": ""},
                {"date": "2026-03-31", "amount": 7.00, "category": "Transports", "description": ""}
            ])
        {'Ēdiens': 15.0, 'Transports': 7.0}
    """
    totals = {}     # Vārdnīca, kur glabās summas pa kategorijām
    for expense in expenses:
        # Paņem kategoriju no ieraksta
        cat = expense["category"]

        # Pieskaita summu attiecīgajai kategorijai
        # ja kategorija vēl neeksistē, sāk ar 0
        totals[cat] = totals.get(cat, 0) + expense["amount"]

    # Izveido jaunu vārdnīcu ar noapaļotām vērtībām (2 zīmes aiz komata)
    return {cat: round(total, 2) for cat, total in totals.items()}

def get_available_months(expenses):
    """
    Atrod visus unikālos mēnešus (YYYY-MM), kuros ir reģistrēti izdevumi.

    Args:
        expenses (list): Saraksts ar izdevumu ierakstiem (dict).

    Returns:
        list: Sakārtots saraksts ar unikālām mēnešu virknēm, piemēram, ["2025-01", "2025-02"].
    
    Examples:
        >>> get_available_months([
                {"date": "2025-02-15", "amount": 10.0, "category": "Ēdiens"},
                {"date": "2025-01-10", "amount": 5.0, "category": "Transports"},
                {"date": "2025-02-20", "amount": 15.0, "category": "Izklaide"}
            ])
        ['2025-01', '2025-02']
    """
    # Izmantojam 'set' (kopu), lai automātiski atlasītu tikai unikālas vērtības
    months = set()
    
    for expense in expenses:
        # No datuma stringa paņem tikai gadu un mēnesi (YYYY-MM)
        # piemērs: "2025-02-15" -> "2025-02"
        month_str = expense["date"][:7]

        # Pievieno kopai (set nepieļauj dublikātus)
        months.add(month_str)
    
    # Sakārto mēnešus augošā secībā un pārvērš par sarakstu
    return sorted(months)