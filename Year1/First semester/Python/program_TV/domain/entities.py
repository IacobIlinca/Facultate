class Emisiune:

    def __init__(self, nume,tip,durata,descriere):
        self.__nume = nume
        self.__tip = tip
        self.__durata = durata
        self.__descriere = descriere

    def get_nume(self):
        return self.__nume

    def get_tip(self):
        return self.__tip

    def get_durata(self):
        return self.__durata

    def get_descriere(self):
        return self.__descriere

    def set_descriere(self,desc):
        self.__descriere = desc

    def set_durata(self,val):
        self.__durata = val

    def __eq__(self, other):
        return self.__nume == other.__nume or  self.__durata == other.__durata

    def __str__(self):
        return self.__nume + "," + self.__tip + "," + self.__durata + "," + self.__descriere
