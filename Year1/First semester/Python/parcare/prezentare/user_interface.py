class Consola():

    def __init__(self, srv_locuri):
        self.__srv_locuri = srv_locuri

    def __ui_cauta_strada(self):
        strada = input(">>>Strada:")
        rezultat = self.__srv_locuri.cauta_strada(strada)
        if len(rezultat)>0:
            #rezult_ord = self.__srv_locuri.ord_nume(rezultat)
            for loc in rezultat:
                print(loc)
        else:
            raise Exception("nu exista!")

    def ui_tipareste(self):
        locuri = self.__srv_locuri.get_all()
        for loc in locuri:
            print(loc)

    def run(self):
        while True:
            cmd = input(">>>Comanda:")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "cauta_strada":
                try:
                    self.__ui_cauta_strada()
                except Exception as ex:
                    print(str(ex))
            elif cmd == "print":
                self.ui_tipareste()
            else:
                print("comanda invalida!")