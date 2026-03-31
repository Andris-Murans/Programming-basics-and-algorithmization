from storage import load_expenses, save_expenses
from logic import sum_total
from datetime import datetime, date

# Iepriekš definēts kategoriju saraksts
CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"]

def add_expense(expenses):
    """
    Pievieno jaunu izdevumu sarakstam un saglabā to failā.

    Lietotājam tiek prasīts ievadīt:
    - datumu (ar noklusējumu - šodiena),
    - kategoriju (izvēle no saraksta),
    - summu,
    - aprakstu.

    Ja ievade ir nekorekta:
    - kategorijai tiek iestatīta vērtība "Cits"
    - nekorekta summa jautā ievadīt vēlreiz
    - datumu jautā ievadīt vēlreiz

    Args:
        expenses (list): Saraksts ar izdevumu ierakstiem (dict).

    Returns:
        None

    Examples:
        (Interaktīva funkcija — piemērs izskatās šādi:)

        Datums (YYYY-MM-DD) [2026-03-31]: 
        Izvēlies kategoriju:
        1) Ēdiens
        2) Transports
        3) Izklaide
        4) Komunālie maksājumi
        5) Veselība
        6) Iepirkšanās
        7) Cits
        Izvēlies (1-7): 1
        Summa (EUR): 12.50
        Apraksts: Pusdienas

        Pievienots: 2026-03-31 | Ēdiens | 12.50 EUR
    """

    print("\n" + "═" * 4 + " Pievienot jaunu izdevumu " + "═" * 4)

    # 1. Datums (noklusējums = šodiena)
    today = date.today().strftime("%Y-%m-%d")
    while True:
        date_input = input(f"Datums (YYYY-MM-DD) [{today}]: ").strip()

        if not date_input:
            date_input = today

        try:
            # pārbauda vai datums ir pareizs
            datetime.strptime(date_input, "%Y-%m-%d")
            break  # ja pareizs → iziet no cikla

        except ValueError:
            print("Nepareizs datums! Lūdzu ievadi formātā YYYY-MM-DD.")

    # 2. Kategorijas izvēle
    print("Izvēlies kategoriju:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    while True:
        try:
            cat_index = int(input(f"Izvēlies (1-{len(CATEGORIES)}): ").strip()) - 1
            category = CATEGORIES[cat_index]
            break
        except (ValueError, IndexError):
            print("Nederīga izvēle, mēģini vēlreiz.")

    # 3. Summas ievade un validācija
    while True:
        try:
            amount = float(input("Summa (EUR): ").strip())

            if amount <= 0:
                print("Summai jābūt lielākai par 0!")
                continue

            break  # pareiza ievade → iziet no cikla

        except ValueError:
            print("Lūdzu ievadi skaitli (piemēram: 12.50)")

    # 4. Apraksts
    while True:
        description = input("Apraksts: ").strip()
        if description:
            break
        print("Apraksts nevar būt tukšs!")

    # 5. Izveido jaunu ierakstu
    new_expense = {
        "date": date_input,
        "amount": round(amount, 2),
        "category": category,
        "description": description
    }

    # 6. Pievieno sarakstam un saglabā
    expenses.append(new_expense)
    save_expenses(expenses)

    print(f"✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")

def show_expenses(expenses):
    """
    Izvada izdevumus tabulā ar automātiski aprēķinātiem kolonnu platumiem.

    Args:
        expenses (list): Saraksts ar izdevumu ierakstiem (dict).

    Returns:
        None
    """

    if not expenses:
        print("\nSaraksts ir tukšs.")
        return

    # 1. Nosakām maksimālos platumus
    date_width = max(len("Datums"), max(len(exp["date"]) for exp in expenses))
    category_width = max(len("Kategorija"), max(len(exp["category"]) for exp in expenses))
    desc_width = max(len("Apraksts"), max(len(exp["description"]) for exp in expenses))

    # Summai ņemam formatētu garumu (piemēram: "12345.67 EUR")
    amount_width = max(len("Summa"), max(len(f"{exp['amount']:.2f} EUR") for exp in expenses))

     # Kopējā līnijas platuma aprēķins
    total_width = date_width + amount_width + category_width + desc_width + 9
    sep = "  "  # atstarpe starp kolonnām


    # 2. Virsraksts
    print("\n" + "=" * total_width)
    print(
        f"{'Datums':<{date_width}}{sep}"
        f"{'Summa':>{amount_width}}{sep}" 
        f"{'Kategorija':<{category_width}}{sep}"
        f"{'Apraksts':<{desc_width}}{sep}"
        )
    print("-" * total_width)

    # 3. Dati
    for exp in expenses:
        print(
            f"{exp['date']:<{date_width}}  "
            f"{exp['amount']:>{amount_width - 4}.2f} EUR  "
            f"{exp['category']:<{category_width}}  "
            f"{exp['description']:<{desc_width}}"
        )

    total = sum_total(expenses)

    # 4. Kopsumma
    print("-" * total_width)
    print(f"{'KOPĀ:':<{date_width}} {total:>{amount_width - 4}.2f} EUR ({len(expenses)} ieraksti)")

    print("=" * total_width)

def show_menu():
    
        print("\n════ Izdevumu izsekotājs ════")
        print("1) Pievienot izdevumu")
        print("2) Parādīt visus izdevumus")
        print("7) Iziet")

        return input("\nIzvēlies darbību (1, 2 vai 7): ")


def main():
    """
    Galvenā programmas funkcija (entry point).

    Ielādē izdevumus no faila un nodrošina lietotāja izvēlnes saskarni.

    Lietotājs var:
    - pievienot jaunu izdevumu
    - apskatīt visus izdevumus
    - iziet no programmas

    Dati tiek saglabāti un atjaunināti visas programmas darbības laikā.

    Returns:
        None

    Examples:
        Programmas palaišana:

        >>> main()

        ════ Izdevumu izsekotājs ════
        1) Pievienot izdevumu
        2) Parādīt visus izdevumus
        7) Iziet

        Izvēlies darbību (1, 2 vai 7):
    """

    # Ielādē datus startējot
    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "7":
            print("Uz redzēšanos!")
            break

        else:
            print("Nepareiza izvēle, mēģini vēlreiz.") 


if __name__ == "__main__":
    main()