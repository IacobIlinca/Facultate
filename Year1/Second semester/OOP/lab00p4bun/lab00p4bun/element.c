#pragma once 
#include "element.h"
#include <stdlib.h>
#include <string.h>

element* create_element(char* nume, char* producator, int cantitate)
{
    element* el = malloc(sizeof (element));
	
	int nrc = (int)strlen(nume) + 1;
	el->nume = malloc(nrc * sizeof(char));
	strcpy(el->nume, nume);
	//de retinut toata asta te rog danielll
	
	nrc = (int)strlen(producator) + 1;
	el->producator = malloc(nrc * sizeof(char));
	strcpy(el->producator, producator);

	el->cantitate = cantitate;
	return el;
}

element* copy_element(element* el){
    return create_element(el->nume, el->producator, el->cantitate);
}


void destroy_element(element* el)
{
	free(el->nume);
    el->nume =  NULL;
	free(el->producator);
    el->producator = NULL;
	free(el);
    el = NULL;
}

int valid_element(element* el)
{
	if (strlen(el->nume) == 0) return 0;
	if (strlen(el->producator) == 0) return 0;
	if (el->cantitate < 0) return 0;
	return 1;
}