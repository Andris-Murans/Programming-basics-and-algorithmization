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
        max_len (int): maksimālais teksta garums pirms '...'

    Returns:
        str: saīsināts teksts

    Example:
        >>> truncate("Hello world", 5)
        "Hello..."
    """
    if not isinstance(text, str):
        raise ValueError("Mainīgajam 'text' jābūt string tipam")
    
    if not isinstance(max_len, int):
        raise ValueError("Mainīgajam 'max_len' jābūt int tipam")
    
    if max_len < 0:
        raise ValueError("Mainīgajam 'max_len' jābūt >= 0")

    if len(text) <= max_len:
        return text

    # text[:max_len]: paņem teksta sākumu no pirmā burta līdz vietai, ko norāda mainīgais max_len.
    return text[:max_len] + "..."   


def count_words(text, separator=None):
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
    
    if separator is not None and not isinstance(separator, str):
        raise ValueError("Mainīgajam 'separator' jābūt string vai None")

    return len(text.split(separator))  # sadala tekstu pēc norādītā separatora

# =========================
# SKAITĻU FUNKCIJAS
# =========================

def clamp(num, low=0, high=100):
    """Ierobežo skaitli diapazonā [low, high].

    Args:
        num (int/float): skaitlis
        low (int/float): apakšējā robeža
        high (int/float): augšējā robeža

    Returns:
        int/float: ierobežotā vērtība

    Example:
        >>> clamp(150)
        100
        >>> clamp(-10)
        0
        >>> clamp(5, 0, 10)
        5
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Mainīgajam 'num' jābūt skaitlim")

    if not isinstance(low, (int, float)) or not isinstance(high, (int, float)):
        raise ValueError("Mainīgajiem 'low' un 'high' jābūt skaitļiem")
    
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
        >>> is_prime(4)
        False
    """
    if not isinstance(num, int):
        raise ValueError("Mainīgajam 'num' jābūt int tipam")

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
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise ValueError("Mainīgajam 'n' jābūt int tipam")

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
    
    Example:
        >>> total([1, 2, 3])
        6
    """
    if not isinstance(numbers, list):
        raise ValueError("numbers jābūt sarakstam")

    result = 0  # Izveido mainīgo, kurā "krās" summu. Tā kā saskaitīšana vēl nav sākusies, tur ir nulle.

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("visiem elementiem jābūt skaitļiem")
        
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
    print("\n*** capitalize f-jas piemērs ***")
    print(capitalize("hello"))

    print("\n*** truncate f-jas piemēri ***")
    # robežgadījums ja f-jā truncate() padod argumentu 'max_len' < 0 
    try:
        print(truncate("Šis ir ļoti garš teksts", -1))
    except ValueError as e:
        print(f"Kļūda: {e}")
    
    print(truncate("Šis ir ļoti garš teksts", 11))
    
    print("\n*** count_words f-jas piemēri ***")
    print(count_words("Python ir foršs"))
    print(count_words("a,b,c", ","))

    print("\n*** clamp f-jas piemēri ***")
    print(clamp(150))
    print(clamp(-10))
    print(clamp(5, 0, 10))

    print("\n*** is_prime f-jas piemēri ***")
    print(is_prime(7))
    print(is_prime(4))

    print("\n*** factorial f-jas piemēri ***")
    print(factorial(5))
    print(factorial(0)) # faktoriāls no nulles matemātikā ir 1
    
    print("\n*** total f-jas piemērs ***")
    print(total([1, 2, 3]))

    print("\n*** average f-jas piemērs ***")
    print(average([1, 2, 3]))