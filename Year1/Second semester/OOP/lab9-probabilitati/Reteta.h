//
// Created by Ilinca on 25-Apr-22.
//

#ifndef LAB4_6OOP_RETETA_H
#define LAB4_6OOP_RETETA_H

#include "Medicament.h"
#include <vector>
#include <algorithm>
#include <random> //std::default_random_engine
#include <chrono> //std::chrono::system_clock

using std::vector;
class List {
    vector<Medicament> listproducts;
public:
    List()=default;

    /*
     * Adaugam un medicament pe reteta
     * pre-m:medicamentul ce se adauga
     * post-medicamentul m va fi in lista
     */

    void addList(const Medicament& m);

    /*
     *Goleste reteta
     * post-lista este goala
     */
    void emptyList();

    /*
     * Adauga un numar random de medicamente in reteta.
     * originalmeds:medicamentele din care se alege
     * howMany: cate medicamente sa se adauge (int)
     * post-medicamentele sunt adaugate in reteta curenta.
     */
    void addrandomlist(vector<Medicament> originalprod, size_t howMany);

    /*
     * Returneaza un vector care contine toate medicamentele de pe reteta.
     */
    const vector<Medicament>& getallfromList();
    void export_reteta(string& fisier);

};

#endif //LAB4_6OOP_RETETA_H
