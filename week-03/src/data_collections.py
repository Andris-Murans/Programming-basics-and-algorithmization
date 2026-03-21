# =========================
# A DAĻA — SARAKSTI (list)
# =========================

print("--- Saraksti ---")

# 1. Izveidojam sarakstu ar vismaz 5 skaitļiem
numbers = [1, 2, 3, 4, 5]

# 2. Pievienojam jaunu elementu saraksta beigās
numbers.append(6)  # tagad saraksts "numbers": [1,2,3,4,5,6]

# 3. Dzēšam pēdējo elementu
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