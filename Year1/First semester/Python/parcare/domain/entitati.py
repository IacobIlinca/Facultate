class Loc():

    def __init__(self, id, nume, strada, nr_utiliz):
        self.__id = id
        self.__nume = nume
        self.__strada = strada
        self.__nr_utiliz = nr_utiliz

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_strada(self):
        return self.__strada

    def get_nr_utiliz(self):
        return self.__nr_utiliz

    def __eq__(self, other):
        return self.__id == other.get_id()

    def __str__(self):
        return "["+str(self.__id)+"]"+self.__nume+":"+self.__strada+"->"+str(self.__nr_utiliz)