from persistenta.repo_cursuri import RepoCursuriFile
from business.service_cursuri import Service_Cursuri
class Teste():

    def __test_citire_ok(self):
        repo_cursuri = RepoCursuriFile("testare/teste.txt")
        assert len(repo_cursuri) == 8

    def __test_cauta_limba_str(self):
        repo_cursuri = RepoCursuriFile("testare/teste.txt")
        all_cursuri = repo_cursuri.get_all()
        assert len(repo_cursuri) == 8
        srv_cursuri = Service_Cursuri(repo_cursuri)
        lb_str = "engleza"
        rezultat = srv_cursuri.cauta_limba_str(lb_str)
        assert len(rezultat) == 2
        assert rezultat[0] == all_cursuri[0]
        assert rezultat[1] == all_cursuri[4]

    def __test_total_inscriere(self):
        repo_cursuri = RepoCursuriFile("testare/teste.txt")
        assert len(repo_cursuri) == 8
        srv_cursuri = Service_Cursuri(repo_cursuri)
        id_curs = "ENG1"
        numar_ore = 2
        rezultat = srv_cursuri.total_inscriere(id_curs, numar_ore)
        inscriere = "Limba straina a cursului este:limba_engleza-> Nivelul cursului este:A1"
        assert len(rezultat) == 2
        assert str(rezultat[0]) == inscriere
        assert rezultat[1]== 140


    def run_all_tests(self):
        print("s-a inceput testarea...")
        self.__test_citire_ok()
        self.__test_cauta_limba_str()
        self.__test_total_inscriere()
        print("testat cu succes!")