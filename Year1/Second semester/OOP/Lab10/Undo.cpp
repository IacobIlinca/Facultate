//
// Created by Ilinca on 27-Apr-22.
//

#include "Undo.h"

const string& UndoException::get_msg() const noexcept {
    return msg;
}

void UndoAdauga::doUndo() {
    repo.stergere_repo(med);
}

void UndoSterge::doUndo() {
    repo.store(med);
}

void UndoModifica::doUndo() {
    repo.modificare_pret_repo(med);
}
