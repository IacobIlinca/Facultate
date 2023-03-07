class ServiceLoc():
    def __init__(self, repo_locuri):
        self.__repo_locuri = repo_locuri

    def cauta_strada(self, strada):
        locuri = self.__repo_locuri.get_all()
        rezultat = []
        for loc in locuri:
            if loc.get_strada() == strada:
                rezultat.append(loc)
        rezultat.sort(key=lambda x:x.get_nume(), reverse=True)
        return rezultat

    # def ord_nume(self,rezultat):
    #
    #     lungime = len(rezultat)
    #     for i in range (0 , lungime-1):
    #         for j in range (i+1, lungime):
    #             if rezultat[i].get_nume() < rezultat[j].get_nume():
    #                 aux = rezultat[i]
    #                 rezultat[i] = rezultat[j]
    #                 rezultat[j] = aux
    #     return rezultat

    def get_all(self):
        rezultat = self.__repo_locuri.get_all()
        return rezultat