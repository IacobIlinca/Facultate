//
// Created by Ilinca on 13-Apr-22.
//

#ifndef LAB4SDA_ITERATORMULTIME_H
#define LAB4SDA_ITERATORMULTIME_H

#pragma once
#include "Multime.h"

typedef int TElem;

class IteratorMultime
{
    friend class Multime;

private:

    //constructorul primeste o referinta catre Container
    //iteratorul va referi primul element din container
    IteratorMultime(const Multime& m);

    //contine o referinta catre containerul pe care il itereaza
    const Multime& mult;

    /* aici e reprezentarea  specifica a iteratorului */
    int curent;

public:

    //reseteaza pozitia iteratorului la inceputul containerului
    void prim();

    //muta iteratorul in container
    // arunca exceptie daca iteratorul nu e valid
    void urmator();

    //verifica daca iteratorul e valid (indica un element al containerului)
    bool valid() const;

    //returneaza valoarea elementului din container referit de iterator
    //arunca exceptie daca iteratorul nu e valid
    TElem element() const;
};



#endif //LAB4SDA_ITERATORMULTIME_H
