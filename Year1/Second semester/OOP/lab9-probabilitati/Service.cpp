//
// Created by Ilinca on 30-Mar-22.
//

#pragma once
#include "Service.h"
#include <assert.h>
#include <functional>
#include <algorithm>
#include "Undo.h"
using std::make_unique;

void Medicamente_Service::add_medicament(string denumire, string producator, string substanta_activa, double pret) {
    Medicament med1{denumire, producator, substanta_activa, pret};
    val.valideaza(med1);
    repo.store(med1);
    UndoActions.push_back( make_unique<UndoAdauga>(repo, med1));
}

void Medicamente_Service::modifica_pret_service(string denumire, string producator, string substanta_activa,
                                                double pret_nou) {
    Medicament med1{denumire, producator, substanta_activa, pret_nou};
    val.valideaza(med1);
    Medicament med2=repo.find(med1.get_denumire(), med1.get_producator());
    repo.modificare_pret_repo(med1);
    UndoActions.push_back(make_unique<UndoModifica>(repo, med2));
}

void Medicamente_Service::stergere_service(string denumire, string producator, string substanta_activa, double pret) {
    Medicament med1{denumire, producator, substanta_activa, pret};
    val.valideaza(med1);
    repo.stergere_repo(med1);
    UndoActions.push_back(make_unique<UndoSterge>(repo, med1));
}

Medicament Medicamente_Service::find_service(string denumire, string producator) {
    return repo.find(denumire, producator);
}

vector<Medicament> Medicamente_Service::filtrare_substanta_activa(string substanta_activa) {
//    vector<Medicament> rezultat;
//    for(const auto& med : repo.get_all_medicamente()) {
//        if(med.get_substanta_activa() == substanta_activa){
//            rezultat.push_back(med);
//        }
//    }
//    return rezultat;

    const vector<Medicament>& allmeds = get_all_medicamente();
    vector<Medicament> rezultat;
    std::copy_if(allmeds.begin(), allmeds.end(), back_inserter(rezultat),[substanta_activa](const Medicament& m)
    {return m.get_substanta_activa()==substanta_activa;});
    return rezultat;
}

vector<Medicament> Medicamente_Service::filtrare_pret(double pret) {
//    vector<Medicament> rezultat;
//    for(const auto& med : repo.get_all_medicamente()) {
//        if(med.get_pret() == pret){
//            rezultat.push_back(med);
//        }
//    }
//    return rezultat;
    const vector<Medicament>& allmeds = get_all_medicamente();
    vector<Medicament> rezultat;
    std::copy_if(allmeds.begin(), allmeds.end(), back_inserter(rezultat),[pret](const Medicament& m)
    {return m.get_pret()==pret;});
    return rezultat;
}

/*
vector<Medicament> Medicamente_Service::general_sort(bool (*mai_mic_f)(const Medicament &, const Medicament &)) {
    vector<Medicament> v{repo.get_all_medicamente()};
    for (size_t i=0;i<v.size();i++) {
        for (size_t j = i + 1; j < v.size(); j++) {
            if (!mai_mic_f(v[i], v[j])) {
                Medicament aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }
    return v;
}

vector<Medicament> Medicamente_Service::sort_by_denumire() {
    auto sorted_copy = repo.get_all_medicamente();
    sort(sorted_copy.begin(), sorted_copy.end(), cmp_denumire);
    return sorted_copy;
}

vector<Medicament> Medicamente_Service::sort_by_producator() {
    auto sorted_copy = repo.get_all_medicamente();
    sort(sorted_copy.begin(), sorted_copy.end(), cmp_producator);
    return sorted_copy;
}

 */
//vector<Medicament> Medicamente_Service::sortservice(int reverse, bool (*functie)(Medicament &, Medicament &)) {
//    vector<Medicament> v{repo.get_all_medicamente() };  //copie
//
//    for (int i=0;i<v.size();i++)
//    {
//        for (int j=i+1;j<v.size();j++)
//        {
//            if (reverse == 0)
//            {
//                //crescator
//                if (!functie(v[i],v[j]))
//                {
//                    Medicament aux = v[i];
//                    v[i] = v[j];
//                    v[j] = aux;
//                }
//            }
//            else
//            {
//                //descrescator
//                if (functie(v[i], v[j]))
//                {
//                    Medicament aux = v[i];
//                    v[i] = v[j];
//                    v[j] = aux;
//                }
//            }
//        }
//    }
//    return v;
//}

vector<Medicament> Medicamente_Service::sortdenumire(int reverse) {
    vector<Medicament> sorted{ repo.get_all_medicamente() };
    sort(sorted.begin(),sorted.end(), cmp_denumire);
    if (reverse == 1) {
        std::reverse(sorted.begin(), sorted.end());
    }
    return sorted;
    //return sortservice(reverse, cmp_denumire);
}

vector<Medicament> Medicamente_Service::sortproducator(int reverse) {
    vector<Medicament> sorted{ repo.get_all_medicamente() };
    sort(sorted.begin(),sorted.end(), cmp_producator);
    if (reverse == 1) {
        std::reverse(sorted.begin(), sorted.end());
    }
    return sorted;
    //return sortservice(reverse, cmp_producator);
}

vector<Medicament> Medicamente_Service::sortdsubstpret(int reverse) {
    vector<Medicament> sorted{ repo.get_all_medicamente() };
    sort(sorted.begin(),sorted.end(), cmp_substspret);
    if (reverse == 1) {
        std::reverse(sorted.begin(), sorted.end());
    }
    return sorted;
    //return sortservice(reverse, cmp_substspret);
}


int Medicamente_Service::all_of_denumire_incepe_cu_a(string denumire) {
    vector<Medicament> copie { repo.get_all_medicamente() };
    if (std::all_of(copie.begin(), copie.end(), [denumire](Medicament& m){ return m.get_denumire() == denumire;}))
    {
        return 1;
    }
    return 0;
}


//FUNCTIONALITATI RETETA

void Medicamente_Service::add_list_service(string denumire) {
    const auto& med = repo.find_denumire(denumire);
    currentlist.addList(med);
}

int Medicamente_Service::add_random_service(int howMany) {
    currentlist.addrandomlist(this->get_all_medicamente(), howMany);
    return currentlist.getallfromList().size();
}

void Medicamente_Service::empty_list_service() {
    currentlist.emptyList();
}

const vector<Medicament>& Medicamente_Service::get_all_from_list_service() {
    return currentlist.getallfromList();
}

void Medicamente_Service::export_reteta(string &fisier) {
    currentlist.export_reteta(fisier);
}


void Medicamente_Service::undo() {
    if (UndoActions.size() < 1) {
        throw UndoException("Nu se poate da undo!\n");
    }
    UndoActions.back()->doUndo();
    UndoActions.pop_back();
}


size_t Medicamente_Service::get_dim_undo() noexcept {
    return UndoActions.size();
}