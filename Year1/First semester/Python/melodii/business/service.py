class ServiceMelodii:

    def __init__(self, valid_melodie, repo_melodii):
        self.__valid_melodie = valid_melodie
        self.__repo_melodii = repo_melodii

    def modifica_melodie(self, melodie, gen, data):
        self.__repo_melodii.modifica_melodie(melodie,gen,data)
