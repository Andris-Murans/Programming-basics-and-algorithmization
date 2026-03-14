"""
guess.py

Minēšanas spēle:
- Programma ģenerē nejaušu skaitli no 1 līdz 100
- Lietotājam ir 10 mēģinājumi to uzminēt
- Programma pasaka vai minējums ir par lielu vai par mazu
- Kad spēle beidzas, parāda mēģinājumu skaitu un pareizo atbildi
- Spēle var tikt spēlēta atkārtoti
"""

import random

while True: 

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\nEs esmu izvēlējies skaitli no 1 līdz 100.")
    print("Mēģini to uzminēt!")

    while True:
        guess = input("Tavs minējums: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Lūdzu ievadi derīgu skaitli!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Par mazu")
        elif guess > secret_number:
            print("Par lielu")
        else:
            print("Apsveicu! Tu uzminēji skaitli!")
            break

        if attempts >= max_attempts:
            print("Tev beidzās mēģinājumi!")
            break

    print(f"Mēģinājumu skaits: {attempts}")
    print(f"Pareizais skaitlis bija: {secret_number}")

    while True:
        play_again = input("Vai spēlēt vēlreiz? (j/n): ").strip().lower()

        if play_again == "j":
            break
        elif play_again == "n":
            print("Paldies par spēli!")
            exit()
        else:
            print("Lūdzu ievadi tikai j vai n.")
            