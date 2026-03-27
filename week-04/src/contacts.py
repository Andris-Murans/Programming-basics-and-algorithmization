import json # Pieslēdz JSON bibliotēku. Ļauj saglabāt Python datus failā un nolasīt datus no faila.
            # Izskatās līdzīgi Python sarakstiem un vārdnīcām.
import sys  # Pieslēdz sistēmas (komandrindas) funkcijas. 
            # Ļauj programmā redzēt, ko ieraksta terminālī.
import os   # Pieslēdz darbu ar failiem un operētājsistēmu. 
            # Ļauj pārbaudīt vai fails eksistē un strādāt ar mapēm un failiem.

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """
    Nolasa kontaktus no JSON faila.

    Ja fails neeksistē, atgriež tukšu sarakstu [].

    Piemērs:
    >>> load_contacts()
    [{"name": "Anna Bērziņa", "phone": "+371 26123456"}]
    """
    if not os.path.exists(CONTACTS_FILE):   # Pārbauda vai fails eksistē. Novērš kļūdu (FileNotFoundError).
        return []

    # Atver failu CONTACTS_FILE lasīšanas režīmā ar UTF-8 kodējumu, 
    # nosauc to par f un, kad pabeidz darbu, aizver to automātiski.
    # 'encoding="utf-8' nodrošina, ka failā varēs pareizi saglabāt latviešu burtus (un citus unikālus simbolus).
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_contacts(contacts):
    """
    Saglabā kontaktu sarakstu JSON failā.

    Parametri:
    contacts (list): saraksts ar kontaktiem

    Piemērs:
    >>> save_contacts([{"name": "Anna Bērziņa", "phone": "+371 26123456"}])
    """
    # Šis kods ieraksta mainīgo 'contacts' failā JSON formātā, 
    # izmantojot UTF-8 kodējumu pareizai latviešu burtu attēlošanai.
    # un atkāpes ('indent=2'), lai fails būtu viegli lasāms cilvēkam.
    # 'ensure_ascii=False'ļauj saglabāt burtus kā "ā", "č", "š" tiešā veidā, nevis kā kodus (piemēram, \u0101 = "ā"). 
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)