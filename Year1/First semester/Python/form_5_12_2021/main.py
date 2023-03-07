from tests.teste import Teste
from validatori.ValidProbLab import Validator_problema_lab
from persistenta.repository import Repo_prob_lab_file
from business.servicii import Service_prob_lab
from prezentare.ui import Consola
if __name__ == '__main__':
   teste = Teste()
   teste.run()

   valid= Validator_problema_lab()
   repo = Repo_prob_lab_file("prob_lab.txt")
   service = Service_prob_lab(valid, repo)

   ui = Consola(service)
   ui.run()