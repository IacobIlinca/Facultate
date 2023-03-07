from validare.validatori import ValidMelodie
from persistenta.repo_melodii import FileRepoMelodii
from business.service import ServiceMelodii
from prezentare.ui import Console
if __name__ == '__main__':

    valid_melodie = ValidMelodie()
    repo_melodii = FileRepoMelodii("melodii.txt")

    service_melodii = ServiceMelodii(valid_melodie,repo_melodii)
    ui = Console(service_melodii)
    ui.run()

