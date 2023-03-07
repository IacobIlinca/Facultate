import datetime

from erori.exceptii import ValidationError, RepositoryError
class Console():
    def __init__(self,service_evenimente):
        self.__service_evenimente = service_evenimente

    def __ui_print_meniu(self):
        print(">>>>>>")
        print("Actiunile utilizatorului sunt:")
        print("1.Adauga un eveniment")


    def __ui_adauga_eveniment(self):
        """
        adauga un eveniment
        :return:
        """
        data = input("Introduceti data evenimentului:")
        ora = input("Introduceti ora evenimentului:")
        descriere = input("Introduceti descrierea evenimentului:")
        self.__service_evenimente.adauga_eveniment(data,ora,descriere)
        print("Eveniment adaugat cu succes!")

    def __ui_afisare_zi_curenta(self):
        """

        :return:
        """
        an = str(datetime.date.today().year)
        luna = str(datetime.date.today().month)
        zi = str(datetime.date.today().day)
        data_curenta = zi + ".0" + luna + "." + an
        lista = self.__service_evenimente.afisare_zi_curenta(data_curenta)
        for ev in lista:
            print(ev)

    def __ui_afisare_data_dorita(self):
        data = input("Introduceti data dorita:")
        lista = self.__service_evenimente.afisare_data_dorita(data)
        for ev in lista:
            print(ev)

    def __ui_exporta_descriere(self):
        descriere = input("Introduceti descrierea:")
        lista = self.__service_evenimente.exporta_descriere(descriere)
        for event in lista:
            print(event)

    def __ui_exporta_final(self):
        nume_fisier = input("Introduceti numele fisierului:")
        descriere = input("Introduceti descrierea:")
        lista = self.__service_evenimente.exporta_descriere(descriere)

        self.__service_evenimente.exporta_final(nume_fisier,lista)

    def __ui_incearca(self):
        nume_fisier = input("Introduceti numele fisierului:")
        descriere = input("Introduceti descrierea:")
        self.__service_evenimente.incearca(nume_fisier, descriere)


    def run(self):
        while True:
            print("Evenimentele din ziua curenta sunt:\n")
            self.__ui_afisare_zi_curenta()
            self.__ui_print_meniu()
            cmd = input(">>>\nOptiunea dumneavoastra este:")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "1":
                try:
                    self.__ui_adauga_eveniment()
                except ValidationError as ve:
                    print("validation error:\n"+str(ve))
                except RepositoryError as re:
                    print("repository error:\n"+str(re))
            elif cmd == "2":
                self.__ui_afisare_data_dorita()
            elif cmd == "3":
                self.__ui_exporta_descriere()
            elif cmd =="4":
                self.__ui_exporta_final()

            else:
                print("Comanda invalida!")

