from exceptii.erori import ValidationError, RepositoryEror
class Console:

    def __init__(self, service_emisiune):
        self.__service_emisiune = service_emisiune

    def __ui_print_meniu(self):
        print(">>>>\nActiunile utilizatorului sunt:")
        print("1.Sterge emisiune")

    def __ui_sterge_emisiune(self):
        nume = input("Numele emisiunii:")
        tip = input("Tipul emisiunii:")
        self.__service_emisiune.sterge_emisiune(nume,tip)

    def __ui_update_emisiune(self):
        nume = input("Numele emisiunii:")
        # tip = input("Tipul emisiunii:")
        # durata = input("Durata emisiuneii:")
        # descriere = input("Descrierea emisiunii:")
        dur_noua = input("noua durata:")
        desc_noua = input("descrierea noua:")
        self.__service_emisiune.update_emisiune(nume,dur_noua,desc_noua)

    def exporta(self):
        nume_fisier = input("Numele fisierului:")
        lista = self.__service_emisiune.get_all()
        self.__service_emisiune.write_to_another_file(nume_fisier,lista)


    def run(self):
        while True:
            self.__ui_print_meniu()
            cmd = input(">>>\nOperatia utilizatorului este:")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "1":
                try:
                    self.__ui_sterge_emisiune()
                except ValidationError as ve:
                    print("validation error:"+str(ve))
                except RepositoryEror as re:
                    print("repository error:"+str(re))
            elif cmd == "2":
                self.__ui_update_emisiune()
            elif cmd == "3":
                self.exporta()
            else:
                print("Comanda invalida!")





