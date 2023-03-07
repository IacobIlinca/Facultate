from domain.entitati import Loc
class RepoLocuriParc():

    def __init__(self):
        self._locuri = []

    def get_all(self):
        return self._locuri[:]

class RepoLocuriParcFile(RepoLocuriParc):

    def __init__(self,file_path):
        self.__file_path = file_path
        RepoLocuriParc.__init__(self)

    def read_all_from_file(self):
        self._locuri = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id = parts[0]
                    nume = parts[1]
                    strada = parts[2]
                    nr_utiliz = parts[3]
                    loc = Loc(id, nume, strada,nr_utiliz)
                    self._locuri.append(loc)

    def get_all(self):
        self.read_all_from_file()
        return RepoLocuriParc.get_all(self)
