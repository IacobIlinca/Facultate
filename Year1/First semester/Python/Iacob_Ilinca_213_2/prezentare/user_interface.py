class Consola():
    def __init__(self, srv_cursuri):
        self.__srv_cursuri = srv_cursuri

    def meniu(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Căutarea de cursuri pe baza limbii străine vizate: 1")
        print("Înscriere curs si suma totala de plata: 2")

    def __ui_cauta_limba_str(self):
        lb_str = input(">>Introduceti string-ul ce va fi cautat ca limba straina:")
        rezultat = self.__srv_cursuri.cauta_limba_str(lb_str)
        if len(rezultat)>0:
            for curs in rezultat:
                print(str(curs))
        else:
            raise Exception("Niciun curs nu contine acel string ca limba straina!")

    def __ui_total_inscriere(self):
        id_curs = input("Introducti id-ul cursului dorit:")
        nr_ore = input("Introducti numarul de ore dorite:")
        rezultat = self.__srv_cursuri.total_inscriere(id_curs, nr_ore)
        if len(rezultat) > 0:
            print(str(rezultat[0]))
            print("Suma totala este:")
            print(str(rezultat[1]))
        else:
            raise Exception("Niciun curs cu id-ul dat!")


    def run(self):
        while True:
            self.meniu()
            cmd = input(">>>Optiunea dumneavoastra este:")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "1":
                try:
                    self.__ui_cauta_limba_str()
                except Exception as ex:
                    print(str(ex))
            elif cmd == "2":
                try:
                    self.__ui_total_inscriere()
                except Exception as ex:
                    print(str(ex))

            else:
                print("Comanda invalida!")