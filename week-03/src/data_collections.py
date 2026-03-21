# =========================
# A DAĻA — SARAKSTI (list)
# =========================

print("--- Saraksti ---")

# 1. Izveidojam sarakstu ar vismaz 5 skaitļiem
numbers = [1, 2, 3, 4, 5]

# 2. Pievienojam jaunu elementu saraksta beigās
numbers.append(6)  # tagad saraksts "numbers": [1,2,3,4,5,6]

# 3. Dzēšam pēdējo elementu sarakstā
numbers.pop()  # noņem 6 no saraksta

# Tagad saraksts atkal ir [1,2,3,4,5]

# 4. Aprēķinām summu un vidējo vērtību ar for ciklu
sum = 0      # šeit krāsim summu
counter = 0      # elementu skaitītājs

for num in numbers:
    sum += num   # pieskaitām katru skaitli
    counter += 1     # palielinām skaitītāju

average = sum / counter  # vidējā vērtība

print(f"Summa: {sum}, Vidējais: {average}")

# 5. Filtrējam pāra skaitļus
even_numbers = []   # izveidojam jaunu sarakstu priekš pāra skaitļiem

for num in numbers:
    if num % 2 == 0:   # ja dalās ar 2 bez atlikuma → pāra skaitlis
        even_numbers.append(num)

print(f"Pāra skaitļi: {even_numbers}")

# 6. Slice (šķēlumi)
first_three = numbers[:3]    # pirmie 3 elementi
last_two = numbers[-2:]      # pēdējie 2 elementi
every_second = numbers[::2]  # katrs otrais elements

print(f"Pirmie 3: {first_three}, Pēdējie 2: {last_two}")
print(f"Katrs otrais: {every_second}")

# =========================
# B DAĻA — VĀRDNĪCAS (dict)
# =========================

print("\n--- Vārdnīcas ---")

# 1. Izveidojam vārdnīcu
students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

# 2. Pievienojam jaunu studentu
students["Pēteris"] = 88

# 3. Mainām esošu atzīmi
students["Jānis"] = 75

# 4. Izvadām visus studentus
for name, grade in students.items():    # .items() ļauj piekļūt visiem vārdnīcas elementiem vienlaicīgi
    print(f"{name}: {grade}")

# 5. Atrodam labāko studentu
best_name = ""  # sākuma vērtība labākā studenta vārdam
best_grade = 0  # sākuma vērtība labākā studenta atzīmei

for name, grade in students.items():
    if grade > best_grade:
        best_grade = grade
        best_name = name

print(f"Labākais students: {best_name} ({best_grade})") # f-string ļauj ievietot mainīgos tieši tekstā

# =========================
# C DAĻA — KOMBINĀCIJA
# =========================

print("\n--- Studenti ar atzīmi >= 80 ---")

# 1. Saraksts ar vārdnīcām
student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 75},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 88}
]

# 2. Filtrējam studentus ar atzīmi >= 80
good_students = []  # izvidojam jaunu sarakstu priekš studentiem ar atzīmi >=80

for student in student_list:
    if student["grade"] >= 80:
        good_students.append(student)

# 3. enumerate() → dod indeksu + vērtību
for i, student in enumerate(good_students, start=1):
    print(f"{i}. {student['name']} — {student['grade']}")