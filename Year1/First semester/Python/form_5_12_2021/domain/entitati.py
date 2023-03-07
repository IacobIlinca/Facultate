class ProbLab(object):

    def __init__(self, nr_lab, descriere, deadline):
        self.__nr_lab = nr_lab
        self.__descriere =descriere
        self.__deadline =  deadline

    def get_nr_lab(self):
        return self.__nr_lab

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_descriere(self, value):
        self.__descriere = value

    def set_deadline(self, value):
        self.__deadline = value

    def __eq__(self, other):
        return self.__nr_lab == other.get_nr_lab()

    def __str__(self):
        return "Numarul laboratorului: "+str(self.__nr_lab)+"cu descrierea: "+str(self.__descriere)+"deadline ["+str(self.__deadline)+"]"

    __repr__= __str__