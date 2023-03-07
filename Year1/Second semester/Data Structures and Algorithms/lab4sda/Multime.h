//
// Created by Ilinca on 13-Apr-22.
//

#ifndef LAB4SDA_MULTIME_H
#define LAB4SDA_MULTIME_H

#pragma once

typedef int TElem;

typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorMultime;

//struct Nod {
//    TElem valoare;
//    Nod* urmator;
//};

class Multime {

    friend class IteratorMultime;

private:
    /* aici e reprezentarea */
//    Nod* prim;
    int capacitate;     //capacitate
    int dimensiune;     //numarul de elemente
    TElem *e;           //vector elemente
    TElem *urm;         //vector legatura urmatoare
    TElem *prec;        //vector legatura precedenta
    int prim;           //primul element al listei
    int ultim;          //ultimul element al listei
    int primLiber;      //primul element din lista spatiului liber

    //functie pentru alocarea unui spatiu liber
    //se returneaza pozitia spatiului liber din lista
    int aloca();

    //functie pentru dealocarea spatiului de pe indicele i
    void dealoca(int i);

    //functie ce creeaza un nod in lista inlantuita
    int creeazaNod(TElem elem);

    //functie ce redimensioneaza lista inlantuita
    void redim();


public:
    //constructorul implicit
    Multime();

    //adauga un element in multime
    //returneaza adevarat daca elementul a fost adaugat (nu exista deja in multime)
    bool adauga(TElem e);

    //sterge un element din multime
    //returneaza adevarat daca elementul a existat si a fost sters
    bool sterge(TElem e);

    //verifica daca un element se afla in multime
    bool cauta(TElem elem) const;


    //intoarce numarul de elemente din multime;
    int dim() const;

    //verifica daca multimea e vida;
    bool vida() const;

    void goleste();

    //returneaza un iterator pe multime
    IteratorMultime iterator() const;

    // destructorul multimii
    ~Multime();

};

#endif //LAB4SDA_MULTIME_H
