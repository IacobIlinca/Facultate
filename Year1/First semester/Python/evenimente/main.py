from validatori.validare import ValidareEveniment
from persistenta.repo_evenimente import FileRepoEvenimente
from business.service import ServiceEvenimente
from prezentare.ui import Console
if __name__ == '__main__':
    valid_eveniment = ValidareEveniment()
    file_path = "evenimente.txt"
    repo_eveniment = FileRepoEvenimente(file_path)
    service_evenimente = ServiceEvenimente(valid_eveniment,repo_eveniment)

    ui = Console(service_evenimente)
    ui.run()
