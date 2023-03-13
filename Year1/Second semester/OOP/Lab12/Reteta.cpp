//
// Created by Ilinca on 25-Apr-22.
//

#include "Reteta.h"
#include <fstream>
using std::ofstream;
using std::shuffle;

void List::addList(const Medicament& m) {
    this->listproducts.push_back(m);
    notify();
}

void List::emptyList() {
    this->listproducts.clear();
    notify();
}

void List::addrandomlist(vector<Medicament> originalprod, size_t howMany) {
    //amestecam elementele vectorului v
    shuffle(originalprod.begin(), originalprod.end(), std::default_random_engine(std::random_device{}()));
    while (listproducts.size() < howMany && originalprod.size() > 0) {
        listproducts.push_back(originalprod.back());
        originalprod.pop_back();
    }
    notify();
}

const vector<Medicament>& List::getallfromList() {
    return this->listproducts;
    notify();
}

void List::export_reteta(string& fisier) {
    fisier += ".csv";
    ofstream fout(fisier);
    for (auto& med : listproducts) {
        fout << med.get_denumire() << "," << med.get_producator() << "," << med.get_substanta_activa() << "," << med.get_pret() << endl;

    }
    notify();
}


