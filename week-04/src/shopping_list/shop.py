import sys
from storage import load_list, save_list


def add_product(name, price):
    """
    Pievieno jaunu produktu un saglabā to failā.

    Parametri:
    name (str): produkta nosaukums
    price (float): produkta cena

    Piemērs:
    >>> add_product("Maize", "1.20")
    """
    products = load_list()

    products.append({
        "name": name,
        "price": price
    })

    save_list(products)

    print(f"✓ Pievienots: {name} ({price:.2f} EUR)")

def list_products():
    """
    Izvada visus produktus uz ekrāna.

    Piemērs:
    >>> list_products()
    1. Maize - 1.20 EUR
    2. Piens - 1.50 EUR
    """
    products = load_list()

    # Ja nav neviena produkta
    if not products:
        print("Iepirkumu saraksts ir tukšs")
        return

    print("\nIepirkumu saraksts:")

    for i, product in enumerate(products, start=1):
        print(f"  {i}. {product['name']} — {product['price']:.2f} EUR")

def total_products():
    """
    Aprēķina un izvada kopējo summu un produktu skaitu.

    Funkcija nolasa produktus no faila, summē visu produktu cenas
    un izvada rezultātu.

    Izvade:
    Kopā: 2.70 EUR (2 produkti)
    """
    products = load_list()

    # p.get("price", 0): Katram produktam p tiek meklēta vērtība pie atslēgas "price". 
    # Ja cena nav norādīta, funkcija .get() atgriež 0, lai kods "nenobruktu" kļūdas (KeyError) dēļ.
    total = sum(p.get("price", 0) for p in products)

    print(f"Kopā: {total:.2f} EUR ({len(products)} produkti)")

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
            price = input("Cena: ").strip()
        
        else:
            name = sys.argv[2]
            price = sys.argv[3]
        
        # -------- VALIDĀCIJA --------
        # tukšs nosaukums
        while not name.strip(): # .strip() lai novērstu tukšas atstarpes
            print("Kļūda: nosaukums nevar būt tukšs")
            name = input("Ievadi nosaukumu vēlreiz: ").strip()
        
        # tukša cena
        while True:
            try:
                price = float(price)

                if price <= 0:
                    print("Kļūda: cenai jābūt lielākai par 0")
                    price = input("Ievadi cenu vēlreiz: ").strip()
                    continue
                break
            except ValueError:
                print("Kļūda: cenai jābūt skaitlim")
                price = input("Ievadi cenu vēlreiz: ").strip()
        
        add_product(name, price)

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