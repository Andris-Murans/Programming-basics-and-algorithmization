def sum_total(expenses):
    """
    Aprēķina visu sarakstā esošo izdevumu kopējo summu.
    
    Args:
    expenses (list): saraksts ar izdevumu vārdnīcām
    
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
    total = 0
    for expense in expenses:
        # Pieskaitām katra izdevuma summu kopējam mainīgajam
        total += expense["amount"]
    
    # Atgriežam noapaļotu rezultātu, lai izvairītos no float precizitātes kļūdām 
    return round(total, 2)