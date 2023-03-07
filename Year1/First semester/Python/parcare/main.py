from persistenta.repo import RepoLocuriParcFile
from business.service import ServiceLoc
from prezentare.user_interface import Consola

if __name__ == '__main__':
    repo_locuri = RepoLocuriParcFile("locuri.txt")
    srv_locuri = ServiceLoc(repo_locuri)
    ui = Consola(srv_locuri)
    ui.run()
