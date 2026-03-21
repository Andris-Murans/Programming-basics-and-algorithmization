# =========================
# VIRKŅU FUNKCIJAS
# =========================

def capitalize(text):
    """Padara pirmo burtu lielo.

    Args:
        text (str): ievades teksts

    Returns:
        str: teksts ar lielo pirmo burtu

    Example:
        >>> capitalize("hello")
        "Hello"
    """
    # isinstance(text, str) pārbauda, vai mainīgais text ir teksts (str).
    # raise apstādina programmas darbību un "izmet" kļūdu.
    # ValueError ir specifisks kļūdas veids, ko izmanto, kad saņemtā vērtība nav piemērota (tips ir nepareizs vai saturs neatbilstošs).
    if not isinstance(text, str):
        raise ValueError("Mainīgajam 'text' jābūt string tipam")

    if text == "":
        return ""

    # text[0]: Paņem pirmo burtu
    # .upper(): Pārvērš pirmo burtu par lielo.
    # text[1:]: Paņem visu pārējo tekstu, sākot no otrā burta (indekss 1) līdz pašām beigām.
    return text[0].upper() + text[1:]


def truncate(text, max_len=20):
    """Saīsina tekstu līdz max_len un pievieno '...'.

    Args:
        text (str): ievades teksts
        max_len (int): maksimālais garums

    Returns:
        str: saīsināts teksts

    Example:
        >>> truncate("Hello world", 5)
        "Hello..."
    """
    if not isinstance(text, str):
        raise ValueError("Mainīgajam 'text' jābūt string tipam")

    if len(text) <= max_len:
        return text

    # text[:max_len]: paņem teksta sākumu no pirmā burta līdz vietai, ko norāda mainīgais max_len.
    return text[:max_len] + "..."   


def count_words(text, separator=" "):
    """Saskaita vārdus tekstā.

    Args:
        text (str): ievades teksts
        separator (str): atdalītājs

    Returns:
        int: vārdu skaits

    Example:
        >>> count_words("Hello world")
        2
        >>> count_words("a,b,c", ",")
        3
    """
    if not isinstance(text, str):
        raise ValueError("Mainīgajam 'text' jābūt string tipam")

    return len(text.split(separator))  # sadala pēc atstarpēm