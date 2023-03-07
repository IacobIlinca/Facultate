//
// Created by Ilinca on 30-Mar-22.
//

#pragma once
#include "UI.h"
#include <iostream>
using namespace std;

void Console::print_meniu() {
    cout<<"Comenzile disponibile sunt:"<<endl;
    cout<<"1. Adauga un medicament."<<endl;
    cout<<"2. Modifica pretul unui medicament."<<endl;
    cout<<"3. Sterge un medicament."<<endl;
    cout<<"4. Afiseaza toate medicamentele."<<endl;
    cout<<"5. Gaseste un medicament dupa denumire si producator."<<endl;
    cout<<"6. Filtrare medicamente dupa substanta activa/pret."<<endl;
    cout<<"7. Sorteaza medicamente dupa denumire/producator/substanta activa+pret."<<endl;
    cout<<"8. Verifica daca toate medicamentele au o denumire data."<<endl;
    cout<<"9. MENIU RETETA MEDICAMENTE"<<endl;
    cout<<"0. Exit."<<endl;
}

void Console::print_meniu_list(){
    cout << "MENIU RETETA MEDICAMENTE:" << endl;
    cout << "1. Adauga medicament in reteta."<<endl;
    cout << "2. Adauga medicamente random in cos."<<endl;
    cout << "3. Goleste reteta."<<endl;
    cout << "4. Afiseaza medicamentele din reteta curenta."<<endl;
    cout << "5. Exporta reteta in fisier csv."<<endl;
    cout << "6. Intoarcere la meniul initial."<<endl;

}

void Console::ui_add() {
    string denumire, producator, substanta_activa;
    double pret;
    cout<<"Denumirea medicamentului este:";
    getline(cin>> ws , denumire);

    cout<<"Producatorul medicamentului este:";
    getline(cin>> ws , producator);

    cout<<"Substanta activa a medicamentului este:";
    getline(cin>> ws , substanta_activa);

    cout<<"Pretul medicamentului este:";
    cin >> pret;

    try{
        srv.add_medicament(denumire, producator, substanta_activa, pret);
    }
    catch (Repo_Exception& re) {
        cout << re.get_error_message();
    }
    catch (Validation_Exception& ve) {
        cout << "Medicamentul introdus nu este valid!" << endl;
        cout << ve.get_error_messages();
    }
}


void Console::print_all_medicamente() {
        const vector<Medicament>& all_medicamente = srv.get_all_medicamente();
        if(all_medicamente.size() == 0)
            cout << "Nu exista medicamente in lista!"<<endl;
        else
            for(const auto& med : all_medicamente){
                cout<<"Denumire: " << med.get_denumire() <<" || Producator: " << med.get_producator() << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

            }

}

void Console::ui_find() {
    string denumire, producator;
    Medicament med;
    cout << "Denumirea medicamentului cautat este:";
    getline(cin>>ws, denumire);

    cout << "Producatorul medicamentului cautat este:";
    getline(cin>>ws, producator);

    try {
        med = srv.find_service(denumire, producator);
        cout<<"Denumire: " << med.get_denumire() <<" || Producator: " << med.get_producator() << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

    }
    catch (Repo_Exception& re) {
        cout << re.get_error_message();
    }
    catch (Validation_Exception& ve) {
        cout << "Date invalide!"<<endl;
        cout << ve.get_error_messages();
    }

}

void Console::ui_modificare() {
    string denumire, producator, substanta_activa;
    double pret_nou;
    cout << "Denumirea medicamentului pe care doriti sa o modificati: \n";
    getline(cin >> ws, denumire);

    cout << "Producatorul medicamentului pe care doriti sa o modificati: \n";
    getline(cin >> ws, producator);

    cout << "Substanta activa a medicamentului pe care doriti sa o modificati: \n";
    getline(cin >> ws, substanta_activa);

    cout << "Noul pret al medicamentului: \n";
    cin >> pret_nou;
    try{
        srv.modifica_pret_service(denumire, producator, substanta_activa, pret_nou);
        cout << "Pretul medicamentului a fost modificat cu succes!!\n";
    }
    catch (Repo_Exception& re){
        cout << re.get_error_message();
    }
    catch (Validation_Exception& ve) {
        cout << "Medicamentul nu este valid!!" << endl;
        cout << ve.get_error_messages();
    }
}

void Console::ui_stergere(){
    string denumire, producator, substanta_activa;
    double pret;
    cout << "Denumirea medicamentului pe care doriti sa il stergeti:\n";
    getline(cin >> ws, denumire);

    cout << "Producatorul medicamentului pe care doriti sa il stergeti:\n";
    getline(cin >> ws, producator);

    cout << "Substanta activa a medicamentului pe care doriti sa il stergeti:\n";
    getline(cin >> ws, substanta_activa);

    cout << "Pretul medicamentului:\n";
    cin >> pret;

    try{
        srv.stergere_service(denumire, producator, substanta_activa, pret);
        cout << "Medicamentul a fost sters cu succes!\n";
    }
    catch (Repo_Exception& re){
        cout << re.get_error_message();
    }
    catch (Validation_Exception& ve){
        cout << ve.get_error_messages();
    }
}

void Console::ui_filtrare() {
    cout << "Optiunile pentru filtrare sunt:\n";
    cout << "1 - dupa substanta activa.\n";
    cout << "2 - dupa pret.\n";
    int filtru;
    string denumire, producator, substanta_activa;
    double pret;
    cout << "Introduceti filtrul dorit:\n";
    cin >> filtru;
    if (filtru == 1) {
        cout << "Introduceti substanta activa dupa care doriti sa se faca filtrarea:\n";
        getline(cin >> ws, substanta_activa);
        if (srv.filtrare_substanta_activa(substanta_activa).size() == 0)
            cout << "Nu exista medicamente cu aceasta substanta activa!\n";
        for (const auto &med: srv.filtrare_substanta_activa(substanta_activa)) {
            cout << "Denumire: " << med.get_denumire() << " || Producator: " << med.get_producator()
                 << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

        }
    }

    if (filtru == 2) {
        cout << "Introduceti pretul dupa care doriti sa se faca filtrarea:\n";
        cin >> pret;
        if (srv.filtrare_pret(pret).size() == 0)
            cout << "Nu exista medicamente cu acest pret!\n";
        for (const auto &med: srv.filtrare_pret(pret)) {
            cout << "Denumire: " << med.get_denumire() << " || Producator: " << med.get_producator()
                 << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

        }
    }
}

//void Console::print_meds

void Console::ui_sort() {
    int ordine, optiune;
    cout << "Sortati dupa:" << endl;
    cout << "1-Denumire    2-Producator    3-Substanta activa+Pret" << endl;
    cin >> optiune;
    cout << "Ordinea poate fi: 0-crescator      1-descrescator:" << endl;
    cin >> ordine;
    if (optiune == 1)
    {
        for (const auto& med: srv.sortdenumire(ordine))
        {
            cout << "Denumire: " << med.get_denumire() << " || Producator: " << med.get_producator()
                 << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

        }
    }
    if (optiune == 2)
    {
        for (const auto& med: srv.sortproducator(ordine))
        {
            cout << "Denumire: " << med.get_denumire() << " || Producator: " << med.get_producator()
                 << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

        }
    }
    if (optiune == 3)
    {
        for (const auto& med: srv.sortdsubstpret(ordine))
        {
            cout << "Denumire: " << med.get_denumire() << " || Producator: " << med.get_producator()
                 << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;

        }
    }
}

void Console::ui_all_of() {
    string denumire;
    cout << "Introduceti denumirea:";
    getline(cin>>ws, denumire);
    if (srv.all_of_denumire_incepe_cu_a(denumire) == 0)
        cout << "Nu toate medicamentele au denumirea data!" << endl;
    if (srv.all_of_denumire_incepe_cu_a(denumire) == 1)
        cout << "Toate medicamentele au denumirea data!" <<endl;
}

//UI LISTA

void Console::print_all_from_list() {
    const vector<Medicament>& allmeds = srv.get_all_from_list_service();
    if(allmeds.size() == 0)
        cout << "Nu exista medicamente." << endl;
    else
        for (const auto& med : allmeds) {
            cout << "Denumire: " << med.get_denumire() << " || Producator: " << med.get_producator()
                 << " || Substanta activa: " << med.get_substanta_activa() << " || Pret: " << med.get_pret() << endl;
        }
}

void Console::ui_add_list() {
    string denumire;
    cout << "Denumirea medicamentului:";
    getline(cin>>ws, denumire);

    try {
        srv.add_list_service(denumire);
        cout << "Medicamentul a fost adaugat cu succes pe reteta." << endl;
    }
    catch (Repo_Exception& re) {
        cout << re.get_error_message();
    }
    catch (Validation_Exception& ve) {
        cout << "Medicamentul nu este valid!" << endl;
        cout << ve.get_error_messages();
    }
}

void Console::ui_add_random_list() {
    int howMany;
    cout << "Cate medicamente sa se adauge in reteta?";
    cin >> howMany;

    try {
        int howManyadded = srv.add_random_service(howMany);
        cout << "S-au adaugat " << howManyadded <<" medicamente in reteta." << endl;

    }
    catch (Repo_Exception& re) {
        cout << re.get_error_message();
    }
}

void Console::ui_empty_list() {
    srv.empty_list_service();
    cout << "S-a golit reteta curenta." << endl;
}

void Console::ui_export_reteta() {
    cout << "Export\n";
    string fisier;
    cout << "Fisier: ";
    cin >> fisier;
    srv.export_reteta(fisier);
}

void Console::ui_reteta() {
    int cmd;
    int runList = 1;
    while(runList) {
        print_meniu_list();
        cout << "Comanda dumneavoastra este:";
        cin >> cmd;
        switch (cmd){
            case 1:
                ui_add_list();
                break;
            case 2:
                ui_add_random_list();
                break;
            case 3:
                ui_empty_list();
                break;
            case 4:
                print_all_from_list();
                break;
            case 5:
                ui_export_reteta();
                break;
            case 6:
                runList = 0;
                break;
            default:
                break;
        }
    }
}


void Console::ui_undo() {
    try{
        srv.undo();
        cout << "Undo realizat cu succes!\n";
    }
    catch (const UndoException& ue) {
        cout << ue.get_msg();
    }
}

void Console:: run(){
    int running = 1;
    int cmd;
    while(running){
        print_meniu();
        cout << "Comanda dumneavoatra este:";
        cin >> cmd;
        switch (cmd) {
            case 1:
                ui_add();
                break;
            case 2:
                ui_modificare();
                break;
            case 3:
                ui_stergere();
                break;
            case 4:
                print_all_medicamente();
                break;
            case 5:
                ui_find();
                break;
            case 6:
                ui_filtrare();
                break;
            case 7:
                ui_sort();
                break;
            case 8:
                ui_all_of();
                break;
            case 9:
                ui_reteta();
                break;
            case 10:
                ui_undo();
                break;
            case 0:
                running = 0;
                break;
            default:
                break;

        }
    }
}

