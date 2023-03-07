from exceptii.erori import RepositoryEror
from domain.entities import Emisiune
class RepoEmisiuni:

    def __init__(self):
        self._emisiuni = []

    def get_all(self):
        return self._emisiuni[:]

    def sterge_emisiune(self,nume,tip):
        """

        :return:
        """
        ok = True
        for em in self._emisiuni:
            if em.get_nume() == nume and em.get_tip() == tip:
                self._emisiuni.remove(em)
                ok = False
        if ok == True:
            raise RepositoryEror("nu exista!")


    def update_emisiune(self,nume,dur_noua,desc_noua):
        for emi in self._emisiuni:
            if emi.get_nume() == nume:
                emi.set_durata(dur_noua)
                emi.set_descriere(desc_noua)

class FileRepoEmisiuni(RepoEmisiuni):
    def __init__(self, file_path):
        RepoEmisiuni.__init__(self)
        self.__file_path = file_path

    def read_all_from_file(self):
        self._emisiuni = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    nume = parts[0]
                    tip = parts[1]
                    durata = parts[2]
                    descriere = parts[3]
                    emisiune = Emisiune(nume,tip,durata,descriere)
                    self._emisiuni.append(emisiune)

    def append_to_file(self,emisiune):
        with open(self.__file_path, "a") as f:
            f.write(str(emisiune.get_nume()) + "," + str(emisiune.get_tip()) + "," + str(emisiune.get_durata()) + "," +str(emisiune.get_descriere()))

    def write_all_to_file(self):
        with open(self.__file_path, "w") as f:
            for emi in self._emisiuni:
                f.write(str(emi.get_nume()) + "," + str(emi.get_tip()) + "," + str(emi.get_durata()) + "," +str(emi.get_descriere()))

    def write_to_another_file(self,file_path,lista):
        f = open(file_path, "w")
        for emi in lista:
            emi_f = str(emi.get_nume()) + "," + str(emi.get_tip()) + "," + str(emi.get_durata()) + "," +str(emi.get_descriere())
            emi_f += "\n"
            f.write(emi_f)
        # with open(file_path, "w") as f:
        #     for emi in lista:
        #         f.write(str(emi.get_nume()) + "," + str(emi.get_tip()) + "," + str(emi.get_durata()) + "," + str(emi.get_descriere()))

    def sterge_emisiune(self,nume,tip):
        self.read_all_from_file()
        RepoEmisiuni.sterge_emisiune(self,nume,tip)
        self.write_all_to_file()

    def update_emisiune(self,nume,dur_noua,desc_noua):
        self.read_all_from_file()
        RepoEmisiuni.update_emisiune(self,nume,dur_noua,desc_noua)
        self.write_all_to_file()

    def get_all(self):
        self.read_all_from_file()
        return RepoEmisiuni.get_all(self)
