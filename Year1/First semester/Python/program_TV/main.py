from validatori.validare import ValidEmisiune
from persistenta.repo_emisiuni import FileRepoEmisiuni
from business.service import ServiceEmisiune
from prezentare.ui import Console
if __name__ == '__main__':
    validator_emisiune = ValidEmisiune()
    repo_emisiuni = FileRepoEmisiuni("emisiuni.txt")
    service_emisiuni = ServiceEmisiune(validator_emisiune, repo_emisiuni)

    ui = Console(service_emisiuni)
    ui.run()
