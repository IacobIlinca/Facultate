from persistenta.repo import RepoElicopterFile
from business.servicii import ServiceElicoptere
from prezentare.user_interface import Consola
from testare.teste import Teste
if __name__ == '__main__':
    repo_elic = RepoElicopterFile("elicoptere.txt")
    srv_elic = ServiceElicoptere(repo_elic)

    teste = Teste()
    teste.run_all_tests()

    ui = Consola(srv_elic)
    ui.run()

