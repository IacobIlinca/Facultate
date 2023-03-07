from domain.domain import get_b, get_a, prim, creeaza_nrcomplex, modul_nrcomplex, valideaza_nrcomplex, valideaza_poz
from functionalitati.functionalitati import copie_lista, suma_subsecventa_parteimag, suma_subsecventa_partereal, inlocuieste_aparitii_nrcomplex, sterge_nrcomplex_interval, sterge_nrcomplex_pozdata, insereaza_nrcomplex_pozdata, adauga_nrcomplex_in_lista, filtrare_desc_parte_imag, filtrare_parte_reala_prim, filtrare_modul_mic, filtrare_modul_egal, filtrare_modul_mare, produs_subsecventa_partereal, produs_subsecventa_parteimag
from service.service import srv_sterge_nrcomplex_pozdata, srv_insereaza_nrcomplex_pozdata, srv_sterge_nrcomplex_interval, srv_inlocuieste_aparitii_nrcomplex, srv_suma_subsecventa, srv_produs_subsecventa, srv_adauga_in_lista


def test_filtrare_desc_parte_imag():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 13.0, 0.85)
    srv_adauga_in_lista(l, 22.07, 30.25)
    srv_adauga_in_lista(l, 13.991, 2.85)
    srv_adauga_in_lista(l, 98.87, 40.75)
    srv_adauga_in_lista(l, 7.0, 3.85)
    assert (len(l) == 5)
    filtrare_desc_parte_imag(l)
    assert ((abs(get_b(l[4]) - 0.85) < 0.00001))

def test_filtrare_parte_reala_prim():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 13.0, 0.85)
    srv_adauga_in_lista(l, 22.07, 30.25)
    srv_adauga_in_lista(l, 13.991, 2.85)
    srv_adauga_in_lista(l, 98.87, 40.75)
    srv_adauga_in_lista(l, 7.0, 3.85)
    assert (len(l) == 5)
    filtrare_parte_reala_prim(l)
    assert (len(l) == 3)

def test_prim():
    x=2
    p=prim(x)
    assert(p==1)
    y=-4
    q=prim(y)
    assert(q==0)
    z=13
    o=prim(z)
    assert(o==1)


def test_filtrare_modul_mic():
    l=[]
    assert( len(l)==0)
    srv_adauga_in_lista(l, 1.01, 0.85)
    srv_adauga_in_lista(l, 22.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 2.85)
    srv_adauga_in_lista(l, 93.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 3.85)
    assert (len(l)==5)
    filtrare_modul_mic(l,10)
    assert (len(l)==2)

def test_filtrare_modul_mare():
    l=[]
    assert( len(l)==0)
    srv_adauga_in_lista(l, 1.01, 0.85)
    srv_adauga_in_lista(l, 22.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 2.85)
    srv_adauga_in_lista(l, 93.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 3.85)
    assert (len(l)==5)
    filtrare_modul_mare(l,10)
    assert (len(l)==3)

def test_filtrare_modul_egal():
    l=[]
    assert( len(l)==0)
    srv_adauga_in_lista(l, 1.01, 0.85)
    srv_adauga_in_lista(l, 22.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 2.85)
    srv_adauga_in_lista(l, 93.87, 40.75)
    srv_adauga_in_lista(l, 3.03, 4.04)
    assert (len(l)==5)
    filtrare_modul_egal(l,10)


def test_produs_subsecventa_parteimag():
    l=[]
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.0, 10.0)
    srv_adauga_in_lista(l, 2.0, 3.0)
    srv_adauga_in_lista(l, 3.0, 1.0)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    p=produs_subsecventa_parteimag(l,0,3)
    assert (abs(p - 30.0) < 0.001)

def test_produs_subsecventa_partereal():
    l=[]
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.0, 10.0)
    srv_adauga_in_lista(l, 2.0, 3.0)
    srv_adauga_in_lista(l, 3.0, 1.0)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    p=produs_subsecventa_partereal(l,0,3)
    assert (abs(p - 6.0) < 0.001)

def test_srv_produs_subsecvente():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.0, 10.0)
    srv_adauga_in_lista(l, 2.0, 3.0)
    srv_adauga_in_lista(l, 3.0, 1.0)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    prod=srv_produs_subsecventa(l, 0, 3)
    assert ((abs(get_a(prod) - 6.0) < 0.00001) and (abs(get_b(prod) - 30.0) < 0.00001))


def test_suma_subsecventa_parteimag():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    s=suma_subsecventa_parteimag(l,0,3)
    assert(abs(s-89.95)<0.001)


def test_suma_subsecventa_partereal():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    s=suma_subsecventa_partereal(l,0,3)
    assert(abs(s-4.09)<0.001)

def test_srv_suma_subsecvente():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    suma=srv_suma_subsecventa(l, 0, 3)
    assert ((abs(get_a(suma) - 4.09) < 0.00001) and (abs(get_b(suma) - 89.95) < 0.00001))


def test_inlocuieste_aparitii_nrcomplex():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    nounrcomplex = creeaza_nrcomplex(2.02, 20.00)
    nrcomplex = creeaza_nrcomplex(1.01, 29.85)
    inlocuieste_aparitii_nrcomplex(l, nrcomplex, nounrcomplex)
    assert ((abs(get_a(nounrcomplex) - get_a(l[0]) < 0.00001) and (abs(get_b(nounrcomplex) - get_b(l[0]) < 0.00001))))


def test_srv_inlocuieste_aparitii_nrcomplex():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 1.01, 29.85)
    assert (len(l) == 5)
    try:

        nrcomplex = creeaza_nrcomplex(1.11, 29.85)
        nounrcomplex = creeaza_nrcomplex(2.22, 34.45)
        srv_inlocuieste_aparitii_nrcomplex(l, nrcomplex, nounrcomplex)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "nrcomplex nu e in lista!\n")


def test_modul_nrcomplex():
    a = 3.0
    b = 4.0
    nrcomplex = creeaza_nrcomplex(a, b)
    m = modul_nrcomplex(nrcomplex)
    assert (abs(m - 5.0) < 0.00001)


def test_sterge_nrcomplex_interval():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 3.06, 35.09)
    srv_adauga_in_lista(l, 9.87, 40.75)
    srv_adauga_in_lista(l, 6.97, 55.99)
    lungime = len(l)
    sterge_nrcomplex_interval(l, 1, 2)
    assert (len(l) == lungime - 1)


def test_srv_sterge_nrcomplex_interval():
    l = []
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 3.06, 35.09)
    assert (len(l) == 3)
    try:
        srv_sterge_nrcomplex_interval(l, -1, 2)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "inc invalid!\n")
    try:
        srv_sterge_nrcomplex_interval(l, 10, 2)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "interval invalid!\n")


def test_sterge_nrcomplex_pozdata():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 3.06, 35.09)
    sterge_nrcomplex_pozdata(l, 1)
    assert (len(l) == 2)


def test_srv_sterge_nrcomplex_pozdata():
    l = []
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 3.06, 35.09)
    assert (len(l) == 3)
    try:
        srv_sterge_nrcomplex_pozdata(l, -1)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "poz invalida!\n")


def test_insereaza_nrcomplex_pozdata():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 3.06, 35.09)
    nrcomplex = creeaza_nrcomplex(5.01, 24.05)
    insereaza_nrcomplex_pozdata(l, nrcomplex, 1)
    assert (len(l) == 4)
    assert (abs(get_a(nrcomplex) - get_a(l[1])) < 0.000001)
    assert (abs(get_b(nrcomplex) - get_b(l[1])) < 0.000001)


def test_srv_adauga_in_lista():
    l = []
    assert (len(l) == 0)
    srv_adauga_in_lista(l, 1.01, 29.85)
    srv_adauga_in_lista(l, 2.07, 30.25)
    srv_adauga_in_lista(l, 3.06, 35.09)
    assert (len(l) == 3)
    try:
        srv_insereaza_nrcomplex_pozdata(l, "", 24.05, 2)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "a invalid!\n")


def test_adauga_nrcomplex_in_lista():
    l = []
    assert (len(l) == 0)
    nrcomplex = creeaza_nrcomplex(5.01, 24.05)
    adauga_nrcomplex_in_lista(l, nrcomplex)
    assert (len(l) == 1)
    assert (abs(get_a(nrcomplex) - get_a(l[0])) < 0.000001)
    assert (abs(get_b(nrcomplex) - get_b(l[0])) < 0.000001)


def test_valideaza_nrcomplex():
    nrcomplex = creeaza_nrcomplex(5.01, 24.05)
    valideaza_nrcomplex(nrcomplex)
    invalid_a_nrcomplex = creeaza_nrcomplex("", 24.05)
    try:
        valideaza_nrcomplex(invalid_a_nrcomplex)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "a invalid!\n")
    invalid_nrcomplex = creeaza_nrcomplex("", "")
    try:
        valideaza_nrcomplex(invalid_nrcomplex)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "a invalid!\nb invalid!\n")


def test_valideaza_poz():
    poz = 2
    valideaza_poz(poz)
    invalid_poz = -5
    try:
        valideaza_poz(invalid_poz)
        assert (False)
    except Exception as ex:
        assert (str(ex) == "poz invalida!\n")


def test_creeaza_nrcomplex():
    a = 5.01
    b = 24.05
    nrcomplex = creeaza_nrcomplex(a, b)
    assert (abs(get_a(nrcomplex) - a < 0.00001))
    assert (abs(get_b(nrcomplex) - b < 0.00001))

def test_undo():
    l = []
    undo_l=[]
    assert (len(l) == 0)
    undo_l.append(copie_lista(l))
    srv_adauga_in_lista(l, 13.0, 0.85)
    undo_l.append(copie_lista(l))
    srv_adauga_in_lista(l, 22.07, 30.25)
    assert len(l)==2
    l = undo_l.pop()
    assert len(l)==1


def run_teste():
    test_creeaza_nrcomplex()
    test_valideaza_nrcomplex()
    test_adauga_nrcomplex_in_lista()
    test_valideaza_poz()
    test_srv_adauga_in_lista()
    test_insereaza_nrcomplex_pozdata()
    test_sterge_nrcomplex_pozdata()
    test_srv_sterge_nrcomplex_pozdata()
    test_sterge_nrcomplex_interval()
   # test_inlocuieste_aparitii_nrcomplex()
    #test_srv_inlocuieste_aparitii_nrcomplex()
    test_modul_nrcomplex()
    test_suma_subsecventa_partereal()
    test_suma_subsecventa_parteimag()
    test_srv_suma_subsecvente()
    test_produs_subsecventa_parteimag()
    test_produs_subsecventa_partereal()
    test_srv_produs_subsecvente()
    test_filtrare_modul_mic()
    test_filtrare_modul_mare()
    test_filtrare_modul_egal()
    test_prim()
    test_filtrare_desc_parte_imag()
    test_undo()