from domain.domain import get_a, get_b, modul_nrcomplex, creeaza_nrcomplex, prim


def to_str_nrcomplex(nrcomplex):
    return str(nrcomplex[0]) + "+" + str(nrcomplex[1]) + "i"


def adauga_nrcomplex_in_lista(l, nrcomplex):  # 1.1
    # functie care adauga numarul complex nrcomplex in lista de numere complexe l
    # input: l- lista de numere complexe, nrcomplex-un numar complex
    # output:-,l'=l U (nrcomplex)
    l.append(nrcomplex)


def insereaza_nrcomplex_pozdata(l, nrcomplex, poz):  # 1.2.
    # functie care insereaza pe pozitia intreaga poz din lista de numere complexe l numarul complex nrcomplex
    # input: l-lista de numere complexe
    #       poz-int>=0->pozitia pe care va fi inserat numarul complex
    #       nrcomplex- numarul complex ce va fi inserat
    # output:-
    l.insert(poz, nrcomplex)


def sterge_nrcomplex_pozdata(l, poz):  # 2.1
    # functie care sterge numarul complex de pe pozitia intreaga poz din lista de numere complexe l
    # input: l-lista de numere complexe
    #       poz-int>=0->pozitia de pe care va fi sters numarul complex
    # output:-, daca totul reuseste cu succes
    del l[poz]


def sterge_nrcomplex_interval(l, inc, sf):  # 2.2
    # functie care sterge din lista l toate numerele complexe regasite pe pozitiile din intervalul specificat
    # input: l-lista de numere complexe
    #       inc-pozitia de inceput de unde se efectueaza stergerea (capatul din stanga al intervalului)
    #       sf-pozitia de final unde se opreste stergerea (capatul din dreapta al intervalului)
    # output:-, daca totul reuseste cu succes
    for i in range(inc, sf):
        del l[i]


def inlocuieste_aparitii_nrcomplex(l, nrcomplex, nounrcomplex):  # 2.3
    # functie care inlocuieste toate aparitiile numarului complex nrcomplex
    # input: l-lista de numere complexe
    #       nrcomplex-numarul complex care a carui aparitii vor fi inlocuite
    #       nounrcomplex-noul numar complex ce va fi inlocuit in lista
    # output:-,daca totul reuseste cu succes
    for i in range(0, len(l)):
        if l[i] == nrcomplex:
            l[i] = nounrcomplex


def tipareste_parteimg_interval(l, inc, sf):  # 3.1
    # functie care tipareste partea imaginara a numerelor dintr-un interval de indici dat
    # input: l-lista de numere complexe
    #       a-partea reala a numarului complex
    #       b-partea imaginara a numarului complex
    #       inc-capatul din stanga al intervalului dat
    #       sf-capatul din dreapta al intervalului dat
    # output:-,daca totul reuseste cu succes
    print("Partea imaginara a numerelor complexe din intervalul dat este:")
    for i in range(inc, sf + 1):
        z = get_b(l[i])
        print(z)


def modul_mai_mic_10(l):  # 3.2
    # functie care tipareste numerele complexe din lista l care au modului mai mic decat 10
    # input:l-lista de numere complexe
    # output: afiseaza numerele complexe cu modul<10 sau mesajul "Nu exista numere complexe cu modulul mai mic decat 10" daca in lista nu sunt astfel de numere
    nr = 0
    for i in range(len(l)):
        m = modul_nrcomplex(l[i])
        if m < 10:
            nr = nr + 1
            print(to_str_nrcomplex(l[i]))
    if nr == 0:
        print("Nu exista numere complexe cu modulul mai mic decat 10")


def modul_mai_mare_egal_10(l):  # 3.3
    # functie care tipareste numerele complexe din lista l care au modului mai mare sau egal cu 10
    # input:l-lista de numere complexe
    # output: afiseaza numerele complexe cu modul>=10 sau mesajul "Nu exista numere complexe cu modulul mai mare sau egal cu 10" daca in lista nu sunt astfel de numere
    nr = 0
    for i in range(len(l)):
        m = modul_nrcomplex(l[i])
        if m >= 10:
            nr = nr + 1
            print(to_str_nrcomplex(l[i]))
    if nr == 0:
        print("Nu exista numere complexe cu modulul mai mare sau egal cu 10")


def suma_subsecventa_partereal(l, inc, sf):   #4.1
    #functie care calculeaza suma partilor reale a numerelor complexe aflate pe pozitiile din intervalul indicat
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output: suma partilor reale a numerelor complexe aflate pe pozitiile din intervalul indicat
    s = 0
    for i in range ( inc, sf ):
        s = get_a (l[i]) +s
    return s

def suma_subsecventa_parteimag(l,inc,sf):   #4.1
    #functie care calculeaza suma partilor imaginare a numerelor complexe aflate pe pozitiile din intervalul indicat
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output: suma partilor imagire a numerelor complexe aflate pe pozitiile din intervalul indicat
    s=0
    for i in range (inc,sf):
        s=get_b(l[i])+s
    return s

def srv_suma_subsecventa(l,inc,sf):     #4.1
    #functie care asambleaza suma numerelor complexe cerute alcatuita din suma partilor reale si suma partilor imaginare
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output:suma,ca un numar complex, numerelor complexe din intervalul dorit, daca totul s-a executat cu succes
    sreal=suma_subsecventa_partereal(l,inc,sf)
    simag=suma_subsecventa_parteimag(l,inc,sf)
    return creeaza_nrcomplex(sreal,simag)


def produs_subsecventa_partereal(l, inc, sf):   #4.2
    #functie care calculeaza produsul partilor reale a numerelor complexe aflate pe pozitiile din intervalul indicat
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output: produsul partilor reale a numerelor complexe aflate pe pozitiile din intervalul indicat
    p=1
    for i in range (inc, sf):
        p=get_a (l[i])*p
    return p

def produs_subsecventa_parteimag(l,inc,sf):   #4.2
    #functie care calculeaza produsul partilor imaginare a numerelor complexe aflate pe pozitiile din intervalul indicat
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output: produsul partilor imaginare a numerelor complexe aflate pe pozitiile din intervalul indicat
    p=1
    for i in range (inc, sf):
        p=get_b(l[i])*p
    return p

def filtrare_desc_parte_imag(l):        #4.3
    #functie care sorteaza lista descrescator dupa partea imaginara a numerelor complexe din ea
    #input:l-lista de numere complexe
    #output:lista numerelor complexe sortata descrescator dupa partea imaginara
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if get_b(l[j])>=get_b(l[i]):
                aux = l[i]
                l[i] = l[j]
                l[j] = aux



def filtrare_parte_reala_prim(l): #5.1
    #functie care elimină din lista l numerele complexe la care partea reala este numar prim
    #input:l-lista de numere complexe
    #output:-,daca totul se executa cu succes
    i=0
    while i<len(l):
        real=get_a(l[i])
        a=int(real)
        frac=real-a
        if frac!=0:
            pass
        else:
            p=prim(a)
            if p==1:
                del l[i]
        i=i+1

def filtrare_modul_mic(l,m): #5.2
    #functie care elimina din lista numerele complexe l care au modulul < decât un număr dat
    #input:l-lista de numere complexe
    #      m-numarul dat cu care se compara modulul numerelor
    #output:-,daca totul se executa cu succes
    i=0
    while i<len(l):
        ma=modul_nrcomplex(l[i])
        if ma<m:
            del l[i]
        else:
            i=i+1


def filtrare_modul_mare(l,m): #5.2
    #functie care elimina din lista numerele complexe l care au modulul > decât un număr dat
    #input:l-lista de numere complexe
    #      m-numarul dat cu care se compara modulul numerelor
    #output:-,daca totul se executa cu succes
    i=0
    while i<len(l):
        ma=modul_nrcomplex(l[i])
        if ma>m:
            del l[i]
        else:
            i=i+1


def filtrare_modul_egal(l,m): #5.2
    #functie care elimina din lista numerele complexe l care au modulul = cu un număr dat
    #input:l-lista de numere complexe
    #      m-numarul dat cu care se compara modulul numerelor
    #output:-,daca totul se executa cu succes
    i = 0
    while i < len(l):
        ma = modul_nrcomplex(l[i])
        if abs(m - ma) < 0.00001:
             del l[i]
        else:
            i = i + 1
"""
def sterge_poz (l,poz):
    del l[poz]
    return l

def inlocuire_back (l,nrcomplex, nounrcomplex):
    for i in range(0, len(l)):
        if l[i] == nrcomplex:
            l[i] = nounrcomplex
    return l

def copie_element(nr,list, poz):
    list.append(nr)
    list.append(poz)
    return list
"""


def copie_lista (l):
    #functie care retine o lista de listele anterioare conform operatiilor efectuate
    ll=[]
    for nrcomplex in l:
        nounrcomplex=nrcomplex[:]
        ll.append(nounrcomplex)
    return ll


