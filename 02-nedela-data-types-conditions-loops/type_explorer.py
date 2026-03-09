"""
type_explorer.py

Šī programma demonstrē:
- Python pamata datu tipus (int, float, str, bool, None)
- mainīgo tipu noteikšanu ar type()
- truthy / falsy uzvedību
- datu tipu konversijas
- robežgadījumus (ValueError)

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
