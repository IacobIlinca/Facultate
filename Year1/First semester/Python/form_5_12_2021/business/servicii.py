from domain.entitati import ProbLab
class Service_prob_lab:

    def __init__(self, valid_prob_lab, repo_prob_lab):
        self.__valid_prob_lab = valid_prob_lab
        self.__repo_prob_lab = repo_prob_lab

    def adauga_prob_lab(self, nr_lab, descriere, deadline):
        prob = ProbLab(nr_lab, descriere,deadline)
        self.__valid_prob_lab.valideaza(prob)
        self.__repo_prob_lab.adauga_prob_lab(prob)

    def cauta_prob(self, nr_lab):
        prob_cautat = self.__repo_prob_lab.cauta_prob(nr_lab)
        file_path_rez = "rezultate.txt"
        with open(file_path_rez, "a") as f:
            f.write("\nlab-ul este:" + "\n" + str(prob.get_nr_lab()) + "," + str(prob.get_descriere()) + "," + str(
                prob.get_deadline()))
