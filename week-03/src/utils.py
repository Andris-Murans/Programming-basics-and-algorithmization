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

# =========================
# SKAITĻU FUNKCIJAS
# =========================

def clamp(num, low, high):
    """Ierobežo skaitli diapazonā [low, high].

    Args:
        num (int/float): skaitlis
        low (int/float): apakšējā robeža
        high (int/float): augšējā robeža

    Returns:
        int/float: ierobežotā vērtība

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if low > high:
        raise ValueError("low nedrīkst būt lielāks par high")

    # min(num, high): Neļauj skaitlim būt lielākam par griestiem. Ja skaitlis ir par lielu, to "nosit" lejā līdz high.
    # max(low, ...): Neļauj rezultātam būt mazākam par grīdu. Ja pēc pirmā soļa skaitlis ir par mazu, to "pavelk" uz augšu līdz low.
    return max(low, min(num, high))


def is_prime(num):
    """Pārbauda vai skaitlis ir pirmskaitlis.

    Args:
        num (int): skaitlis

    Returns:
        bool: True ja pirmskaitlis

    Example:
        >>> is_prime(7)
        True
    """
    if not isinstance(num, int):
        raise ValueError("num jābūt int")

    # num < 2: Skaitļi, kas mazāki par 2 (piemēram, 0, 1 vai negatīvi skaitļi), nav pirmskaitļi, tāpēc funkcija uzreiz pasaka False.
    if num < 2:
        return False
    # num ** 0.5: Nepārbauda visus skaitļus līdz galam, bet tikai līdz skaitļa kvadrātsaknei.
    # Tas padara kodu daudz ātrāku, jo, ja dalītājs nav atrasts līdz saknei, tā tālāk vairs nebūs.
    for i in range(2, int(num ** 0.5) + 1):
        # num % i == 0: Ja skaitlis dalās ar kādu citu skaitli bez atlikuma, tas nav pirmskaitlis, un funkcija atgriež False.
        if num % i == 0:    
            return False

    return True


def factorial(n):
    """Aprēķina n! (faktoriālu).

    Args:
        n (int): skaitlis (n >= 0)

    Returns:
        int: faktoriāls

    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise ValueError("n jābūt int")

    # n < 0: Faktoriāls negatīviem skaitļiem neeksistē, tāpēc programma neļauj turpināt.
    if n < 0:
        raise ValueError("n jābūt >= 0")

    # result = 1: Izveido mainīgo, kurā "krās" reizinājumu. Mēs sākam ar 1, jo, reizinot ar 0, viss rezultāts vienmēr būtu 0.
    result = 1

    # result *= i: Katrā solī esošais rezultāts tiek sareizināts ar nākamo skaitli (1, tad reiz 2, tad reiz 3...).
    for i in range(1, n + 1):
        result *= i

    return result

# =========================
# SARAKSTU FUNKCIJAS
# =========================

def total(numbers):
    """Aprēķina saraksta summu.

    Args:
        numbers (list): skaitļu saraksts

    Returns:
        int/float: summa
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")

    result = 0  # Izveido mainīgo, kurā "krās" summu. Tā kā saskaitīšana vēl nav sākusies, tur ir nulle.

    for num in numbers:
        result += num   # Katru atrasto skaitli pieskaita pie jau esošās summas.

    return result


def average(numbers):
    """Aprēķina vidējo vērtību.

    Args:
        numbers (list): skaitļu saraksts

    Returns:
        float: vidējais

    Example:
        >>> average([1,2,3])
        2.0
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")

    # Ja saraksts būs tukšs, programma mēģinātu dalīt ar nulli, kas matemātikā nav iespējams un izraisītu kļūdu (ZeroDivisionError).
    if len(numbers) == 0:
        raise ValueError("saraksts nedrīkst būt tukšs")

    # izsauc iepriekš izveidoto f-ju total() un izmanto len() f-ju saraksta garuma noteikšanai
    return total(numbers) / len(numbers)

# =========================
# DEMO BLOKS
# =========================

# if __name__ == "__main__": nodrošina, ka šie testi (print) izpildīsies tikai tad, ja tu palaidīsi šo konkrēto failu.
# Ja kāds cits programmētājs mēģinās "importēt" tavas funkcijas savā projektā, testi automātiski neizpildīsies un netraucēs viņa darbam.
if __name__ == "__main__":
    print(capitalize("hello"))
    print(truncate("Šis ir ļoti garš teksts", 10))
    print(count_words("Python ir foršs"))

    print(clamp(15, 0, 10))
    print(is_prime(7))
    print(factorial(5))

    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))