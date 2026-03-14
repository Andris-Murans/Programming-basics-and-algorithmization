"""
eligibility.py

Programma pārbauda vai persona:
- var balsot
- var īrēt auto
- var saņemt senioru atlaidi
- var saņemt studentu atlaidi
"""
# -----------------------------------
# 1. Vecuma ievade ar kļūdu apstrādi
# -----------------------------------

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

# ---------------
# 2. j/n ievades
# ---------------

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

# -----------------------------
# 3. pārvērš j/n uz True/False
# -----------------------------

has_license = license_input == "j"
is_student = student_input == "j"
is_veteran = veteran_input == "j"

# -------------
# 4. balsošana
# -------------

if age >= 18:
    vote = "Jā ✓"
else:
    vote = "Nē ✗"

# ------------
# 5. auto īre
# ------------

if age >= 21 and has_license:
    rent = "Jā ✓"
elif age < 21:
    rent = "Nē ✗ (par jaunu)"
else:
    rent = "Nē ✗ (nav apliecības)"

# -------------------
# 6. senioru atlaide
# -------------------

if age >= 65 or is_veteran:
    senior = "Jā ✓"
else:
    senior = "Nē ✗"

# --------------------
# 7. studentu atlaide
# --------------------

if 16 <= age <= 26 and is_student:
    student = "Jā ✓"
else:
    student = "Nē ✗"       
