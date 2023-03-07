from erori.exceptii import RepositoryError, StudentAlreadyAssignedException
from domain.entitati import Disciplina

class RepoDiscipline (object):

    def __init__(self):
        self._discipline = []

    def __len__(self):
        return len(self._discipline)

    def adauga_disciplina(self, disc):
        # metoda a clasei disciplina ce adauga o disciplina din lista
        # input: disc-disciplina ce se doreste a fi adaugata
        # output: lista modificata daca totul este ok
        for _disc in self._discipline:
            if _disc == disc:
                raise RepositoryError("id existent!")
        self._discipline.append(disc)


    def cauta_dupa_id_disc(self, id_disc):
        # metoda a clasei disciplina ce cauta dupa id o disciplin din lista
        # input: id_disc-id-ul disciplinei ce se doreste a fi cautata in lista
        # output: disciplina cu id-ul dorit, sau mesaj daca id-ul nu e in lista
        ok = True
        for _disc in self._discipline:
            if _disc.get_id_disc() == id_disc:
                return _disc

        return None
        """
        if ok:
            raise RepositoryError("id inexistent!")
        """

    def modifica_disciplina(self, id_disc, profesor):
        # metoda a clasei disciplina ce modifica numele profesorului unei discipline din lista
        # input: id_disc-id-ul disciplinei ce se doreste a fi modificata
        #        profesor-noul nume al profesorului
        # output: lista modificata daca totul este ok
        for _disc in self._discipline:
            if _disc.get_id_disc() == id_disc:
                _disc.set_profesor(profesor)


    def get_all_diciplines(self):
        """
        :return: functie care returneaza lista de discipline
        """
        return self._discipline[:]

    def sterge_disciplina(self, id_disc_sters , n=None):
        # metoda a clasei disciplina ce sterge o disciplina din lista
        # input: id_disc-id-ul disciplinei ce se doreste a fi stearsa din lista
        # output: lista modificata daca totul este ok, sau mesaj daca id-ul dat nu e in lista
        # lungime = len(self._discipline)
        # poz = -2
        # ok = True
        # for i in range (0, lungime):
        #     if self._discipline[i].get_id_disc() == id_disc :
        #         poz = i
        #         break
        # if poz!=-2:
        #
        #         self._discipline.remove(self._discipline[poz])
        # elif ok:
        #     raise RepositoryError("id inexistent!")
        if n == None:
            n = len(self._discipline)-1
        if n>=0:
            if self._discipline[n].get_id_disc() == id_disc_sters:
                self._discipline.remove(self._discipline[n])
                return
            else:
                return self.sterge_disciplina(id_disc_sters, n-1)
        else:
            raise RepositoryError("id inexistent!\n")


class FileRepoDiscipline(RepoDiscipline):
    def __init__(self, file_path):
        RepoDiscipline.__init__(self)
        self.__file_path = file_path

    def __read_all_from_file(self):

        """
        :functie care citeste toate elementele dintr-un fisier
        :return: lista de discipline
        """
        self._discipline = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            contor = 1
            ok=0
            for line in lines:
                line=line.strip()
                if (len(line)>0):
                    if contor%3==1:
                        id_disc = int(line)
                    elif contor%3==2:
                        nume = str(line)
                    elif contor%3==0:
                        profesor = str(line)
                        ok=1
                    contor+=1
                if ok==1:
                    disciplina = Disciplina(id_disc, nume, profesor)
                    ok=0
                    self._discipline.append(disciplina)

    def __append_to_file(self, disciplina):
        """
        :functie care adauga la  finalul fisierului o disciplina
        :param student: disciplina ce se doreste a fi adaugata
        :return: lista de discipline/fisierul modificata
        """
        with open(self.__file_path, "a") as f:
            f.write(str(disciplina.get_id_disc())+"\n"+disciplina.get_nume()+"\n"+disciplina.get_profesor()+"\n")

    def __file_overwrite(self):
        """
        :functie care suprascrie fisierul ce contine lista de discipline
        :return: lista de discipline/fisierul modificat
        """
        with open(self.__file_path, "w") as f:
            for _disc in self._discipline:
                f.write(str(_disc.get_id_disc()) + "\n" + str(_disc.get_nume()) + "\n" + str(_disc.get_profesor())+"\n")

    def adauga_disciplina(self, disciplina):
        """
        :functia pentru repozitorul cu fisiere ce adauga o disciplina in lista&fisier
        :param disciplina: disciplina ce se doreste a fi adaugata
        :return: lista de discipline/fisierul modificat
        """
        self.__read_all_from_file()
        RepoDiscipline.adauga_disciplina(self, disciplina)
        self.__append_to_file(disciplina)

    def cauta_dupa_id(self, id_disc):
        """
        :functie din repozitorul de fisier care cauta in lista o disciplina cu id-ul dat
        :param id_disc: id-ul disciplinei ce se doreste a fi cautat
        :return: disciplina gasita daca exista, sau un mesaj altfel
        """
        self.__read_all_from_file()
        return RepoDiscipline.cauta_dupa_id_disc(self, id_disc)

    def get_all_diciplines(self):
        """
        :return: lista de discipline
        """
        self.__read_all_from_file()
        return RepoDiscipline.get_all_diciplines(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoDiscipline.__len__(self)

    def modifica_disciplina(self, id_disc, profesor):
        """
        :functia pentru repozitorul cu fisiere ce modifica numele profesorului unei discipline in lista&fisier
        :param id_disc: id-ul disciplinei ce se doreste a fi modificata
        :param profesor: noul nume de profesor ce ii va fi atribuit disciplinei date
        :return: lista de discipline/fisierul modificat
        """
        self.__read_all_from_file()
        RepoDiscipline.modifica_disciplina(self, id_disc, profesor)
        self.__file_overwrite()

    def sterge_disciplina(self, id_disc_sters , n=None):
        """
        :functia pentru repozitorul cu fisiere ce sterge o disciplina in lista&fisier
        :param id_disc_sters: disciplina ce se doreste a fi stearsa
        :return: lista de discipline/fisierul modificat
        """
        self.__read_all_from_file()
        RepoDiscipline.sterge_disciplina(self, id_disc_sters)
        self.__file_overwrite()


