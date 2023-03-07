from domain.entitati import Inscriere
class Service_Cursuri():

    def __init__(self, repo_cursuri):
        self.__repo_cursuri = repo_cursuri

    def cauta_limba_str(self,lb_str):
        # functie care returneaza cursurile ce continut string-ul dat in limba straina
        #input: lb_str= string-ul cautat
        #output: rezultat-lista de cursuri ce contin string-ul dat in limba straina
        cursuri = self.__repo_cursuri.get_all()
        rezultat = []
        for curs in cursuri:
            if lb_str in curs.get_limba_straina():
                rezultat.append(curs)

        return rezultat

    def total_inscriere(self, id_curs, numar_ore):
        #functie care gaseste cursul cu id-ul dat si calculeaza suma de plata in functie de numarul de ore
        #input: id_curs - id-ul cursului dorit
        #       numar_ore - numarul de ore dorite
        #output: rezultat- o lista ce contine inscrierea dorita si suma de plata
        rezultat = []
        inscriere = 0
        cursuri = self.__repo_cursuri.get_all()
        for curs in cursuri:
            if curs.get_id_curs() == id_curs:
                inscriere = Inscriere(curs, numar_ore)
        suma = inscriere.get_total()
        rezultat.append(inscriere)
        rezultat.append(suma)
        return rezultat


