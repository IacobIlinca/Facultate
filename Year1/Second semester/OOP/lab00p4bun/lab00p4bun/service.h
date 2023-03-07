#pragma once
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
//#include <crtdbg.h>
#include "lista.h"
//#include "repo.h"
#include "../repo.h"

typedef struct{
    repository* repo;
} service;

service* creeaza_service(repository* repo);

void destroy_service(service* srv);

/*
Functie care adauga un element in lista 
input : srv-service
		nume - char
		producator - char
		cantitate - int
output : 1 daca s a adaugat cu suuces 
		0 in cazu in care nu s a adaugat

*/
int add_element(service* srv, char* nume, char* producator, int cantitate);

/*
Funcite care steerge un element din lista
input : srv-service
		nume - char
output: 1 daca s a sters 0 in caz contrat
*/
int sterge_elemet(service* srv, char* nume);

/*
Functie care mldicia un element din lista
input : srv-service
		nume - cahr
		priodyucator -char
		cantitate - int
output: 1 - daca s a modificat cu succes
		0 in caz contrat
*/
int modifica_element(service* srv, char* nume, int cantitate);

/*
Functie care cauta un element in lista
input : lista -lista
		nume -char
output : 1 daca e in lista
		0 in caz contrat
*/
int find_element(lista* v, char* nume);


typedef int (*Compararefct)(element* el1, element* el2, int optiune);
/*
Functie care compara 2 elemente dupa cantitate
input : el1, el2-elemente
		optiune-cantitatea dupa care se compara
output : e1 sau e2 in functie de care satisface relatia probata
*/
int cmpfc_cantitate(element* el1, element* el2, int optiune);
/*
Functie care compara 2 elemente dupa nume
input : el1, el2-elemente
		optiune-numele dupa care se compara
output : e1 sau e2 in functie de care satisface relatia probata
*/
int cmpfc_nume(element* el1, element* el2, int optiune);
/*
Functie care sorteza lista crescator dupa cantitate
inp[ut srv-service
output o lista de tip lista care e sortata
*/
lista* sortare(service* srv, Compararefct fn, int optiune);

/*
Functie care afiseaza elementele din lista care au cantitatea mai mica ca un nr dat
input :srv-service
		canord - int
output : o lista de tip lista care contine elementele care satisfac conditia
*/

lista* filtru_cant(service* srv, int canord);
/*
Functie care afiseaza elementele din lista care au numele dat
input : srv-service
		canord - int
output : o lista de tip lista care contine elementele care satisfac conditia
*/
lista* filtru_nume(service* srv, char* chr);
/*
Functie care apeleaza undo
input : srv-service
output : lista de undo
*/
int apelare_undo(service* srv);

/*
Functie care afiseaza elementele din lista care au numele dat si cantitatea multiplu de 3
input : srv-service
		chr-char
output : o lista de tip lista care contine elementele care satisfac conditia
*/
lista* multiplu_trei(service* srv, char* chr);
