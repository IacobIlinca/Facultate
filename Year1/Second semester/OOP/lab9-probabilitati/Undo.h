//
// Created by Ilinca on 27-Apr-22.
//

#ifndef LAB4_6OOP_UNDO_H
#define LAB4_6OOP_UNDO_H

#pragma once
#include "Repository.h"
#include <string>
using std::string;

class ActiuneUndo{
private:
public:
    virtual void doUndo() = 0;
    virtual ~ActiuneUndo() = default;
};

class UndoAdauga: public ActiuneUndo {
private:
    Medicament_Repository& repo;
    Medicament med;
public:
    UndoAdauga(Medicament_Repository& _repo, const Medicament& _med) : repo{_repo }, med{ _med }{};
    void doUndo() override;
};


class UndoSterge: public ActiuneUndo {
private:
    Medicament_Repository& repo;
    Medicament med;
public:
    UndoSterge(Medicament_Repository& _repo, const Medicament& _med) : repo{_repo }, med{_med }{};
    void doUndo() override;
};


class UndoModifica: public ActiuneUndo {
private:
    Medicament_Repository& repo;
    Medicament med;
public:
    UndoModifica(Medicament_Repository& _repo, const Medicament& _med) :repo{ _repo }, med{ _med }{};
    void doUndo() override;
};


class UndoException {
private:
    string msg;
public:
    UndoException(const string& msg) :msg{ msg }{};
    const string& get_msg() const noexcept;
};

#endif //LAB4_6OOP_UNDO_H
