from erori.exceptii import RepositoryError, StudentAlreadyAssignedException
from domain.entitati import Student

class RepoStudenti (object):

    def __init__(self):
        self._studenti = []

    def __len__(self):
        return len(self._studenti)

    def adauga_student(self,stud):
        #metoda a clasei studenti ce adauga un student in lista
        #input: stud-studentul ce se doreste a fi adaugat in lista
        #output: lista modificata daca totul este ok, sau mesaj daca id-ul exista deja in lista
        for _stud in self._studenti:
            if _stud == stud:
                raise RepositoryError("id existent!")
        self._studenti.append(stud)

    def adauga_student_recursiv(self, i ,stud):
        """
        :functie care adauga un student in lista recursiv
        :param i: indice
        :param stud: studentul ce se doreste a fi adaugat
        :return: lista modificata daca totul este ok, sau un mesaj daca id-ul exista deja in lista
        """
        if i>= len(self._studenti):
            self._studenti.append(stud)
            return
        elif self._studenti[i]==stud:
            raise RepositoryError("id existent!\n")
        else:
            self.adauga_student_recursiv(i+1, stud)


    def cauta_dupa_id(self, id_stud):
        # metoda a clasei studenti ce cauta dupa id un student in lista
        # input: id_stud-id-ul studentului ce se doreste a fi cautat in lista
        # output: studentul cu id-ul cautat, sau mesaj daca id-ul nu exista in lista
        """
        Complexitatea functiei este θ(n)
        Caz favorabil: primul element este cel cautat, se executa un singur pas, atunci T(n)=1, ce apartine de O(1)
        Caz defavorabil: nu esxista in lista studentul cu id-ul cautat, atunci se executa n pasi, T(n)=n, ce apartine de θ(n)
        Caz mediu: for-ul poate fi executat de 1,2,..,n ori(la fel de probabil oricare dintre variante), atunci T(n)=(n+1)/2, ce apartine de θ(n)
        """
        ok = True
        for _stud in self._studenti:
            if _stud.get_id_stud() == id_stud:
                return _stud
        return None

        # if ok:
        #     raise RepositoryError("id inexistent!")


    def modifica_student(self, id_stud, nume):
        # metoda a clasei studenti ce modifica numele unui student in lista
        # input: id_stud-id-ul studentului ce se doreste a fi modificat in lista
        #        nume- noul nume ce se doreste a fi dat studentului
        # output: lista modificata daca totul este ok
        for _stud in self._studenti:
            if _stud.get_id_stud() == id_stud:
                _stud.set_nume(nume)

    def get_all_students(self):
        """
        :functie care returneaza lista de studenti
        :return: lista de studenti
        """
        return self._studenti[:]

    def sterge_student(self, id_stud):
        # metoda a clasei studenti ce sterge un student in lista
        # input: id_stud-id-ul studentului ce se doreste a fi sters din lista
        # output: lista modificata daca totul este ok, sau mesaj daca id-ul dat nu e in lista
        lungime = len(self._studenti)
        poz = -2
        ok = True
        for i in range (0, lungime):
            if self._studenti[i].get_id_stud() == id_stud :
                poz = i
                break
        if poz!=-2:

                self._studenti.remove(self._studenti[poz])
        else:
            raise RepositoryError("id inexistent!")


    def sterge_student_recursiv(self, id_stud_sters, n=None):
        """
        :functie care sterge in mod recursiv un obiect de tipul student din lista
        :param id_stud_sters: id-ul studentului ce se doreste sa fie sters
        :param n: indice
        :return: lista modificata dupa stergerea studentului, sau mesaj daca studentul cu id-ul dat nu e in lista
        """
        if n == None:
            n = len(self._studenti)-1
        if n>=0:
            if self._studenti[n].get_id_stud() == id_stud_sters:
                self._studenti.remove(self._studenti[n])
                return
            else:
                return self.sterge_student_recursiv(id_stud_sters, n-1)
        else:
            raise RepositoryError("id inexistent!\n")


class FileRepoStudenti(RepoStudenti):
    def __init__(self, file_path):
        RepoStudenti.__init__(self)
        self.__file_path = file_path

    def __read_all_from_file(self):
        """
        :functie care citeste toate elementele dintr-un fisier
        :return: lista de studenti
        """
        self._studenti = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            contor = 1
            ok = 0
            for line in lines:
                line=line.strip()
                if (len(line)>0):
                    if contor%2==1:
                        id_stud = int(line)
                    elif contor%2==0:
                        nume = str(line)
                        ok=1
                    contor+=1

                if ok==1:
                    student = Student(id_stud, nume)
                    ok=0
                    self._studenti.append(student)

    def __append_to_file(self, student):
        """
        :functie care adauga la  finalul fisierului un student
        :param student: studentul ce se doreste a fi adaugat
        :return: lista de studenti/fisierul modificata
        """
        with open(self.__file_path, "a") as f:
            f.write("\n"+str(student.get_id_stud())+"\n"+student.get_nume())

    def __file_overwrite(self):
        """
        :functie care suprascrie fisierul ce contine lista de studenti
        :return: lista de studenti/fisierul modificat
        """
        with open(self.__file_path, "w") as f:
            for _stud in self._studenti:
                f.write("\n"+str(_stud.get_id_stud()) + "\n" + str(_stud.get_nume()) )

    def adauga_student(self,stud):
        """
        :functia pentru repozitorul cu fisiere ce adauga un student in lista&fisier
        :param stud: studentul ce se doreste a fi adaugat
        :return: lista de studenti/fisierul modificat
        """
        self.__read_all_from_file()
        RepoStudenti.adauga_student(self,stud)
        self.__append_to_file(stud)

    def cauta_dupa_id(self, id_stud):
        """
        :functie din repozitorul de fisier care cauta in lista un student cu id-ul dat
        :param id_stud: id-ul studentului ce se doreste a fi cautat
        :return: studentul gasit daca exista, sau un mesaj altfel
        """
        self.__read_all_from_file()
        return RepoStudenti.cauta_dupa_id(self, id_stud)

    def get_all_students(self):
        """
        :functie din repozitorul de fisier care returneaza lista de studenti din fisier
        :return: lista de studenti din fisier
        """
        self.__read_all_from_file()
        return RepoStudenti.get_all_students(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoStudenti.__len__(self)

    def modifica_student(self, id_stud, nume):
        """
        :functia pentru repozitorul cu fisiere ce modifica numele unui student in lista&fisier
        :param id_stud: id-ul studentului ce se doreste a fi modificat
        :param nume: noul nume ce ii va fi atribuit studentului dat
        :return: lista de studenti/fisierul modificat
        """
        self.__read_all_from_file()
        RepoStudenti.modifica_student(self, id_stud, nume)
        self.__file_overwrite()

    def sterge_student(self, id_stud_sters, n=None):
        """
        :functia pentru repozitorul cu fisiere ce sterge un student in lista&fisier
        :param stud: studentul ce se doreste a fi sters
        :return: lista de studenti/fisierul modificat
        """
        self.__read_all_from_file()
        RepoStudenti.sterge_student(self, id_stud_sters)
        self.__file_overwrite()