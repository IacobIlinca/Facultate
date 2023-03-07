from prezentare.user_interface import Consola
from business.servicii import ServiceStudenti, ServiceDiscipline, ServiceNote
from repozitorii.RepoNote import RepoNote, FileRepoNote
from repozitorii.RepoStudenti import RepoStudenti, FileRepoStudenti
from repozitorii.RepoDiscipline import RepoDiscipline, FileRepoDiscipline
from validare.validatori import ValidatorStudent, ValidatorDisciplina, ValidatorNota
from tests.teste_final import Teste
# from tests.teste import Teste
from tests.teste_fisiere import Teste_Fisiere

import unittest
from domain.entitati import Student, Disciplina, Nota

# if __name__ == '__main__':
#     # testsuite = unittest.TestLoader().discover('.')
#     # unittest.TextTestRunner(verbosity=1).run(testsuite)
#


if __name__ == '__main__':
    valid_student = ValidatorStudent()
    valid_disciplina = ValidatorDisciplina()
    valid_nota = ValidatorNota()

    print("salvare memorie sau salvare fisier ?")
    cmd = input(">>")

    if cmd == "memorie":
        repo_studenti = RepoStudenti()
        repo_discipline = RepoDiscipline()
        repo_note = RepoNote()

    else:
        repo_studenti = FileRepoStudenti("studenti.txt")
        repo_discipline = FileRepoDiscipline("discipline.txt")
        repo_note = FileRepoNote("note.txt")

    srv_studenti = ServiceStudenti(valid_student, repo_studenti)
    srv_discipline = ServiceDiscipline(valid_disciplina, repo_discipline)
    srv_note = ServiceNote(repo_note, valid_nota, repo_studenti, repo_discipline)

    ui = Consola (srv_studenti, srv_discipline, srv_note)
    # fisier
    # teste_fisiere = Teste_Fisiere()
    # teste_fisiere.run_all_tests()
    ui.run()
