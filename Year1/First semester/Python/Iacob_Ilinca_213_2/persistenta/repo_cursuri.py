from domain.entitati import Curs
class RepoCursuri():

    def __init__(self):
        self._cursuri = []

    def get_all(self):
        #functie care returneaza toate entitatile
        return self._cursuri[:]

    def __len__(self):
        #functie care returneaza numarul de entitati
        return len(self._cursuri)

class RepoCursuriFile(RepoCursuri):

    def __init__(self, file_path):
        RepoCursuri.__init__(self)
        self.__file_path = file_path

    def read_all_from_file(self):
        #functie care realizeaza citirea tuturor datelor din fisier
        self._cursuri = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id_curs = parts[0]
                    limba_straina = parts[1]
                    nivel = parts[2]
                    pret_pe_ora = parts[3]
                    curs = Curs(id_curs, limba_straina, nivel, pret_pe_ora)
                    self._cursuri.append(curs)

    def get_all(self):
        #functie care returneaza toate entitatile din fisier
        self.read_all_from_file()
        return RepoCursuri.get_all(self)

    def __len__(self):
        #functie care calculeaza numarul de entitati din fisier
        self.read_all_from_file()
        return len (RepoCursuri.get_all(self))