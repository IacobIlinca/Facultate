class Elicopter():

    def __init__(self, id, nume, scopuri, an):
        self.__id = id
        self.__nume = nume
        self.__scopuri = scopuri
        self.__an = an

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_scopuri(self):
        return self.__scopuri

    def get_an(self):
        return self.__an

    def __eq__(self, other):
        return self.__id == other.get_id()

    def __str__(self):
        return "Elicopterul [" + str(self.__id)+"] cu numele: "+self.__nume+", avand scopurile:"+self.__scopuri+", din anul:"+str(self.__an)


