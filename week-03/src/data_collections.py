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