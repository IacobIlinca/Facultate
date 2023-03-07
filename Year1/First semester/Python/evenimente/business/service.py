from domain.entitati import Eveniment
class ServiceEvenimente():

    def __init__(self, valid_eveniment, repo_eveniment):
        self.__valid_eveniment = valid_eveniment
        self.__repo_eveniment = repo_eveniment

    def adauga_eveniment(self, data,ora,descriere):
        """
        adauga un eveniment
        :param data:
        :param ora:
        :param descriere:
        :return:
        """
        eveniment = Eveniment(data,ora,descriere)
        self.__valid_eveniment.valideaza(eveniment)
        self.__repo_eveniment.adauga_eveniment(eveniment)

    def afisare_zi_curenta(self,data_curenta):
        """

        :param data_curenta:
        :return:
        """
        lista = []
        evenimente = self.__repo_eveniment.get_all()
        for event in evenimente:
            if event.get_data() == str(data_curenta):
                lista.append(event)
        for i in range (0,len(lista)-1):
            for j in range (i+1, len(lista)):
                parts1 = lista[i].get_ora().split(":")
                ora1 = int(parts1[0])
                minut1 = int (parts1[1])
                parts2 = lista[j].get_ora().split(":")
                ora2 = int(parts2[0])
                minut2 = int(parts2[1])
                if ora1>ora2:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        return lista

    def afisare_data_dorita(self, data_dorita):
        """

        :param data_dorita:
        :return:
        """
        lista = []
        evenimente = self.__repo_eveniment.get_all()
        for event in evenimente:
            if event.get_data() == str(data_dorita):
                lista.append(event)
        return lista


    def exporta_descriere(self, descriere):
        """
        vf ce evenimente au in descriere sirul dat si le ord dupa data si ora evenimentului
        :param descriere:
        :return:
        """
        evenimente = self.__repo_eveniment.get_all()
        lista = []
        for event in evenimente:
            if descriere in event.get_descriere():
                lista.append(event)

        for i in range(0,len(lista)-1):
            data_i = lista[i].get_data().split(".")
            zi_i = data_i[0]
            luna_i = data_i[1]
            an_i = data_i[2]

            orar_i = lista[i].get_ora().split(":")
            ora_i = orar_i[0]
            minut_i = orar_i[1]
            for j in range(i+1, len(lista)):
                ok = 0
                data_j = lista[j].get_data().split(".")
                zi_j = data_j[0]
                luna_j = data_j[1]
                an_j = data_j[2]

                if an_i>an_j:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif an_i == an_j:
                    if luna_i>luna_j:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
                    elif luna_i == luna_j:
                        if zi_i>zi_j:
                            aux = lista[i]
                            lista[i] = lista[j]
                            lista[j] = aux
                        elif zi_j == zi_i:
                            orar_j = lista[j].get_ora().split(":")
                            ora_j = orar_j[0]
                            minut_j = orar_j[1]
                            if ora_i>orar_j:
                                aux = lista[i]
                                lista[i] = lista[j]
                                lista[j] = aux
                            elif ora_i == ora_j:
                                if minut_i>minut_j:
                                    aux = lista[i]
                                    lista[i] = lista[j]
                                    lista[j] = aux

        return lista


    def exporta_final(self,file_path_new,evenimente):
         self.__repo_eveniment.write_all_to_rez_file(file_path_new,evenimente)















