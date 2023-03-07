//
// Created by Ilinca on 28-Mar-22.
//

#include "repo.h"

repository* creeaza_repository(){
    repository* repo = malloc(sizeof(repository));
    repo->elemente = create_lista();
    repo->lista_undo = create_lista();
    return repo;
}

void distruge_repository(repository* repo)
{
    destroy_lista(repo->elemente);
    for(int i=0;i<repo->lista_undo->length;i++)
        destroy_lista(repo->lista_undo->elems[i]);
    free(repo->lista_undo->elems);
    repo->lista_undo->elems = NULL;
    free(repo->lista_undo);
    repo->lista_undo = NULL;
    free(repo);
    repo = NULL;

}

lista* copy_list(repository* repo)
{
    lista* list = create_lista();
    for(int i=0;i<repo->elemente->length;i++)
    {
        element* el = copy_element(repo->elemente->elems[i]);
        add_elem(list,el);
    }
    return list;
}

void add_repository(repository* repo, element* el)
{
    add_elem(repo->lista_undo, copy_list(repo));
    add_elem(repo->elemente, el);
}

ElemType stergere_repository(repository* repo, int poz)
{
    add_elem(repo->lista_undo, copy_list(repo));
    return stergere(repo->elemente, poz);
}

void modificare_repository(repository* repo, int poz, int cantitate)
{
    add_elem(repo->lista_undo, copy_list(repo));
    element* el = get(repo->elemente, poz);
    el->cantitate = cantitate;
}

int executare_undo(repository* repo)
{
    if(repo->lista_undo->length == 0)
        return 0;
    destroy_lista(repo->elemente);
    repo->elemente = repo->lista_undo->elems[--repo->lista_undo->length];
    return 1;
}