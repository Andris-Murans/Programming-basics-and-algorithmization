"""
eligibility.py

Programma pārbauda vai persona:
- var balsot
- var īrēt auto
- var saņemt senioru atlaidi
- var saņemt studentu atlaidi
"""
# 1. Vecuma ievade ar kļūdu apstrādi
try:
    age = int(input("Ievadi vecumu: "))

    # pārbauda vai vecums nav negatīvs
    if age < 0:
        print("Kļūda: vecums nevar būt negatīvs!")
        exit()

except ValueError:
    # ja ievada tekstu nevis skaitli
    print("Kļūda: vecumam jābūt skaitlim!")
    exit()
