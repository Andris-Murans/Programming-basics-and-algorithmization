"""
fizzbuzz.py

Programma:
- pieņem skaitli N no komandrindas (sys.argv)
- izvada skaitļus no 1 līdz N
- Fizz ja dalās ar 3
- Buzz ja dalās ar 5
- FizzBuzz ja dalās ar 3 un 5
"""

import sys

if len(sys.argv) < 2:
    print("Kļūda: jānorāda skaitlis N.")
    print("Piemērs: python fizzbuzz.py 15")
    sys.exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print("Kļūda: N jābūt veselam skaitlim.")
    sys.exit()

for i in range(1, N + 1):

    # vispirms pārbauda dalāmību ar abiem
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # dalās ar 3
    elif i % 3 == 0:
        print("Fizz")

    # dalās ar 5
    elif i % 5 == 0:
        print("Buzz")

    # ja nedalās ne ar vienu
    else:
        print(i)