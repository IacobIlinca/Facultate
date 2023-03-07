from ui.ui import ui_print_nrcomplexe
from service.service import srv_adauga_in_lista, srv_sterge_nrcomplex_pozdata
from functionalitati.functionalitati import copie_lista, filtrare_parte_reala_prim

def run():
    global l, undo_l
    undo_l=[]
    l=[]
    not_gata=True
    while not_gata:

        cmd = input(">>>\nOptiunea dumneavoastra este:")
        operatie = cmd.split(",")
        for i in range (0, len(operatie)):
            x = operatie[i].split(" ")
            if x[0] == "exit":
                return
            if x[0] == "":
                continue
            if x[0] == "undo":
                if undo_l == []: raise ValueError("No operation to undo")
                l=undo_l.pop()
            elif x[0] == "add":
                #adauga element nou in lista
                if len(x) < 3:
                    print ("comandă rulată cu prea puțini parametri")

                else:
                    try:
                        a = float(x[1])
                    except ValueError:
                        print("Valoare numerica invalida pentru a!")
                        return
                    try:
                        b = float(x[2])
                    except ValueError:
                        print("Valoare numerica invalida pentru b!")
                        return
                    undo_l.append(copie_lista(l))
                    srv_adauga_in_lista(l,a,b)
                    #ui_print_nrcomplexe(l)
            elif x[0] == "sterge":
                #sterge elementul de pe o pozitie data
                if len(x) < 2:
                    print ("comandă rulată cu prea puțini parametri")
                else:
                    undo_l.append(copie_lista(l))
                    poz= int(x[1])
                    srv_sterge_nrcomplex_pozdata(l, poz)
                    #ui_print_nrcomplexe(l)
            elif x[0] == "filtreaza":
                #Filtrare parte reala prim – elimină din listă numerele complexe la care partea reala este prim
                undo_l.append(copie_lista(l))
                filtrare_parte_reala_prim(l)
                #ui_print_nrcomplexe(l)
            elif x[0] =="tipareste":
                ui_print_nrcomplexe(l)
            else:
                print("comanda invalida")

