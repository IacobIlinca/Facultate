//
// Created by Ilinca on 30-Mar-22.
//

#ifndef LAB4_6OOP_UI_H
#define LAB4_6OOP_UI_H

#pragma once
#include "Service.h"

class Console{
private:
    Medicamente_Service& srv;
public:
    Console(Medicamente_Service& srv) :srv{ srv } {};
    Console(const Console& ot) = delete;
    /*
     * Printeaza meniul aplicatiei
     */
    void print_meniu();
    /*
     * Functia de ui pentru adaugarea unui medicament
     */
    void ui_add();
    /*
     * Functia de ui pentru printarea medicamentelor
     */
    void print_all_medicamente();
    /*
     * Functia de ui pentru modificarea unui medicament
     */
    void ui_modificare();
    /*
     * Functia de ui pentru stergerea unui medicament
     */
    void ui_stergere();
    void ui_find();
    /*
     * Functia de ui pentru filtrarea unui medicament
     */
    void ui_filtrare();

    void ui_sort();
    void ui_all_of();


    //UI PENTRU LISTA
    void print_meniu_list();
    void ui_add_list();
    void ui_add_random_list();
    void ui_empty_list();
    void ui_reteta();
    void ui_export_reteta();
    void print_all_from_list();

    void ui_undo();

    void run();

};

#endif //LAB4_6OOP_UI_H
