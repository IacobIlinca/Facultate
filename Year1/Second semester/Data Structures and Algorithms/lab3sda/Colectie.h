//
// Created by Ilinca on 28-Mar-22.
//

#ifndef LAB2SDA_COLECTIE_H
#define LAB2SDA_COLECTIE_H
#pragma once

#define NULL_TELEM -1
typedef int TElem;

class IteratorColectie;

class Node;

typedef Node *PNode;       //se defineste tipul PNode ca fiind adresa unui Node

class Node
{
public:
    friend class Colectie;

    Node(TElem e, int frecventa, PNode urm, PNode prev);

    TElem element();
    int frecventa();
    PNode urmator();
    PNode precedent();

private:
    TElem data;       //elementul propriu-zis
    int fr;         //frecventa elementului
    PNode next;     //pointer la urmatorul nod din LDI
    PNode prev;     //pointer la anteriorul nod din LDI

};

class Colectie
{
    friend class IteratorColectie;

private:
    /* aici e reprezentarea */
    PNode head;
    //????PNode tail;

public:
    //constructorul implicit
    Colectie();

    //adauga un element in colectie
    void adauga(TElem e);

    //sterge o aparitie a unui element din colectie
    //returneaza adevarat daca s-a putut sterge
    bool sterge(TElem e);

    //verifica daca un element se afla in colectie
    bool cauta(TElem elem) const;

    //returneaza numar de aparitii ale unui element in colectie
    int nrAparitii(TElem elem) const;


    //intoarce numarul de elemente din colectie;
    int dim() const;

    //verifica daca colectia e vida;
    bool vida() const;

    int elementeCuFrecventaData(int frecventa) const;

    //returneaza un iterator pe colectie
    IteratorColectie iterator() const;

    // destructorul colectiei
    ~Colectie();

};


#endif //LAB2SDA_COLECTIE_H
