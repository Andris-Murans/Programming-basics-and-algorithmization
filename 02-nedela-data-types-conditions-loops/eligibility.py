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

# 2. j/n ievades

while True:
    license_input = input("Vai ir autovadītāja apliecība? (j/n): ").lower() # lower() pārvērš visu uz maziem burtiem

    if license_input == "j" or license_input == "n":    # pārbauda vai ievadīts j vai n
        break
    else:
        print("Lūdzu ievadi tikai j vai n.")    # ja nav ievadīts j vai n izvada paziņojumu

while True:
    student_input = input("Vai ir students? (j/n): ").lower()

    if student_input == "j" or student_input == "n":
        break
    else:
        print("Lūdzu ievadi tikai j vai n.")

while True:
    veteran_input = input("Vai ir veterāns? (j/n): ").lower()

    if veteran_input == "j" or veteran_input == "n":
        break
    else:
        print("Lūdzu ievadi tikai j vai n.")
        