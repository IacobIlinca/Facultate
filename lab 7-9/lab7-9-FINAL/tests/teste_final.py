from tests.teste_studenti_ut import Testestud
from tests.teste_disc_ut import Testedisc
from tests.teste_note_ut import Testenote
class Teste():

    def __init__(self):
        self.__teste_stud = Testestud()
        self.__teste_disc = Testedisc()
        self.__teste_note = Testenote()

    def run_all_tests(self):
        print("Start teste...")
        self.__teste_stud.run_all_tests_studenti()
        self.__teste_disc.run_all_tests_discipline()
        self.__teste_note.run_all_tests_note()