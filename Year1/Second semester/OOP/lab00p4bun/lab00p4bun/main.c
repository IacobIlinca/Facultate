#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "service.h"
#include "teste.h"
#define _CRTDBG_MAP_ALLOC 
//#include <crtdbg.h>

void run_ui();
void ui_add(service *srv);
void ui_sterge(service *srv);
void ui_modifica(service *srv);
void ui_filtru(service *srv);
void ui_sort(service* srv);
void ui_print(lista *v);
void ui_sort_cmp(service* srv);
void ui_undo(service* srv);
void ui_multiplu_trei(service* srv);

int main()
{

	run_all_tests();
	run_ui();
	//_CrtDumpMemoryLeaks();
	return 0;
}

void print_meniu()
{
    printf("Program minunat realizat cu multa munca si truda...\n");
    printf("Developement team: Dani \n");
    printf("Meniu programel cofetarie :\n");
    printf("1. adauga materie \n");
    printf("2. sterge materie \n");
    printf("3. modifica materie \n");
    printf("4. afiseaza materii dupa criteriu \n");
    printf("5. ordoneaza dupa nume sau cantitate \n");
    printf("6. afiseaza elementele\n");
    printf("7. undo\n");
    printf("8. Filtrare noua-dupa nume si cantitate multipliu de 3\n");
    printf("0. exit \n");
}


void run_ui()
{
	int cmd=69;
	repository* repo = creeaza_repository();
    service* srv = creeaza_service(repo);
	//lista v = create_lista();

	while (cmd!=0)
	{
        print_meniu();
		printf(">> ");
		scanf("%d", &cmd);

		if (cmd == 1)
			ui_add(srv);

		if (cmd == 2)
			ui_sterge(srv);

		if (cmd == 3)
			ui_modifica(srv);

		if (cmd == 4)
			ui_filtru(srv);

		if (cmd == 5)
			ui_sort(srv);

		if (cmd == 6)
			ui_print(srv->repo->elemente);

        if (cmd == 7)
            ui_undo(srv);

        if (cmd == 8)
            ui_multiplu_trei(srv);

		if (cmd == 0)
		{	
			destroy_service(srv);
			printf("Gata pe azi...\n");
			break;
		}

		
	}
}

void ui_add(service *srv)
{
	printf("Adaugare materie...\n");
	char nume[30], producator[30];
	int cantitate;
	printf("Introdu numele :\n");
	scanf("%s", nume);

	printf("Introdu producator :\n");
	scanf("%s", producator);

	printf("Cantiate : \n");
	scanf("%d", &cantitate);

	int a = add_element(srv, nume, producator, cantitate);
	if (a == 0)
	{
		printf("Nu s a adaugat");
	}
	else printf("Materie adaugata cu suuces ");

}

void ui_print(lista* v)
{
	printf("%d <--\n", size(v));
	for (int i = 0; i < v->length; i++)
	{
        element* el = v->elems[i];
		printf("%s  :  %s  :  %d \n",el->nume, el->producator, el->cantitate);
	}

}

void ui_sterge(service* srv)
{
	printf("Stergere materie...\n");
	char nume[30];
	printf("Introdu nume : \n");
	scanf("%s", nume);
	int a = sterge_elemet(srv, nume);
	if (a == 0) printf("Nu s a sters !\n");
	else printf("Stergere efectuata cu suuces \n");

}

void ui_modifica(service* srv)
{
	printf("Modificare element... \n");
	char nume[30]; int cannou;
	printf("Introdu numele :\n");
	scanf("%s", nume);

	printf("Introdu cantitate noua :\n");
	scanf("%d", &cannou);

	int a = modifica_element(srv, nume,cannou);
	if (a == 0) printf("Modificare a esuat !\n");
	else printf("Modificare realizata cu suuces \n");

}

void ui_filtru(service* srv)
{
    printf("Filtrare in functie de nume-o litera/ cantitate?: \n");
    char optiune[100];
    scanf("%s", optiune);
    lista* lista_filt = NULL;
    if(strcmp(optiune, "cantitate") == 0)
    {
        int cant;
        printf("Introduceti cantitatea: \n");
        scanf("%d", &cant);
        lista_filt = filtru_cant(srv, cant);
    } else if (strcmp(optiune, "nume") == 0)
    {
        char chr[10];
        printf("Introduceti prima litera a produsului(majuscula): \n");
        scanf("%s", chr);
        lista_filt = filtru_nume(srv, chr);
    }
    if(lista_filt == NULL) return;
    ui_print(lista_filt);
    destroy_lista(lista_filt);
}

void ui_sort(service* srv)
{
    printf("Nume/Cantitate: \n");
    char optiune[100];
    scanf("%s", optiune);

    printf("1-ascendent, 0- descendent");
    int directie;
    scanf("%d", &directie);

    lista* lista_sort = NULL;
    if(strcmp(optiune, "cantitate") == 0)
    {
        lista_sort = sortare(srv, cmpfc_cantitate, directie);
    } else if (strcmp(optiune, "nume") == 0)
    {
        lista_sort = sortare(srv, cmpfc_nume, directie);
    }
    if(lista_sort == NULL) return;
    ui_print(lista_sort);
    destroy_lista(lista_sort);
}

void ui_undo(service* srv)
{
    int rezultat = apelare_undo(srv);
    if(rezultat)
        printf("Undo efectuat cu succes!!!!\n");
    else
        printf("IMPOSIBIL DE REALIZAT UNDO!!!\n");
}

void ui_multiplu_trei(service* srv)
{
    printf("Filtrare in functie de nume si cantitate multipla de 3: \n");
    char nume[100];
    scanf("%s", nume);
    lista* lista_mult = NULL;
    lista_mult = multiplu_trei(srv, nume);

    if(lista_mult == NULL) return;
    ui_print(lista_mult);
    destroy_lista(lista_mult);
}



//void ui_filtru(service* srv)
//{
//	printf("Afisare materie cu cantitate mai mica decat cea data :\n");
//	int can;
//	printf("Introodu cantitate :\n");
//	scanf("%d", &can);
//
//	lista lisfiltr = filtru_crit(v, can);
//	ui_print(&lisfiltr);
//	destroy_lista(&lisfiltr);
//}
//void ui_sort(lista* v)
//{
//	printf("sortare cresc dupa cantitate..\n");
//
//	lista lista_sort = sortare(v, cmpfc);
//	ui_print(&lista_sort);
//	destroy_lista(&lista_sort);
//}

