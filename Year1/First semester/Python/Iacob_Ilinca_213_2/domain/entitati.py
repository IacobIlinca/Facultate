class Curs():

    def __init__(self, id_curs, limba_straina, nivel, pret_pe_ora):
        self.__id_curs = id_curs
        self.__limba_straina = limba_straina
        self.__nivel = nivel
        self.__pret_pe_ora = pret_pe_ora

    def get_id_curs(self):
        return self.__id_curs

    def get_limba_straina(self):
        return self.__limba_straina

    def get_nivel(self):
        return self.__nivel

    def get_pret_pe_ora(self):
        return self.__pret_pe_ora

    def __eq__(self, other):
        return self.__id_curs == other.get_id_curs()

    def __str__(self):
        return "["+str(self.__id_curs)+"]"+self.__limba_straina+":la nivelul:"+str(self.__nivel)+"cu pretul pe ora ->"+str(self.__pret_pe_ora)

class Inscriere():

    def __init__(self, curs, numar_ore):
        self.__curs = curs
        self.__numar_ore = numar_ore

    def get_total(self):
        return int(self.__numar_ore) * int(self.__curs.get_pret_pe_ora())

    def __str__(self):
        return "Limba straina a cursului este:"+self.__curs.get_limba_straina()+"-> Nivelul cursului este:"+str(self.__curs.get_nivel())
