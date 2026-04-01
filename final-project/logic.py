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
