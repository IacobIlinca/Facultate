class Student ():

    def __init__(self, id_stud, nume):
        self.__id_stud = id_stud
        self.__nume = nume

    def get_id_stud(self):
        return self.__id_stud

    def get_nume(self):
        return self.__nume

    def set_nume(self, value):
        self.__nume = value

    def __eq__(self, other):
        return self.__id_stud == other.__id_stud

    def __str__(self):
        return "["+str(self.__id_stud)+"]"+self.__nume

class Disciplina ():
    def __init__(self, id_disc, nume, profesor):
        self.__id_disc = id_disc
        self.__nume = nume
        self.__profesor = profesor

    def get_id_disc(self):
        return self.__id_disc

    def get_nume(self):
        return self.__nume

    def set_nume(self, value):
        self.__nume = value

    def get_profesor(self):
        return self.__profesor

    def set_profesor(self, value):
        self.__profesor = value

    def __eq__(self, other):
        return self.__id_disc == other.__id_disc

    def __str__(self):
        return "[" + str(self.__id_disc) + "]" + self.__nume + "->" + self.__profesor


class Nota():
    def __init__(self,id_nota,  id_student, id_disciplina, valoare):
        self.__id_nota = id_nota
        self.__student = None
        self.__disciplina = None
        self.__valoare = valoare
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina

    def get_id_nota(self):
        return self.__id_nota

    def get_id_student(self):
        return self.__id_student

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_student(self):
        return self.__student

    def get_disciplina(self):
        return self.__disciplina

    def get_valoare(self):
        return self.__valoare

    def set_student(self, value):
        self.__student = value

    def set_disciplina(self, value):
        self.__disciplina = value

    def set_valoare(self, value):
        self.__valoare = value

    def __eq__(self, other):
        return self.__id_nota == other.__id_nota

    def __str__(self):
        #return 'Student: [' + str(self.__student.get_nume()) + '; ' + '] Disciplina: [' + str(self.__disciplina.get_nume()) + '; ' + str(self.__disciplina.get_profesor()) + '] Valoare: ' + str(self.__valoare)
        return "Student: [ID:" + str(self.__id_student()) + ']; Disciplina: [ID:' + str(self.__id_disciplina()) + '; Valoare nota: ' + str(self.__valoare) +'{'+ str(self.__id_nota)+'}'


class DisciplinaNrNoteDTO(object):

    def __init__(self, numeDisciplina, nrNote):
        self.__numeDisciplina = numeDisciplina
        self.__nrNote = nrNote

    def __str__(self):
        st = ""
        st += self.__numeDisciplina + " " + str(self.__nrNote)
        return st

    def __eq__(self, other):
        return self.__numeDisciplina == other.__numeDisciplina and self.__nrNote == other.__nrNote


class NoteStudentDTO(object):

    def __init__(self, nume_stud, lista_note):
        self.__nume_stud = nume_stud
        self._lista_note = lista_note

    def __str__(self):
        st = ""
        st += str(self.__nume_stud) + ":\n"
        for nota in self._lista_note:
            st += "\t" + str(nota[0])+" "+str(nota[1]) + "\n"
        return st

    def __eq__(self, other):
        return self.__nume_stud == other.__nume_stud and self._lista_note == other._lista_note


class NotaGeneralaStudentDTO(object):

    def __init__(self, nume_stud, nota_generala):
        self.__nume_stud = nume_stud
        self.__nota_generala = nota_generala

    def __str__(self):
        st = ""
        st += self.__nume_stud + " " + str(self.__nota_generala)
        return st

    def __eq__(self, other):
        return self.__nume_stud == other.__nume_stud and self.__nota_generala == other.__nota_generala

class DisciplinaNrNoteDTO(object):

    def __init__(self, nume_disc, nr_note):
        self.__nume_disc = nume_disc
        self.__nr_note = nr_note

    def __str__(self):
        st = ""
        st+=self.__nume_disc + " " + str(self.__nr_note)
        return st

    def __eq__(self, other):
        return self.__nume_disc == other.__nume_disc and self.__nr_note == other.nr_note


class DiscStudNrNoteDTO():
    def __init__(self, disciplina, nr_note):
        self.__disciplina = disciplina
        self.__nr_note = nr_note

    def __str__(self):
        return str(self.__disciplina)+" are urm nr de note:"+str(self.__nr_note)
