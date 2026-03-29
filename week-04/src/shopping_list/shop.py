import sys
from storage import load_list, save_list, get_price, set_price
import utils

def add_product(name, qty, price):
    """
    Pievieno jaunu produktu un saglabā to failā.

    Parametri:
    name (str): produkta nosaukums
    qty (int): daudzums
    price (float): produkta cena

    Piemērs:
    >>> add_product("Maize", 3, 1.20)
    """
    products = load_list()

    

    item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    products.append(item)
    save_list(products)

    total = utils.calc_line_total(item)

    print(f"✓ Pievienots: {name} x {qty} ({price:.2f} EUR/gab.) = {total:.2f} EUR")

def list_products():
    """
    Izvada visus produktus uz ekrāna ar daudzumu un kopējo cenu.

    Piemērs:
    >>> list_products()
    Iepirkumu saraksts:
      1. Maize x 3 - 1.20 EUR/gab. - 3.60 EUR
      2. Piens x 2 - 1.50 EUR/gab. - 3.00 EUR
    """
    products = load_list()

    # Ja nav neviena produkta
    if not products:
        print("Iepirkumu saraksts ir tukšs")
        return

    print("\nIepirkumu saraksts:")

    for i, product in enumerate(products, start=1):

        qty = product.get('qty', 1)
        price = product.get('price', 0)

        total = utils.calc_line_total(product)

        print(f"  {i}. {product['name']} x {qty} — {price:.2f} EUR/gab. - {total:.2f} EUR")

def total_products():
    """
    Aprēķina un izvada kopējo summu, vienību skaitu un produktu skaitu.

    Izvade:
    Kopā: 6.60 EUR (5 vienības, 2 produkti)
    """
    products = load_list()

    # p.get("price", 0): Katram produktam p tiek meklēta vērtība pie atslēgas "price". 
    # Ja cena nav norādīta, funkcija .get() atgriež 0, lai kods "nenobruktu" kļūdas (KeyError) dēļ.
    total_price = utils.calc_grand_total(products)
    total_qty = utils.count_units(products)

    print(f"Kopā: {total_price:.2f} EUR ({total_qty} vienības, {len(products)} produkti)")

def clear_products():
    """
    Izdzēš visus produktus no iepirkumu saraksta.

    Funkcija pārraksta failu ar tukšu sarakstu [] un izvada apstiprinājumu.

    Izvade:
    ✓ Saraksts iztukšots
    """
    save_list([])
    print("✓ Saraksts iztukšots")

def main():
    # ---------------------
    # 1. Komandas pārbaude
    # ---------------------
    if len(sys.argv) < 2:
        print("Kļūda: nav komandas")
        print("\nIespējamās komandas: add, list, total, clear")
        print("  add    - pievieno produktu")
        print("  list   - parāda visus produktus")
        print("  total - parāda kopējo produktu skaitu un summu")
        print("  clear - notīra visu sarakstu")
        return

    command = sys.argv[1].lower()

    # ---------------
    # 2. ADD komanda
    # ---------------
    if command == "add":

        # Ja nav argumentu, lieto input()
        if len(sys.argv) < 4:
            print("\nIevadi produktu:")

            name = input("Nosaukums: ").strip()
            qty = input("Daudzums: ").strip()
                    
        else:
            name = sys.argv[2]
            qty = sys.argv[3]
                    
        # -------- VALIDĀCIJA --------
        # Nosaukums
        while not name.strip(): # .strip() lai novērstu tukšas atstarpes
            print("Kļūda: nosaukums nevar būt tukšs")
            name = input("Ievadi nosaukumu vēlreiz: ").strip()
        
        # Daudzums
        while True:
            try:
                qty = int(qty)

                if qty <= 0:
                    print("Kļūda: daudzumam jābūt lielākam par 0")
                    qty = input("Ievadi daudzumu vēlreiz: ").strip()
                    continue
                break
            except ValueError:
                print("Kļūda: daudzumam jābūt veselam skaitlim")
                qty = input("Ievadi daudzumu vēlreiz: ").strip()

        # Cena
        price = get_price(name)

        if price is not None:
            print(f"Atrasta cena: {price:.2f} EUR/gab.")
            
            while True:
                choice = input("[A]kceptēt / [M]ainīt? ").strip().lower()

                if choice == "a":
                    break

                elif choice == "m":
                    while True:
                        try:
                            price = float(input("Jaunā cena: ").strip())
                            if price <= 0:
                                print("Kļūda: cenai jābūt > 0")
                                continue

                            set_price(name, price)
                            print(f"✓ Cena atjaunināta: {name} ({price:.2f} EUR)")
                            break
                        except ValueError:
                            print("Kļūda: ievadi skaitli")

                    break

                else:
                    print("Ievadi tikai A vai M")

        else:
            print("Cena nav zināma.")

            while True:
                try:
                    price = float(input("Ievadi cenu: ").strip())
                    if price <= 0:
                        print("Kļūda: cenai jābūt > 0")
                        continue

                    set_price(name, price)
                    print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")
                    break
                except ValueError:
                    print("Kļūda: ievadi skaitli")
            
        add_product(name, qty, price)

    # ----------------
    # 3. LIST komanda
    # ----------------
    elif command == "list":
        list_products()

    # -----------------
    # 4. TOTAL komanda
    # -----------------
    elif command == "total":
        total_products()

    # -----------------
    # 5. CLEAR komanda
    # -----------------
    elif command == "clear":
        clear_products()

    # --------------------
    # 5. Nezināma komanda
    # --------------------
    else:
        print("Nezināma komanda")
        print("Pieejamās komandas: add, list, total, clear")

if __name__ == "__main__":
    main()