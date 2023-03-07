from erori.exceptii import RepositoryError
from domain.entitati import Eveniment
class RepoEvenimente():

    def __init__(self):
        self._evenimente = []

    def __len__(self):
        return len(self._evenimente)

    def get_all(self):
        return self._evenimente[:]

    def adauga_eveniment(self,eveniment):
        """
        adauga un eveniment in lista de evenimente
        :param eveniment: evenimentul de tip eveniment ce va fi adaugat
        :return: mesaj daca e adaugat cu succes
        :raise: exceptie daca evenimrnul e deja in lista
        """
        for ev in self._evenimente:
            if ev == eveniment:
                raise RepositoryError("eveniment existent")
        self._evenimente.append(eveniment)

class FileRepoEvenimente(RepoEvenimente):

        def __init__(self, file_path):
            RepoEvenimente.__init__(self)
            self._file_path = file_path

        def __read_all_from_file(self):
            """
            citeste evenimentele din fisier
            :return:
            """
            self._evenimente = []
            with open(self._file_path,"r") as f:
                lines = f.readlines()
                for line in lines:
                    line.strip()
                    if len(line)>0:
                        parts = line.split(",")
                        data = parts[0]
                        ora = parts[1]
                        descriere = parts[2]
                        eveniment = Eveniment(data, ora, descriere)
                        self._evenimente.append(eveniment)

        def append_to_file(self,eveniment):
            """
            functie care adauga la finalul fisierului un eveniment
            :param eveniment: evenimentul  ce se doreste a fi adaugat
            :return: fisierul modificat
            """
            with open(self._file_path,"a") as f:
                f.write(str(eveniment.get_data())+","+str(eveniment.get_ora())+","+str(eveniment.get_descriere()+"\n"))

        def write_all_to_rez_file(self,file_path_rez,evenimente):
            """
            suprascrie continutul fisierului
            :return:
            """
            f = open(file_path_rez,"w")
            for event in evenimente:
                event_f = str(event.get_data()) + "," + str(event.get_ora()) + "," + str(event.get_descriere())
                event_f += "\n"
                f.write(event_f)
            # with open(file_path_rez, "w")as f:
            #     f.write(str(evenimente.get_data()) + "," + str(evenimente.get_ora()) + "," + str(evenimente.get_descriere() + "\n"))


        def adauga_eveniment(self,eveniment):
            """
            functie care adauga un evenimet in fisier
            :param eveniment: ev ce va fi adaugat
            :return:
            """
            self.__read_all_from_file()
            RepoEvenimente.adauga_eveniment(self, eveniment)
            self.append_to_file(eveniment)

        def get_all(self):
            self.__read_all_from_file()
            return RepoEvenimente.get_all(self)





