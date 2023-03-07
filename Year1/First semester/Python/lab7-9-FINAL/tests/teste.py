from domain.entitati import Student , Disciplina ,Nota, NotaGeneralaStudentDTO
from validare.validatori import ValidatorStudent, ValidatorDisciplina, ValidatorNota
from erori.exceptii import ValidationError, RepositoryError
from repozitorii.RepoNote import RepoNote
from repozitorii.RepoDiscipline import RepoDiscipline
from repozitorii.RepoStudenti import RepoStudenti
from business.servicii import ServiceStudenti, ServiceDiscipline, ServiceNote
class Teste (object):

    def __test_creeaza_student (self):
        id_stud = 23
        nume = "Ion Popescu"
        stud = Student (id_stud, nume)
        assert (stud.get_id_stud() == id_stud)
        assert (stud.get_nume() == nume)

        alt_nume = "Maria Ionescu"
        alt_stud = Student(id_stud, alt_nume)
        assert (stud==alt_stud)
        assert (stud.__eq__(alt_stud))

        assert (str(stud)=="[23]Ion Popescu")
        assert (stud.__str__() == "[23]Ion Popescu" )

    def __test_valideaza_student(self):
        id_stud = 23
        nume = "Ion Popescu"
        stud = Student(id_stud, nume)
        valid = ValidatorStudent()
        valid.valideaza(stud)

        inv_id_stud = -23
        inv_nume = ""
        stud_inv_id = Student(inv_id_stud, nume)
        stud_inv = Student(inv_id_stud, inv_nume)

        try:
            valid.valideaza (stud_inv_id)
            assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")
        """
        try:
            valid.valideaza (stud_inv)
            assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\n")
        """

    def __test_adauga_student_repo(self):
        repo = RepoStudenti()
        assert (len(repo) == 0)
        assert (repo.__len__()==0)
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
        """
        id_stud_inexist = 24
        try:
            repo.cauta_dupa_id(id_stud_inexist)
            assert (False)
        except RepositoryError as re:
            assert (str(re)=="id inexistent!")
        """

        alt_nume = "Vlad Marinescu"
        alt_stud_same_id = Student(id_stud, alt_nume)
        try:
            repo.adauga_student(alt_stud_same_id)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id existent!")

    def __test_adauga_student_service(self):

        repo = RepoStudenti()
        valid = ValidatorStudent()
        srv = ServiceStudenti(valid, repo)
        id_stud = 23
        nume = "Ion Popescu"
        assert (srv.get_nr_studenti()==0)
        srv.adauga_student(id_stud, nume)
        assert (srv.get_nr_studenti() == 1)
        alt_nume = "Vlad Marinescu"
        try:
            srv.adauga_student(id_stud, alt_nume)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id existent!")

        inv_id_stud = -23
        inv_nume = ""
        try:
           srv.adauga_student(inv_id_stud, nume)
           assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")

    def __test_creeaza_disciplina(self):
        id_disc = 23
        nume = "FP"
        profesor = "Andrei Man"
        disc = Disciplina(id_disc, nume, profesor)
        assert (disc.get_id_disc() == id_disc)
        assert (disc.get_nume() == nume)
        assert (disc.get_profesor() == profesor)

        alt_nume = "Maria Ionescu"
        alt_profesor = "Marcel Petru"
        alta_disc = Disciplina(id_disc, alt_nume, alt_profesor)
        assert (disc == alta_disc)
        assert (disc.__eq__(alta_disc))

        assert (str(disc) == "[23]FP->Andrei Man")
        assert (disc.__str__() == "[23]FP->Andrei Man")


    def __test_valideaza_disciplina(self):
        id_disc = 23
        nume = "Andrei Man"
        profesor = "Andrei Man"
        disc = Disciplina(id_disc, nume, profesor)
        valid = ValidatorDisciplina()
        valid.valideaza(disc)

        inv_id_disc = -23
        disc_inv_id = Disciplina(inv_id_disc, nume, profesor)

        try:
            valid.valideaza(disc_inv_id)
            assert (False)
        except ValidationError as ve:
            assert (str(ve) == "id invalid!\n")

    def __test_adauga_disciplina_repo(self):
        repo = RepoDiscipline()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_disc = 23
        nume = "FP"
        profesor = "Andrei Man"
        disc = Disciplina(id_disc, nume, profesor)

        repo.adauga_disciplina(disc)
        assert (len(repo) == 1)
        disc_gasit = repo.cauta_dupa_id_disc(id_disc)
        assert (disc_gasit == disc)
        assert (disc_gasit.get_nume() == disc.get_nume())
        assert (disc_gasit.get_profesor() == disc.get_profesor())
        all = repo.get_all_diciplines()
        assert (len(all) == 1)
        assert (all[0] == disc)
        assert (all[0].get_nume() == disc.get_nume())
        assert (all[0].get_profesor() == disc.get_profesor())
        """
        id_disc_inexist = 24
        try:
            repo.cauta_dupa_id_disc(id_disc_inexist)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id inexistent!")
        """

        alt_nume = "LC"
        alt_disc_same_id = Disciplina(id_disc, alt_nume, profesor)
        try:
            repo.adauga_disciplina(alt_disc_same_id)
            assert (False)
        except RepositoryError as re:
            assert (str(re) == "id existent!")

    def __test_adauga_disciplina_service(self):
        repo = RepoDiscipline()
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

    def __test_cautare_student_repo(self):
        repo = RepoStudenti()
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

    def __test_cautare_student_service(self):
        repo = RepoStudenti()
        valid = ValidatorStudent()
        srv = ServiceStudenti(valid, repo)
        id_stud1 = 23
        nume1 = "Ion Popescu"
        assert (srv.get_nr_studenti() == 0)
        srv.adauga_student(id_stud1, nume1)
        assert (srv.get_nr_studenti() == 1)
        id_stud2 = 26
        nume2 = "Marcel Ropescu"
        stud2 = Student(id_stud2, nume2)
        srv.adauga_student(id_stud2, nume2)
        assert (srv.get_nr_studenti() == 2)
        stud_gasit = srv.cautare_student(id_stud2)
        assert (stud_gasit == stud2)

    def __test_cautare_disciplina_repo(self):
        repo = RepoDiscipline()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_disc = 23
        nume = "FP"
        profesor = "Andrei Man"
        disc = Disciplina(id_disc, nume, profesor)
        repo.adauga_disciplina(disc)
        assert (len(repo) == 1)
        disc_gasita = repo.cauta_dupa_id_disc(id_disc)
        assert (disc_gasita == disc)
        assert (disc_gasita.get_nume() == disc.get_nume())
        assert (disc_gasita.get_profesor() == disc.get_profesor())

    def __test_cautare_disciplina_service(self):
        repo = RepoDiscipline()
        valid = ValidatorDisciplina()
        srv = ServiceDiscipline(valid, repo)
        id_disc1 = 23
        nume1 = "FP"
        profesor1 = "Ion Marc"
        assert (srv.get_nr_discipline() == 0)
        srv.adauga_disciplina(id_disc1, nume1, profesor1)
        assert (srv.get_nr_discipline() == 1)
        id_disc2 = 26
        nume2 = "ASC"
        profesor2 = "Marcel Ropescu"
        disc2 = Disciplina(id_disc2, nume2, profesor2)
        srv.adauga_disciplina(id_disc2, nume2, profesor2)
        assert (srv.get_nr_discipline() == 2)
        disc_gasita = srv.cautare_disciplina(id_disc2)
        assert (disc_gasita == disc2)

    def __test_modificare_student_repo(self):
        repo = RepoStudenti()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_stud = 23
        nume = "Ion Popescu"
        stud = Student(id_stud, nume)
        repo.adauga_student(stud)
        assert (len(repo) == 1)
        nou_nume = "Marcel Pavel"
        repo.modifica_student(id_stud, nou_nume)
        assert (len(repo) == 1)
        all = repo.get_all_students()
        assert (len(all) == 1)
        assert (all[0].get_nume() == nou_nume)

    def __test_modificare_student_service(self):
        repo = RepoStudenti()
        valid = ValidatorStudent()
        srv = ServiceStudenti(valid, repo)
        id_stud = 23
        nume = "Ion Popescu"
        student = Student(id_stud, nume)
        assert (srv.get_nr_studenti() == 0)
        srv.adauga_student(id_stud, nume)
        assert (srv.get_nr_studenti() == 1)
        nou_nume = "Ioan Petre"
        srv.modifica_student(id_stud, nou_nume)

    def __test_modificare_disciplina_repo(self):
        repo = RepoDiscipline()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_disc = 23
        nume = "FP"
        profesor = "Ion Popescu"
        disc = Disciplina(id_disc, nume, profesor)
        repo.adauga_disciplina(disc)
        assert (len(repo) == 1)
        nou_profesor = "Marcel Pavel"
        repo.modifica_disciplina(id_disc, nou_profesor)
        assert (len(repo) == 1)
        all = repo.get_all_diciplines()
        assert (len(all) == 1)
        assert (all[0].get_profesor() == nou_profesor)

    def __test_modificare_disciplina_service(self):
        repo = RepoDiscipline()
        valid = ValidatorDisciplina()
        srv = ServiceDiscipline(valid, repo)
        id_disc = 23
        nume = "FP"
        profesor = "Ion Popescu"
        disciplina = Disciplina(id_disc, nume ,profesor)
        assert (srv.get_nr_discipline() == 0)
        srv.adauga_disciplina(id_disc, nume, profesor)
        assert (srv.get_nr_discipline() == 1)
        nou_profesor = "Ioan Petre"
        srv.modifica_disciplina(id_disc,nou_profesor)

    def __test_sterge_student_repo(self):
        repo = RepoStudenti()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_stud = 23
        nume = "Ion Popescu"
        stud = Student(id_stud, nume)
        repo.adauga_student(stud)
        assert (len(repo) == 1)
        id_stud2= 34
        nume2 = "Ioan Pic"
        stud2 = Student(id_stud2, nume2)
        repo.adauga_student(stud2)
        assert (len(repo) == 2)
        repo.sterge_student(id_stud2)
        assert (len(repo) == 1)

    def __test_sterge_student_service(self):
        repo = RepoStudenti()
        valid = ValidatorStudent()
        srv = ServiceStudenti(valid, repo)
        id_stud = 23
        nume = "Ion Popescu"
        assert (srv.get_nr_studenti() == 0)
        srv.adauga_student(id_stud, nume)
        assert (srv.get_nr_studenti() == 1)
        id_stud2 = 223
        nume2 = "Ionel Mopescu"
        srv.adauga_student(id_stud2, nume2)
        assert (srv.get_nr_studenti() == 2)
        srv.sterge_student(id_stud2)
        assert (srv.get_nr_studenti() == 1)


    def __test_sterge_disciplina_repo(self):
        repo = RepoDiscipline()
        assert (len(repo) == 0)
        assert (repo.__len__() == 0)
        id_disc = 23
        nume = "FP"
        profesor = "Ion Popescu"
        disc = Disciplina(id_disc, nume, profesor)
        repo.adauga_disciplina(disc)
        assert (len(repo) == 1)
        id_disc2= 34
        nume2 = "ASC"
        profesor2 = "Ioan Pic"
        disc2 = Disciplina(id_disc2, nume2, profesor2)
        repo.adauga_disciplina(disc2)
        assert (len(repo) == 2)
        repo.sterge_disciplina(id_disc2)
        assert (len(repo) == 1)

    def __test_sterge_disciplina_service(self):
        repo = RepoDiscipline()
        valid = ValidatorDisciplina()
        srv = ServiceDiscipline(valid, repo)
        id_disc = 23
        nume = "FP"
        profesor = "Ion Popescu"
        assert (srv.get_nr_discipline() == 0)
        srv.adauga_disciplina(id_disc, nume, profesor)
        assert (srv.get_nr_discipline() == 1)
        id_disc2 = 223
        nume2 = "ASC"
        profesor2 = "Ionel Mopescu"
        srv.adauga_disciplina(id_disc2, nume2, profesor2)
        assert (srv.get_nr_discipline() == 2)
        srv.sterge_disciplina(id_disc2)
        assert (srv.get_nr_discipline() == 1)



    def __test_creeaza_nota(self):
        stud = Student(1, 'Pop Ana')
        dis = Disciplina(10, 'fp', 'Man Sergiu')
        nota = Nota(12, stud, dis, 8)
        nota.set_student(stud)
        nota.set_disciplina(dis)
        assert nota.get_id_nota() == 12
        assert nota.get_disciplina() == dis
        assert nota.get_student() == stud
        assert nota.get_valoare() == 8


    def __test_adauga_nota_repo(self):
        id_nota=56
        valoare=9
        student = Student(1, "marcel")
        disciplina = Disciplina(2,"analiza", "berinde")
        repo= RepoNote()

        nota = Nota(id_nota, 1, 2, valoare)
        assert (len(repo) == 0)
        repo.adauga_nota(nota)
        assert(len(repo) == 1)
        note=repo.get_all()
        assert (note[0].get_id_nota() == id_nota)
        assert (note[0].get_id_student() == 1)
        assert (note[0].get_id_disciplina() == 2)
        assert (abs(note[0].get_valoare() -valoare<0.00001))
        assert (len(repo) == 1)
        alta_nota = repo.cauta_nota_dupa_id(56)
        assert (alta_nota.get_id_nota() == id_nota)
        assert (alta_nota.get_id_student() == 1)
        assert (alta_nota.get_id_disciplina() == 2)
        assert (abs(alta_nota.get_valoare() - valoare) < 0.0001)
        """"
        try:
            alta_nota = repo.cauta_nota_dupa_id(586)
            assert False
        except RepositoryError as re:
            assert (str(re) == "Nota inexistenta!\n")
        """
        id_nota2 = 56
        valoare2 = 5
        student2= Student(15, "marin")
        disciplina2 = Disciplina(8, "fp" ,"ion popa")
        nota_acelasi_id = Nota(id_nota2, student2, disciplina2, valoare2)
        """
        try:
            repo.adauga_nota(nota_acelasi_id)
            assert False
        except RepositoryError as re:
            assert (str(re) == "Nota cu id deja existent!\n")
        """


    def __test_sterge_nota_repo(self):
        id_nota = 4
        valoare = 5
        student = Student(1, "marcel")
        disciplina = Disciplina (1, "analiza" , "berinde")
        repo= RepoNote()
        nota = Nota(id_nota, 1, 1, valoare)
        assert (len (repo) == 0)
        repo.adauga_nota(nota)
        assert (len(repo) == 1)
        alt_id_nota = 5
        alta_valoare = 6
        alt_student = Student(2, "mihai")
        alta_disciplina = Disciplina(6, "analiza", "berinde")
        alta_nota = Nota(alt_id_nota, 2, 6, alta_valoare)
        repo.adauga_nota(alta_nota)
        assert(len (repo)==2)
        repo.sterge_nota(4)
        assert (len(repo) == 1)
        try:
            nota2 = repo.cauta_nota_dupa_id(4)
            assert False
        except RepositoryError as re:
            assert str(re) == "Nota inexistenta\n"
        note = repo.get_all()
        assert note[0].get_id_nota() == alt_id_nota
        assert note[0].get_id_student() == 2
        assert note[0].get_id_disciplina() == 6
        assert abs(note[0].get_valoare() - alta_valoare) < 0.0001

    def __test_update_nota_repo(self):
        id_nota = 4
        valoare = 5
        student = Student(1, "marcel")
        disciplina = Disciplina(1, "analiza", "berinde")
        repo = RepoNote()
        nota = Nota(id_nota, student, disciplina, valoare)
        assert (len(repo) == 0)
        repo.adauga_nota(nota)
        assert (len(repo) == 1)
        valoare_noua = 9
        nota_updated = Nota(id_nota, student, disciplina, valoare_noua)
        repo.update_nota(id_nota, valoare_noua)
        assert (abs(nota.get_valoare() - valoare_noua) < 0.001)

    def __test_srv_adauga_nota(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        assert (srv_stud.get_nr_studenti() == 0)
        id_stud = 1
        nume_stud = "marcel"
        srv_stud.adauga_student(id_stud,nume_stud)
        assert (srv_stud.get_nr_studenti() == 1)

        valid_disc =ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        assert (srv_disc.get_nr_discipline() == 0)
        id_disc = 1
        nume_disc = "analiza"
        profesor = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc, profesor)
        assert (srv_disc.get_nr_discipline() == 1)

        id_nota = 2
        valoare = 6
        valid_nota = ValidatorNota()
        repo_note = RepoNote()
        srv_note = ServiceNote(repo_note, valid_nota, repo_stud, repo_disc)
        srv_note.adauga_nota(id_nota, 1, 1, valoare)
        assert (len(repo_note) ==1)
        # nota_gasita = srv_note.cauta_nota_dupa_id(id_nota)
        # assert (nota_gasita.get_id_nota()== id_nota)
        # assert (nota_gasita.get_id_student() == 1)
        # assert (nota_gasita.get_id_disciplina()== 1)
        # assert (abs(nota_gasita.get_valoare() - valoare) < 0.001)
        # note = srv_note.get_all()
        # assert (note[0].get_id_nota() == id_nota)
        # assert (note[0].get_id_student() == 1)
        # assert (note[0].get_id_disciplina() == 1)
        # assert (abs(note[0].get_valoare() - valoare) < 0.001)

    def __test_srv_sterge_nota(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        assert (srv_stud.get_nr_studenti() == 0)
        id_stud = 1
        nume_stud = "marcel"
        srv_stud.adauga_student(id_stud, nume_stud)
        assert (srv_stud.get_nr_studenti() == 1)

        valid_disc = ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        assert (srv_disc.get_nr_discipline() == 0)
        id_disc = 1
        nume_disc = "analiza"
        profesor = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc, profesor)
        assert (srv_disc.get_nr_discipline() == 1)

        id_nota = 2
        valoare = 6
        valid_nota = ValidatorNota()
        repo_note = RepoNote()
        srv_note = ServiceNote(repo_note, valid_nota, repo_stud, repo_disc)
        srv_note.adauga_nota(id_nota, id_stud, id_disc, valoare)
        assert (len(repo_note) == 1)

        alt_id_nota = 4
        alta_valoare = 9
        srv_note.adauga_nota(alt_id_nota, id_stud, id_disc, alta_valoare)
        srv_note.sterge_nota(id_nota)
        try:
            nota_gasita = srv_note.cauta_nota_dupa_id(2)
            assert False
        except RepositoryError as re:
            assert str(re) == "Nota inexistenta\n"


    def __test_srv_update_nota(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        assert (srv_stud.get_nr_studenti() == 0)
        id_stud = 1
        nume_stud = "marcel"
        srv_stud.adauga_student(id_stud, nume_stud)
        assert (srv_stud.get_nr_studenti() == 1)

        valid_disc = ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        assert (srv_disc.get_nr_discipline() == 0)
        id_disc = 1
        nume_disc = "analiza"
        profesor = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc, profesor)
        assert (srv_disc.get_nr_discipline() == 1)

        id_nota = 2
        valoare = 6
        valid_nota = ValidatorNota()
        repo_note = RepoNote()
        srv_note = ServiceNote(repo_note, valid_nota, repo_stud, repo_disc)
        srv_note.adauga_nota(id_nota, id_stud, id_disc, valoare)
        assert (len(repo_note) == 1)

        valoare_noua =1
        srv_note.update_nota(id_nota, valoare_noua)
        nota_gasita = srv_note.cauta_nota_dupa_id(id_nota)
        #assert (abs(nota_gasita.get_valoare() - valoare_noua) < 0.001)
        note = srv_note.get_all()
        #assert abs(note[0].get_valoare() - valoare_noua) < 0.001

    def __test_srv_get_note_la_o_disciplina_alfabetic(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        assert (srv_stud.get_nr_studenti() == 0)
        id_stud1 = 1
        nume_stud1 = "Marcel Pop"
        srv_stud.adauga_student(id_stud1, nume_stud1)
        id_stud2 = 2
        nume_stud2 = "Ion George"
        srv_stud.adauga_student(id_stud2, nume_stud2)
        assert (srv_stud.get_nr_studenti() == 2)
        valid_disc = ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        id_disc = 5
        nume_disc = "analiza"
        prof = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc,prof)
        assert (srv_disc.get_nr_discipline() == 1)
        valid_nota= ValidatorNota()
        repo_nota = RepoNote()
        srv_note = ServiceNote(repo_nota, valid_nota, repo_stud, repo_disc)
        id_nota1 = 9
        valoare1 = 5
        srv_note.adauga_nota(id_nota1,id_stud1, id_disc ,valoare1)
        id_nota2 = 10
        valoare2 = 8
        srv_note.adauga_nota(id_nota2, id_stud1, id_disc, valoare2)
        id_nota3 = 11
        valoare3 = 9
        srv_note.adauga_nota(id_nota3, id_stud2, id_disc, valoare3)
        assert (len(repo_nota) == 3)
        note = srv_note.get_note_la_o_disciplina_alfabetic(id_disc)
        assert (note == ["Ion George:\n\t9\n","Marcel Pop:\n\t8\n\t5\n"])

    def __test_srv_get_note_la_o_disciplina_dupa_nota(self):
        valid_stud = ValidatorStudent()
        repo_stud = RepoStudenti()
        srv_stud = ServiceStudenti(valid_stud, repo_stud)
        assert (srv_stud.get_nr_studenti() == 0)
        id_stud1 = 1
        nume_stud1 = "Marcel Pop"
        srv_stud.adauga_student(id_stud1, nume_stud1)
        id_stud2 = 2
        nume_stud2 = "Ion George"
        srv_stud.adauga_student(id_stud2, nume_stud2)
        assert (srv_stud.get_nr_studenti() == 2)
        valid_disc = ValidatorDisciplina()
        repo_disc = RepoDiscipline()
        srv_disc = ServiceDiscipline(valid_disc, repo_disc)
        id_disc = 5
        nume_disc = "analiza"
        prof = "berinde"
        srv_disc.adauga_disciplina(id_disc, nume_disc, prof)
        assert (srv_disc.get_nr_discipline() == 1)
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
        assert (len(repo_nota) == 3)
        note = srv_note.get_note_la_o_disciplina_dupa_nota(id_disc)
        assert (note == ["Ion George:\n\t9\n", "Marcel Pop:\n\t5\n\t8\n"])

    def __test_srv_get_20_toate_discipline_dupa_nota(self):
        validStud = ValidatorStudent()
        repoStud = RepoStudenti()
        srvStud = ServiceStudenti(validStud, repoStud)
        assert srvStud.get_nr_studenti() == 0
        idStud = 123
        numeStud = "george"
        student1 = Student(idStud, numeStud)
        srvStud.adauga_student(idStud, numeStud)
        idStud2 = 124
        numeStud2 = "mihai"
        student2 = Student(idStud2, numeStud2)
        srvStud.adauga_student(idStud2, numeStud2)
        idStud3 = 125
        numeStud3 = "tudor"
        student3 = Student(idStud3, numeStud3)
        srvStud.adauga_student(idStud3, numeStud3)
        assert srvStud.get_nr_studenti() == 3
        validDis = ValidatorDisciplina()
        repoDis = RepoDiscipline()
        srvDis = ServiceDiscipline(validDis, repoDis)
        assert srvDis.get_nr_discipline() == 0
        idDisciplina = 123
        numeDisciplina = "matematica"
        profesor = "berinde"
        srvDis.adauga_disciplina(idDisciplina, numeDisciplina, profesor)
        assert srvDis.get_nr_discipline() == 1
        validNota = ValidatorNota()
        repoNota = RepoNote()
        srvNota = ServiceNote(repoNota, validNota, repoStud, repoDis)
        idNota = 456
        valoare = 5.6
        srvNota.adauga_nota(idNota, idStud, idDisciplina, valoare)
        idNota2 = 457
        valoare2 = 6
        srvNota.adauga_nota(idNota2, idStud, idDisciplina, valoare2)
        idNota3 = 458
        valoare3 = 8.9
        srvNota.adauga_nota(idNota3, idStud2, idDisciplina, valoare3)
        idNota4 = 459
        valoare4 = 7.2
        srvNota.adauga_nota(idNota4, idStud3, idDisciplina, valoare4)
        assert len(repoNota) == 4
        note_generale = srvNota.medie_generala()
        assert note_generale[0][0] == student1
        assert abs(note_generale[0][1] - 5.8) < 0.001
        assert note_generale[1][0] == student2
        assert abs(note_generale[1][1] - 8.9) < 0.001
        assert note_generale[2][0] == student3
        assert abs(note_generale[2][1] - 7.2) < 0.001
        nota1 = NotaGeneralaStudentDTO(note_generale[1][0].get_nume(), note_generale[1][1])
        note_20 = srvNota.get_20_studenti_nota()
        assert len(note_20) == 1
        assert note_20[0] == nota1

    def run_all_tests(self):
        print ("start all tests")

        self.__test_creeaza_student()
        self.__test_valideaza_student()
        self.__test_adauga_student_repo()
        self.__test_adauga_student_service()

        self.__test_creeaza_disciplina()
        self.__test_valideaza_disciplina()
        self.__test_adauga_disciplina_repo()
        self.__test_adauga_disciplina_service()

        self.__test_cautare_student_repo()
        self.__test_cautare_student_service()

        self.__test_cautare_disciplina_repo()
        self.__test_cautare_disciplina_service()

        self.__test_modificare_student_repo()
        self.__test_modificare_student_service()

        self.__test_modificare_disciplina_repo()
        self.__test_modificare_disciplina_service()

        self.__test_sterge_student_repo()
        self.__test_sterge_student_service()

        self.__test_sterge_disciplina_repo()
        self.__test_sterge_disciplina_service()

        self.__test_creeaza_nota()
        self.__test_adauga_nota_repo()
        self.__test_sterge_nota_repo()
        self.__test_update_nota_repo()
        self.__test_srv_adauga_nota()
        self.__test_srv_sterge_nota()
        self.__test_srv_update_nota()

        self.__test_srv_get_note_la_o_disciplina_alfabetic()
        self.__test_srv_get_note_la_o_disciplina_dupa_nota()
        #self.__test_srv_get_20_toate_discipline_dupa_nota()

        print ("finished all tests succesufully")
