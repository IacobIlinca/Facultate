//
// Created by Ilinca on 30-Mar-22.
//

#ifndef LAB4_6OOP_SERVICE_H
#define LAB4_6OOP_SERVICE_H

#pragma once
#include "Repository.h"
#include "Validators.h"
#include "Reteta.h"
#include <functional>
using std::unique_ptr;
#include "Undo.h"
using std::function;
using std::unique_ptr;

class Medicamente_Service {
private:
    Medicament_Repository& repo;
    //Medicament_Validator& val;

    List currentlist;

    vector<unique_ptr<ActiuneUndo>>UndoActions;

    vector<Medicament> general_sort(bool(*mai_mic_f)(const Medicament&, const Medicament&));

public:
    Medicamente_Service(Medicament_Repository& med_repo) :repo{ med_repo } {};

    //constructor de copiere
    //punem delete fiindca nu vrem sa se faca nicio copie la Service
    //(in aplicatie avem 1 singur Service)
    Medicamente_Service(const Medicamente_Service& ot) = delete;

    /*
    Adauga un medicament cu denumirea denumire, producatorul producator, substanta activa substanta activa si pretul pret
    *@param denumire: denumirea medicamentului care se adauga (string)
    *@param producator: producatorul medicamentului care se adauga (string)
    *@param substanta_activa: substanta activa medicamentului care se adauga (string)
    *@param pret: pretul medicamentului care se adauga (double)
    *
    * @throws:
    *	RepoException daca mai exista medicament cu denumirea si producatorul dat
    *	ValidationException daca medicamentul nu este valid
    */

    void add_medicament(string denumire, string producator, string substanta_activa, double pret);

    /*
    Returneaza un vector cu toate medicamentele disponibile

    @return: lista cu toate medicamentele disponibile (vector cu obiecte de tip Medicament)
    */

    const vector<Medicament>& get_all_medicamente() {
        return this->repo.get_all_medicamente();
    }


    /*
    Modifica pretul unui medicament cu denumirea denumire, producatorul producator, substanta activa substanta activa si noul pret pret_nou
    *@param denumire: denumirea medicamentului ce se modifica (string)
    *@param producator: producatorul medicamentului ce se modifica (string)
    *@param substanta_activa: substanta activa medicamentului ce se modifica (string)
    *@param pret_nou: pretul nou al medicamentului (double)
    *
    * @throws:
    *	RepoException daca nu exista medicament cu denumirea si producatorul dat
    *	ValidationException daca medicamentul nu este valid
    */
    void modifica_pret_service(string denumire, string producator, string substanta_activa, double pret_nou);
    /*
    Sterge un medicament cu denumirea denumire, producatorul producator, substanta activa substanta activa si pretul pret
    *@param denumire: denumirea medicamentului ce se sterge (string)
    *@param producator: producatorul medicamentului ce se sterge (string)
    *@param substanta_activa: substanta activa medicamentului ce se sterge (string)
    *@param pret: pretul medicamentului ce se sterge (double)
    *
    * @throws:
    *	RepoException daca nu exista medicament cu denumirea si producatorul dat
    *	ValidationException daca medicamentul nu este valid
    */
    void stergere_service(string denumire, string producator, string substanta_activa, double pret);

    void stergere_dupa_denumire(string denumire);

    Medicament find_service(string denumire, string producator);
    Medicament find_dupa_denumire(string denumire);
    /*
     * Filtreaza medicamentele din lista care au substanta activa substanta_activa
     *@param substanta_activa: substanta activa dupa care se face filtrarea (string)
     *@return: lista noua cu medicamentele filtrate
     */
    vector<Medicament> filtrare_substanta_activa(string substanta_activa);
    /*
     * Filtreaza medicamentele din lista care au pretul pret
     *@param substanta_activa: pretul dupa care se face filtrarea (double)
     *@return: lista noua cu medicamentele filtrate
     */
    vector<Medicament> filtrare_pret(double pret);

    /*
    functie de sortare a produselor dupa denumire
    param reverse: 0-ordine crescatoare,1-descrescatoare
     */
    vector<Medicament> sort_by_denumire();
    /*
    functie de sortare a produselor dupa producator
    param reverse: 0-ordine crescatoare,1-descrescatoare*/
    vector<Medicament> sort_by_producator();

    /*
     Functie de sortare generala
     functie - functie de comparare, verifica daca are loc relatia intre cele 2 produse
     returneaza o lista sortata dupa criteriu dat ca paramatru
    */
    vector<Medicament> sortservice(int reverse, bool (*functie)(Medicament&, Medicament&));

    vector<Medicament> sortdenumire(int reverse);
    vector<Medicament> sortproducator(int reverse);
    vector<Medicament> sortdsubstpret(int reverse);
    int all_of_denumire_incepe_cu_a(string denumire);

    List& getcos() {
        return this->currentlist;
    }

    //FUNCTIONALITATI RETETA
    /*
     * adauga un medicament cu denumirea data pe reteta
     * @param denumire:denumirea produsului ce se doreste a fi adaugat pe reteta
     * post: medicamentul dat este adaugat in lista
     * @throws: RepoException daca nu exista medicament cu denumirea data
     */
    void add_list_service(string denumire);

    /*
     * Adauga un nr dat de medicamente random in reteta
     * @param:howMany: cate medicamente se adauga (int)
     * @return: nr de produse adaugate pe reteta
     * post: list' = list + {med random}
     */
    int add_random_service(int howMany);

    /*
     * elimina toate produsele din lista
     * post:lista nu contine niciun produs
     */
    void empty_list_service();

    /*
     * returneaza un vector cu toate medicamentele de pe reteta
     */
    const vector<Medicament>& get_all_from_list_service();

    void export_reteta(string& fisier);

    void undo();
    size_t get_dim_undo() noexcept;
};

void teste_service();

#endif //LAB4_6OOP_SERVICE_H
