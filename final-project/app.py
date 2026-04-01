from storage import load_expenses, save_expenses
import logic
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

        ✓ Pievienots: 2026-03-31 | Ēdiens | 12.50 EUR | Pusdienas
    """

    print("\n" + "═" * 4 + " Pievienot jaunu izdevumu " + "═" * 4)

    # 1. Datums (noklusējums = šodiena)
    today = date.today().strftime("%Y-%m-%d")
    while True:
        # Lietotājs ievada datumu (vai nospiež Enter -> tiek izmantots today)
        date_input = input(f"Datums (YYYY-MM-DD) [{today}]: ").strip()

        if not date_input:
            date_input = today  # tukša ievade -> šodienas datums

        try:
            # Mēģina pārveidot tekstu uz datetime objektu (validācija)
            datetime.strptime(date_input, "%Y-%m-%d")
            break  # ja datums derīgs -> iziet no cikla

        except ValueError:
            # Ja datums nepareizs -> prasa ievadīt vēlreiz
            print("Nepareizs datums! Lūdzu ievadi formātā YYYY-MM-DD.")

    # 2. Kategorijas izvēle
    print("Izvēlies kategoriju:")

    # Izvada visas kategorijas ar numuriem
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    while True:
        try:
            # Lietotājs ievada skaitli -> pārvērš indeksā
            cat_index = int(input(f"Izvēlies (1-{len(CATEGORIES)}): ").strip()) - 1
            category = CATEGORIES[cat_index]    # paņem izvēlēto kategoriju
            break
        except (ValueError, IndexError):
            # Ja ievade nav derīga -> atkārto
            print("Nederīga izvēle, mēģini vēlreiz.")

    # 3. Summas ievade un validācija
    while True:
        try:
            # Pārvērš ievadi uz float
            amount = float(input("Summa (EUR): ").strip())

             # Pārbauda vai summa ir pozitīva
            if amount <= 0:
                print("Summai jābūt lielākai par 0!")
                continue

            break  # pareiza ievade -> iziet no cikla

        except ValueError:
            # Ja nav skaitlis -> kļūdas ziņojums
            print("Lūdzu ievadi skaitli (piemēram: 12.50)")

    # 4. Apraksts (neļauj tukšu)
    while True:
        description = input("Apraksts: ").strip()
        if description:
            break   # ja nav tukšs -> OK
        print("Apraksts nevar būt tukšs!")

    # 5. Izveido jaunu izdevuma ierakstu (dict)
    new_expense = {
        "date": date_input,
        "amount": round(amount, 2),     # noapaļo naudas vērtību
        "category": category,
        "description": description
    }

    # 6. Pievieno sarakstam un saglabā failā
    expenses.append(new_expense)
    save_expenses(expenses)

    # Apstiprinājuma ziņojums lietotājam
    print(f"✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")

def show_expenses(expenses):
    """
    Izvada izdevumus tabulā ar automātiski aprēķinātiem kolonnu platumiem.

    Args:
        expenses (list): Saraksts ar izdevumu ierakstiem (dict).

    Returns:
        None
    """

    # Ja nav datu -> informē lietotāju
    if not expenses:
        print("\nSaraksts ir tukšs.")
        return

    # 1. Aprēķina katras kolonnas platumu (lai viss būtu izlīdzināts)
    date_width = max(len("Datums"), max(len(exp["date"]) for exp in expenses))
    category_width = max(len("Kategorija"), max(len(exp["category"]) for exp in expenses))
    desc_width = max(len("Apraksts"), max(len(exp["description"]) for exp in expenses))

    # Summai ņemam formatētu garumu (piemēram: "12345.67 EUR")
    amount_width = max(len("Summa"), max(len(f"{exp['amount']:.2f} EUR") for exp in expenses))

    # Kopējais tabulas platums
    total_width = date_width + amount_width + category_width + desc_width + 9

    # atstarpe starp kolonnām
    sep = "  "

    # 2. Virsraksts
    print("\n" + "=" * total_width)

    # Kolonnu nosaukumi ar izlīdzināšanu
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

    # Aprēķina kopējo summu
    total = sum_total(expenses)

    # 4. Kopsumma
    print("-" * total_width)
    print(f"{'KOPĀ:':<{date_width}} {total:>{amount_width - 4}.2f} EUR ({len(expenses)} ieraksti)")

    print("=" * total_width)

def show_menu():
        # Izvada galveno izvēlni
        print("\n════ Izdevumu izsekotājs ════")
        print("1) Pievienot izdevumu")
        print("2) Parādīt visus izdevumus")
        print("3) Filtrēt pēc mēneša")
        print("4) Kopsavilkums pa kategorijām")
        print("5) Dzēst izdevumu")
        print("7) Iziet")

        # Atgriež lietotāja izvēli
        return input("\nIzvēlies darbību (1, 2, 3, 4, 5 vai 7): ")


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

    # Ielādē izdevumus no faila
    expenses = load_expenses()

    # Programmas galvenais cikls
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)
        
        elif choice == "3":
            print("\n════ Filtrēt pēc mēneša ════")

            # 1. Dabū pieejamos mēnešus
            months = logic.get_available_months(expenses)

            # Ja saraksts tukšs -> izvada paziņojumu
            if not months:
                print("Nav datu.")
                continue

            # 2. Izvada mēnešu sarakstu
            print("\nPieejamie mēneši:")
            for i, m in enumerate(months, 1):
                print(f"  {i}) {m}")

            # 3. Lietotāja izvēle (atkārto līdz pareizi)
            while True:
                try:
                    index = int(input("Izvēlies mēnesi: > ")) - 1
                    selected = months[index]
                    break  # ja viss OK -> iziet no cikla

                except (ValueError, IndexError):
                    print("Nepareiza izvēle! Mēģini vēlreiz.")

            # 4. Sadala gadu un mēnesi
            year, month = map(int, selected.split("-"))

            # 5. Filtrē datus
            filtered = logic.filter_by_month(expenses, year, month)

            # 6. Ja nav rezultātu
            if not filtered:
                print("Nav ierakstu šajā mēnesī.")
                continue

            # 7. Izvade
            print(f"\n{selected} izdevumi:")

            for exp in filtered:
                print(f"{exp['date']} | {exp['amount']:>6.2f} EUR | {exp['category']:<10} | {exp['description']}")

            # 8. Kopsumma
            total = logic.sum_total(filtered)
            print(f"Kopā: {total:.2f} EUR ({len(filtered)} ieraksti)")

        elif choice == "7":
            print("Uz redzēšanos!")
            break

        else:
            # Ja ievade nav derīga
            print("Nepareiza izvēle, mēģini vēlreiz.") 

# Programmas starta punkts
if __name__ == "__main__":
    main()