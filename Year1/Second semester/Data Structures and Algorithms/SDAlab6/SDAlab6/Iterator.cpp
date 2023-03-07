#include "Iterator.h"
#include "DO.h"
#include <iostream>
using namespace std;

Iterator::Iterator(const DO& d) : dict(d) {
	/* de adaugat */
    curent = 0;
    deplasare();
    int minmax = this->dict.el[curent].first;
    for(int i=0;i<this->dict.cp;i++)
        if(dict.el[i].first != NULL_TELEM && dict.el[i].first != STERS && dict.REL(dict.el[i].first, minmax)) {
            minmax = dict.el[i].first;
            curent = i;
        }
   // deplasare();
}

void Iterator::prim() {
	/* de adaugat */
    //curent = 0;
   // deplasare();
    curent = 0;
    deplasare();
    int minmax = this->dict.el[curent].first;
    for(int i=0;i<this->dict.cp;i++)
        if(dict.el[i].first != NULL_TELEM && dict.el[i].first != STERS && dict.REL(dict.el[i].first, minmax)) {
            minmax = dict.el[i].first;
            curent = i;
        }

}

void Iterator::urmator() {
   // curent = 0;
    int minim = this->dict.el[curent].first;
    //std::cout<<curent<<"\n";
    for(int i=0;i<this->dict.cp;i++)
        if(dict.el[i].first != NULL_TELEM && dict.el[i].first != STERS && dict.REL(dict.el[i].first, minim)) {
            minim = dict.el[i].first;
            curent = i;
        }
   // std::cout<<curent<<"\n";
}

bool Iterator::valid() const {
	/* de adaugat */
	return (curent<dict.cp && this->dict.el[curent].first != NULL_TELEM);
}

TElem Iterator::element() const {
	/* de adaugat */
    if(!valid())
        throw std::exception();
	return dict.el[curent];
}

void Iterator::deplasare() {
    while((curent<dict.cp) && (dict.el[curent].first==NULL_TELEM || dict.el[curent].first==STERS))
        curent++;
}




