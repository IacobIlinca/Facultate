from erori.exceptii import ValidationError, RepositoryError
class Consola:
    def __init__(self, service):
        self.__service = service

    def __ui_adauga_prob(self):
        try:
            nr_lab = int(input("Numarul problemei laboratorului:"))
        except ValueError:
            print("numeric invalid!\n")
            return
        descriere= input("Descriereea labului:")
        try:
            deadline = int(input("Deadline-ul laboratorului:"))
        except ValueError:
            print("numeric invalid!\n")
            return
        self.__service.adauga_prob_lab(nr_lab,descriere,deadline)

    def __ui_cauta_prob(self):
        try:
            nr_lab = int(input("nr lab:"))
        except ValueError:
            print("numeric invalida!")
            return
        rez = self.__service.cauta_prob(nr_lab)
        return rez




    def run(self):
        while True:
            cmd = input("Optiunea dumneavoastra este:")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "adauga_prob":
                try:
                    self.__ui_adauga_prob()
                except ValidationError as ve:
                    print("validation error:\n" + str(ve))
                except RepositoryError as re:
                    print("repository error:\n" + str(re))
            elif cmd == "cauta_prob":
                try:
                    rez = self.__ui_cauta_prob()
                    print(str(rez))
                except RepositoryError as re:
                    print("repository error:\n" + str(re))

            else:
                print("comanda invalida!")