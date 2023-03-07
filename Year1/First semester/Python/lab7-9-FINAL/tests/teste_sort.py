import random
import unittest

from domain.entitati import Student, Disciplina, Nota
from repozitorii.RepoNote import RepoNote
from repozitorii.RepoDiscipline import RepoDiscipline
from sorters.sorters import MergeSorter, BingoSorter, comparare_noua, comparare_noua2


class Teste(unittest.TestCase):

    def test_all(self):

        self.test_merge_sorter_list()
        self.test_bingo_sorter_list()
        self.test_comparare_noua()


    def test_merge_sorter_list(self):
        sorter_merge = MergeSorter()
        vector = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(vector)
        sorter_merge.sort(vector)
        self.assertEqual(vector, [0,1,2,3,4,5,6,7,8,9])
        random.shuffle(vector)
        sorter_merge.sort(vector, reversed=True)
        self.assertEqual(vector, [9,8,7,6,5,4,3,2,1,0])
        random.shuffle(vector)
        sorter_merge.sort(vector, cmp=lambda x, y: x >= y)
        self.assertEqual(vector, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_bingo_sorter_list(self):
        sorter_bingo = BingoSorter()
        vector = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
        random.shuffle(vector)
        sorter_bingo.sort(vector)
        self.assertEqual(vector, [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])
        random.shuffle(vector)
        sorter_bingo.sort(vector, reversed=True)
        self.assertEqual(vector, [[8, 9], [6, 7], [4, 5], [2, 3], [0, 1]])
        random.shuffle(vector)
        sorter_bingo.sort(vector, cmp=lambda x, y: x >= y)
        self.assertEqual(vector, [[8, 9], [6, 7], [4, 5], [2, 3], [0, 1]])

    def test_comparare_noua(self):
        sorter_merge = MergeSorter()
        repo = RepoNote()
        stud1 = Student(1, "Marcel")
        stud2 = Student(2, "Ana")
        stud3 = Student(3, "Ionel")
        disc = Disciplina(5, "analiza","berinde")

        nota1 = Nota(1,1,5,9)
        nota1.set_student(stud1)
        nota1.set_disciplina(disc)

        nota2 = Nota(2,2,5,6)
        nota2.set_student(stud2)
        nota2.set_disciplina(disc)

        nota3 = Nota(3,3,5,9)
        nota3.set_student(stud3)
        nota3.set_disciplina(disc)

        repo.adauga_nota(nota1)
        repo.adauga_nota(nota2)
        repo.adauga_nota(nota3)

        note = repo.get_all()
        sorter_merge.sort(note, cmp=comparare_noua)
        self.assertTrue(note[0] == nota2)
        self.assertTrue(note[1] == nota1)
        self.assertTrue(note[2] == nota3)

    def test_comparare_buna(self):
        sorter = MergeSorter()
        repo = RepoDiscipline()
        disc1 = Disciplina(1,"fp","briciu")
        disc2 = Disciplina(2, "analiza", "berinde")
        disc3 = Disciplina(3, "analiza", "aurelian")
        disc4 = Disciplina(4, "lc","pop")
        repo.adauga_disciplina(disc1)
        repo.adauga_disciplina(disc2)
        repo.adauga_disciplina(disc3)
        repo.adauga_disciplina(disc4)
        discipline = repo.get_all_diciplines()
        sorter.sort(discipline, cmp=comparare_noua2)
        self.assertTrue(discipline[0]==disc3)
        self.assertTrue(discipline[1] == disc2)
        self.assertTrue(discipline[2] == disc1)
        self.assertTrue(discipline[3] == disc4)





