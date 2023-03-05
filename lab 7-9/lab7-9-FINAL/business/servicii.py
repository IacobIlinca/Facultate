import random
import string

from domain.entitati import Student, Disciplina, Nota, NoteStudentDTO, NotaGeneralaStudentDTO, DisciplinaNrNoteDTO, \
    DiscStudNrNoteDTO
from erori.exceptii import RepositoryError, StudentNotFoundException, DisciplinaNotFoundException
from domain.dtos import DiscNoteDTO, NotaDTO
from sorters.sorters import MergeSorter, BingoSorter, comparare_noua, comparare_noua2


class ServiceStudenti:
    def __init__(self, valid_student, repo_studenti):
        self.__valid_student = valid_student
        self.__repo_studenti = repo_studenti

    def get_nr_studenti(self):
        return len(self.__repo_studenti)

    def get_all_studenti(self):
        studenti = self.__repo_studenti.get_all_students()
        for student in studenti:
            print(student)

    def get_all_stud(self):
        return self.__repo_studenti.get_all_students()

    def adauga_student(self, id_stud, nume):
        # functie care adauga un student cu id-ul id_stud(int) si numele nume(string)
        # input: id_stud - int
        #        nume - string
        # output: -, daca totul reuseste cu succes
        # raises: RepositoryError sau ValidationError
        student = Student(id_stud, nume)
        self.__valid_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)

    def cautare_student(self, id_stud):
        # functie care cauta dupa id un student cu id-ul id_stud(int)
        # input: id_stud - int
        # output: studentul stud daca id-ul e in lista
        # raises: id inexistent, daca id-ul nu e in lista
        stud = self.__repo_studenti.cauta_dupa_id(id_stud)
        return stud

    def modifica_student(self, id_stud, nume):
        # functie care modifica numele unui student cu id-ul id_stud(int) coul nume nume(string)
        # input: id_stud - int
        #        nume - string
        # output: -, daca totul reuseste cu succes
        # raises: RepositoryError sau ValidationError
        self.__repo_studenti.modifica_student(id_stud, nume)

    def sterge_student(self, id_stud, n):
        # functie care sterge un student cu id-ul id_stud(int)
        # input: id_stud - int
        # output: -, daca totul reuseste cu succes
        # raises: id inexistent, daca id-ul nu e in lista
        self.__repo_studenti.sterge_student(id_stud, n)

    def generate_random_id_stud(self):
        return random.randrange(1, 10000000)

    def generate_random_nume(self):
        nume_lungime = random.randrange(1, 10)
        nume = ""
        for _ in range(nume_lungime):
            nume = nume + random.choice(string.ascii_letters)
        return nume

    def generate_random_student(self, x):
        err = ""
        for _ in range(x):
            id_stud = self.generate_random_id_stud()
            nume = self.generate_random_nume()
            try:
                self.adauga_student(id_stud, nume)
            except RepositoryError as re:
                print(re)
            """
            if ok == 1:
                err += "numarul complex nu e in lista!\n"
            if len(err) > 0:
                raise Exception(err)
            """


class ServiceDiscipline (object):

    def __init__(self, valid_disciplina, repo_discipline):
        self.__valid_disciplina = valid_disciplina
        self.__repo_discipline = repo_discipline

    def get_nr_discipline(self):
        """
        :return: numarul de discipline din lista data
        """
        return len(self.__repo_discipline)

    def get_all_discipline(self):
        """
        :return: returneaza lista de discipline
        """
        discipline = self.__repo_discipline.get_all_diciplines()
        for disciplina in discipline:
            print(disciplina)

    def get_all(self):
        """
        :return: returneaza lista de discipline
        """
        return self.__repo_discipline.get_all_diciplines()

    def tura2_comp_noua(self):
        """
        Functie ce foloseste compararea noua:ordoneaza disciplinele dupa nume, mai apoi dupa profesor
        :return: lista de discipline ordonata crescator
        """
        disc = self.__repo_discipline.get_all_diciplines()
        # for d in disc:
        #     print(str(d))
        sorter = MergeSorter()
        sorter.sort(disc, cmp=comparare_noua2)
        return disc

    def adauga_disciplina(self, id_disc, nume, profesor):
        """
        functie care adauga o disciplina cu id-ul id_disc(int), numele nume(string) si profesorul profesor(string)
        input: id_disc - int
               nume - string
               profesor - string
        output: -, daca totul reuseste cu succes
        raises: RepositoryError sau ValidationError
        """
        disciplina = Disciplina(id_disc, nume, profesor)
        self.__valid_disciplina.valideaza(disciplina)
        self.__repo_discipline.adauga_disciplina(disciplina)

    def cautare_disciplina(self, id_disc):
        """
        functie care cauta dupa id o disciplina cu id-ul id_disc(int)
        input: id_disc - int
        output: disc, disciplina cu id-ul cautat
        raises: id inexistent, daca id-ul nu e in lista
        """
        disc = self.__repo_discipline.cauta_dupa_id_disc(id_disc)
        return disc

    def modifica_disciplina(self, id_disc, profesor):
        """
        functie care adauga o modifica cu id-ul id_disc(int) cu noul nume al profesorului profesor(string)
        input: id_disc - int
               profesor - string
        output: -, daca totul reuseste cu succes
        raises: id inexistent, daca id-ul nu e in lista
        """
        self.__repo_discipline.modifica_disciplina(id_disc, profesor)

    def sterge_disciplina(self, id_disc_sters, n):
        """
        functie care sterge o disciplina cu id-ul id_disc(int)
        input: id_disc - int
        output: -, daca totul reuseste cu succes
        raises: id inexistent, daca id-ul nu e in lista
        """
        self.__repo_discipline.sterge_disciplina(id_disc_sters, n)

    def generate_random_id_disc (self):
        return random.randrange(1,10000000)

    def generate_random_nume(self):
        nume_lungime = random.randrange(1, 10)
        nume = ""
        for _ in range (nume_lungime):
            nume = nume + random.choice(string.ascii_letters)
        return nume

    def generate_random_profesor(self):
        prof_lungime = random.randrange(1, 10)
        prof = ""
        for _ in range (prof_lungime):
            prof = prof + random.choice(string.ascii_letters)
        return prof

    def generate_random_disciplina (self, x):
        err = ""
        for _ in range (x):
            id_disc = self.generate_random_id_disc()
            nume = self.generate_random_nume()
            prof = self.generate_random_profesor()
            try:
                self.adauga_disciplina(id_disc,nume, prof)
            except RepositoryError as re:
                print (re)
class ServiceNote():
    def __init__(self, repo_note, valid_nota, repo_studenti, repo_discipline):
        self.__repo_note = repo_note
        self.__valid_nota = valid_nota

        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline

    # def studenti_alfabetic(self, id_disc):
    #
    #     discipline = self.__repo_discipline.get_all_diciplines()
    #     discipline2 = []
    #     for disc in discipline:
    #         note = self.__repo_note.note_disciplina(disc.get_id_disc())
    #         x = [student.get_nume(), note]
    #         studenti2.append(x)
    #     studenti_sorted = sorted(studenti2, key=lambda elem: (elem[0]))
    #     return studenti_sorted
    #
    # def studenti_alfabetic_c(self, id_disc):
    #
    #     studenti = self.__repo_studenti.get_all_students()
    #     studenti2 = []
    #     for student in studenti:
    #         note = self.__repo_note.note_student(student.get_id_stud())
    #         x = [student.get_nume(), note]
    #         studenti2.append(x)
    #     studenti_sorted = sorted(studenti2, key=lambda elem: (elem[0]))
    #     return studenti_sorted

    def cauta_nota_dupa_id(self, id_nota):
        """
        o functie care cauta o nota dupa un id dat
        :param idNota - id-ul notei
        :return un obiect de tipul Nota
        """
        return self.__repo_note.cauta_nota_dupa_id(id_nota)

    def get_nr_note(self):
        return len(self.__repo_note)

    def adauga_nota(self,id_nota, id_stud, id_disc, valoare):
        """
        metoda ce adauga o nota
        input: id_student- id-ul studentului (int)
              id_disciplina- id-ul disciplinei (int)
              valoare- valoarea notei asignate (float)
        output: Nota adaugata!
        raises: StudentNotFoundException daca nu exista produs cu id dat
               StudentNotFoundException daca nu exista magazin cu id dat
               ValidationException daca item-ului nu e valid
               StudentAlreadyAssigned daca item-ul deja exista
        """
        student = self.__repo_studenti.cauta_dupa_id(id_stud)
        disciplina = self.__repo_discipline.cauta_dupa_id_disc(id_disc)
        nota = Nota(id_nota, id_stud, id_disc, valoare)
        nota.set_student(student)
        nota.set_disciplina(disciplina)
        #print(nota)
        self.__valid_nota.validate(nota)
        self.__repo_note.adauga_nota(nota)

    def sterge_nota(self, id_nota):
        """
        :functie care sterge din lista nota cu id-ul dat
        :param id_nota: id-ul notei ce se doreste a fi stearsa
        :return: lista modificata
        """
        self.__repo_note.sterge_nota(id_nota)

    def update_nota(self, id_nota, valoare_noua):
        #o functie care face update la valoarea unei note identificata prin idNota
        #input: id_nota - id-ul notei
        #       valoare_noua-noua valoare a notei
        # nota = self.cauta_nota_dupa_id(id_nota)
        # student = nota.get_student()
        # disciplina = nota.get_disciplina()
        # nota_noua = Nota(id_nota, student, disciplina, valoare_noua)
        # self.__valid_nota.validate(nota_noua)
        # self.__repo_note.update_nota(id_nota, nota_noua)
        self.__repo_note.update_nota(id_nota, valoare_noua)

    def get_note_la_o_disciplina_alfabetic(self, id_disciplina):
        #o functie care returneaza toti studentii ordonati alfabetic si notele lor la o disciplina
        #input:id_disciplina - id-ul disciplinei
        #output:o lista de obiecte de tipul NoteStudentDTO
        disciplina = self.__repo_discipline.cauta_dupa_id(id_disciplina)
        lista = []
        toate_note = self.__repo_note.get_all()
        note_la_disciplina = []
        for nota in toate_note:
            if nota.get_id_disciplina() == id_disciplina:
                stud_nota = []
                student = self.__repo_studenti.cauta_dupa_id(nota.get_id_student())
                nota.set_student(student)
                stud_nota.append(nota.get_student())
                stud_nota.append(nota.get_valoare())
                lista.append(stud_nota)
                ok = 0
        def takefirst(elem):
            return elem[0].get_nume()
        lista.sort(key= takefirst, reverse = False)

        note_dto = NoteStudentDTO(disciplina.get_nume(), lista)
        return note_dto




        #         note_la_disciplina.append(nota)
        # for i in range(len(note_la_disciplina) - 1):
        #     for j in range(i + 1, len(note_la_disciplina)):
        #         student = self.__repo_studenti.cauta_dupa_id()
        #         if note_la_disciplina[i].get_student().get_nume() > note_la_disciplina[j].get_student().get_nume():
        #             aux = note_la_disciplina[i]
        #             note_la_disciplina[i] = note_la_disciplina[j]
        #             note_la_disciplina[j] = aux
        # note_studenti = {}
        # for nota in note_la_disciplina:
        #     student = nota.get_student()
        #     if student.get_id_stud() not in note_studenti:
        #         note_studenti[student.get_id_stud()] = []
        #     note_studenti[student.get_id_stud()].append(nota.get_valoare())
        #
        # rezultat = []
        # for note_student in note_studenti:
        #     id_stud = note_student
        #     student = self.__repo_studenti.cauta_dupa_id(id_stud)
        #     lista_note = note_studenti[note_student]
        #     nota_student_dto = NoteStudentDTO(student.get_nume(), lista_note)
        #     rezultat.append(str(nota_student_dto))
        # return rezultat

    def get_all(self):
        return self.__repo_note.get_all()


    def get_note_la_o_disciplina_dupa_nota(self, id_disciplina):
        #o functie care returneaza toti studentii ordonati dupa nota si notele lor la o disciplina
        #input: id_disciplina - id-ul disciplinei
        #output: o lista de obiecte de tipul NoteStudentDTO

        disciplina = self.__repo_discipline.cauta_dupa_id(id_disciplina)
        lista = []
        toate_note = self.__repo_note.get_all()
        note_la_disciplina = []
        for nota in toate_note:
            if nota.get_id_disciplina() == id_disciplina:
                stud_nota = []
                student = self.__repo_studenti.cauta_dupa_id(nota.get_id_student())
                nota.set_student(student)
                stud_nota.append(nota.get_student())
                stud_nota.append(nota.get_valoare())
                lista.append(stud_nota)
                ok = 0

        def takefirst(elem):
            return elem[1]
        sorter = MergeSorter()
        sorter.sort(lista,key=takefirst, reversed=False)

        note_dto = NoteStudentDTO(disciplina.get_nume(), lista)
        return note_dto



        # disciplina = self.__repo_discipline.cauta_dupa_id_disc(id_disciplina)
        # toate_note = self.__repo_note.get_all()
        # note_la_disciplina = []
        # for nota in toate_note:
        #     if nota.get_disciplina() == disciplina:
        #         note_la_disciplina.append(nota)
        # note_studenti = {}
        # for nota in note_la_disciplina:
        #     student = nota.get_student()
        #     if student.get_id_stud() not in note_studenti:
        #         note_studenti[student.get_id_stud()] = []
        #     note_studenti[student.get_id_stud()].append(nota.get_valoare())
        # rezultat_neordonat = []
        # for note_student in note_studenti:
        #     id_stud = note_student
        #     student = self.__repo_studenti.cauta_dupa_id(id_stud)
        #     lista_note = note_studenti[note_student]
        #     nota_student_dto = NoteStudentDTO(student.get_nume(), lista_note)
        #     medie = 0
        #     for nota in lista_note:
        #         medie += nota
        #     medie = medie / len(lista_note)
        #     nota_tuplu = (str(nota_student_dto), medie)
        #     rezultat_neordonat.append(nota_tuplu)
        # for i in range(len(rezultat_neordonat)-1):
        #     for j in range(i+1, len(rezultat_neordonat)):
        #         if rezultat_neordonat[i][1] < rezultat_neordonat[j][1]:
        #             aux = rezultat_neordonat[i]
        #             rezultat_neordonat[i] = rezultat_neordonat[j]
        #             rezultat_neordonat[j] = aux
        # rezultat = []
        # for nota in rezultat_neordonat:
        #     rezultat.append(nota[0])
        # return rezultat

    def medie_generala(self):
        #functie care calculeaza media generala a notelor tuturor studentilor la toate disciplinele
        #output: o lista de liste de forma [student, medie generala]
        studenti = self.__repo_studenti.get_all_students()
        discipline = self.__repo_discipline.get_all_diciplines()
        note = self.__repo_note.get_all()
        note_gen = []
        for student in studenti :
            student_medie = [0, 0]
            student_medie[0] = student
            medie_generala = 0
            for disciplina in discipline :
                medie_disciplina = 0
                nr_note_disc = 0
                for nota in note:
                    if nota.get_id_student() == student.get_id_stud() and nota.get_id_disciplina() == disciplina.get_id_disc():
                        medie_disciplina = medie_disciplina + nota.get_valoare()
                        nr_note_disc = nr_note_disc + 1
                if nr_note_disc !=0 :
                    medie_disciplina = medie_disciplina / nr_note_disc
                medie_generala = medie_generala + medie_disciplina
            if len(discipline)!=0 :
                medie_generala = medie_generala / len(discipline)
            student_medie[1] = medie_generala
            note_gen.append(student_medie)
            return note_gen

    def get_20_studenti_nota (self):
        #functie ce returneaza primii 20% studenti ordonati dupa media generala la toate disciplinele
        #output:primii 20% din studentii existenti cu media cea mai mare [nume_stud, medie]
        note_gen = self.medie_generala()
        for i in range (len(note_gen) -1):
            for j in range (i+1, len(note_gen)):
                if note_gen[i][1] < note_gen[j][1]:
                    aux =note_gen[i]
                    note_gen[i] = note_gen[j]
                    note_gen[j] = aux
        douazeci = []
        lungime = len(self.__repo_studenti)
        lungime = lungime *20/100
        i = 0
        while i< lungime:
            nota = note_gen[i]
            nota_dto = NotaGeneralaStudentDTO(nota[0].get_nume(), nota[1])
            douazeci.append(nota_dto)
            i=i+1
        return douazeci

    def get_discipline_cele_mai_multe_note(self):
        lista_disc = self.__repo_discipline.get_all_diciplines()
        lista_nr_note = []
        for disc in lista_disc:
            nr_note = 0
            id_disc = disc.get_id_disc()
            note = self.__repo_note.get_all()
            for _nota in note:
                if _nota.get_id_disciplina() == id_disc:
                    nr_note +=1

            if len(note) == 0:
                raise RepositoryError("Nu sunt note!")
                return

            disc_nr_note = []
            disc_nr_note.append(disc)
            disc_nr_note.append(nr_note)
            lista_nr_note.append(disc_nr_note)

        lista_nr_note = lista_nr_note[0:3]

        def __takesecond(elem):
            return elem[1]

        # lista_nr_note.sort(reverse = True, key = __takesecond)
        sorter = BingoSorter()

        sorter.sort(lista_nr_note, key=__takesecond, reversed=True)

        lista = []
        for el in lista_nr_note:
            disc = el[0]
            nr_note = el[1]
            disc_nr_note = DiscStudNrNoteDTO(disc, nr_note)
            lista.append(disc_nr_note)

        return lista

    def comparare_noua_srv(self):
        sorter = MergeSorter()
        note = self.__repo_note.get_all()
        sorter.sort(note, cmp=comparare_noua)
        return note






        # toate_discipline = self.__repo_discipline.get_all_diciplines()
        # toate_note = self.__repo_note.get_all()
        # disciplina_nr_note = {}
        # for disciplina in toate_discipline:
        #     if disciplina.get_id_disc() not in disciplina_nr_note:
        #         disciplina_nr_note[disciplina.get_id_disc()] = 0
        #     for nota in toate_note:
        #         if nota.get_disciplina() == disciplina:
        #             disciplina_nr_note[disciplina.get_id_disc()] += 1
        # rezultat = []
        # nrDis = 0
        # for contor in range(len(disciplina_nr_note)-1):
        #     if nrDis < 3:
        #         nrmax = 0
        #         idDis = -1
        #         for disciplina in disciplina_nr_note:
        #             if disciplina_nr_note[disciplina] > nrmax:
        #                 nrmax = disciplina_nr_note[disciplina]
        #                 idDis = disciplina
        #         disciplina = self.__repo_discipline.cauta_dupa_id_disc(idDis)
        #         disciplinaNrNote = DisciplinaNrNoteDTO(disciplina.get_nume(), nrmax)
        #         rezultat.append(disciplinaNrNote)
        #         nrDis +=1
        #         disciplina_nr_note.pop(idDis)
        #         contor -= 1
        # return rezultat

    def get_all_note_file(self):
        note_dtos = self.__repo_note.get_all()
        note_disc_stud = {}
        for nota_dto in note_dtos:
            stud = self.__repo_studenti.cauta_dupa_id(nota_dto.get_id_student())
            disc = self.__repo_discipline.cauta_dupa_id(nota_dto.get_id_disciplina())
            nota_dto.set_student(stud)
            nota_dto.set_disciplina(disc)
            if disc.get_id_disc() not in note_disc_stud:
                note_disc_stud[disc.get_id_disc()] = []
            note_disc_stud[disc.get_id_disc()].append(nota_dto)
        rezultat = []
        for disc_stud in note_disc_stud:
            id_disc = disc_stud
            disc = self.__repo_discipline.cauta_dupa_id_disc(id_disc)
            studenti = note_disc_stud[disc_stud]
            disc_stud_dto = DiscNoteDTO(disc.get_nume(), studenti)
            rezultat.append(disc_stud_dto)
        return rezultat



