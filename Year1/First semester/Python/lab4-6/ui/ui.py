from domain.domain import creeaza_nrcomplex
from functionalitati.functionalitati import copie_lista, tipareste_parteimg_interval, modul_mai_mic_10, modul_mai_mare_egal_10, filtrare_desc_parte_imag, filtrare_parte_reala_prim, filtrare_modul_mare, filtrare_modul_egal, filtrare_modul_mic
from service.service import srv_suma_subsecventa, srv_produs_subsecventa, srv_adauga_in_lista, srv_sterge_nrcomplex_pozdata, srv_insereaza_nrcomplex_pozdata, srv_sterge_nrcomplex_interval, srv_inlocuieste_aparitii_nrcomplex

# Meniu
def print_meniu():
    print("Actiunile pe care utilizatorul le poate alege sunt:")
    print("1.1 Adauga numar complex la sfarsitul listei")
    print("1.2 Inserare numar complex pe o pozitie data")
    print("2.1 Sterge elementul de pe o pozitie data")
    print("2.2 Sterge elementele de pe un interval de pozitii")
    print("2.3 Inlocuieste toate aparitiile unui numar complex cu un alt numar complex")
    print("3.1 Tipareste partea imaginara pentru numerele din lista(se da sub secventa)")
    print("3.2 Tipareste toate numerele complexe care au modulul mai mic decat 10")
    print("3.3 Tipareste toate numerele complexe care au modulul egal cu 10")
    print("4.1 Tipareste suma numerelor dintr-o subsecventă dată")
    print("4.2 Tipareste produsul numerelor dintr-o subsecventă dată")
    print("4.3 Tipărește lista sortată descrescător după partea imaginara")
    print("5.1 Filtrare parte reala prim – elimină din listă numerele complexe la care partea reala este prim")
    print("5.2 Filtrare modul – elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat")
    print("6. Undo")

def to_str_nrcomplex(nrcomplex):
    return str(nrcomplex[0]) + "+" + str(nrcomplex[1]) + "i"

def ui_adauga_nrcomplex(l):  # 1.1.
    print("Introduceti partea reala a numarului complex ce se doreste a fi adaugat in lista")
    try:
        a = float(input("a="))
    except ValueError:
        print("Valoare numerica invalida pentru a!")
        return
    print("Introduceti partea reala a numarului complex ce se doreste a fi adaugat in lista")
    try:
        b = float(input("b="))
    except ValueError:
        print("Valoare numerica invalida pentru b!")
        return
    srv_adauga_in_lista(l, a, b)
    print("A fost adaugat in lista numarul complex ")


def ui_insereaza_nrcomplex_pozdata(l):  # 1.2.
    print("Introduceti partea reala a numarului complex ce se doreste a fi inserat in lista")
    try:
        a = float(input("a="))
    except ValueError:
        print("Valoare numerica invalida pentru a!")
        return
    print("Introduceti partea reala a numarului complex ce se doreste a fi inserat in lista")
    try:
        b = float(input("b="))
    except ValueError:
        print("Valoare numerica invalida pentru b!")
        return
    print("Introduceti pozitia pe care se doreste sa fie inserat numarul complex in lista l")
    try:
        poz = int(input("poz="))
    except ValueError:
        print("Valoare numerica invalida pentru poz!")
        return
    srv_insereaza_nrcomplex_pozdata(l, a, b, poz)
    print("A fost inserat in lista numarul complex pe pozitia data")



def ui_srv_sterge_nrcomplex_pozdata(l):  # 2.1
    print("Introduceti pozitia de pe care se doreste sa se stearga numarul")
    try:
        poz = int(input("poz="))
    except ValueError:
        print("Valoare numerica invalida pentru poz!")
        return
    srv_sterge_nrcomplex_pozdata(l, poz)
    print("A fost sters din lista numarul complex de pe pozitia data")



def ui_srv_sterge_nrcomplex_interval(l):  # 2.2
    print(
        "Introduceti capatul din stanga al intervalului din care se doreste sa se stearga numerele complexe din lista l")
    try:
        inc = int(input("inc="))
    except ValueError:
        print("Valoare numerica invalida pentru inc!")
        return
    print(
        "Introduceti capatul din dreapta al intervalului unde se doreste sa se opreasca stergerea numerele complexe din lista l")
    try:
        sf = int(input("sf="))
    except ValueError:
        print("Valoare numerica invalida pentru sf!")
        return
    srv_sterge_nrcomplex_interval(l, inc, sf)
    print("Au fost sterse numerel complexe de pe pozitiile din intervalul dat din lista")


def ui_srv_inlocuieste_aparitii_nrcomplex(l):  # 2.3
    nou=[]
    print("Introduceti partea reala a numarului complex a carui aparitii se doresc a fi inlocuite")
    try:
        a = float(input("a="))
    except ValueError:
        print("Valoare numerica invalida pentru a!")
        return
    print("Introduceti partea imaginara a numarului complex a carui aparitii se doresc a fi inlocuite")
    try:
        b = float(input("b="))
    except ValueError:
        print("Valoare numerica invalida pentru b!")
        return
    print("Introduceti partea reala a numarului complex cu care se va inlocui in lista")
    try:
        x = float(input("x="))
    except ValueError:
        print("Valoare numerica invalida pentru x!")
        return
    print("Introduceti partea imaginara a numarului complex cu care se va inlocui in lista")
    try:
        y = float(input("y="))
    except ValueError:
        print("Valoare numerica invalida pentru b!")
        return
    nrcomplex = creeaza_nrcomplex(a, b)
    nounrcomplex = creeaza_nrcomplex(x, y)
    srv_inlocuieste_aparitii_nrcomplex(l, nrcomplex, nounrcomplex)
    print("A fost adaugat in lista numarul complex ")



def ui_tipareste_parteimg_interval(l):  # 3.1
    print("Introduceti capatul stang al intervalului dorit:")
    try:
        inc = int(input("inc="))
    except ValueError:
        print("Valoare numerica invalida pentru inc!")
        return
    print("Introduceti capatul drept al intervalului dorit:")
    try:
        sf = int(input("sf="))
    except ValueError:
        print("Valoare numerica invalida pentru sf!")
        return
    tipareste_parteimg_interval(l, inc, sf)
    print("A fost tiparita partea intreaga pentru toate numerele din intervalul dat")


def ui_modul_mai_mic_10(l):  # 3.2
    modul_mai_mic_10(l)
    print("Au fost tiparite toate numerele a caror modul este mai mic decat 10")


def ui_modul_mai_mare_egal_10(l):  # 3.3
    modul_mai_mare_egal_10(l)
    print("Au fost tiparite toate numerele a caror modul este mai mare sau egal cu 10")


def ui_sumasubsecventa(l):
    print("Introduceti capatul stang al intervalului dorit:")
    try:
        inc = int(input("inc="))
    except ValueError:
        print("Valoare numerica invalida pentru inc!")
        return
    print("Introduceti capatul drept al intervalului dorit:")
    try:
        sf = int(input("sf="))
    except ValueError:
        print("Valoare numerica invalida pentru sf!")
        return
    suma=srv_suma_subsecventa(l,inc,sf)
    print("Suma numerelor complexe din intervalul dorit este:\n")
    print(to_str_nrcomplex(suma))

def ui_prodsubsecventa(l):  #4.2
    print("Introduceti capatul stang al intervalului dorit:")
    try:
        inc = int(input("inc="))
    except ValueError:
        print("Valoare numerica invalida pentru inc!")
        return
    print("Introduceti capatul drept al intervalului dorit:")
    try:
        sf = int(input("sf="))
    except ValueError:
        print("Valoare numerica invalida pentru sf!")
        return
    prod=srv_produs_subsecventa(l,inc,sf)
    print("Produsul numerelor complexe din intervalul dorit este:\n")
    print(to_str_nrcomplex(prod))

def ui_filtrare_desc_parte_imag(l):     #4.3
    filtrare_desc_parte_imag(l)
    print("Lista de numere complexe a fost sortata descrescator dupa partea imaginara")

def ui_filtrare_parte_reala_prim(l): #5.1
    filtrare_parte_reala_prim(l)
    print("Au fost eliminate din listă numerele complexe la care partea reala este prim")

def ui_filtrare_modul(l): #5.2
    print("Introduceti numarul cu care se doreste sa se compare modulul numerelor complexe")

    nr = int(input("valoare_de_comparat="))
    print("Ce relatie doriti sa se verifice intre numarul dat si modulul numerelor complexe din lista?")
    print("Optiunile dumneavoastra sunt:<,>,=")

    a = input("optiunea aleasa este:")
    if a=="<":
        filtrare_modul_mic(l,nr)
    elif a==">":
        filtrare_modul_mare(l, nr)
    elif a == "=":
        filtrare_modul_egal(l, nr)
l=[]
undo_l=[]
def run():
    global l, undo_l
    undo_l=[]
    l=[]
    not_gata=True
    while not_gata:
        print_meniu()

        cmd = input(">>>\nOptiunea dumneavoastra este:")
        if (cmd == "exit"):
            return
        if cmd == "":
            continue
        if cmd == "1.1":
            try:
                undo_l.append(copie_lista(l))
                ui_adauga_nrcomplex(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "1.2":
            try:
                undo_l.append(copie_lista(l))
                ui_insereaza_nrcomplex_pozdata(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "2.1":
            try:
                undo_l.append(copie_lista(l))
                ui_srv_sterge_nrcomplex_pozdata(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "2.2":
            try:
                undo_l.append(copie_lista(l))
                ui_srv_sterge_nrcomplex_interval(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "2.3":
            try:
                undo_l.append(copie_lista(l))
                ui_srv_inlocuieste_aparitii_nrcomplex(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "3.1":
            try:
                ui_tipareste_parteimg_interval(l)
                ultima=cmd
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "3.2":
            try:
                ui_modul_mai_mic_10(l)
                ultima=cmd
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "3.3":
            try:
                ui_modul_mai_mare_egal_10(l)
                ultima=cmd
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "4.1":
            try:
                ui_sumasubsecventa(l)
                ultima=cmd
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "4.2":
            try:
                ui_prodsubsecventa(l)
                ultima=cmd
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "4.3":
            try:
                ui_filtrare_desc_parte_imag(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "5.1":
            try:
                undo_l.append(copie_lista(l))
                ui_filtrare_parte_reala_prim(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd == "5.2":
            try:
                undo_l.append(copie_lista(l))
                ui_filtrare_modul(l)
                ultima=cmd
                print("Actualele elemente din lista sunt:")
                ui_print_nrcomplexe(l)
                print(">>>>\n")
            except Exception as ex:
                print(ex)
        elif cmd=="6":
            if undo_l == []: raise ValueError("No operation to undo")
            l=undo_l.pop()
            print("S-a realizat undo la ultima operatie efectuata")
            print("Actualele elemente din lista sunt:")
            ui_print_nrcomplexe(l)
            print(">>>>\n")

        elif cmd == "print_nrcomplexe":
            ui_print_nrcomplexe(l)
        else:
            print("comanda invalida!")



def ui_print_nrcomplexe(l):
    for nrcomplex in l:
        print(to_str_nrcomplex(nrcomplex))
