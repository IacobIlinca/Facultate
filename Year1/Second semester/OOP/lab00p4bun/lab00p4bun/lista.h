#pragma once
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
//#include <crtdbg.h>
#include "element.h"

typedef void* ElemType;

typedef struct {

	ElemType* elems;
	int length;
	int capacity;

}lista;

/*
Functie care creeaza o lista goala de elemente
input : - 
output lista
*/
lista* create_lista();

/*
Functie care distruge lista data si elementele sale 
input : lista de distrus
output : -
*/
void destroy_lista(lista *v);


/*
Functie care returneza un element aflat pe o anumita pozitite in lista
input : o lista 
		poz - char
output : elementul de pe acea pozitie
*/
ElemType get(lista* v, int poz);


/*
Functie care returneaza marimea listei
input : lista 
output : int - dimensiunea
*/
int size(lista* v);

/*
Functie car eadauga un element in lista 
input : v - pointer la lista
		el de tip element
*/
void add_elem(lista* v, ElemType el);

/*
Functie care sterge un element din lista 
input : pointer la lista
		poz - int 
outp[ut : elementul sters
*/
ElemType stergere(lista* v, int poz);

/*
Functie care pune un element pe o anumita pozitie in lista
input : pointer la lista
		poz - int 
		el - elemtn
output : elementul in locul caruia am pus un alt element
*/
ElemType set_element(lista* v, int poz, ElemType el);
