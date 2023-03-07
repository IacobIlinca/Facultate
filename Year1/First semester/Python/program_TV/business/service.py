class ServiceEmisiune:

    def __init__(self, valid_emisiune, repo_emisiune):
        self.__valid_emisiune = valid_emisiune
        self.__repo_emisiune = repo_emisiune

    def get_all(self):
        return self.__repo_emisiune.get_all()

    def sterge_emisiune(self,nume,tip):
        self.__repo_emisiune.sterge_emisiune(nume,tip)

    def update_emisiune(self,nume,dur_noua,desc_noua):
        self.__repo_emisiune.update_emisiune(nume,dur_noua,desc_noua)

    def ordonare_cres_durata(self):
        emisiuni = self.__repo_emisiune.get_all()
        for i in (0,len(emisiuni)):
            for j in (i+1, len(emisiuni)):
                if emisiuni[i].get_durata()>emisiuni[j].get_durata():
                    emisiuni[i],emisiuni[j] = emisiuni[j],emisiuni[i]
        return emisiuni

    def lista(self):
        lista = self.__repo_emisiune.get_all()
        return lista[1]

    def write_to_another_file(self,file_path,lista):
        self.__repo_emisiune.write_to_another_file(file_path,lista)


