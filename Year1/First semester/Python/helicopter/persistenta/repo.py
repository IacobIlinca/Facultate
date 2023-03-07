from domain.entitati import Elicopter
class RepoElicopter():

    def __init__(self):
        self._elicoptere = []

    def get_all(self):
        return self._elicoptere[:]

    def __len__(self):
        return len(self._elicoptere)

class RepoElicopterFile(RepoElicopter):

    def __init__(self, file_path):
        RepoElicopter.__init__(self)
        self.__file_path = file_path

    def read_all_from_file(self):
        self._elicoptere = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in  lines:
                line = line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id = parts[0]
                    nume= parts[1]
                    scopuri = parts[2]
                    an = parts[3]
                    elic =  Elicopter(id, nume, scopuri,an)
                    self._elicoptere.append(elic)

    def get_all(self):
        self.read_all_from_file()
        return RepoElicopter.get_all(self)

    def __len__(self):
        self.read_all_from_file()
        return RepoElicopter.__len__(self)
