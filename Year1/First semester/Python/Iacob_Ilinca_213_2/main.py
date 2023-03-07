from persistenta.repo_cursuri import RepoCursuriFile
from business.service_cursuri import Service_Cursuri
from prezentare.user_interface import Consola
from testare.teste import Teste

if __name__ == '__main__':
    repo_cursuri = RepoCursuriFile("cursuri.txt")
    srv_cursuri  = Service_Cursuri(repo_cursuri)

    teste = Teste()
    teste.run_all_tests()

    ui = Consola(srv_cursuri)
    ui.run()
