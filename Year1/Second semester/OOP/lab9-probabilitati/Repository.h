//
// Created by Ilinca on 30-Mar-22.
//

#ifndef LAB4_6OOP_REPOSITORY_H
#define LAB4_6OOP_REPOSITORY_H

#pragma once
#include "Medicament.h"
#include <vector> //include "vectordinamictemplate.h"
using std::vector;

/*
 * Clasa de exceptii specifice Repository
 */

class Repo_Exception{

private:
    string error_msg;
public:
    Repo_Exception(string error_msg) :error_msg{ error_msg } {};
    string get_error_message(){
        return this->error_msg;
    }
};

class Medicament_Repository{

private:
    vector<Medicament> all_medicamente;
public:
    Medicament_Repository() = default;
    //constructor de copiere
    //punem delete fiindca nu vrem sa se faca nicio copie la Repository
    //(in aplicatie avem 1 singur Repo)
    Medicament_Repository(const Medicament_Repository& ot) = delete;

    virtual /*
	Adauga un medicament in lista
	@param m: medicamentul care se adauga (Medicament)
	@return -
	post: medicamentul va fi adaugat in lista

	@throws: RepoException daca un medicament cu aceeasi denumire si acelasi producator
			 exista deja
	*/
    void store(const Medicament& m);

    virtual /*
	Returneaza o lista cu toate medicamentele
	@return: lista cu medicamentele (vector of Medicament objects)
	*/
    const vector<Medicament>& get_all_medicamente();

    /*
	Cauta un medicament cu denumirea si producatorul dat

	@param denumire: denumirea dupa care se cauta
	@param producator: producatorul dupa care se cauta
	@returns: entitatea Medicament cu denumirea si producatorul dat (daca aceasta exista)
	@throws: RepoException daca nu exista medicamentul cu denumirea si producatorul dat*/
    const Medicament& find(string denumire, string producator);

    virtual
    const Medicament& find_denumire(string denumire);

    virtual /*
	Verifica daca un medicament dat exista in lista

	@param m: medicamentul care se cauta in lista
	@return: true daca medicamentul exista, false altfel
	*/
    bool exists(const Medicament& m);

    virtual /*
     * Modifica pretul unui medicament dat
     * @param med: medicamentul ce se doreste sa fie modificat
     * @throws: RepoException daca medicamentul nu se afla
			    in lista
     */
    void modificare_pret_repo(const Medicament& med);

    virtual /*
     * Sterge din lista un medicament dat
     * @param med: medicamentul ce se doreste sa fie sters
     * @throws: RepoException daca medicamentul nu se afla
			    in lista
     */

    void stergere_repo(const Medicament& med);
};

class RepoFile: public Medicament_Repository {
private:
    string filename;
    void load();
    void write();
public:
    RepoFile() = delete;
    RepoFile(string fname) :Medicament_Repository(), filename{ fname } { load(); };
    RepoFile(const RepoFile& r) = delete;
    ~RepoFile() = default;

    void store(const Medicament& m) override;
    void stergere_repo(const Medicament& m) override;
    void modificare_pret_repo(const Medicament& m) override;

};

class RepositoryLaborator : public Medicament_Repository
{
private:
    const double probability = 1;
public:
    RepositoryLaborator() noexcept : Medicament_Repository() {};

    void store(const Medicament& med) override;
    void stergere_repo(const Medicament& med) override;
    const Medicament& find_denumire(string denumire) override;
    void modificare_pret_repo(const Medicament& med) override;
    const vector<Medicament>& get_all_medicamente() override;
    bool exists(const Medicament& med) override;
};

void teste_repo();

#endif //LAB4_6OOP_REPOSITORY_H
