#include "Iterator.h"
#include "DO.h"
#include <iostream>

#include <exception>
using namespace std;

int goToNextPrime(int nr) {
    if (nr == 2) {
        return nr;
    }
    if (nr % 2 == 0) {
        nr++;
    }
    nr -= 2;
    bool isPrime = false;
    while (!isPrime) {
        nr += 2;
        isPrime = true;
        int d;
        for (d = 3; d * d <= nr; d += 2) {
            if (nr % d == 0) {
                isPrime = false;
                break;
            }
        }
    }
    return nr;
}

bool rel(TCheie c1, TCheie c2) {
    if (c1 <= c2) {
        return true;
    }
    else {
        return false;
    }
}

int DO::h1(TCheie c) const {
    int hash = abs(c) % cp;
    return hash;
}

int DO::h2(TCheie c) const {
    int hash = 1 + abs(c) % (cp-1);
    return hash;

}

int DO::hash(TCheie c, int i) const {
    int hash1 = h1(c);
    int hash2 = h2(c);
    int hash = (hash1 + abs(hash2) % cp) % cp;
    return hash;
}


DO::DO(Relatie r) {
    REL = r;
	/* de adaugat */
    cp = 3319;
    el = new TElem[cp]; //telem sau tcheie?
    for (int i = 0; i < cp; i++) {
        el[i].first = NULL_TELEM;
        el[i].second = NULL_TELEM;
    }
     n = 0;
}

//adauga o pereche (cheie, valoare) in dictionar
//daca exista deja cheia in dictionar, inlocuieste valoarea asociata cheii si returneaza vechea valoare
//daca nu exista cheia, adauga perechea si returneaza null
TValoare DO::adauga(TCheie c, TValoare v) {
	/* de adaugat */
    TElem elem = make_pair(c,v);
    if(cauta(c) == NULL_TVALOARE) {
        int i = 0;
        int hash = this->hash(c, i);
        while (i < cp && el[hash].first != NULL_TELEM && el[hash].first != STERS) {
            i++;
            hash = this->hash(c, i);
        }

        if (i == cp) {
            resizeAndRehash();
            i = 0;
            hash = this->hash(c, i);
            while (i < cp && el[hash].first != NULL_TELEM && el[hash].first != STERS) {
                i++;
                hash = this->hash(c, i);
            }
        }
        el[hash] = elem;
        this->n++;
        return NULL_TVALOARE;
    }
    else {
        int i=0;
        int hash = this->hash(c,i);
        while(i<cp && el[hash].first != NULL_TELEM ) {
            if(el[hash].first == c) {
                int val_veche=el[hash].second;
                el[hash].second=v;
                return val_veche;
            }
            i++;
            hash = this->hash(c,i);
        }

    }

//    int i = 0;
//    do {
//        int j = hash(elem.first, i);
//        if(el[j].first == NULL_TELEM || el[j].second == STERS) {
//            el[j] = elem;
//            n++;
//            return NULL_TVALOARE;
//        }
//        else if (el[j] == elem) {
//            int val_veche=el[j].second;
//                el[j].second=v;
//                return val_veche;
//        }
//        else {
//            i++;
//        }
//    } while (i<cp);
//    if( i == cp ) {
//        resizeAndRehash();
//    }

}

//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null
TValoare DO::cauta(TCheie c) const {
	/* de adaugat */
    int i=0;
    int hash = this->hash(c,i);
    while(i<cp && el[hash].first != NULL_TELEM ) {
        if(el[hash].first == c) {
            return el[hash].second;
        }
        i++;
        hash = this->hash(c,i);
    }

	return NULL_TVALOARE;
}

//sterge o cheie si returneaza valoarea asociata (daca exista) sau null
TValoare DO::sterge(TCheie c) {
	/* de adaugat */
	int i = 0;
    int hash = this->hash(c,i);
    while(i<cp && el[hash].first != NULL_TELEM) {
        if(el[hash].first == c) {
            el[hash].first = STERS;
            n--;
            return el[hash].second;
        }
        i++;
        hash = this->hash(c,i);
    }
    return NULL_TVALOARE;
}

//returneaza numarul de perechi (cheie, valoare) din dictionar
int DO::dim() const {
	/* de adaugat */
	return this->n;
}

//verifica daca dictionarul e vid
bool DO::vid() const {
	/* de adaugat */
	return n == 0;
}

Iterator DO::iterator() const {
	return  Iterator(*this);
}

DO::~DO() {
	/* de adaugat */
    delete[] el;
}

void DO::resizeAndRehash() {
    TElem *oldElements = el;
    int oldCapacity = cp;
    cp *= 2;
    cp = goToNextPrime(cp);
    el = new TElem[cp];
    for (int i = 0; i < cp; i++) {
        el[i].first = NULL_TELEM;
        el[i].second = NULL_TELEM;

    }
    for (int i = 0; i < oldCapacity; i++) {
        TElem current = oldElements[i];
        if (current.first != NULL_TELEM && current.first != STERS) {
            int j = 0;
            int hash = this->hash(current.first, j);
            while (j < cp && el[hash].first != NULL_TELEM) {
                j++;
                hash = this->hash(current.first, j);
            }
            el[hash] = current;
        }
    }
    delete[]oldElements;

//    TElem* newE = new TElem[this->cp*2];
//    for(int i =0;i<this->cp*2;++i) {
//        newE[i].first = NULL_TELEM;
//        newE[i].second = NULL_TELEM;
//    }
//
//    TElem* oldE = this->el;
//    this->el = newE;
//    this->cp = this->cp * 2;
//    this->n = 0;
//
//    for (int i = 0; i < this->cp / 2; ++i) {
//        if (oldE[i].first != NULL_TELEM) {
//            this->adauga(oldE[i].first, oldE[i].second);
//        }
//
//    }
//    delete[] oldE;

}
