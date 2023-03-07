from domain.entitati import Nota, Student, Disciplina
from validare.validatori import ValidatorNota, ValidatorStudent, ValidatorDisciplina
from repozitorii.RepoNote import RepoNote
from repozitorii.RepoStudenti import RepoStudenti
from repozitorii.RepoDiscipline import  RepoDiscipline
from business.servicii import ServiceNote, ServiceStudenti, ServiceDiscipline
from erori.exceptii import RepositoryError, ValidationError

import unittest


class Testenote(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.nota = Nota(1,2,3,9)
        self.valid = ValidatorNota()
        self.repo_note = RepoNote()
        self.repo_stud = RepoStudenti()
        self.repo_disc = RepoDiscipline()
        self.service = ServiceNote(self.repo_note, self.valid, self.repo_stud, self.repo_disc)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_creare_nota(self):
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)
        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        nota = Nota(id_nota, id_stud, id_disc,valoare)
        nota.set_student(student)
        nota.set_disciplina(disciplina)

        self.assertEqual(nota.get_id_nota(), 12)
        self.assertEqual(nota.get_id_student(), 1)
        self.assertEqual(nota.get_id_disciplina(), 5)
        self.assertEqual(nota.get_valoare(),9)
        self.assertEqual(nota.get_student(), student)
        self.assertEqual(nota.get_disciplina(), disciplina)

        id_stud2 = 12
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)
        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 8
        nota2 = Nota(id_nota, id_stud2, id_disc2, valoare2)
        nota.set_student(student2)
        nota.set_disciplina(disciplina2)

        self.assertEqual(nota, nota2)
        self.assertTrue(nota2.__eq__(nota))

    def test_repo_adaugare_nota(self):
        self.assertEqual(len(self.repo_note), 0)
        self.assertTrue(self.repo_note.__len__() == 0)

        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)
        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        nota = Nota(id_nota, id_stud, id_disc, valoare)
        self.repo_note.adauga_nota(nota)
        self.assertEqual(len(self.repo_note), 1)

        id_stud2 = 12
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)
        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 8
        nota2 = Nota(id_nota, id_stud2, id_disc2, valoare2)

        self.assertRaises(RepositoryError, self.repo_note.adauga_nota, nota2)

    def test_repo_get_all_note(self):
        self.assertEqual(len(self.repo_note),0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)
        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        nota = Nota(id_nota, id_stud, id_disc, valoare)
        self.repo_note.adauga_nota(nota)
        self.assertEqual(len(self.repo_note), 1)

        id_nota2 = 9
        id_stud2 = 12
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)
        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 8
        nota2 = Nota(id_nota2, id_stud2, id_disc2, valoare2)
        self.repo_note.adauga_nota(nota2)
        self.assertEqual(len(self.repo_note), 2)
        note = self.repo_note.get_all()
        self.assertEqual(note[1].get_id_nota(), 9)
        self.assertEqual(note[1].get_id_student(), id_stud2)
        self.assertEqual(note[1].get_id_disciplina(), id_disc2)

    def test_repo_stergere_nota(self):
        self.assertTrue(len(self.repo_note) == 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)
        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        nota = Nota(id_nota, id_stud, id_disc, valoare)
        self.repo_note.adauga_nota(nota)
        self.assertEqual(len(self.repo_note), 1)

        id_nota2 = 9
        id_stud2 = 12
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)
        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 8
        nota2 = Nota(id_nota2, id_stud2, id_disc2, valoare2)
        self.repo_note.adauga_nota(nota2)
        self.assertEqual(len(self.repo_note), 2)

        id_sters = 9
        self.repo_note.sterge_nota(id_sters)
        self.assertEqual(len(self.repo_note), 1)

        id_sters_inex = 90
        self.assertRaises(RepositoryError, self.repo_note.sterge_nota, id_sters_inex)

    def test_repo_modificare_nota(self):
        self.assertEqual(len(self.repo_note), 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)
        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        nota = Nota(id_nota, id_stud, id_disc, valoare)
        self.repo_note.adauga_nota(nota)
        self.assertEqual(len(self.repo_note), 1)

        id_nota2 = 9
        id_stud2 = 12
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)
        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 8
        nota2 = Nota(id_nota2, id_stud2, id_disc2, valoare2)
        self.repo_note.adauga_nota(nota2)
        self.assertEqual(len(self.repo_note), 2)

        id_nota_modif = 9
        valoare_noua = 5
        self.repo_note.update_nota(id_nota_modif, valoare_noua)
        note = self.repo_note.get_all()
        self.assertTrue(note[1].get_id_nota()==9)
        self.assertTrue(note[1].get_id_student() == 12)
        self.assertTrue(note[1].get_id_disciplina() == 52)
        self.assertTrue(note[1].get_valoare() == 5)

    def test_repo_cautare_nota(self):
        self.assertEqual(len(self.repo_note), 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)
        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        nota = Nota(id_nota, id_stud, id_disc, valoare)
        self.repo_note.adauga_nota(nota)
        self.assertEqual(len(self.repo_note), 1)

        id_nota2 = 9
        id_stud2 = 12
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)
        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 8
        nota2 = Nota(id_nota2, id_stud2, id_disc2, valoare2)
        self.repo_note.adauga_nota(nota2)
        self.assertEqual(len(self.repo_note), 2)

        id_cautat = 9
        nota_cautata = self.repo_note.cauta_nota_dupa_id(id_cautat)
        self.assertTrue(nota_cautata.get_id_nota()==id_cautat)

        id_cautat = 99
        self.assertRaises(RepositoryError, self.repo_note.cauta_nota_dupa_id,id_cautat)


    def test_service_adaugare_nota(self):
        self.assertEqual(self.service.get_nr_note(), 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)

        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        self.repo_stud.adauga_student(student)
        self.repo_disc.adauga_disciplina(disciplina)
        self.service.adauga_nota(id_nota, id_stud, id_disc, valoare)
        self.assertEqual(self.service.get_nr_note(), 1)

        id_stud2 = 2
        nume_stud2 = "Ionel"
        student = Student(id_stud2, nume_stud2)

        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 5

        self.assertRaises(RepositoryError, self.service.adauga_nota,id_nota, id_stud2, id_disc2,valoare2)

        id_stud3 = -2
        nume_stud3 = ""
        student = Student(id_stud3, nume_stud3)

        id_disc3 = -52
        nume_disc3 = ""
        prof3 = ""
        disciplina = Disciplina(id_disc3, nume_disc3, prof3)
        valoare3 = -5

        self.assertRaises(ValidationError, self.service.adauga_nota, id_nota, id_stud3, id_disc3, valoare3)

    def test_service_stergere_nota(self):
        self.assertEqual(self.service.get_nr_note(), 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)

        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        self.repo_stud.adauga_student(student)
        self.repo_disc.adauga_disciplina(disciplina)
        self.service.adauga_nota(id_nota, id_stud, id_disc, valoare)
        self.assertEqual(self.service.get_nr_note(), 1)

        id_sters = 12
        self.service.sterge_nota(id_sters)
        self.assertEqual(self.service.get_nr_note(), 0)

        self.assertRaises(RepositoryError, self.service.sterge_nota, 67)

    def test_service_modificare_nota(self):
        self.assertEqual(self.service.get_nr_note(), 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)

        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        self.repo_stud.adauga_student(student)
        self.repo_disc.adauga_disciplina(disciplina)
        self.service.adauga_nota(id_nota, id_stud, id_disc, valoare)
        self.assertEqual(self.service.get_nr_note(), 1)

        id_modif = 12
        valoare_noua = 6
        self.service.update_nota(id_modif, valoare_noua)
        note = self.service.get_all()
        self.assertTrue(note[0].get_id_nota()==12)
        self.assertTrue(note[0].get_valoare() == 6)

    def test_service_cautare_nota(self):
        self.assertEqual(self.service.get_nr_note(), 0)
        id_nota = 12
        id_stud = 1
        nume_stud = "Ion"
        student = Student(id_stud, nume_stud)

        id_disc = 5
        nume_disc = "fp"
        prof = "briciu"
        disciplina = Disciplina(id_disc, nume_disc, prof)
        valoare = 9
        self.repo_stud.adauga_student(student)
        self.repo_disc.adauga_disciplina(disciplina)
        self.service.adauga_nota(id_nota, id_stud, id_disc, valoare)
        self.assertEqual(self.service.get_nr_note(), 1)

        id_nota2 = 13
        id_stud2 = 2
        nume_stud2 = "Ionel"
        student2 = Student(id_stud2, nume_stud2)

        id_disc2 = 52
        nume_disc2 = "lc"
        prof2 = "pop"
        disciplina2 = Disciplina(id_disc2, nume_disc2, prof2)
        valoare2 = 5
        self.repo_stud.adauga_student(student2)
        self.repo_disc.adauga_disciplina(disciplina2)
        self.service.adauga_nota(id_nota2, id_stud2, id_disc2, valoare2)
        self.assertEqual(self.service.get_nr_note(), 2)

        id_cautat = 13
        nota_cautata = self.service.cauta_nota_dupa_id(id_cautat)
        self.assertTrue(nota_cautata.get_id_nota()==id_cautat)

        id_cautat_inex = 113
        self.assertRaises(RepositoryError, self.service.cauta_nota_dupa_id, id_cautat_inex)

    def test_service_get_note_la_o_disciplina_alfabetic(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        self.assertTrue(srv_stud.get_nr_studenti() == 0)
        id_stud1 = 1
        nume_stud1 = "Marcel Pop"
        srv_stud.adauga_student(id_stud1, nume_stud1)
        id_stud2 = 2
        nume_stud2 = "Ion George"
        srv_stud.adauga_student(id_stud2, nume_stud2)
        self.assertTrue (srv_stud.get_nr_studenti() == 2)
        valid_disc = ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        id_disc = 5
        nume_disc = "analiza"
        prof = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc, prof)
        self.assertTrue (srv_disc.get_nr_discipline() == 1)
        valid_nota = ValidatorNota()
        repo_nota = RepoNote()
        srv_note = ServiceNote(repo_nota, valid_nota, repo_stud, repo_disc)
        id_nota1 = 9
        valoare1 = 5
        srv_note.adauga_nota(id_nota1, id_stud1, id_disc, valoare1)
        id_nota2 = 10
        valoare2 = 8
        srv_note.adauga_nota(id_nota2, id_stud1, id_disc, valoare2)
        id_nota3 = 11
        valoare3 = 9
        srv_note.adauga_nota(id_nota3, id_stud2, id_disc, valoare3)
        self.assertTrue (len(repo_nota) == 3)
        # note = srv_note.get_note_la_o_disciplina_alfabetic(id_disc)
        # self.assertTrue (note == ["Ion George:\n\t9\n","Marcel Pop:\n\t8\n\t5\n"])


    def test_service_get_note_la_o_disciplina_dupa_nota(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        self.assertTrue(srv_stud.get_nr_studenti() == 0)
        id_stud1 = 1
        nume_stud1 = "Marcel Pop"
        srv_stud.adauga_student(id_stud1, nume_stud1)
        id_stud2 = 2
        nume_stud2 = "Ion George"
        srv_stud.adauga_student(id_stud2, nume_stud2)
        self.assertTrue(srv_stud.get_nr_studenti() == 2)
        valid_disc = ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        id_disc = 5
        nume_disc = "analiza"
        prof = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc, prof)
        self.assertTrue(srv_disc.get_nr_discipline() == 1)
        valid_nota = ValidatorNota()
        repo_nota = RepoNote()
        srv_note = ServiceNote(repo_nota, valid_nota, repo_stud, repo_disc)
        id_nota1 = 9
        valoare1 = 5
        srv_note.adauga_nota(id_nota1, id_stud1, id_disc, valoare1)
        id_nota2 = 10
        valoare2 = 8
        srv_note.adauga_nota(id_nota2, id_stud1, id_disc, valoare2)
        id_nota3 = 11
        valoare3 = 9
        srv_note.adauga_nota(id_nota3, id_stud2, id_disc, valoare3)
        self.assertTrue(len(repo_nota) == 3)
        # note = srv_note.get_note_la_o_disciplina_dupa_nota(id_disc)
        # self.assertTrue (note == ["Ion George:\n\t9\n", "Marcel Pop:\n\t5\n\t8\n"])

    def run_all_tests_note(self):
        self.test_creare_nota()
        self.test_repo_adaugare_nota()
        self.test_repo_get_all_note()
        self.test_repo_cautare_nota()
        self.test_repo_stergere_nota()
        self.test_repo_modificare_nota()
        self.test_service_modificare_nota()
        self.test_service_adaugare_nota()
        self.test_service_stergere_nota()
        self.test_service_cautare_nota()
        self.test_service_get_note_la_o_disciplina_alfabetic()
        self.test_service_get_note_la_o_disciplina_dupa_nota()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()