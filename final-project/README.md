# 💰 Izdevumu izsekotājs (CLI)

Izdevumu izsekotājs ir Python komandrindas lietojumprogramma personīgo izdevumu uzskaitei un analīzei. 
Tā ļauj lietotājam reģistrēt izdevumus, grupēt tos pa kategorijām, analizēt datus pa mēnešiem un eksportēt rezultātus Excel saderīgā formātā.

---

## 💡 Galvenās iespējas

- **Izdevumu uzskaite** - Pievieno summu, kategoriju un aprakstu ar automātisku datuma validāciju.

- **Datu analīze** - Filtrēšana pēc mēneša un kopsummas aprēķins pa kategorijām.

- **CSV eksports** - Datu saglabāšana failā, kas saderīgs ar Excel (utf-8-sig kodējums).

- **Datu drošība** - Automātiska datu saglabāšana JSON failā starp sesijām.

---

## 🛠️ Uzstādīšana

1. Klonē repozitoriju:

git clone https://github.com/Andris-Murans/Programming-basics-and-algorithmization.git

2. Palaid programmu:

```
python expense_tracker/app.py
```

---

## ▶️ Lietošana

Palaižot programmu, tiek parādīta izvēlne:

**1) Pievienot izdevumu** – ievada datumu, kategoriju, summu un aprakstu
**2) Parādīt visus izdevumus** – tabulas veidā ar kopsummu
**3) Filtrēt pēc mēneša** – apskatīt konkrēta mēneša izdevumus
**4) Kopsavilkums pa kategorijām** – izdevumu sadalījums
**5) Dzēst izdevumu** – no saraksta pēc numura
**6) Eksportēt CSV** – saglabā datus failā
**7) Iziet** – aizver programmu

---

## 📁 Struktūra

app.py – Galvenā izvēlne un lietotāja saskarne.

storage.py – Darbs ar JSON failiem (ielāde/saglabāšana).

logic.py – Biznesa loģika (filtrēšana, grupēšana, aprēķini).

export.py – Eksports uz CSV formātu.

docs/ – Plānošanas un izstrādes dokumentācija.

---

## 👨‍🎓 Autors

Andris Murāns — Programmēšanas pamati, 2025