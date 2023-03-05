from domain.entitati import Student , Disciplina ,Nota, NotaGeneralaStudentDTO
from validare.validatori import ValidatorStudent, ValidatorDisciplina, ValidatorNota
from erori.exceptii import ValidationError, RepositoryError
from repozitorii.RepoNote import RepoNote
from repozitorii.RepoDiscipline import RepoDiscipline, FileRepoDiscipline
from repozitorii.RepoStudenti import RepoStudenti, FileRepoStudenti
from business.servicii import ServiceStudenti, ServiceDiscipline, ServiceNote
class Teste_Fisiere():
    def __test_adauga_student_repo(self):
        file_path = "tests/test_studenti.txt"
        with open(file_path, "w") as f:
            f.write("")
        try:
            repo = FileRepoStudenti(file_path)
        except Exception as ex:
            print(ex)
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_stud = 23
        nume = "Ion Popescu"
        stud = Student(id_stud, nume)
        repo.adauga_student(stud)
        assert (len(repo) == 1)
        stud_gasit = repo.cauta_dupa_id(id_stud)
        assert (stud_gasit == stud)
        assert (stud_gasit.get_nume() == stud.get_nume())
        all = repo.get_all_students()
        assert (len(all) == 1)
        assert (all[0] == stud)
        assert (all[0].get_nume() == stud.get_nume())

    def __test_adauga_disciplina_service(self):
        file_path = "tests/test_discipline.txt"
        with open(file_path, "w") as f:
            f.write("")
        repo = FileRepoDiscipline(file_path)
        valid = ValidatorDisciplina()
        srv = ServiceDiscipline(valid, repo)
        id_disc = 23
        nume = "FP"
        profesor = "Andrei Man"
        assert (srv.get_nr_discipline() == 0)
        srv.adauga_disciplina(id_disc, nume, profesor)
        assert (srv.get_nr_discipline() == 1)
        alt_nume = "Analiza"
        try:
            srv.adauga_disciplina(id_disc, alt_nume, profesor)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id existent!")

        inv_id_disc = -23
        try:
            srv.adauga_disciplina(inv_id_disc, nume, profesor)
            assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")

    def run_all_tests(self):
        print ("start all tests")
        self.__test_adauga_student_repo()
        self.__test_adauga_disciplina_service()
        print("finished all tests succesufully")