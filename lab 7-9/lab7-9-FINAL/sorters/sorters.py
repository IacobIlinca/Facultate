class Sorter():

    def _identitate(self, x):
        return x

    def _negare(self, x):
        return not x

    def sort(self, list, key=lambda x: x, cmp=lambda x, y: x < y, reversed=False):
        pass


class MergeSorter(Sorter):
    def sort(self, list, key=lambda x: x, cmp=lambda x, y: x < y, reversed=False):
        st = 0
        dr = len(list) - 1
        if reversed:
            operatie = self._negare
        else:
            operatie = self._identitate
        self.__merge_sort_r(list, key, cmp, operatie, st, dr)

    def __merge_sort_r(self, list, key, cmp, operatie, st, dr):
        if st < dr:
            mij = st + (dr - st) // 2
            self.__merge_sort_r(list, key, cmp, operatie, st, mij)
            self.__merge_sort_r(list, key, cmp, operatie, mij + 1, dr)
            self.__merge(list, key, cmp, operatie, st, mij, dr)

    def __merge(self, list, key, cmp, operatie, st, mij, dr):
        i = st
        j = mij + 1
        k = st
        aux = [None] * len(list)
        while i <= mij and j <= dr:
            if operatie(cmp(key(list[i]), key(list[j]))):
                aux[k] = list[i]
                k += 1
                i += 1
            else:
                aux[k] = list[j]
                k += 1
                j += 1
        while i <= mij:
            aux[k] = list[i]
            k += 1
            i += 1
        while j <= dr:
            aux[k] = list[j]
            k += 1
            j += 1

        for i in range(st, dr + 1):
            list[i] = aux[i]


class BingoSorter(Sorter):

    @staticmethod
    def valoare_minima(list, cmp, key):
        mini = [0, 0]
        for i in range(0, len(list)):
            if cmp(key(list[i]), key(mini)):
                mini[1] = list[i]
        return mini

    @staticmethod
    def valoare_maxima(list, cmp, key):
        maxi = list[0]
        for i in range(0, len(list)):
            if cmp(list[i], maxi):
                pass
            else:
                maxi = list[i]
        return key(maxi)

    def sort(self, list, key=lambda x: x, cmp=lambda x, y: x[1] < y[1], reversed=False):
        # if reversed:
        #     cmp = lambda x,y:cmp (y,x)
        sorted_elements = 0
        while sorted_elements != len(list):
            new_list = []
            if sorted_elements == 0:
                new_list = list
            else:
                new_list = list[:-sorted_elements]
            max_val = self.valoare_maxima(new_list, cmp, key)
            aparitii = 0
            elemente = []
            for i in range(0, len(list) - sorted_elements):
                if key(list[i]) == max_val:
                    aparitii += 1
                    elemente.append(list[i])
                else:
                    list[i - aparitii] = list[i]
            for i in range (len(list)-sorted_elements-aparitii, len(list)-sorted_elements):
                list[i] = elemente[0]
                elemente = elemente[1:]
            sorted_elements += aparitii

        if reversed:
            list.reverse()


        # min_val = self.valoare_minima(list, cmp, key)
        # max_val = self.valoare_maxima(list, cmp, key)
        # if reversed:
        #     operatie = self._negare
        # else:
        #     operatie = self._identitate
        # self.__bingo_sort(list, key, cmp,operatie,min_val, max_val)

    def __bingo_sort(self, list, key, cmp, operatie, min_val, max_val):
        bingo = min_val
        next_avail = 1
        next_bingo = max_val
        n = len(list)
        while bingo < max_val:
            start_pos = next_avail
            for i in range(start_pos, n):
                if list[i] == bingo:
                    aux = list[i]
                    list[i] = list[next_avail]
                    list[next_avail] = aux
                    next_avail += 1
                elif operatie(cmp(key(list[i]), key(next_bingo))):
                    # elif list[i] < next_bingo:
                    next_bingo = list[i]
            bingo = next_bingo
            next_bingo = max_val


def comparare_noua(nota1, nota2):
    """
    :Compararea se va face pentru note:prima data dupa valoarea notei, mai apoi in caz de egalitate dupa numele studentului
    :param nota1:una din notele ce se doresc a fi comparate
    :param nota2:una din notele ce se doresc a fi comparate
    """
    if nota1.get_valoare() < nota2.get_valoare():
        return True
    if nota1.get_valoare() == nota2.get_valoare() and nota1.get_id_nota() < nota2.get_id_nota():
        return True
    return False


def comparare_noua2(x, y):
    """
    :Compararea se va face pentru discipline:prima data dupa nume, mai apoi in caz de egalitate dupa numele profesorului
    :param x:una din disciplinele ce se doresc a fi comparate
    :param y:una din disciplinele ce se doresc a fi comparate
    """
    if x.get_nume() < y.get_nume():
        return True
    if x.get_nume() == y.get_nume() and x.get_profesor() < y.get_profesor():
        return True
    return False
