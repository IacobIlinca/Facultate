//
// Created by Ilinca on 28-Mar-22.
//

#ifndef LAB1SDA_MATRICE_H
#define LAB1SDA_MATRICE_H

#pragma once

typedef int TElem;


#define NULL_TELEMENT 0

class Matrice {

private:
    /* aici e reprezentarea */
    int nr_linii,nr_col; //nr de linii si nr de coloane
    int capacit; //capacitatea vectorilor c si v
    int dimens; //deimensiunea vectorilor c si v
    TElem* linii;  //vector pe linii
    TElem* coloane; //vector pe coloane
    TElem* val; //vector de valori

    void redimensioneaza(); //redimensioneaza vectorii de valoare si cei de coloane
    void adauga(int poz, int l, int c, TElem e);  //adauga elementul e pe linia l si coloana c
    void sterge(int poz, int l);    //sterge elem de pe poz


public:

    //constructor
    //se arunca exceptie daca nrLinii<=0 sau nrColoane<=0
    Matrice(int nrLinii, int nrColoane);


    //destructor
    ~Matrice(){};

    //returnare element de pe o linie si o coloana
    //se arunca exceptie daca (i,j) nu e pozitie valida in Matrice
    //indicii se considera incepand de la 0
    TElem element(int i, int j) const;


    // returnare numar linii
    int nrLinii() const;

    // returnare numar coloane
    int nrColoane() const;


    // modificare element de pe o linie si o coloana si returnarea vechii valori
    // se arunca exceptie daca (i,j) nu e o pozitie valida in Matrice
    TElem modifica(int i, int j, TElem);

};


#endif //LAB1SDA_MATRICE_H
