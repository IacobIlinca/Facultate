from domain.entitati import ProbLab
from validatori.ValidProbLab import Validator_problema_lab
from erori.exceptii import ValidationError
from persistenta.repository import Repo_prob_lab
class Teste:
    def creeaza_prob_lab(self):
        nr_lab = 12
        descriere = "disecrii_broaste"
        deadline = 20
        prob_lab = ProbLab( nr_lab, descriere, deadline)
        assert prob_lab.get_nr_lab() == nr_lab
        assert prob_lab.get_descriere() == descriere
        assert prob_lab.get_deadline() == deadline

    def creeaza_inv(self):
        inv_nr = -12
        inv_descriere = ""
        inv_deadline = 90
        inv_prob = ProbLab(inv_nr, inv_descriere, inv_deadline)
        valid = Validator_problema_lab()
        try:
            valid.valideaza(inv_prob)
            assert False
        except ValidationError as ve:
            #print(str(ve))
            assert str(ve) == "id numeric invalid!descriere invalida!deadline invalid!"

    def test_adauga_repo(self):
        repo = Repo_prob_lab()
        assert len(repo) == 0
        nr_lab = 2
        descriere = "ana"
        deadline = 8
        prob = ProbLab(nr_lab, descriere, deadline)
        repo.adauga_prob_lab(prob)
        assert len(repo) == 1





    def run(self):
        print ("start tests...")
        self.creeaza_prob_lab()
        self.creeaza_inv()
        self.test_adauga_repo()
        print("finished tests succesfully!")