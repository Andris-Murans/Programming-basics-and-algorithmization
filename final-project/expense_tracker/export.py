import csv
import os

# Nosaka mapes ceļu, kur atrodas šis Python fails
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CSV kolonnu nosaukumi jeb galvene
HEADERS = ["Datums", "Summa", "Kategorija", "Apraksts"]

def export_to_csv(expenses, filename="izdevumi.csv"):
    """
    Eksportē izdevumus CSV failā ar utf-8-sig kodējumu.

    Args:
        expenses (list): Saraksts ar izdevumiem.
        filename (str): Faila nosaukums.

    Returns:
        bool: True, ja veiksmīgi, False ja kļūda.
    """

    # Ja nav datu, nav ko eksportēt
    if not expenses:
        print("Nav datu eksportēšanai.")
        return False
    
    # Izveido pilnu ceļu, izmantojot lietotāja sniegto nosaukumu
    filepath = os.path.join(BASE_DIR, filename)

    try:
        # utf-8-sig nodrošina, ka Excel pareizi rāda latviešu burtus
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)

            # Ieraksta galveni
            writer.writerow(HEADERS)

            # Ieraksta datus
            for exp in expenses:
                writer.writerow([
                    exp.get("date", ""),
                    f"{exp.get('amount', 0):.2f}",  # Formatē summu ar 2 zīmēm aiz komata
                    exp.get("category", ""),
                    exp.get("description", "")
                ])

        print(f"✓ Eksportēts uz: {filepath}")
        return True

    except Exception as e:
        print(f"Kļūda eksportējot failu '{filename}': {e}")
        return False