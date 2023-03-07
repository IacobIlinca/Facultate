#pragma once
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
//#include <crtdbg.h>

typedef struct {

	char* nume;
	char* producator;
	int cantitate;

}element;

/*
*Functie care creeaza un element 
* input : nume - char 
*		producator -char
*		cantitate - int
*	output : un element cu proprietatiile date sa zice,m
*/
element* create_element(char* nume,char* producator,int cantitate);

/*
*Funcite care distruge un element
* input : un element 
* output - 
*/
void destroy_element(element* m);

/*
*Functie care valideaza un elelemnt 
* input : m -element de validat
* output : 1 daca e valid 
*			0 daca nu e valid
*/
int valid_element(element* m);

element* copy_element(element* el);

