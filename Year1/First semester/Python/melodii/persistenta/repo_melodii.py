from domain.entities import Melodie
class RepoMelodii:

    def __init__(self):
        self._melodii = []

    def get_all(self):
        return self._melodii[:]

    def modifica_melodie(self, melodie, gen, data):
        for mel in self._melodii:
            if mel == melodie:
                mel.set_gen(gen)
                mel.set_data(data)
                return
        print("ok")

class FileRepoMelodii(RepoMelodii):

    def __init__(self,file_path):
        RepoMelodii.__init__(self)
        self.__file_path = file_path

    def read_all_from_file(self):
        self._melodii = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    titlu = parts[0]
                    artist = parts[1]
                    gen = parts[2]
                    data = parts[3]
                    melodie = Melodie(titlu,artist,gen,data)
                    self._melodii.append(melodie)

    def append_to_file(self,melodie):
        with open(self.__file_path, "a") as f:
            f.write(str(melodie.get_titlu())+","+str(melodie.get_artist())+","+str(melodie.get_gen())+","+str(melodie.get_data())+"\n")

    def file_overwrite(self):
        f = open(self.__file_path, "w")
        for melodie in self._melodii:
            f.write(str(melodie.get_titlu())+","+str(melodie.get_artist())+","+str(melodie.get_gen())+","+str(melodie.get_data()))

    def write_to_a_new_file(self,new_file_path, lista):
        f = open(new_file_path, "w")
        for melodie in lista:
            f.write(str(melodie.get_titlu()) + "," + str(melodie.get_artist()) + "," + str(melodie.get_gen()) + "," + str(melodie.get_data()) + "\n")

    def get_all(self):
        self.read_all_from_file()
        return RepoMelodii.get_all(self)

    def modifica_melodie(self, melodie, gen, data):
        self.read_all_from_file()
        RepoMelodii.modifica_melodie(self, melodie, gen, data)
        self.file_overwrite()




