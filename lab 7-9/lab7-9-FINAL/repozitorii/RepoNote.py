from domain.entitati import Nota
from erori.exceptii import RepositoryError, StudentAlreadyAssignedException
from domain.dtos import NotaDTO

class RepoNote:
    def __init__(self):
        self._note = []

    def note_student(self, id_student):
        note = []
        for nota in self._note:
            if nota.get_student().get_id_stud() == id_student:
                note.append(nota.get_valoare())
        return note

    def note_disciplina(self, id_disc):
        note = []
        for nota in self._note:
            if nota.get_disciplina().get_id_disc() == id_disc:
                note.append(nota.get_valoare())
        return note

    def cauta_nota_dupa_id(self, id_nota):
        #o functie care incearca sa caute o nota dupa id in caz ca nu o gaseste ridica un RepoError cu textul "Nota inexistenta\n"
        #input: id_nota - id-ul notei
        #output: un obiect de tipul Nota
        gasit = False
        for nota in self._note:
            if nota.get_id_nota() == id_nota:
                gasit = True
                return nota
        if gasit == False:
            raise RepositoryError ("Nota inexistenta\n")

    def adauga_nota (self, nota):
        #metoda care adauga o nota
        #input: nota care se doreste a fi adaugata
        #output: raises ProductAlreadyAssignedException daca exista deja pentru student nota la disciplina data
        gasit = False
        for _nota in self._note:
            if _nota.get_id_nota() == nota.get_id_nota():
                gasit = True
                raise RepositoryError("Nota cu id deja existent\n")
        if gasit == False:
            self._note.append(nota)

    def sterge_nota(self, id_nota):
        # o functie care sterge o nota, identificabila dupa idNota, din lista de note
        #input:id_nota - id-ul notei

        for _nota in self._note:
            if _nota.get_id_nota() == id_nota:
                self._note.remove(_nota)
                return
        raise RepositoryError("Nota nu exista!")

        # nota = self.cauta_nota_dupa_id(id_nota)
        # self._note.remove(nota)

    def update_nota(self, id_nota, valoare_noua):
        #modifica valoarea unei note
        #input:id_nota - id-ul notei
        #      nota_noua - un obiect de tipul Nota ce are noile caracteristici dorite

        nota = self.cauta_nota_dupa_id(id_nota)

        nota.set_valoare(valoare_noua)

    def add_ran(self,nota):
        self._note.append(nota)

    def get_all(self):
        #Returneaza toate notele din lista
        #input: -
        #output: lista de note
        return self._note[:]

    def __len__(self):
        #returneaza lungimea listei
        return len(self._note)

class FileRepoNote(RepoNote):

    def __init__(self, file_path):
        self.__file_path = file_path
        RepoNote.__init__(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoNote.__len__(self)

    def __read_all_from_file(self):
        """
        :functie care citeste toate elementele dintr-un fisier
        :return: lista de note
        """
        self._note = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            contor = 1
            ok = 0
            for line in lines:
                line = line.strip()
                if (len(line) > 0):
                    if contor % 4 == 1:
                        id_nota = int(line)
                    elif contor % 4 == 2:
                        id_stud = int(line)
                    elif contor % 4 == 3:
                        id_disc = int(line)
                    elif contor % 4 == 0:
                        valoare = float(line)
                        ok = 1
                    contor += 1
                if ok == 1:
                    nota = Nota(id_nota, id_stud,id_disc, valoare)
                    ok = 0
                    self._note.append(nota)

    def get_all(self):
        """
        :return: functie care returneaza lista de note din fisier
        """
        self.__read_all_from_file()
        return RepoNote.get_all(self)

    def __append_to_file(self, nota):
        """
        :functie care adauga la  finalul fisierului o nota
        :param nota: nota ce se doreste a fi adaugata
        :return: lista de note/fisierul modificata
        """
        with open(self.__file_path, "a") as f:
            f.write("\n"+str(nota.get_id_nota())+"\n"+str(nota.get_id_student())+"\n"+str(nota.get_id_disciplina())+"\n"+str(nota.get_valoare()))


    def __file_overwrite(self):
        """
        :functie care suprascrie fisierul ce contine lista de note
        :return: lista de note/fisierul modificat
        """
        with open(self.__file_path, "w") as f:
            for nota in self._note:
                f.write("\n"+str(nota.get_id_nota())+"\n"+str(nota.get_id_student())+"\n"+str(nota.get_id_disciplina())+"\n"+str(nota.get_valoare()))

    def adauga_nota(self, nota):
        """
        :functia pentru repozitorul cu fisiere ce o nota in lista&fisier
        :param nota: nota ce se doreste a fi adaugata
        :return: lista de note/fisierul modificat
        """
        self.__read_all_from_file()
        RepoNote.adauga_nota(self, nota)
        self.__append_to_file(nota)

    def sterge_nota(self, id_nota):
        """
        :functia pentru repozitorul cu fisiere ce sterge o nota in lista&fisier
        :param id_nota: nota ce se doreste a fi stearsa
        :return: lista de note/fisierul modificat
        """
        self.__read_all_from_file()
        RepoNote.sterge_nota(self, id_nota)
        self.__file_overwrite()

    def update_nota(self, id_nota, valoare_noua):
        """
        :functia pentru repozitorul cu fisiere ce modifica valoarea unei note in lista&fisier
        :param id_nota: id-ul notei ce se doreste a fi modificata
        :param valoare_noua: noua valoare ce va fi atribuita notei
        :return: lista de note/fisierul modificat
        """
        self.__read_all_from_file()
        RepoNote.update_nota(self, id_nota, valoare_noua)
        self.__file_overwrite()

