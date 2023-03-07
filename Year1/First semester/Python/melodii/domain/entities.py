class Melodie:

    def __init__(self, titlu, artist,gen, data):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__data = data

    def get_titlu(self):
        return self.__titlu

    def get_artist(self):
        return self.__artist

    def get_gen(self):
        return self.__gen

    def get_data(self):
        return self.__data

    def set_gen(self,gen):
        self.__gen = gen

    def set_data(self,data):
        self.__data = data

    def __eq__(self, other):
        return str(self.__titlu) == str(other.get_titlu()) or str(self.__gen) == str(other.get_gen()) or str(self.__artist) == str(other.get_artist()) or str(self.__data) == str(other.get_data())

    def __str__(self):
        return self.__titlu + "," + self.__artist + ","+ self.__gen + "," + self.__data
