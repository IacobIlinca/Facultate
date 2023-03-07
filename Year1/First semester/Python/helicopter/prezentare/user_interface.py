class Consola():
    def __init__(self, srv_elic):
        self.__srv_elic = srv_elic

    def __ui_afisare_scop(self):
        scop = input(">>Scop:")
        rezultat = self.__srv_elic.cauta_scop(scop)
        if rezultat == -1:
            return
        else:
            rezultat_ordonat = self.__srv_elic.ord_desc_nume(rezultat)
            for elic in rezultat_ordonat:
                print(str(elic))

    def __ui_scop_an(self):
        scopuri = self.__srv_elic.scop_an()
        if len(scopuri)>0:
            print(scopuri)
        else:
            raise Exception("Niciun elicopter gasit!")

    def run(self):
        while True:
            cmd = input(">>>>>")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "afisare_scop":
                self.__ui_afisare_scop()
            elif cmd == "scop_an":
                self.__ui_scop_an()
            else:
                print("comanda invalida!")