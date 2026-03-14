# converter.py

# -----------------------------------
# 1. Definējam konversijas konstantes
# -----------------------------------
# Konstantes raksta ar LIELAJIEM BURTIEM.
# Tās ir vērtības, kuras programmā nemainās.

KM_TO_MI = 0.621371      # 1 kilometrs = 0.621371 jūdzes
KG_TO_LB = 2.20462       # 1 kilograms = 2.20462 mārciņas
L_TO_GAL = 0.264172      # 1 litrs = 0.264172 galoni
USD_TO_EUR = 0.84235020  # 1 dolārs = 0.84235020 eiro

# ------------------------------
# 2. Parādām lietotājam izvēlni
# ------------------------------
print("Izvēlies konversiju:")
print("1) km <-> mi")       # no km uz jūdzēm
print("2) kg <-> lb")       # no kg uz mārciņām
print("3) L <-> gal")       # no litriem uz galoniem
print("4) $ <-> €")         # no dolāriem uz eiro

# input() nolasa lietotāja ievadi no tastatūras
choice = input("> ")

# ------------------
# 3. Kļūdu apstrāde
# ------------------
# try nozīmē – mēģini izpildīt kodu
# ja rodas kļūda (piemēram, ievadīts teksts skaitļa vietā),
# tad tiks izpildīts except bloks

try:

    # ---------------------------------------------
    # 4. Ja lietotājs izvēlas kilometrus un jūdzes
    # ---------------------------------------------
    if choice == "1":

        print("Virziens: 1) km -> mi  2) mi -> km")
        direction = input("> ")     # izvēlas virzienu konversijai
                                    # no km uz jūdzēm vai otrādi
        # float() pārvērš ievadīto tekstu par decimālskaitli
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            # km -> mi
            result = value * KM_TO_MI
            # Izvades formatēšana izmantojot f-string ar divām zīmēm aiz komata
            # :.2f nozīmē 2 cipari aiz komata
            print(f"{value:.2f} km = {result:.2f} mi")

        elif direction == "2":
            # mi -> km
            result = value / KM_TO_MI
            print(f"{value:.2f} mi = {result:.2f} km")

        else:
            print("Nepareizs virziens!")

    # -------------------------
    # 5. Kilogrami un mārciņas
    # -------------------------
    elif choice == "2":

        print("Virziens: 1) kg -> lb  2) lb -> kg")
        direction = input("> ")
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * KG_TO_LB
            print(f"{value:.2f} kg = {result:.2f} lb")

        elif direction == "2":
            result = value / KG_TO_LB
            print(f"{value:.2f} lb = {result:.2f} kg")

        else:
            print("Nepareizs virziens!")

    # -------------------
    # 6. Litri un galoni
    # -------------------
    elif choice == "3":

        print("Virziens: 1) L -> gal  2) gal -> L")
        direction = input("> ")
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * L_TO_GAL
            print(f"{value:.2f} L = {result:.2f} gal")

        elif direction == "2":
            result = value / L_TO_GAL
            print(f"{value:.2f} gal = {result:.2f} L")

        else:
            print("Nepareizs virziens!")

    # ------------------
    # 7. Dolāri un eiro
    # ------------------
    elif choice == "4":

        print("Virziens: 1) $ -> €  2) € -> $")
        direction = input("> ")
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * USD_TO_EUR
            print(f"{value:.2f} $ = {result:.2f} €")

        elif direction == "2":
            result = value / USD_TO_EUR
            print(f"{value:.2f} € = {result:.2f} $")

        else:
            print("Nepareizs virziens!")

    # -------------------------
    # 8. Ja izvēle nav pareiza
    # -------------------------
    else:
        print("Nepareiza izvēle!")

# -----------------------------------
# 9. Kļūdas paziņojums
# -----------------------------------
# Ja lietotājs ievada tekstu skaitļa vietā,
# piemēram: "abc", tad float() izraisīs ValueError
# un tiks izpildīts šis bloks

except ValueError:
    print("Kļūda: jāievada skaitlis.")
