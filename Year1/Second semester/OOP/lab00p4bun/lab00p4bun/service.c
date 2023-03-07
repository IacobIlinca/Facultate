#pragma once 

#include <string.h>
#include "service.h"

service* creeaza_service(repository* repo)
{
    service* srv = malloc(sizeof(service));
    srv->repo = repo;
    return srv;
}

void destroy_service(service* srv)
{
    distruge_repository(srv->repo);
    free(srv);
    srv = NULL;
}

int add_element(service* srv, char* nume, char* producator, int cantitate)
{
	element* el = create_element(nume, producator, cantitate);
	int vali = valid_element(el);
	if (vali == 0)
	{
		destroy_element(el);
		return 0;
	}
    add_repository(srv->repo, el);
	return 1;
}

int sterge_elemet(service* srv, char* nume)
{
	int poz = find_element(srv->repo->elemente, nume);
	if (poz != -1)
	{
		ElemType el = stergere_repository(srv->repo, poz);
		destroy_element(el);
		return 1;
	}
	return 0;
}

int modifica_element(service* srv, char* nume, int cantitate)
{
	int poz = find_element(srv->repo->elemente, nume);
	if (poz != -1)
	{
        modificare_repository(srv->repo, poz, cantitate);
		return 1;
	}
	return 0;
}

int find_element(lista* v, char* nume)
{
	int i,index = -1;
	for (i = 0; i < v->length; i++)
	{
		element* el = get(v, i);
		if (strcmp(el->nume, nume) == 0)
		{
			index = i;
			break;
		}
	}
	
	return index;
}


lista* filtru_cant(service* srv, int canord)
{
	lista* m = create_lista();
    lista* v = srv->repo->elemente;
	int i;
	for (i = 0; i < v->length; i++)
	{
		element* el;
		el = get(v, i);
		if (el->cantitate < canord)
			add_elem(m, create_element(el->nume,el->producator,el->cantitate));
	}
	return m;
}

lista* filtru_nume(service* srv, char* chr)
{
    lista* m = create_lista();
    lista* v = srv->repo->elemente;
    int i;
    for(i=0;i<v->length;i++)
    {
        element* el;
        el = get(v, i);
        if(el->nume[0] == chr[0])
            add_elem(m, create_element(el->nume, el->producator, el->cantitate));
    }
    return m;
}

//lista sortare(lista* v)
//{
//	lista m = create_lista();
//	int i ;
//	for (i = 0; i < v->length; i++)
//	{
//		element el;
//		el = get(v, i);
//		add_elem(&m, create_element(el.nume, el.producator, el.cantitate));
//	}
//	int j;
//	
//	for (i = 0; i < m.length-1; i++)
//	{
//		for (j = i+1; j < m.length; j++)
//		{
//			if (m.elems[i].cantitate > m.elems[j].cantitate)
//			{
//				element eli,elj,ela;
//				eli = get(&m, i);
//				elj = get(&m, j);
//				ela=set_element(&m, i, elj);
//				ela=set_element(&m, j, eli);
//				
//				
//			}
//		}
//	}
//	return m;
//}

int cmpfc_cantitate(element* el1, element* el2,int optiune)
{
    if(optiune) {
        return el1->cantitate > el2->cantitate;
    } else {
        return el1->cantitate < el2->cantitate;    }
}

int cmpfc_nume(element* el1, element* el2, int optiune)
{
    if(optiune){
        return strcmp(el1->nume, el2->nume)>0;
    } else {
        return strcmp(el1->nume, el2->nume)<0;
    }
}

lista* sortare(service* srv,Compararefct cmpfc, int optiune)
{
	lista* m = create_lista();
    lista* v = srv->repo->elemente;
	
	int i;
	for (i = 0; i < v->length; i++)
	{
		element* el;
		el = get(v, i);
		add_elem(m, create_element(el->nume, el->producator, el->cantitate));
	}
	int j;

	for (i = 0; i < m->length - 1; i++)
	{
		for (j = i + 1; j < m->length; j++)
		{
			if (cmpfc(m->elems[i],m->elems[j], optiune)==1)
			{
				ElemType eli, elj, ela;
				eli = get(m, i);
				elj = get(m, j);
				ela = set_element(m, i, elj);
				ela = set_element(m, j, eli);


			}
		}
	}
	return m;
}

int apelare_undo(service* srv){
    return executare_undo(srv->repo);
}

lista* multiplu_trei(service* srv, char* chr)
{
    lista* m = create_lista();
    lista* v = srv->repo->elemente;
    int i;
    for(i=0;i<v->length;i++)
    {
        element* el;
        el = get(v, i);
        if((strcmp(el->nume, chr) == 0) && (el->cantitate%3 ==0))
            add_elem(m, create_element(el->nume, el->producator, el->cantitate));
    }
    return m;
}
