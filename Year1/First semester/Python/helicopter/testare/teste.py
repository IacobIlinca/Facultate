from persistenta.repo import RepoElicopterFile
from business.servicii import ServiceElicoptere
class Teste():

    def __test_citire(self):
        repo_elic = RepoElicopterFile("testare/teste.txt")
        assert len(repo_elic) == 7

    def __test_afisare_scop(self):
        repo_elic = RepoElicopterFile("testare/teste.txt")
        all_elic = repo_elic.get_all()
        assert len(repo_elic) == 7
        srv_elic = ServiceElicoptere(repo_elic)
        scop = "mare"
        rezultat = srv_elic.cauta_scop(scop)
        assert len(rezultat) == 1
        assert rezultat[0] == all_elic[6]


    def __test_scop_an(self):
        repo_elic = RepoElicopterFile("testare/teste.txt")
        all_elic = repo_elic.get_all()
        assert len(repo_elic) == 7
        srv_elic = ServiceElicoptere(repo_elic)
        scopuri = srv_elic.scop_an()
        assert(len(scopuri) == 7 )
        scop = "mare"
        assert len(scopuri[scop]) == 1


    def run_all_tests(self):
        print("start tests...")
        self.__test_citire()
        self.__test_afisare_scop()
        self.__test_scop_an()
        print("tested succesfully!")