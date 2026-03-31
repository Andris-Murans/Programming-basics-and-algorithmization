Izdevumu izsekotāja projekta plāns

A. Programmas apraksts

Šī ir Python komandrindas (CLI) lietojumprogramma, kas paredzēta personīgo finanšu uzskaitei. 
Lietotājs var reģistrēt izdevumus, norādot summu, kategoriju un aprakstu, kā arī analizēt datus, 
filtrējot tos pēc mēneša vai skatot kopsavilkumu pa kategorijām.

B. Datu struktūra

Dati tiks glabāti JSON failā (expenses.json) kā saraksts ar vārdnīcām. Katrs izdevums saturēs šādus laukus:

date: datums ISO formātā "YYYY-MM-DD".
amount: izdevumu summa kā skaitlis ar peldošo komatu (float).
category: kategorija no iepriekš definēta saraksta.
description: īss apraksts par tēriņu.

Piemērs:
{
  "date": "2025-02-15",
  "amount": 12.50,
  "category": "Ēdiens",
  "description": "Pusdienas kafejnīcā"
}

Lietotājs nevarēs pats izdomāt kategoriju, bet izvēlēsies to no jau gatava saraksta (CATEGORIES).
Tas palīdz izvairīties no kļūdām un nodrošina, ka visi dati ir vienādi un saprotami.
Plānots izmantot šādas kategorijas: Ēdiens, Transports, Izklaide, Komunālie maksājumi, Veselība, Iepirkšanās un Cits.

JSON formāts nodrošina vienkāršu datu lasāmību gan cilvēkam, gan programmai, kā arī saglabā datu tipus (piemēram, skaitļus).

C. Moduļu plāns

Projekts tiks sadalīts četros loģiskos moduļos:

app.py: Atbild par lietotāja interfeisu, izvēlnes attēlošanu un ievades saņemšanu.
storage.py: Nodrošina datu ielādi un saglabāšanu JSON failā (load_expenses, save_expenses).
logic.py: Satur "tīras" funkcijas datu apstrādei, piemēram, filtrēšanu pēc mēneša un kopsummu aprēķināšanu.
export.py: Nodrošina datu eksportēšanu uz CSV formātu.

D. Lietotāja scenāriji

Scenārijs 1: Lietotājs izvēlas "Pievienot izdevumu", ievada korektus datus, 
             un programma apstiprina veiksmīgu pievienošanu, parādot kopsavilkumu.
Scenārijs 2: Lietotājs vēlas redzēt tikai februāra izdevumus. 
             Programma atlasa atbilstošos datus un parāda tos noformētā tabulā ar kopējo mēneša summu.
Scenārijs 3: Lietotājs mēģina pievienot izdevumu ar nepareizu summas formātu (piemēram, tekstu). 
             Programma parāda kļūdas paziņojumu un neļauj saglabāt bojātus datus un lūdz ievadīt datus vēlreiz.
Scenārijs 4: (Kategorijas izvēle): Lietotājs pievieno jaunu izdevumu. 
             Programma parāda numurētu kategoriju sarakstu. Lietotājs ievada skaitli (piemēram, "1" priekš "Ēdiens"). 
             Programma saglabā atbilstošo kategorijas nosaukumu JSON failā.

E. Robežgadījumi

Tukšs fails: Ja expenses.json neeksistē vai ir tukšs, 
             programma atgriež tukšu sarakstu un neizmet kļūdu.
Nepareiza ievade: Ja lietotājs ievada negatīvu summu vai neeksistējošu datumu, 
                  programma lūdz ievadīt datus atkārtoti.
Datu trūkums: Ja lietotājs izvēlas "Parādīt izdevumus", bet saraksts ir tukšs, 
              tiek attēlots paziņojums "Nav reģistrētu izdevumu".