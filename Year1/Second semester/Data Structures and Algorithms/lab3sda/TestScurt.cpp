//
// Created by Ilinca on 28-Mar-22.
//
#include "TestScurt.h"
#include <assert.h>
#include <iostream>
#include "Colectie.h"
#include "IteratorColectie.h"





void testAll() { //apelam fiecare functie sa vedem daca exista
    Colectie c;
    assert(c.vida() == true);
    assert(c.dim() == 0); //adaug niste elemente
    c.adauga(5);
    c.adauga(1);
    c.adauga(10);
    c.adauga(7);
    c.adauga(1);
    c.adauga(11);
    c.adauga(-3);
    assert(c.dim() == 7);
    assert(c.cauta(10) == true);
    assert(c.cauta(16) == false);
    assert(c.nrAparitii(1) == 2);
    assert(c.nrAparitii(7) == 1);
    assert(c.sterge(1) == true);
    assert(c.sterge(6) == false);
    assert(c.dim() == 6);
    assert(c.nrAparitii(1) == 1);

    //std::cout << c.elementeCuFrecventaData(1);
    assert(c.elementeCuFrecventaData(1) == 6);
    IteratorColectie ic = c.iterator();
    ic.prim();
    while (ic.valid()) {
        TElem e = ic.element();
        ic.urmator();
    }
    std::cout<<"Finished short tests\n";
}


void test_func_noua(){
    Colectie c;
    assert(c.vida() == true);
    assert(c.dim() == 0); //adaug niste elemente
    c.adauga(5);
    c.adauga(1);
    c.adauga(11);
    c.adauga(5);
    c.adauga(2);
    c.adauga(2);
    c.adauga(2);
    assert(c.elementeCuFrecventaData(1) == 2);
    assert(c.elementeCuFrecventaData(2) == 1);
    assert(c.elementeCuFrecventaData(3) == 1);
    int rez;
    try{
        rez = c.elementeCuFrecventaData(-2);
        assert(false);
    }
    catch (std::exception){
        assert(true);
    }

    std::cout << "Finished home tests\n";
}
