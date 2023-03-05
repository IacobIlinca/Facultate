class NotaDTO():

    def __init__(self, id_nota, id_disc, id_stud, valoare):
        self.__id_nota = id_nota
        self.__id_stud = id_stud
        self.__stud = None
        self.__id_disc = id_disc
        self.__disc = None
        self.__valoare = valoare

    def get_id_nota(self):
        return self.__id_nota

    def get_id_disc(self):
        return self.__id_disc

    def get_id_stud(self):
        return self.__id_stud

    def get_valoare(self):
        return self.__valoare

    def get_stud(self):
        return self.__stud

    def set_stud(self, value):
        self.__stud = value

    def get_disc(self):
        return self.__disc

    def set_disc(self, value):
        self.__disc = value

    def __str__(self):
        return self.__stud.get_nume()+"["+str(self.__valoare)+"]"

class DiscNoteDTO():
    def __init__(self, nume_disc, lista_studenti):
        self.__nume_disc = nume_disc
        self.__lista_studenti = lista_studenti

    def __str__(self):
        st = ""
        st+= self.__nume_disc+":\n"
        for student in self.__lista_studenti:
            st+= "\t"+str(student)+"\n"
        return st
