from domain.entities import Melodie
class Console:

    def __init__(self, service_melodii):
        self.__service_melodii = service_melodii

    def __ui_print_meniu(self):
        print(">>>Actiunile utilizatorului sunt:")
        print("1. Modifica o melodie")

    def __ui_modifica_melodie(self):
        titlu = input("Titlu este:")
        artist = input("Artistul este:")
        gen = input("Genul este:")
        data = input("Data este:")
        melodie = Melodie(titlu,artist,gen,data)
        gen_nou = input("Noul gen este:")
        data_noua = input("Noua data este:")
        self.__service_melodii.modifica_melodie(melodie,gen_nou, data_noua)


    def run(self):
        while True:
            self.__ui_print_meniu()
            cmd = input(">>>Optiunea dumneavoastra este:")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "1":
                self.__ui_modifica_melodie()
