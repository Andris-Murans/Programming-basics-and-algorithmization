"""
fizzbuzz.py

Programma:
- pieņem skaitli N no komandrindas (sys.argv)
- izvada skaitļus no 1 līdz N
- Fizz ja dalās ar 3
- Buzz ja dalās ar 5
- Jazz ja dalās ar 7
- FizzBuzz ja dalās ar 3 un 5
- FizzJazz ja dalās ar 3 un 7
- BuzzJazz ja dalās ar 5 un 7
- FizzBuzzJazz ja dalās ar 3 un 5 un 7
"""

# pievieno (importē) sistēmas moduli sys,
# lai varētu izmantot funkcijas un datus, kas saistīti ar programmas darbību un komandrindu

import sys 

# -----------------------------
# 1. Pārbauda vai ir arguments
# -----------------------------

# pārbauda vai lietotājs ir iedevis skaitli
# 1 elements = tikai programmas nosaukums
# 2 elementi = programma + skaitlis
# sys.argv ir saraksts ar komandrindas argumentiem
# len() nozīmē cik elementu ir sarakstā

if len(sys.argv) < 2:
    print("Kļūda: jānorāda skaitlis N.")
    print("Piemērs: python fizzbuzz.py 15")
    sys.exit()  # nozīmē beigt programmu uzreiz

# --------------------------------------
# 2. Pārbauda vai arguments ir skaitlis
# --------------------------------------

try:
    N = int(sys.argv[1])
except ValueError:
    print("Kļūda: N jābūt veselam skaitlim.")
    sys.exit()

# ---------------------
# 3. Cikls no 1 līdz N
# ---------------------

for i in range(1, N + 1):

    result = ""

    # pārbauda vai dalās ar 3
    if i % 3 == 0:
        result += "Fizz"

    # pārbauda vai dalās ar 5
    if i % 5 == 0:
        result += "Buzz"

    # pārbauda vai dalās ar 7
    if i % 7 == 0:
        result += "Jazz"

    # ja nedalās ne ar vienu, izdrukā pašu skaitli
    if result == "":
        print(i)
    else:
        print(result)