from domain.entitati import Disciplina
from validare.validatori import ValidatorDisciplina
from repozitorii.RepoDiscipline import RepoDiscipline
from business.servicii import ServiceDiscipline
from erori.exceptii import ValidationError, RepositoryError

import unittest


class Testedisc(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.disciplina = Disciplina(12, "analiza", "berinde")
        self.valid = ValidatorDisciplina()
        self.repo = RepoDiscipline()
        self.service = ServiceDiscipline(self.valid, self.repo)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_creeare_disciplina(self):
        self.assertEqual(self.disciplina.get_id_disc(),12)
        self.assertEqual(self.disciplina.get_nume(), "analiza")
        self.assertEqual(self.disciplina.get_profesor(), "berinde")

        alt_nume = "algebra"
        alt_profesor = "modoi"
        alta_disc = Disciplina(12, alt_nume, alt_profesor)

        self.assertEqual(self.disciplina, alta_disc)
        self.assertTrue(alta_disc.__eq__(self.disciplina))

        self.assertEqual(str(self.disciplina),"[12]analiza->berinde")
        self.assertTrue(self.disciplina.__str__()=="[12]analiza->berinde")

    def test_validare_disciplina(self):
        self.valid.valideaza(self.disciplina)

        id_inv = -44
        disc_id_inv = Disciplina(id_inv, "analiza", "berinde")
        try:
            self.valid.valideaza(disc_id_inv)
            self.assertTrue(False)
        except ValidationError as ve:
            self.assertEqual(str(ve), "id invalid!\n")

        nume_inv = ""
        prof_inv = ""
        disc_inv = Disciplina(id_inv, nume_inv, prof_inv)
        try:
            self.valid.valideaza(disc_inv)
            self.assertTrue(False)
        except ValidationError as ve:
            self.assertEqual(str(ve), "id invalid!\n")

    def test_repo_adaugare_disciplina(self):
        self.assertEqual(len(self.repo),0)
        self.assertTrue(self.repo.__len__()==0)

        self.repo.adauga_disciplina(self.disciplina)
        self.assertEqual(len(self.repo), 1)

        alt_nume = "algebra"
        alt_prof = "modoi"
        disc_id_deja = Disciplina(12, alt_nume, alt_prof)
        try:
            self.repo.adauga_disciplina(disc_id_deja)
            self.assertTrue(False)
        except RepositoryError as re:
            self.assertEqual(str(re), "id existent!")

    def test_repo_get_all(self):
        self.assertTrue(len(self.repo)==0)
        self.repo.adauga_disciplina(self.disciplina)

        id_disc1 = 3
        nume1 = "fp"
        prof1 = "briciu"
        disc1 = Disciplina(id_disc1, nume1,prof1)
        self.repo.adauga_disciplina(disc1)

        id_disc2 = 4
        nume2 = "lc"
        prof2 = "pop"
        disc2 = Disciplina(id_disc2, nume2, prof2)
        self.repo.adauga_disciplina(disc2)

        discipline = self.repo.get_all_diciplines()
        self.assertEqual(len(discipline),3)

    def test_repo_cautare_disc(self):
        self.assertEqual(len(self.repo), 0)
        self.repo.adauga_disciplina(self.disciplina)

        id_disc1 = 3
        nume1 = "fp"
        prof1 = "briciu"
        disc1 = Disciplina(id_disc1, nume1, prof1)
        self.repo.adauga_disciplina(disc1)

        id_disc2 = 4
        nume2 = "lc"
        prof2 = "pop"
        disc2 = Disciplina(id_disc2, nume2, prof2)
        self.repo.adauga_disciplina(disc2)

        id_cautat = 3
        disc_cautata = self.repo.cauta_dupa_id_disc(id_cautat)
        self.assertTrue(disc_cautata.get_id_disc()==id_cautat)

        id_cautat_inex = 6
        disc_cautata = self.repo.cauta_dupa_id_disc(id_cautat_inex)
        self.assertTrue(disc_cautata == None)

    def test_repo_modificare_disc(self):
        self.repo.adauga_disciplina(self.disciplina)

        id_disc1 = 3
        nume1 = "fp"
        prof1 = "briciu"
        disc1 = Disciplina(id_disc1, nume1, prof1)
        self.repo.adauga_disciplina(disc1)

        prof_nou = "marin"
        self.repo.modifica_disciplina(id_disc1, prof_nou)
        discipline = self.repo.get_all_diciplines()
        self.assertTrue(discipline[1].get_id_disc()==3)
        self.assertTrue(discipline[1].get_nume() == "fp")
        self.assertTrue(discipline[1].get_profesor() == "marin")

    def test_repo_stergere_disciplina(self):
        self.assertTrue(len(self.repo) == 0)
        self.repo.adauga_disciplina(self.disciplina)
        id_disc1 = 3
        nume1 = "fp"
        prof1 = "briciu"
        disc1 = Disciplina(id_disc1, nume1, prof1)
        self.repo.adauga_disciplina(disc1)

        id_disc2 = 4
        nume2 = "lc"
        prof2 = "pop"
        disc2 = Disciplina(id_disc2, nume2, prof2)
        self.repo.adauga_disciplina(disc2)

        self.assertTrue(len(self.repo) == 3)

        id_sters = 3
        self.repo.sterge_disciplina(id_sters)
        self.assertTrue(len(self.repo) == 2)

        id_sters_inex = 9
        self.assertRaises(RepositoryError, self.repo.sterge_disciplina, id_sters_inex)

    def test_service_adaugare_discilina(self):
        self.assertEqual(self.service.get_nr_discipline(),0)
        self.service.adauga_disciplina(3, "fp", "briciu")
        self.assertEqual(self.service.get_nr_discipline(),1)

        alt_nume = "lc"
        alt_prof = "pop"
        self.assertRaises(RepositoryError, self.service.adauga_disciplina,3,alt_nume, alt_prof)

        id_inv = -89
        nume_inv = ""
        prof_inv = ""
        self.assertRaises(ValidationError, self.service.adauga_disciplina, id_inv, nume_inv, prof_inv)

    def test_service_cautare_disciplina(self):
        self.assertTrue(self.service.get_nr_discipline()==0)

        id_disc1 = 3
        nume1 = "fp"
        prof1 = "briciu"
        self.service.adauga_disciplina(id_disc1, nume1, prof1)

        id_disc2 = 4
        nume2 = "lc"
        prof2 = "pop"
        self.service.adauga_disciplina(id_disc2, nume2, prof2)

        id_disc3 = 5
        nume3 = "asc"
        prof3 = "vancea"
        self.service.adauga_disciplina(id_disc3, nume3, prof3)

        self.assertTrue(self.service.get_nr_discipline() == 3)

        id_cautat = 5
        disc_cautata = self.service.cautare_disciplina(id_cautat)
        self.assertTrue(disc_cautata.get_id_disc()==id_cautat)

        id_cautat_inex = 57
        disc_cautata = self.service.cautare_disciplina(id_cautat_inex)
        self.assertTrue(disc_cautata == None)

    def test_service_modificare_disciplina(self):
        self.service.adauga_disciplina(3, "fp","briciu")

        id_mod = 3
        prof_nou = "licu"

        self.service.modifica_disciplina(id_mod, prof_nou)
        disc = self.service.get_all()
        self.assertTrue(disc[0].get_id_disc()==3)
        self.assertTrue(disc[0].get_nume() == "fp")
        self.assertTrue(disc[0].get_profesor() == "licu")


    def test_service_stergere_disciplina(self):

        self.assertEqual(self.service.get_nr_discipline(), 0)
        self.service.adauga_disciplina(3, "fp", "briciu")
        self.assertEqual(self.service.get_nr_discipline(), 1)

        id_sters = 3
        n=None
        self.service.sterge_disciplina(id_sters,n)
        self.assertEqual(self.service.get_nr_discipline(), 0)

        self.assertRaises(RepositoryError, self.service.sterge_disciplina,89,n)


    def run_all_tests_discipline(self):
        self.test_creeare_disciplina()
        self.test_validare_disciplina()
        self.test_repo_adaugare_disciplina()
        self.test_repo_cautare_disc()
        self.test_repo_stergere_disciplina()
        self.test_repo_modificare_disc()
        self.test_repo_get_all()
        self.test_service_stergere_disciplina()
        self.test_service_modificare_disciplina()
        self.test_service_cautare_disciplina()
        self.test_service_adaugare_discilina()

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()