#pragma once 
#include <string.h>
#include <stdlib.h>
#include "lista.h"

lista* create_lista()
{
	lista* v = malloc(sizeof(lista));
	v->capacity = 2;
	v->length = 0;
	v->elems = malloc(v->capacity * sizeof(ElemType));
	return v;
}

void destroy_lista(lista* v)
{
	for (int i = 0; i < v->length; i++)
	{
		element* el = get(v, i);
		destroy_element(el);
	}
	v->length = 0;
	free(v->elems);
    v->elems = NULL;
    free(v);
    v = NULL;
}


ElemType get(lista* v, int poz)
{
	return v->elems[poz];
}




int size(lista* v)
{
	return v->length;
}


void add_elem(lista* v, ElemType el)
{
	if (v->length == v->capacity)
	{
		int newcapacity = v->capacity * 2;
		ElemType* aux = malloc(sizeof(ElemType) * newcapacity);
		for (int i = 0; i < v->length; i++)
			aux[i] = v->elems[i];

		free(v->elems);
		v->elems = aux;
		v->capacity = newcapacity;
	}
	v->elems[v->length] = el;
	v->length++;
}


ElemType stergere(lista* v, int poz)
{
	ElemType el = v->elems[poz];
    v->length--;
    v->elems[poz] = v->elems[v->length];
    if(v->length <= v->capacity/4) v->capacity = v->capacity/4;
    return el;
}

ElemType set_element(lista* v, int poz, ElemType el) {
	ElemType replacedElement = v->elems[poz];
	v->elems[poz] = el;
	return replacedElement;
}
