# Izstrādes žurnāls

## 1. solis: Plānošana

Definēju projekta pamatprasības un mērķi: *izveidot CLI rīku izdevumu uzskaitei*.
Izstrādāju datu struktūru JSON formātā, izvēloties vārdnīcu sarakstu, 
lai katram izdevumam būtu skaidri atslēgu nosaukumi (`date`, `amount`, `category`, `description`).

Sadalīju programmu četros moduļos (`app`, `storage`, `logic`, `export`), lai ievērotu koda atdalīšanas principu.
Nostiprināju zināšanas par Git feature branch lietošanu, izveidojot atsevišķu zaru dokumentācijai.

---

## 2. solis: Pamata darbības

Šajā solī izveidoju JSON datu glabāšanas sistēmu. 
Pārkopēju `storage.py` loģiku no 4. nedēļas uzdevuma un pielāgoju to izdevumu struktūrai.

Visvairāk laika patērēju, meklējot, kā validēt lietotāja ievadīto datumu, 
līdz atklāju `datetime.strptime()` funkciju, kas ļauj pārbaudīt datuma formātu.

Arī izvades formatēšana prasīja daudz laika, bet apguvu formatēšanas iespējas.

Šajā solī iemācījos strādāt ar datu validāciju, failu apstrādi un izvades noformēšanu.

---

## 3. solis: Filtrēšana, kopsavilkums un dzēšana

Šajā solī izveidoju papildus funkcijas filtrēšanai pēc mēneša, 
kopsavilkuma izvadei pa kategorijām un izdevuma dzēšanai.

Papildināju `app.py` izvēlni ar jaunajām komandām (3, 4, 5) un pievienoju nepieciešamo lietotāja ievades apstrādi.

Sākumā nebija skaidrs, kā lietotājam ērti piedāvāt tikai tos mēnešus, kuros tiešām ir veikti ieraksti.
Uzzināju par `set()` funkciju, ar kuras palīdzību no visiem datumiem var atlasīt unikālus mēnešu ierakstus, 
izvairoties no dublikātiem.

Uzlaboju arī lietotāja saskarni, lai tā būtu pārskatāmāka un vieglāk lietojama.

---

## 4. solis: CSV eksports un dokumentācija

Šajā solī izveidoju iespēju eksportēt izdevumus CSV failā, izmantojot `csv` moduli.  
Sākumā bija neskaidrības ar latviešu simbolu attēlošanu Excel, bet atradu risinājumu — izmantot utf-8-sig kodējumu.  

Pievienoju eksportēšanas funkciju galvenajā izvēlnē un lietotāja ievadi faila nosaukumam.  

Papildus izveidoju README.md un DEVLOG.md dokumentāciju.  
Sākumā nezināju kā formatēt tekstu veidojot dokumentāciju, bet tad atradu risinājumu - izmantot **Markdown** teksta formatēšanas veidu.

Šajā solī iemācījos strādāt ar failu eksportēšanu, kodējumiem, projekta dokumentēšanu un to formatēšanu.