//
// Created by Ilinca on 28-Mar-22.
//

#include "Matrice.h"

#include <exception>
#include <iostream>

using namespace std;

/*
 * complexitate:  BC=WC=AC=theta(n);
 */

void Matrice::redimensioneaza() {
    auto coloane_nou = new TElem[2*capacit];
    auto val_nou = new TElem[2*capacit];

    for(int i=0;i<dimens;i++)
    {
        coloane_nou[i] = this->coloane[i];
        val_nou[i] = this->val[i];
    }
    capacit = capacit*2;
    delete[] coloane;
    delete[] val;
    this->coloane = coloane_nou;
    this->val = val_nou;

}

/*
 * Complexitate: BC=amortizata theta(1), WC=theta(n), AC=O(n)
 */
void Matrice::adauga(int poz, int l, int c, TElem e){
    if(dimens == capacit-1)
        redimensioneaza();
    this->dimens++;
    for(int i=dimens;i>=poz+1;i--)
    {
        this->coloane[i] = this->coloane[i-1];
        this->val[i] = this->val[i-1];
    }
    this->coloane[poz] = c;
    this->val[poz] = e;
    for(int i=l;i<=this->nr_linii;i++)
        this->linii[i] = this->linii[i]+1;
}
/*
* Complexitate: BC=WC=AC=theta(m);
*/
Matrice::Matrice(int m, int n) {
    /* de adaugat */
    if(m<=0 || n<=0)
        throw exception();
    this->nr_linii = m;
    this->nr_col = n;

    this->linii = new TElem[m+1];   //vector pe linii
    for(int i=0;i<=m;i++)
        this->linii[i] = NULL_TELEMENT;

    this->capacit = 2;
    this->dimens = 0;
    this->val = new TElem[capacit]; //vector de valori
    this->coloane = new TElem[capacit]; //vector pe coloane

}
/*
* Complexitate: BC=WC=AC=theta(n);
*/
void Matrice::sterge(int poz, int l){
    for(int i=poz;i<=this->dimens;i++) {
        this->coloane[i] = coloane[i + 1];
        this->val[i] = val[i + 1];
    }

    this->dimens--;
    for(int i = l+1;i<this->nr_linii;i++)
        this->linii[i]--;   //muta tot cu o poz la stanga
}

/*
* Complexitate: BC=WC=AC=theta(1);
*/
int Matrice::nrLinii() const{
    /* de adaugat */
    return this->nr_linii;
}

/*
* Complexitate: BC=AC=WC=theta(1);
*/
int Matrice::nrColoane() const{
    /* de adaugat */
    return this->nr_col;
}

/*
* Complexitate: BC=theta(1), WC=theta(m),AC=O(m);
*/
TElem Matrice::element(int i, int j) const{
    /* de adaugat */
    if(i<0 || j<0)
        throw exception();
    int coloana_curenta;
    for(int poz=this->linii[i];poz<this->linii[i+1];poz++)
    {
        coloana_curenta = this->coloane[poz];
        if(coloana_curenta == j)
            return this->val[poz];
        else if (coloana_curenta >j)
            break;
    }
    return NULL_TELEMENT;
}


/*
* Complexitate: BC=amortizata theta(1), WC=theta(m),AC=O(m);
*/
TElem Matrice::modifica(int i, int j, TElem e) {
    /* de adaugat */
    if( i>=this->nr_linii || j>=this->nr_col || i<0 ||j<0)
        throw exception();
    int p; //= this->linii[i];
    int coloana_curenta = -1;
    for(p=this->linii[i];p<this->linii[i+1];p++)
        {
            coloana_curenta = this->coloane[p];
            if(coloana_curenta >= j)
                break;
        }
    if(coloana_curenta != j)
    {
        //daca ajung aici inseamna ca elem de pe poz data ii 0
        if(e!=0)
            adauga(p,i+1,j,e);
        return 0;
    }
    else if (e==0)
        //daca elementul pe care vrem sa il adaugam in matrice este 0, pur si simplu il stergem fiind matrice rara
        sterge(p,i);
    else {
        auto z = this->val[p];
        this->val[p] = e;  //altfel modific valoarea
        return z;       //ii ok aici?

    }

    cout<<"Valorile din vectorul de linii sunt:";
    for(int l=0;l<=nr_linii;l++)
        cout<<"linii["<<l<<"] = "<<linii[l]<<'\n';

    return 0;

}


