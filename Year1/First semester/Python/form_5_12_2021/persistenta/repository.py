from erori.exceptii import RepositoryError
from domain.entitati import ProbLab
class Repo_prob_lab:

    def __init__(self):
        self._prob_lab = []

    def adauga_prob_lab(self, prob):
        for _prob in self._prob_lab:
            if _prob == prob:
                raise RepositoryError("prob existenta!")
        self._prob_lab.append(prob)

    def __len__(self):
        return len(self._prob_lab)

    def get_all(self):
        return self._prob_lab[:]

    def cauta_prob(self, nr_lab):
        ok = True
        for _prob in self._prob_lab:
            if int(_prob.get_nr_lab()) == nr_lab:
                return _prob
        if ok:
            raise RepositoryError("tranzactie inexistenta!")

class Repo_prob_lab_file(Repo_prob_lab):

    def __init__(self, file_path):
        self.__file_path = file_path
        Repo_prob_lab.__init__(self)

    def read_all_from_file(self):
        self._prob_lab= []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line=line.strip()
                if len(line)>0:
                    parts=line.split(",")
                    nr_lab = parts[0]
                    descriere = parts[1]
                    deadline = parts[2]
                    prob_lab = ProbLab(nr_lab, descriere, deadline)
                    self._prob_lab.append(prob_lab)

    def append_to_file(self, prob):
        with open(self.__file_path, "a") as f:
            f.write("\n"+str(prob.get_nr_lab())+","+prob.get_descriere()+","+str(prob.get_deadline()))

    def adauga_prob_lab(self, prob):
        self.read_all_from_file()
        Repo_prob_lab.adauga_prob_lab(self, prob)
        self.append_to_file(prob)

    def get_all(self):
        self.read_all_from_file()
        return Repo_prob_lab.get_all(self)

    def cauta_tranz(self, nr_lab):
        self.read_all_from_file()
        prob = Repo_prob_lab.cauta_prob(self, nr_lab)
        return prob
