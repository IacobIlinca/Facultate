#pragma once
#include "teste.h"
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>


//teste element
void test_crez_destroy_element()
{
	char *a="abc", *b="abc";
	int c=69;
	element* el;
	el = create_element(a, b, c);
	assert(el->cantitate == c);
	assert(strcmp(el->nume, a) == 0);
	assert(strcmp(el->producator, b) == 0);
	destroy_element(el);
}
void test_valid_element()
{
	char a[30] = "abc", b[30] = "abc";
	int c = 69;
	element* el,*el2;
    el = create_element(a, b, c);
    assert(valid_element(el) == 1);
    el2 = create_element("", "", -34);
    assert(valid_element(el2) == 0);
    destroy_element(el2);
    el2 = create_element("a", "", -34);
    assert(valid_element(el2) == 0);
    destroy_element(el2);
    el2 = create_element("a", "a", -34);
    assert(valid_element(el2) == 0);
    destroy_element(el2);
    destroy_element(el);

}

void test_copy_element() {
    char a[30] = "abc", b[30] = "abc";
    int c = 69;
    element *el, *el2;
    el = create_element(a, b, c);
    el2 = copy_element(el);
    assert(strcmp(el->nume, el2->nume) == 0);
    assert(strcmp(el->producator, el2->producator) == 0);
    assert(el->cantitate == el2->cantitate);
    destroy_element(el2);
    destroy_element(el);
}
//teste lista

void test_crez_dest_lista(){
	lista* l;
	l = create_lista();
	assert(size(l) == 0);
	assert(l->capacity == 2);
	assert(l->length == 0);
	destroy_lista(l);
	//assert(l->length == 0);
}


void test_agss()
{
    lista *l;
    l = create_lista();
    assert(size(l) == 0);
    element *el1, *el2;
    el1 = create_element("a", "a", 23);
    add_elem(l, el1);
    assert(size(l) == 1);
    el2 = create_element("b", "b", 12);
    element *el3 = set_element(l, 0, el2);
    destroy_element(el1);
    element *el = l->elems[0];
    assert(el->cantitate == 12);
    element *el4 = create_element("aaaa", "bbb", 25);
    add_elem(l, el4);
    element *el5 = create_element("aaaaaa", "bbb", 25);
    add_elem(l, el5);
    assert(l->capacity == 4);
    destroy_lista(l);

}

void test_stergere_lista() {
    lista *l;
    l = create_lista();
    assert(size(l) == 0);
    element *el1, *el2;
    el1 = create_element("a", "a", 23);
    add_elem(l, el1);
    assert(size(l) == 1);
    el2 = create_element("b", "b", 12);
    add_elem(l, el2);
    stergere(l, 0);
    assert(size(l) == 1);
    element *remaining = l->elems[0];
    assert(remaining->cantitate == 12);
    destroy_element(el1);
    destroy_lista(l);
}


//teste repo
void test_create_destroy_repo() {
    repository *repo = creeaza_repository();
    assert(size(repo->elemente) == 0);
    assert(size(repo->lista_undo) == 0);
    distruge_repository(repo);
}


void test_copy_list() {
    repository *repo = creeaza_repository();
    element *el1 = create_element("a", "a", 23);
    add_repository(repo, el1);
    lista *list = copy_list(repo);
    element *copyEl = list->elems[0];
    assert(el1->cantitate == copyEl->cantitate);
    destroy_lista(list);
    distruge_repository(repo);
}

void test_stergere_repo() {
    repository *repo = creeaza_repository();
    element *el1 = create_element("a", "a", 23);
    add_repository(repo, el1);
    assert(size(repo->elemente) == 1);
    stergere_repository(repo, 0);
    assert(size(repo->elemente) == 0);
    distruge_repository(repo);
    destroy_element(el1);
}

void test_modifica_repo() {
    repository *repo = creeaza_repository();
    element *el1 = create_element("a", "a", 23);
    add_repository(repo, el1);
    modificare_repository(repo, 0, 50);
    el1 = repo->elemente->elems[0];
    assert(el1->cantitate == 50);
    distruge_repository(repo);
}

void test_executare_undo() {
    repository *repo = creeaza_repository();
    assert(executare_undo(repo) == 0);
    element *el1 = create_element("a", "a", 23);
    add_repository(repo, el1);
    assert(size(repo->elemente) == 1);
    element *el2 = create_element("aaa", "a", 23);
    add_repository(repo, el2);
    assert(size(repo->elemente) == 2);
    executare_undo(repo);
    assert(size(repo->elemente) == 1);
    distruge_repository(repo);
}



//teste service
void test_add_elem()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    char *nume = "a";
    char *producator = "a";
    int a = add_element(service, nume, producator, 69);
    assert(a == 1);
    char *nume1 = "";
    char *producator1 = "";
    a = add_element(service, nume1, producator1, -90);
    assert(a == 0);
    destroy_service(service);
}
void test_sterge_elem()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    a = add_element(service, "b", "b", 89);
    assert(a == 1);
    a = sterge_elemet(service, "a");
    assert(a == 1);
    assert(size(repo->elemente) == 1);
    element *el = get(repo->elemente, 0);
    assert(el->cantitate == 89);
    a = sterge_elemet(service, "w");
    assert(a == 0);
    destroy_service(service);
}
void test_modif_elem()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    assert(a == 1);
    a = modifica_element(service, "a", 23);
    element *el = get(repo->elemente, 0);
    assert(el->cantitate == 23);
    assert(a == 1);
    assert(size(repo->elemente) == 1);
    a = modifica_element(service, "c", 67);
    assert(a == 0);
    destroy_service(service);
}
void test_find_elem()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    assert(a == 1);
    a = find_element(repo->elemente, "a");
    assert(a == 0);
    destroy_service(service);

}
void test_sort()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    assert(a == 1);
    a = add_element(service, "b", "b", 45);
    a = add_element(service, "c", "c", 90);
    lista *sorted = sortare(service, (Compararefct) cmpfc_cantitate, 1);
    assert(size(sorted) == 3);
    element *el = sorted->elems[0];
    assert(el->cantitate == 45);
    el = sorted->elems[1];
    assert(el->cantitate == 69);
    el = sorted->elems[2];
    assert(el->cantitate == 90);
    destroy_lista(sorted);
    sorted = sortare(service, (Compararefct) cmpfc_cantitate, 0);
    el = sorted->elems[0];
    assert(el->cantitate == 90);
    el = sorted->elems[1];
    assert(el->cantitate == 69);
    el = sorted->elems[2];
    assert(el->cantitate == 45);
    destroy_lista(sorted);
    sorted = sortare(service, (Compararefct) cmpfc_nume, 1);
    el = sorted->elems[0];
    assert(strcmp(el->nume, "a") == 0);
    el = sorted->elems[1];
    assert(strcmp(el->nume, "b") == 0);
    el = sorted->elems[2];
    assert(strcmp(el->nume, "c") == 0);
    destroy_lista(sorted);
    sorted = sortare(service, (Compararefct) cmpfc_nume, 0);
    el = sorted->elems[0];
    assert(strcmp(el->nume, "c") == 0);
    el = sorted->elems[1];
    assert(strcmp(el->nume, "b") == 0);
    el = sorted->elems[2];
    assert(strcmp(el->nume, "a") == 0);
    destroy_lista(sorted);

    destroy_service(service);

}

void test_filtru()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    assert(a == 1);
    a = add_element(service, "b", "b", 45);
    a = add_element(service, "ac", "c", 90);
    lista *fil = filtru_cant(service, 70);
    assert(size(fil) == 2);

    lista *filtr = filtru_nume(service, "a");
    assert(size(filtr) == 2);

    destroy_service(service);
    destroy_lista(fil);
    destroy_lista(filtr);

}


void test_undo() {
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    assert(a == 1);
    apelare_undo(service);
    assert(size(repo->elemente) == 0);
    destroy_service(service);
}

void test_multiplu_trei()
{
    repository *repo = creeaza_repository();
    service *service = creeaza_service(repo);
    int a = add_element(service, "a", "a", 69);
    assert(a == 1);
    a = add_element(service, "b", "b", 45);
    a = add_element(service, "ac", "c", 90);
    lista *lista_mul = multiplu_trei(service, "ac");
    assert(size(lista_mul) == 1);

//    lista *filtr = filtru_nume(service, "a");
//    assert(size(filtr) == 2);

    destroy_service(service);
    destroy_lista(lista_mul);

}

void run_all_tests()
{	
	printf("Start teste...\n");
	test_crez_destroy_element();
	test_valid_element();

    test_agss();
    test_copy_element();

    test_crez_dest_lista();
    test_stergere_lista();


    test_create_destroy_repo();
    test_copy_list();
    test_stergere_repo();
    test_modifica_repo();
    test_executare_undo();


    test_add_elem();
    test_sterge_elem();
    test_modif_elem();
    test_find_elem();
    test_sort();
    test_filtru();
    test_undo();
    test_multiplu_trei();

    printf("Teste incheiate cu sucees , miramas...\n");
}