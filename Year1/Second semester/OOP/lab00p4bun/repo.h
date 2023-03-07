//
// Created by Ilinca on 28-Mar-22.
//

#ifndef LAB00P4BUN_REPO_H
#define LAB00P4BUN_REPO_H

#include "lista.h"

typedef struct {
    lista* elemente;
    lista* lista_undo;
}repository;
/*
Functie care creeaza o lista goala de elemente
input : -
output lista
*/
repository* creeaza_repository();
/*
Functie care distruge lista data si elementele sale
input : lista de distrus
output : -
*/
void distruge_repository(repository* repo);
/*
 * Adauga un element in lista
 * in:repo-lista, el-elementul de adaugat
 *
 */
void add_repository(repository* repo, element* el);
/*
Functie care sterge un element din lista
input : pointer la lista
		poz - int
outp[ut : elementul sters
*/
ElemType stergere_repository(repository* repo, int poz);
/*
Functie care modifica un element din lista
input : pointer la lista
		poz - int
outp[ut : elementul modificat
*/
void modificare_repository(repository* repo, int poz, int cantitate);

/*
Functie care executa undo-ul
input : pointer la lista
outp[ut : lista de undo
*/
int executare_undo(repository* repo);

/*
Functie care creeaza o copie la lista
input : pointer la lista
outp[ut : copia listei
*/
lista* copy_list(repository* repo);

#endif //LAB00P4BUN_REPO_H
