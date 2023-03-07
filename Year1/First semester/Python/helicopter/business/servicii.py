from erori.exceptii import SrvError
class ServiceElicoptere():

    def __init__(self, repo_elic):
        self.__repo_elic = repo_elic

    def ord_desc_nume(self, elicoptere):
        if elicoptere == -1:
            return
        else:
            lungime = len(elicoptere)
            for i in range (0 , lungime-1):
                for j in range (i+1, lungime):
                    if elicoptere[i].get_nume() < elicoptere[j].get_nume():
                        aux = elicoptere[i]
                        elicoptere[i] = elicoptere[j]
                        elicoptere[j] = aux
            return elicoptere


    def cauta_scop(self, scop):
        elicoptere = self.__repo_elic.get_all()
        rezultat = []
        for _elic in elicoptere:
            if scop in _elic.get_scopuri():
                rezultat.append(_elic)
        if len(rezultat)>0:
            return rezultat
        else:
            print("nu exista elicoptere cu scopul cerut!")
            rezultat = -1
            return rezultat

    def scopuri(self):
        elicoptere = self.__repo_elic.get_all()
        scopuri = []
        for _elic in elicoptere:
            scop_elic = _elic.get_scopuri()
            scop_elic = scop_elic.split(" ")
            for scop in scop_elic:
                if scop not in scopuri:
                    scopuri.append(scop)
        return scopuri

    def scop_an(self):
       scopuri = {}
       elicoptere = self.__repo_elic.get_all()
       for elic in elicoptere:
           scop = elic.get_scopuri().split(" ")
           for _scop in scop:
               if _scop not in scopuri:
                   scopuri[_scop] = [elic.get_an()]
               else:
                   scopuri[_scop].append(elic.get_an())
       return scopuri

