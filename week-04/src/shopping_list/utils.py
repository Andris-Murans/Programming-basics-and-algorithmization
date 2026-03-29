def calc_line_total(item):
    """
    Aprēķina vienas rindas summu (qty × price)

    Parametri:
    item (dict): produkts ar laukiem 'qty' un 'price'

    Atgriež:
    float
    """
    qty = item.get("qty", 1)
    price = item.get("price", 0)
    return qty * price


def calc_grand_total(items):
    """
    Aprēķina kopējo summu visiem produktiem.

    Parametri:
    items (list): produktu saraksts

    Atgriež:
    float
    """
    return sum(calc_line_total(item) for item in items)


def count_units(items):
    """
    Saskaita kopējo vienību skaitu.

    Parametri:
    items (list): produktu saraksts

    Atgriež:
    int
    """
    return sum(item.get("qty", 1) for item in items)