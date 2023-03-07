from domain.domain import valideaza_poz, valideaza_inc, valideaza_sf, vf_nrcomplex_in_lista, valideaza_interval, valideaza_nrcomplex, creeaza_nrcomplex
from functionalitati.functionalitati import adauga_nrcomplex_in_lista, inlocuieste_aparitii_nrcomplex, suma_subsecventa_partereal, suma_subsecventa_parteimag, produs_subsecventa_parteimag, produs_subsecventa_partereal, sterge_nrcomplex_interval, insereaza_nrcomplex_pozdata, sterge_nrcomplex_pozdata

def srv_adauga_in_lista(l, a, b):  # 1.1
    # functie care creeaza un numar complex cu partea reala a (float) si partea imaginara(float) b
    # valideaza numarul complex nou creat si incearca sa o adauge in lista de numere complexe l
    # input: l-lista de numere complexe
    #       a-float
    #       b-float
    # output: -, daca totul reuseste cu succes
    # raises: Exception cu textul
    # .......
    nrcomplex = creeaza_nrcomplex(a, b)
    valideaza_nrcomplex(nrcomplex)
    adauga_nrcomplex_in_lista(l, nrcomplex)

def srv_insereaza_nrcomplex_pozdata(l, a, b, poz):  # 1.2
    # functie care creeaza un numar complex cu partea reala a (float) si partea imaginara(float) b
    # valideaza numarul complex nou creat si incearca sa il insereze in lista de numere complexe l pe pozitia poz data
    # input: l-lista de numere complexe
    #       a-float
    #       b-float
    #       poz-int>=0
    # output: -, daca totul reuseste cu succes
    # raises: Exception cu textul
    # .......
    nrcomplex = creeaza_nrcomplex(a, b)
    valideaza_nrcomplex(nrcomplex)
    valideaza_poz(poz)
    insereaza_nrcomplex_pozdata(l, nrcomplex, poz)

def srv_sterge_nrcomplex_pozdata(l, poz):  # 2.1
    # functie care incearca sa stearga din lista l numarul complex aflat pe pozitia data poz
    # input: l-lista de numere complexe
    #       poz-int>=0
    # output:-,daca totul reuseste cu succes
    valideaza_poz(poz)
    sterge_nrcomplex_pozdata(l, poz)


def srv_sterge_nrcomplex_interval(l, inc, sf):  # 2.2
    # functie care incearca sa stearga din lista l numerele complexe aflate pe pozitiile cuprinse in intervalul dat
    # input: l-lista de numere complexe
    #       poz-int>=0
    #       inc-capatul din stanga al intervalului de unde se doreste stergerea numerelor complexe
    #       sf-capatul din dreapta al intervalului unde se sfarseste stergerea numerelor complexe
    # output:-,daca totul reuseste cu succes
    valideaza_inc(inc)
    valideaza_sf(sf)
    valideaza_interval(inc, sf)
    sterge_nrcomplex_interval(l, inc, sf)

def srv_inlocuieste_aparitii_nrcomplex(l, nrcomplex, nounrcomplex):  # 2.3
    # functie care incearca sa inlocuiasca toate aparitiile numarului complex nrcomplex cu numarul complex nounrcomplex
    # input: l-lista de numere complexe
    #       nrcomplex-numar complex
    #       nounrcomplex-numar complex
    # output:-,daca totul reuseste cu succes
    vf_nrcomplex_in_lista(l,nrcomplex)
    inlocuieste_aparitii_nrcomplex(l, nrcomplex, nounrcomplex)

def srv_suma_subsecventa(l,inc,sf):     #4.1
    #functie care asambleaza suma numerelor complexe cerute alcatuita din suma partilor reale si suma partilor imaginare
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output:suma,ca un numar complex, numerelor complexe din intervalul dorit, daca totul s-a executat cu succes
    sreal=suma_subsecventa_partereal(l,inc,sf)
    simag=suma_subsecventa_parteimag(l,inc,sf)
    return creeaza_nrcomplex(sreal,simag)

def srv_produs_subsecventa(l,inc,sf):     #4.2
    #functie care asambleaza sprodusul numerelor complexe cerute alcatuita din produsul partilor reale si produsul partilor imaginare
    #input: l-lista de numere complexe
    #       inc-capatul din stanga al intervalului dorit
    #       sf-capatul din dreapta al intervalului dorit
    #output:produsul,ca un numar complex, numerelor complexe din intervalul dorit, daca totul s-a executat cu succes
    preal=produs_subsecventa_partereal(l,inc,sf)
    pimag=produs_subsecventa_parteimag(l,inc,sf)
    return creeaza_nrcomplex(preal,pimag)

