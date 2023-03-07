from domain.entitati import Student
from validare.validatori import ValidatorStudent
from repozitorii.RepoStudenti import RepoStudenti
from business.servicii import ServiceStudenti
from erori.exceptii import ValidationError, RepositoryError

import unittest


class Testestud(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.student = Student(1, "Marcel")
        self.valid = ValidatorStudent()
        self.repo = RepoStudenti()
        self.service = ServiceStudenti(self.valid, self.repo)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_creeare_student(self):
        self.assertEqual(self.student.get_id_stud(), 1)
        self.assertEqual(self.student.get_nume(), "Marcel")

        alt_nume = "Ion"
        alt_stud = Student(1, alt_nume)

        self.assertEqual(self.student, alt_stud)
        self.assertTrue(alt_stud.__eq__(self.student))

        self.assertEqual(str(self.student), "[1]Marcel")
        self.assertTrue(self.student.__str__() == "[1]Marcel")

    def test_validare_student(self):
        self.valid.valideaza(self.student)

        id_invalid = -12
        stud_id_inv = Student(id_invalid, "Marcel")
        try:
            self.valid.valideaza(stud_id_inv)
            self.assertTrue(False)
        except ValidationError as ve:
            self.assertEqual(str(ve), "id invalid!\n")

        nume_invalid = ""
        stud_inv_total = Student(id_invalid, nume_invalid)
        # try:
        #     self.valid.valideaza(stud_inv_total)
        #     self.assertTrue(False)
        # except ValidationError as ve:
        #     self.assertEqual(str(ve), "id invalid!\n")

    def test_repo_adauga_student(self):
        self.assertEqual(len(self.repo),0)
        self.assertTrue(self.repo.__len__()==0)

        self.repo.adauga_student(self.student)
        self.assertEqual(len(self.repo),1)

        alt_nume = "Ion"
        stud_id_deja = Student(1, alt_nume)
        try:
            self.repo.adauga_student(stud_id_deja)
            self.assertTrue(False)
        except RepositoryError as re:
            self.assertTrue(str(re) == "id existent!")

    def test_repo_cautare_student(self):
        self.assertEqual(len(self.repo), 0)

        id_stud1 = 1
        nume1 = "Ion"
        stud1 = Student(id_stud1, nume1)
        self.repo.adauga_student(stud1)

        id_stud2 = 2
        nume2 = "Petre"
        stud2 = Student(id_stud2, nume2)
        self.repo.adauga_student(stud2)

        id_stud3 = 3
        nume3 = "Carmen"
        stud3 = Student(id_stud3, nume3)
        self.repo.adauga_student(stud3)

        id_cautat = 2
        stud_cautat = self.repo.cauta_dupa_id(id_cautat)
        self.assertTrue(stud_cautat.get_id_stud()==id_cautat)

        id_cautat = 80
        stud_cautat_nu = self.repo.cauta_dupa_id(id_cautat)
        self.assertTrue(stud_cautat_nu == None)

    def test_repo_modifica_student(self):
        self.repo.adauga_student(self.student)

        id_stud = 2
        nume = "Ion"
        student = Student(id_stud, nume)
        self.repo.adauga_student(student)

        nume_nou = "Rares"
        self.repo.modifica_student(id_stud, nume_nou)
        studenti = self.repo.get_all_students()
        self.assertTrue(studenti[1].get_id_stud()==2)
        self.assertTrue(studenti[1].get_nume() == "Rares")

    def test_repo_get_all_students(self):
        self.assertTrue(len(self.repo) == 0)
        self.repo.adauga_student(self.student)

        id_stud = 2
        nume = "Ion"
        student = Student(id_stud, nume)
        self.repo.adauga_student(student)

        id_stud3 = 3
        nume3 = "Carmen"
        stud3 = Student(id_stud3, nume3)
        self.repo.adauga_student(stud3)

        studenti = self.repo.get_all_students()
        self.assertEqual(len(studenti),3)

    def test_repo_stergere_student(self):
        self.assertTrue(len(self.repo) == 0)
        id_stud1 = 1
        nume1 = "Ion"
        stud1 = Student(id_stud1, nume1)
        self.repo.adauga_student(stud1)

        id_stud2 = 2
        nume2 = "Petre"
        stud2 = Student(id_stud2, nume2)
        self.repo.adauga_student(stud2)

        id_stud3 = 3
        nume3 = "Carmen"
        stud3 = Student(id_stud3, nume3)
        self.repo.adauga_student(stud3)

        self.assertTrue(len(self.repo) == 3)

        n = None
        id_stud_sters = 2
        self.repo.sterge_student_recursiv(id_stud_sters,n)
        self.assertTrue(len(self.repo) == 2)

        id_stud_sters_inex = 200
        self.assertRaises(RepositoryError, self.repo.sterge_student, id_stud_sters_inex)

#teste service ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def test_service_adauga_student_BLACK_BOX(self):
        studenti = self.service.get_all_stud()
        l = len(studenti)
        self.service.adauga_student(1,"Marcel")
        studenti = self.service.get_all_stud()
        self.assertTrue(len(studenti)==l+1)
        self.assertTrue(studenti[0].get_id_stud()==1)
        self.assertTrue(studenti[0].get_nume() == "Marcel")

        self.assertRaises(RepositoryError, self.service.adauga_student,1,"Ionel")
        self.assertRaises(ValidationError, self.service.adauga_student,-90,"Gica")
        self.assertRaises(ValidationError, self.service.adauga_student, 9, "")
        self.assertRaises(ValidationError, self.service.adauga_student, -90, "")


    def test_srv_adauga_student(self):
        self.assertEqual(self.service.get_nr_studenti(),0)
        self.service.adauga_student(1, "Marcel")
        self.assertEqual(self.service.get_nr_studenti(), 1)

        alt_nume = "Ion"
        self.assertRaises(RepositoryError, self.service.adauga_student, 1, alt_nume)

        id_inv = -12
        nume_inv = ""
        self.assertRaises(ValidationError,self.service.adauga_student,id_inv,nume_inv)

    def test_service_cautare_student(self):
        self.assertTrue(self.service.get_nr_studenti() == 0)
        id_stud1 = 1
        nume1 = "Ion"
        stud1 = Student(id_stud1, nume1)
        self.repo.adauga_student(stud1)

        id_stud2 = 2
        nume2 = "Petre"
        stud2 = Student(id_stud2, nume2)
        self.repo.adauga_student(stud2)

        id_stud3 = 3
        nume3 = "Carmen"
        stud3 = Student(id_stud3, nume3)
        self.repo.adauga_student(stud3)

        self.assertTrue(self.service.get_nr_studenti() == 3)

        id_cautat = 2
        student_cautat = self.service.cautare_student(id_cautat)
        self.assertTrue(student_cautat.get_id_stud() == id_cautat)

        id_cautat_inex = 200
        student_cautat_inex = self.service.cautare_student(id_cautat_inex)
        self.assertTrue(student_cautat_inex == None)

    def test_service_modificare_student(self):
        self.service.adauga_student(1, "Marcel")
        nume_nou = "Mariusica"

        self.service.modifica_student(1,nume_nou)
        studenti = self.service.get_all_stud()

        self.assertTrue(studenti[0].get_id_stud()==1)
        self.assertTrue(studenti[0].get_nume() == "Mariusica")

    def test_service_stergere_student(self):
        self.assertTrue(self.service.get_nr_studenti()==0)
        self.service.adauga_student(1, "Marcel")
        self.assertTrue(self.service.get_nr_studenti() == 1)

        id_sters = 1
        n = None
        # self.service.sterge_student(id_sters,n)
        # self.assertTrue(self.service.get_nr_studenti() == 0)

        id_sters_inex = 90
        #self.assertRaises(RepositoryError, self.service.sterge_student, id_sters_inex,n)


    def run_all_tests_studenti(self):
        self.test_creeare_student()
        self.test_validare_student()
        self.test_repo_adauga_student()
        self.test_repo_cautare_student()
        self.test_repo_stergere_student()
        self.test_repo_modifica_student()
        self.test_repo_get_all_students()
        self.test_service_stergere_student()
        self.test_service_modificare_student()
        self.test_service_cautare_student()
        self.test_srv_adauga_student()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
