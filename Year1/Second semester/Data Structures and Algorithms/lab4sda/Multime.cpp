//
// Created by Ilinca on 13-Apr-22.
//

#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>

using namespace std;

//WC=BC=teta(n)
void Multime::redim() {
    TElem* elem_nou = new int[2*capacitate];
    TElem* urm_nou = new int[2*capacitate];
    TElem* prec_nou = new int[2*capacitate];

    //copiem valorile vechi in zona noua
    for(int i=0;i<dimensiune;i++)
        elem_nou[i] = e[i];
    for(int i=0;i<dimensiune;i++)
        urm_nou[i] = urm[i];
    for(int i=0;i<dimensiune;i++)
        prec_nou[i] = prec[i];

    capacitate = 2 * capacitate;

    delete[] e;
    delete[] urm;
    delete[] prec;

    //indicam spre noile zone
    e = elem_nou;
    urm = urm_nou;
    prec = prec_nou;

    //facem legaturile pt spatiul nou creat
    for(int i=capacitate/2; i<capacitate;i++)
        urm[i] = i+1;

    for(int i=capacitate/2; i<capacitate-1;i++)
        prec[i+1] = i;

    prec[capacitate/2] = ultim;
    primLiber = capacitate/2;
}

//WC=BC=teta(1)
int Multime::aloca() {
    //se sterge primul element din lista spatiului liber
    int i = primLiber;
    primLiber = urm[primLiber];
    return i;
}


//WC=BC=teta(1)
void Multime::dealoca(int i) {
    //pozitia i se muta in lista spatiului liber
    urm[i] = primLiber;
    primLiber = i;
}


//BC=teta(1), WC=teta(n)-pt redimensionare, OC=O(n)
int Multime::creeazaNod(TElem elem) {
    if(dimensiune == capacitate)
        redim();
    int i = aloca();
    this->e[i] = elem;
    urm[i] = -1;
    prec[i] = -1;
    return i;
}

//o posibila relatie
//WC=BC=teta(1)
bool rel(TElem e1, TElem e2) {
    if (e1 <= e2) {
        return true;
    }
    else {
        return false;
    }
}


//WC=BC=teta(capacitate)
Multime::Multime() {
    /* de adaugat */
    prim = -1;
    ultim = -1;
    this->capacitate = 10;      //setam capacitatea listei

    //alocam spatiu
    e = new TElem[capacitate];
    urm = new TElem[capacitate];
    prec = new TElem[capacitate];

    this->dimensiune = 0;       //setam dimensiunea initiala a listei
    //stabilim legaturile initiale
    //toate pozitiile initial sunt marcate ca spatiu liber
    for(int i=0;i<capacitate-1;i++)
    {
        urm[i] = i+1;
        prec[i+1] = i;
    }
    urm[capacitate-1] = -1;
    prec[0] = -1;
    primLiber =0;
}


//BC=teta(1)-pt prima poz, WC=teta(1)-pt ultima poz
//OC=O(N)
bool Multime::adauga(TElem elem) {
    /* de adaugat */
    int poz = creeazaNod(elem);
    if (prim == -1)     //lista e vida
    {
        dimensiune++;
        prim = poz;
        ultim = poz;
        urm[poz] = -1;
        prec[poz] = -1;
        return true;
    }
    else
    {
        auto curent = prim;
        while (rel(e[curent], elem) && curent != -1)
        {
            if(e[curent] == elem)
            {
                //verificam ca elementul sa nu se afle deja in multime
                dealoca(poz);
                return false;
            }
            curent = urm[curent];
        }
        if(curent == prim)
        {
            //inserare pe primul loc
            prec[prim] = poz;
            urm[poz] = prim;
            prim = poz;
            dimensiune++;
            return true;
        }
        if(curent == -1)
        {
            //inseram pe ultimul loc
            urm[ultim] = poz;
            prec[poz] = ultim;
            ultim = poz;
            dimensiune++;
            return true;
        }
        //inseram oriunde in lista, intre 2 elemnte oarecare
        urm[poz] = curent;
        auto poz_nod_prec = prec[curent];
        urm[poz_nod_prec] = poz;
        prec[poz] = poz_nod_prec;
        prec[curent] = poz;
        dimensiune++;
        return true;
    }
    return false;
}

//BC=teta(1)-pt primul element, WC=teta(1)-pt ultimul element sau elem ce nu exista
//OC=O(N)
bool Multime::sterge(TElem elem) {
    /* de adaugat */
    int curent = prim;
    while ( e[curent] != elem && curent != -1 )
        curent = urm[curent];
    if ( curent == -1)        //am ajuns la final
        return false;
    if (curent == prim)
    {
        //stergem primul element
        if (dimensiune == 1)
        {
            //daca asta e unicul element din lista
            dealoca(curent);
            prim = -1;
            ultim = -1;
            dimensiune--;
            return true;
        }
        else
        {
            //stergem de pe prima poz, dar mai sunt alte elem in lista
            prec[urm[prim]] = -1;       //dispare legatura dintr urmator si curent
            prim = urm[prim];
            dealoca(curent);
            dimensiune--;
            return true;
        }
    }
    if(curent == ultim)
    {
        //stergem ultimul nod
        auto poz_nod_prec = prec[ultim];
        prec[ultim] = -1;
        urm[poz_nod_prec] = -1;
        ultim = poz_nod_prec;
        dimensiune--;
        dealoca(curent);
        return true;
    }

    //stergem de pe o poz oarecare, dintre 2 noduri oarecare
    auto poz_nod_prec = prec[curent];
    auto poz_nod_urm = urm[curent];
    prec[poz_nod_urm] = poz_nod_prec;
    urm[poz_nod_prec] = poz_nod_urm;
    urm[curent] = -1;
    prec[curent] = -1;
    dimensiune--;
    dealoca(curent);
    return true;
}

//BC=teta(1)-pt prima poz, WC=teta(1)-pt ultima poz sau nu exista
//OC=O(N)
bool Multime::cauta(TElem elem) const {
    /* de adaugat */
    //lista e vida
    if (prim == -1)
        return false;
    int curent = prim;      //incepem parcurgerea de la inceputul listei
    while(e[curent] != elem && curent != -1)
        curent = urm[curent];
    if(curent == -1)
        return false;       //s-a ajuns la finalul listei fara a fi gasit elementul elem
    return true;
}

//BC=WC=teta(1)
int Multime::dim() const {
    /* de adaugat */
    return this->dimensiune;

}

//BC=WC=teta(1)
bool Multime::vida() const {
    /* de adaugat */
    if(prim == -1)
        return true;
    return false;
}

//BC=WC=teta(1)
IteratorMultime Multime::iterator() const {
    return IteratorMultime(*this);
}

//BC=WC=teta(n^2)
void Multime::goleste() {
//    int curent = prim;
//    if (prim != -1)
//    {
//        while(curent != -1) //nu am ajuns la final
//        {
//            int nou = curent;
//            dealoca(curent);
//            curent = urm(curent);
//
//        }
//    }
    int curent = prim;
    int nr_doi = urm[curent];
    while(nr_doi != -1)
    {
        sterge(e[prec[nr_doi]]);
        nr_doi = urm[nr_doi];

    }

    sterge(e[ultim]);

}

//BC=WC=teta(1)
Multime::~Multime() {
    /* de adaugat */
    delete[] e;
    delete[] urm;
    delete[] prec;
}




