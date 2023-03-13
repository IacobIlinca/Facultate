//
// Created by Ilinca on 30-Mar-22.
//

#include "Repository.h"
#include <assert.h>
#include <algorithm>
#include <fstream>
#include <sstream>
using std::ifstream;
using std::stringstream;
using std::ofstream;

const Medicament& Medicament_Repository::find(string denumire, string producator) {
    //    for(const Medicament& m: this->all_medicamente){
    //        if(m.get_denumire() == denumire && m.get_producator() == producator){
    //            return m;
    //        }
    //    }
    //    throw Repo_Exception("Medicamentul cu denumirea "+denumire+" si producatorul "+producator+" nu este in lista");

    vector<Medicament>::iterator f = std::find_if(this->all_medicamente.begin(), this->all_medicamente.end(), [=](const Medicament& m)
        {return m.get_denumire() == denumire && m.get_producator() == producator; });

    if (f != this->all_medicamente.end())
        return (*f);
    else
        throw Repo_Exception("Medicamentul pe care il cautati nu exista.");

}

const Medicament& Medicament_Repository::find_denumire(string denumire) {
    for (const Medicament& m : this->all_medicamente) {
        if (m.get_denumire() == denumire) {
            return m;
        }
    }
    throw Repo_Exception("Medicamentul cu denumirea " + denumire + " nu este in lista");

}

bool Medicament_Repository::exists(const Medicament& m) {
    try {
        find(m.get_denumire(), m.get_producator());
        return true;
    }
    catch (Repo_Exception) {
        return false;
    }
}

const vector<Medicament>& Medicament_Repository::get_all_medicamente() {
    return this->all_medicamente;
}

void Medicament_Repository::store(const Medicament& m) {
    if (exists(m)) {
        throw Repo_Exception("Medicamentul cu denumirea " + m.get_denumire() + " si producatorul " + m.get_producator() + " nu este in lista");
    }
    this->all_medicamente.push_back(m);
}


void Medicament_Repository::modificare_pret_repo(const Medicament& med) {
    if (!exists(med)) {
        throw Repo_Exception("Medicamentul dorit nu este in lista!\n");
    }
    int i = 0;
    for (auto& medic : this->all_medicamente) {
        if (medic.get_denumire() == med.get_denumire() && medic.get_producator() == med.get_producator() && medic.get_substanta_activa() == med.get_substanta_activa()) {
            medic.set_pret(med.get_pret());
            //medic=med;
        }
        i++;
    }
}

void Medicament_Repository::stergere_repo(const Medicament& med) {
    if (!exists(med)) {
        throw Repo_Exception("Medicamentul nu este in lista.\n");
    }
    /*
    int i = 0;
    for (auto& medic : this->all_medicamente) {
        if (medic.get_denumire() == med.get_denumire() && medic.get_producator() == med.get_producator() && medic.get_substanta_activa() == med.get_substanta_activa() && medic.get_pret() == med.get_pret()) {
            this->all_medicamente.erase(this->all_medicamente.begin() + i);
        }
        i++;
    }
    */
    for (size_t i = 0; i < all_medicamente.size(); i++) {
        if (all_medicamente[i].get_denumire() == med.get_denumire()) {
            all_medicamente.erase(all_medicamente.begin() + i);
        }
    }
}


void RepoFile::load() {
    ifstream prodFile(this->filename);
    if (!prodFile.is_open()) {
        throw Repo_Exception("Cannot read from file" + filename + "!\n");
    }
    string line;
    while (getline(prodFile, line))
    {
        string denumire, producator, substanta_activa;
        double pret;

        stringstream linestream(line);
        string current_item;
        int item_no = 0;
        while (getline(linestream, current_item, ','))
        {
            if (item_no == 0) denumire = current_item;
            if (item_no == 1) producator = current_item;
            if (item_no == 2) substanta_activa = current_item;
            if (item_no == 3) pret = stod(current_item);
            item_no++;
        }
        Medicament m{ denumire, producator, substanta_activa, pret };
        Medicament_Repository::store(m);
    }
    prodFile.close();
}

void RepoFile::write() {
    ofstream medOutput(this->filename);
    if (!medOutput.is_open())
        throw Repo_Exception("Cannot write to file " + filename + " !\n");
    for (auto& med : get_all_medicamente())
    {
        medOutput << med.get_denumire() << "," << med.get_producator() << "," << med.get_substanta_activa() << "," << med.get_pret() << endl;
    }
    medOutput.close();
}

void RepoFile::store(const Medicament& m) {
    Medicament_Repository::store(m);
    write();
}

void RepoFile::modificare_pret_repo(const Medicament& m) {
    Medicament_Repository::modificare_pret_repo(m);
    write();
}

void RepoFile::stergere_repo(const Medicament& m) {
    Medicament_Repository::stergere_repo(m);
    write();
}
