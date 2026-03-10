"""
type_explorer.py

Šī programma demonstrē:
- Python pamata datu tipus (int, float, str, bool, None)
- mainīgo tipu noteikšanu ar type()
- truthy / falsy uzvedību
- datu tipu konversijas
- robežgadījumus (ValueError, edge cases)

"""
print("\n=== Uzdevums 1: Tipu pētnieks ===\n")

# ------------------------------------------
# 1. MAINĪGO DEFINĒŠANA
# ------------------------------------------

name = "Andris"      # str
age = 43             # int
height = 1.75        # float
is_student = False   # bool
data = None          # NoneType

# ------------------------------------------
# 2. KONSOLES IZVADE AR KATRA MAINĪGĀ TIPU
# ------------------------------------------

print("1. MAINĪGIE UN TO TIPI\n")

print(f"name = {name} -> {type(name)}") # f-string (formatēta virkne) ļauj ievietot mainīgos vai izteiksmes tieši tekstā, izmantojot {}
print(f"age = {age} -> {type(age)}")
print(f"height = {height} -> {type(height)}")
print(f"is_student = {is_student} -> {type(is_student)}")
print(f"data = {data} -> {type(data)}")

# ------------------------------------------
# 3. TRUTHY / FALSY PIEMĒRI
# ------------------------------------------

print("\n2. TRUTHY / FALSY PIEMĒRI\n")

print(bool(False))      # Loģiskā vērtība False
print(bool(0))          # Nulle Pythonā ir falsy
print(bool(0.0))        # Peldošā punkta nulle ir falsy
print(bool(""))         # Tukša virkne ir falsy
print(bool([]))         # Tukšs saraksts ir falsy
print(bool({}))         # Tukša vārdnīca ir falsy
print(bool(None))       # Nav vērtības, ir falsy
print(bool("0"))        # Virkne nav tukša, ir truthy
print(bool(" "))        # Atstarpe ir simbols, ir truthy
print(bool([0]))        # Saraksts nav tukšs, ir truthy
print(bool(-1))         # Nenulles skaitlis ir truthy
print(bool("Python"))   # Netukša virkne ir truthy

# ------------------------------------------
# 4. DATU TIPU PĀRVEIDOŠANA
# ------------------------------------------

print("\n3. DATU TIPU PĀRVEIDOŠANA\n")

# Mainīgo definēšana
text_integer_number = "3"
text_decimal_number = "3.14"

print("1) string → int\n")
# Pārvēršam tekstu par skaitli
integer_number = int(text_integer_number)   # int() pārvērš tekstu ar skaitli par veselu skaitli
print(f"text_integer_number = {text_integer_number} -> {type(text_integer_number)}")
print(f"number = {integer_number} -> {type(integer_number)}")

print("\n2) string → float\n")
# Pārvēršam tekstu par daļskaitli
decimal_number = float(text_decimal_number)   # float() pārvērš tekstu par decimālskaitli
print(f"text_decimal_number = {text_decimal_number} -> {type(text_decimal_number)}")
print(f"number = {decimal_number} -> {type(decimal_number)}")

print("\n3) float → int\n")
# Pārvēršam daļskaitli par veselu skaitli
number = int(decimal_number)   # int() neapaļo skaitli, tas vienkārši nogriež decimāldaļu
print(f"decimal_number = {decimal_number} -> {type(decimal_number)}")
print(f"number = {number} -> {type(number)}")

print("\n4) Zinātniskais pieraksts\n")
# 1000.0 — "1e3" ir zinātniskais pieraksts (1 × 10³), Python to pārvērš par float
print("1e3 = 1 × 10³ = 1000")
print(float("1e3"))

# ------------------------------------------
# 5. ROBEŽGADĪJUMI (EDGE CASES)
# ------------------------------------------

print("\n4. ROBEŽGADĪJUMI (EDGE CASES)\n")

# 1. Tekstu "abc" nevar pārvērst par skaitli
# int() gaida tekstu, kas satur tikai ciparus
# print(int("abc"))  # ValueError

# 2. Tekstu ar decimālskaitli nevar tieši pārvērst par int
# print(int("3.14"))  # ValueError

# Pareizais veids būtu vispirms pārvērst par float
print(int(float("3.14")))  # 3

# 3. Tukša virkne pārvērsta par bool
# Python tukšas vērtības interpretē kā False
print(bool(""))  # False

# 4. Virkne ar atstarpi NAV tukša
print(bool(" "))  # True

# 5. Skaitlis 0 pārvērsts par bool
print(bool(0))  # False

# 6. Zinātniskais pieraksts
# int() to tieši nesaprot
# print(int("1e3"))  # ValueError

# Bet float() to saprot
print(float("1e3"))  # 1000.0

# 7. int() nevar pārvērst virkni par skaitli, ja tā nesastāv no cipariem
print("\nRobežgadījums: int('abc')")
try:
    value = int("abc")
except ValueError:
    print("ValueError: 'abc' nevar pārvērst par int")
