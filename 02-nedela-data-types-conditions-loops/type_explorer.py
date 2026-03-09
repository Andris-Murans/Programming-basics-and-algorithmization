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