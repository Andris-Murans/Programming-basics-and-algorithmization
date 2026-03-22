def is_email(text):
    """Pārbauda, vai teksts izskatās kā e-pasta adrese.

    Funkcija veic vienkāršu pārbaudi — vai tekstā ir simboli '@' un '.'.
    Tā nepārbauda pilnu e-pasta standartu, tikai pamata struktūru.

    Args:
        text (str): teksts, ko pārbaudīt

    Returns:
        bool: True, ja teksts atbilst vienkāršam e-pasta formātam, citādi False

    Example:
        >>> is_email("anna@inbox.lv")
        True
        >>> is_email("anna")
        False
        >>> is_email("anna@")
        False
        >>> is_email("anna@.")
        True
        >>> is_email("")
        False

    Notes:
        Šī ir vienkāršota validācija un negarantē, ka e-pasts ir reāli eksistējošs.
    """
    if not isinstance(text, str):
        return False

    return "@" in text and "." in text


def is_phone_number(text):
    """Pārbauda, vai teksts ir derīgs Latvijas telefona numurs.

    Derīgs formāts:
    +371 XXXXXXXX (8 cipari pēc atstarpes)

    Args:
        text (str): telefona numurs tekstā

    Returns:
        bool: True, ja atbilst formātam, citādi False

    Example:
        >>> is_phone_number("+371 26123456")
        True
        >>> is_phone_number("26123456")
        False
        >>> is_phone_number("+371 123")
        False
        >>> is_phone_number("+371 2612A456")
        False
        >>> is_phone_number(None)
        False

    Notes:
        Netiek pārbaudīts, vai numurs reāli eksistē.
    """
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):    # startswith() → pārbauda teksta sākumu
        return False

    # Paņem visu tekstu sākot no 5. indeksa (pēc "+371 ")
    number = text[5:]

    # Pārbauda 2 lietas:
    # 1. Vai garums ir tieši 8 simboli
    # 2. Vai visi simboli ir cipari (isdigit())
    return len(number) == 8 and number.isdigit()


def is_valid_age(age):
    """Pārbauda, vai vecums ir derīgs.

    Vecumam jābūt veselam skaitlim diapazonā no 0 līdz 150.

    Args:
        age (int): personas vecums

    Returns:
        bool: True, ja vecums ir derīgs, citādi False

    Example:
        >>> is_valid_age(25)
        True
        >>> is_valid_age(-5)
        False
        >>> is_valid_age(200)
        False
        >>> is_valid_age("a")
        False

    Notes:
        Funkcija nepieņem decimālskaitļus vai tekstu.
    """
    return isinstance(age, int) and 0 <= age <= 150


def is_strong_password(text):
    """Pārbauda, vai parole ir pietiekami droša.

    Parole ir derīga, ja:
    - satur vismaz 8 simbolus
    - satur vismaz vienu burtu
    - satur vismaz vienu ciparu

    Args:
        text (str): parole

    Returns:
        bool: True, ja parole ir stipra, citādi False

    Example:
        >>> is_strong_password("abc12345")
        True
        >>> is_strong_password("abcdefg")
        False
        >>> is_strong_password("12345678")
        False

    Notes:
        Netiek pārbaudīti speciālie simboli (piemēram, !@#).
    """
    if not isinstance(text, str):
        return False

    # 'c.isalpha()' vai simbols ir burts
    # 'c.isdigit()' vai simbols ir cipars
    # 'c.isalpha() for c in text' katram simbolam izveido True/False
    # 'any' nozīmē: vai IR kaut viens True? 
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)

    return len(text) >= 8 and has_letter and has_digit


def is_valid_date(text):
    """Pārbauda, vai teksts atbilst datuma formātam YYYY-MM-DD.

    Funkcija pārbauda:
    - vai teksts sastāv no trim daļām (gads, mēnesis, diena)
    - vai tās ir skaitliskas
    - vai mēnesis ir 1–12 un diena 1–31

    Args:
        text (str): datums tekstā

    Returns:
        bool: True, ja formāts ir derīgs, citādi False

    Example:
        >>> is_valid_date("2024-05-10")
        True
        >>> is_valid_date("2024-13-01")
        False
        >>> is_valid_date("2024/05/10")
        False
        >>> is_valid_date("202-05-10")
        False
        >>> is_valid_date("2024-02-31")
        True

    Notes:
        Netiek pārbaudīts, vai datums ir reāli eksistējošs (piem., februāra dienas).
    """
    if not isinstance(text, str):
        return False

    # sadala tekstu daļās
    parts = text.split("-")

    # pārbauda vai ir tieši 3 daļas
    if len(parts) != 3:
        return False

    # sadala saraksta elementus atsevišķos mainīgajos
    year, month, day = parts

    return (
        year.isdigit() and len(year) == 4 and
        month.isdigit() and 1 <= int(month) <= 12 and
        day.isdigit() and 1 <= int(day) <= 31
    )


if __name__ == "__main__":
    print("\n--- EMAIL ---")
    print(is_email("anna@inbox.lv"))   # True
    print(is_email("anna"))            # False
    print(is_email("anna@"))           # False
    print(is_email("anna@."))          # True
    print(is_email(""))                # False

    print("\n--- PHONE NUMBER ---")
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))       # False
    print(is_phone_number("+371 123"))       # False
    print(is_phone_number("+371 2612A456"))  # False
    print(is_phone_number(None))             # False

    print("\n--- AGE ---")
    print(is_valid_age(25))   # True
    print(is_valid_age(-5))   # False
    print(is_valid_age(200))  # False
    print(is_valid_age("a"))  # False

    print("\n--- PASSWORD ---")
    print(is_strong_password("abc12345"))  # True
    print(is_strong_password("abc"))       # False
    print(is_strong_password("12345678"))  # False

    print("\n--- DATE ---")
    print(is_valid_date("2024-05-10"))  # True
    print(is_valid_date("2024-13-01"))  # False
    print(is_valid_date("2024/05/10"))  # False
    print(is_valid_date("202-05-10"))   # False
    print(is_valid_date("2024-02-31"))  # True