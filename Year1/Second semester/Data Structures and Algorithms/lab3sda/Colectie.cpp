//
// Created by Ilinca on 28-Mar-22.
//

#include "Colectie.h"
#include "IteratorColectie.h"
#include <exception>
#include <iostream>

using namespace std;

/*
* Complexitate: BC=WC=AC=theta(1)
*/
Node::Node(TElem data, int frecventa, PNode next, PNode prev){
    this->data = data;
    this->fr = frecventa;
    this->next = next;
    this->prev = prev;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
TElem Node:: element() {
     return data;   //trebuie sa returnez si frecventa aici?
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
int Node::frecventa() {
    return fr;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
PNode Node::urmator(){
    if(this!= nullptr)
        return next;
    return nullptr;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
PNode Node::precedent() {
    return prev;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
Colectie::Colectie() {
    /* de adaugat */
    head = nullptr;
}

/*
* Complexitate: BC=theta(1),WC=theta(n),AC=O(n);
*/
void Colectie::adauga(TElem elem) {
    /* de adaugat */
    //adaugare la inceputul LDI
    PNode node = head;    //this->head sau doar head?
    while (node != nullptr && node->data != elem)
        node = node->next;

    if (node != nullptr) node->fr ++;
    else {
            Node* new_node = new Node (elem, 1, head, nullptr);
//            head = new_node;
//            new_node->next->prev = new_node;
            if(head == nullptr)
            {
                head = new_node;
                return;
            }
            new_node->next = head;
            head->prev = new_node;
            head = new_node;
        }

}

/*
* Complexitate: BC=theta(1),WC=theat(n),AC=O(n);
*/
bool Colectie::sterge(TElem elem) {
    /* de adaugat */
    PNode node = head;    //this->head sau doar head?
    while (node != nullptr && node->data != elem)
        node = node->next;

    if (node != nullptr) {
        node->fr --;   //elementul apare de mai multe ori in lista, decrementam doar frecventa
        if(node->fr == 0)
        {
            PNode previous = node->prev;
            PNode next = node->next;

            if(previous != nullptr){
                previous->next = next;
            } else {
                head = next;
            }

            if(next != nullptr){
                next->prev = previous;
            }
            delete node;
            return true;
        }
        return true;
    }

    return false;  //elementul nu se afla in colectie
}

/*
* Complexitate: BC=theta(1),WC=theta(n),AC=O(n);
*/
bool Colectie::cauta(TElem elem) const {
    /* de adaugat */
    PNode node = head;    //this->head sau doar head?
    while (node != nullptr && node->data != elem)
        node = node->next;

    //daca nu a ajuns la final, inseamna ca elementul a fost gasit si se afla in lista
    if(node != nullptr) return true;

    return false;
}

/*
* Complexitate: BC=theta(1),WC=theta(n),AC=O(n);
*/
int Colectie::nrAparitii(TElem elem) const {
    /* de adaugat */
    PNode node = head;    //this->head sau doar head?
    while (node != nullptr && node->data != elem)
        node = node->next;

    if(node == nullptr)
        return 0;  //in acest caz, elem nu este in lista
    //odata iesit de aici, inseamna ca in node se afla informatia cautata
    return node->fr;

}

/*
* Complexitate: BC=WC=AC=theta(n);
*/
int Colectie::dim() const {
    /* de adaugat */
    PNode node = head;    //this->head sau doar head?
    int dimensiune = 0;
    while (node != nullptr )
    {
        dimensiune = dimensiune + node->fr;     //dc nu trece aici?
        node = node->next;

    }
    if(dimensiune > 0) return dimensiune;
    return 0;
}

/*
* Complexitate: BC=WC=AC=theta(1)
*/
bool Colectie::vida() const {
    /* de adaugat */
//    PNode node = head;    //this->head sau doar head?
//    int dimensiune = 0;
//    while (node != nullptr )
//    {
//        node = node->next;
//        dimensiune++;
//    }
//    if(dimensiune == 0) return true; //colectia este vida
//    else return false;  //colectia nu este vida

    if(head == nullptr) return true;
    return false;
}

/*
* Complexitate: BC=WC=AC=theta(n)
*/
int Colectie::elementeCuFrecventaData(int frecventa) const {
    int nr = 0;
    PNode node = head;    //this->head sau doar head?
    if(frecventa <= 0){
        throw exception();
    }
    while (node != nullptr){
        if(node->frecventa() == frecventa){
            nr = nr+1;
        }
        node = node->next;
    }

    return nr;
}


/*
* Complexitate: BC=WC=AC=theta(1);
*/
IteratorColectie Colectie::iterator() const {
    return  IteratorColectie(*this);
}

/*
* Complexitate: BC=WC=AC=O(n);
*/
Colectie::~Colectie() {
    /* de adaugat */
    while(head != nullptr){
        PNode p = head;
        head = head->next;
        delete p;
    }
}



