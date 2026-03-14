"""
guess.py

Minēšanas spēle:
- Ģenerē nejaušu skaitli no 1 līdz 100
- Ir 10 mēģinājumi to uzminēt
- Dod padomu vai par lielu vai par mazu
- Spēles beigās parāda mēģinājumu skaitu un pareizo atbildi
- Spēle var tikt spēlēta atkārtoti
"""

import random   # bibliotēka, kas ļauj ģenerēt nejaušus skaitļus

# =======================
# Galvenais spēles cikls
# =======================

while True: 

    # ģenerē nejaušu skaitli no 1 līdz 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\nEs esmu izvēlējies skaitli no 1 līdz 100.")
    print("Mēģini to uzminēt!")

    # ===============
    # Minējumu cikls
    # ===============

    while True:
        guess = input("Tavs minējums: ")

        # pārbauda vai ievade ir skaitlis
        try:
            guess = int(guess)
        except ValueError:
            print("Lūdzu ievadi derīgu skaitli!")
            continue    # atgriežas cikla sākumā

        attempts += 1

        # pārbauda minējumu
        if guess < secret_number:
            print("Par mazu")
        elif guess > secret_number:
            print("Par lielu")
        else:
            print("Apsveicu! Tu uzminēji skaitli!")
            break
        
        # ja mēģinājumu skaits sasniedz 10
        if attempts >= max_attempts:
            print("Tev beidzās mēģinājumi!")
            break
    
    # parāda rezultātu
    print(f"Mēģinājumu skaits: {attempts}")
    print(f"Pareizais skaitlis bija: {secret_number}")

    # =========================
    # Play again ievades cikls
    # =========================

    while True:
        # jautā lietotājam vai spēlēt vēlreiz
        play_again = input("Vai spēlēt vēlreiz? (j/n): ").strip().lower()

        # ja ievada "j" → sāk jaunu spēli
        if play_again == "j":
            break   # iziet no šī validācijas cikla un turpina spēli
        # ja ievada "n" → beidz spēli
        elif play_again == "n":
            print("Paldies par spēli!")
            exit()  # pilnībā iziet no programmas
        # ja ievada kaut ko citu → paziņojums un atkārto jautājumu
        else:
            print("Lūdzu ievadi tikai j vai n.")
            