//
// Created by Ilinca on 13-Apr-22.
//

#include "IteratorMultime.h"
#include "Multime.h"

//BC=WC=teta(1)
IteratorMultime::IteratorMultime(const Multime& m): mult(m) {
    /* de adaugat */
    curent = m.prim;
}

//BC=WC=teta(1)
TElem IteratorMultime::element() const {
    /* de adaugat */
    return mult.e[curent];
}

//BC=WC=teta(1)
bool IteratorMultime::valid() const {
    /* de adaugat */
    return curent != -1;
}

//BC=WC=teta(1)
void IteratorMultime::urmator() {
    /* de adaugat */
    curent = mult.urm[curent];
}

//BC=WC=teta(1)
void IteratorMultime::prim() {
    /* de adaugat */
    curent = mult.prim;
}


