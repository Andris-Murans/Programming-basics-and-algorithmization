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

def add_contact(name, phone):
    """
    Pievieno jaunu kontaktu un saglabā to failā.

    Parametri:
    name (str): kontakta vārds
    phone (str): telefona numurs

    Piemērs:
    >>> add_contact("Anna Bērziņa", "+371 26123456")
    """
    contacts = load_contacts()

    contacts.append({
        "name": name,
        "phone": phone
    })

    save_contacts(contacts)

    print(f"✓ Pievienots: {name} ({phone})")

def list_contacts():
    """
    Izvada visus kontaktus uz ekrāna.

    Piemērs:
    >>> list_contacts()
    1. Anna Bērziņa - +371 26123456
    2. Jānis Kalniņš - +371 29876543
    """
    contacts = load_contacts()

    # Ja nav neviena kontakta
    if not contacts:
        print("Nav kontaktu")
        return

    print("Kontakti:")

    # 'enumerate(contacts, start=1)' paņem sarakstu 'contacts' un katram elementam piešķir kārtas numuru, 
    # sākot no 1 (pēc noklusējuma programmēšanā sāk no 0).
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} — {contact['phone']}")

def search_contacts(query):
    """
    Meklē kontaktus pēc vārda (vai tā daļas).

    Parametri:
    query (str): meklējamais teksts

    Piemērs:
    >>> search_contacts("Anna")
    Atrasti 1 kontakti:
    1. Anna Bērziņa - +371 26123456
    """
    contacts = load_contacts()

    # Ja nav neviena kontakta
    if not contacts:
        print("Nav neviena kontakta")
        return

    results = []

    # Meklēšana (case-insensitive)
    for contact in contacts:
        # .get() ir "drošības spilvens" – tā paņem vērtību no vārdnīcas, bet, ja tādas tur nav,
        # programma nenobruks un atgriezīs tukšumu ("") vai ctu izvēlētu tekstu (piemēram, "Nezināms").
        name = contact.get("name", "")

        if query.lower() in name.lower():
            results.append(contact)

    # Ja nekas nav atrasts
    if not results:
        print("Nekas netika atrasts")
        return

    print(f"Atrasti {len(results)} kontakti:")

    for i, contact in enumerate(results, start=1):
        name = contact.get("name", "Nezināms")
        phone = contact.get("phone", "Nav numura")

        print(f"{i}. {name} — {phone}")