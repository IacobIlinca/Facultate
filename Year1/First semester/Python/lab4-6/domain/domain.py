import math


def creeaza_nrcomplex(a, b):
    # functie care creeaza un numar complex cu partea reala (un numar real) a si cu partea imaginara(un numar real) b
    # input: a-float
    #       b-float
    # output: rez-un numar complex cu partea reala a si partea imaginara b
    nrcomplex = []
    nrcomplex.append(a)
    nrcomplex.append(b)
    return nrcomplex


def get_a(nrcomplex):
    # functie care returneaza identificatorul partea reala a numarului complex nrcomplex
    # input: nrcomplex- un nrcomplex
    # output: rez-float, identificatorul parte reala a numarului complex nrcomplex
    a = nrcomplex[0]
    return a


def get_b(nrcomplex):
    # functie care returneaza identificatorul partea imaginara a numarului complex nrcomplex
    # input: nrcomplex- un nrcomplex
    # output: rez-float, identificatorul parte imaginara a numarului complex nrcomplex
    return nrcomplex[1]


def egale_nrcomplexe(nrc0, nrc1):
    # functie care verifica daca 2 numere complexe sunt egale
    return (get_a(nrc0) == get_a(nrc1)) and (get_b(nrc0) == get_b(nrc1))


def modul_nrcomplex(nrcomplex):
    # functie care calculeaza valoarea modulului numarului complex
    # input:nrcomplex- un numar complex
    # output:m-valoarea modulului lui nrcomplex
    p = get_a(nrcomplex)
    q = get_b(nrcomplex)
    e = p * p
    f = q * q
    m = math.sqrt(e + f)
    return m


def valideaza_nrcomplex(nrcomplex):
    # functie care verifica daca un numar complex are partea reala si partea imaginara nevide
    # input:nrcomplex-numar complex
    # output:-, daca numarul complex e valid
    # raises: Exception cu textul
    #       "a invalid!\n" daca partea reala a numarului complex e vida
    #       "b invalid!\n" daca partea imaginara a numarului complex e vida
    err = ""
    if get_a(nrcomplex) == "":
        err += "a invalid!\n"
    if get_b(nrcomplex) == "":
        err += "b invalid!\n"
    if len(err) > 0:
        raise Exception(err)


def vf_nrcomplex_in_lista(l, nrcomplex):
    # functie care verifica daca numarul complex nrcomplex apare cel putin o data in lista l
    # input: l-lista de numere complexe
    #       nrcomplex-numarul complex ce trebuie verificat
    # output:-,daca numarul complex e in lista
    # raises:Exception cu textul:
    #       "numarul complex nu e in lista!\n" daca numarul complex nu apare in lista l
    err = ""
    ok = 0
    for i in range(len(l)):
        if (abs(get_a(nrcomplex) - get_a(l[i]) >= 0.00001) or abs(get_b(nrcomplex) - get_b(l[0]) >= 0.00001)):
            ok = 1
    if ok == 1:
        err += "numarul complex nu e in lista!\n"
    if len(err) > 0:
        raise Exception(err)


def valideaza_poz(poz):
    # functie care verifica daca o pozitie este un numar pozitiv
    # input: poz-int>=0
    # output:-, daca pozitia este valida
    # raises: Exception cu textul
    #       "poz invalida!\n" daca pozitia este un numar <0
    err = ""
    if poz < 0:
        err += "poz invalida!\n"
    if len(err) > 0:
        raise Exception(err)


def valideaza_inc(inc):
    # functie care verifica daca capatul din stanga al intervalului este un numar pozitiv
    # input: inc-int>=0
    # output:-, daca capatul din stanga este valid
    # raises: Exception cu textul
    #       "capatul din stanga al intervalului invalid!\n" daca capatul din stanga al intervalului este un numar <0
    err = ""
    if inc < 0:
        err += "capatul din stanga al intervalului invalid!\n"
    if len(err) > 0:
        raise Exception(err)


def valideaza_sf(sf):
    # functie care verifica daca capatul din dreapta al intervalului este un numar pozitiv
    # input: sf-int>=0
    # output:-, daca capatul din dreapta este valid
    # raises: Exception cu textul
    #       "capatul din dreapta al intervalului invalid!\n" daca capatul din dreapta al intervalului este un numar <0
    err = ""
    if sf < 0:
        err += "capatul din dreapta al intervalului invalid!\n"
    if len(err) > 0:
        raise Exception(err)


def valideaza_interval(inc, sf):
    # functie care verifica daca intervalul este corect ales, respectiv daca sf>=inc
    # input: inc-int>=0
    #       sf-int>=0
    # output:-, daca intervalul este valid
    # raises: Exception cu textul
    #       "Interval invalid!\n" daca capatul din dreapta este mai mic decat capatul din stanga
    err = ""
    if sf < inc:
        err += "Interval invalid!\n"
    if len(err) > 0:
        raise Exception(err)


def prim(x):
    #functie care verifica daca numarul dat x este sau nu prim
    #input:x-numarul ce se doreste sa fie verificat
    #output: 1-daca numarul este prim, o in caz contrar
    ok = 1
    nr = 0
    if x < 2:
        ok = 0
    if x % 2 == 0 and x != 2:
        ok = 0
    if x == 2:
        ok = 1
    else:
        for i in range(2, x // 2):
            if x % i == 0:
                nr = nr + 1
        if nr != 0:
            ok = 0
    return ok
