//
// Created by Ilinca on 28-Mar-22.
//

#include <exception>
#include "IteratorColectie.h"
#include "Colectie.h"

/*
* Complexitate: BC=WC=AC=theta(1)
*/
IteratorColectie::IteratorColectie(const Colectie& c): col(c) {
    /* de adaugat */
    curent = c.head;
    currentFrequency = 1;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
void IteratorColectie::prim() {
    /* de adaugat */
    curent = col.head;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
void IteratorColectie::urmator() {
    /* de adaugat */
    if (currentFrequency < curent->frecventa()) {
        currentFrequency += 1;
    } else {
        curent = curent->urmator();
        currentFrequency = 1;
    }
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
bool IteratorColectie::valid() const {
    /* de adaugat */
    return curent != nullptr;
}


/*
* Complexitate: BC=WC=AC=theta(1)
*/
TElem IteratorColectie::element() const {
    /* de adaugat */
    if (!valid()) {
        throw std::exception();
    }
    return curent->element();
}

