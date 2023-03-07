//
// Created by Ilinca on 28-Apr-22.
//

#include "Teste_fisiere.h"
#include "Repository.h"
#include <assert.h>

void test_adauga_fisier(){
    RepoFile repoF{"test_med1.txt"};
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"theraflu","theta","calciu",8.6};
    Medicament med4{"borenar","delta","sodiu",9};
    Medicament med5{ "xyzal","alfa","zinc",27 };
    Medicament med6{"acutan","omega","fier",55};

    repoF.store(med1);
    assert(repoF.get_all_medicamente().size() == 1);
    try {
        repoF.store(med1);
        assert(false);
    }
    catch (Repo_Exception& re) {
        assert(true);
    }
    assert(repoF.get_all_medicamente().size() == 1);
    repoF.store(med2);
    assert(repoF.get_all_medicamente().size() == 2);
    RepoFile repo_load{"test_med1.txt"};
    assert(repo_load.get_all_medicamente().size() == 2);

    repoF.stergere_repo(med2);
    assert(repoF.get_all_medicamente().size() == 1);
    try {
        repoF.stergere_repo(med2);
        assert(false);
    }
    catch (Repo_Exception& re) {
        assert(re.get_error_message() == "Medicamentul nu este in lista.\n");
    }
    assert(repoF.get_all_medicamente().size() == 1);
    repoF.stergere_repo(med1);
    assert(repoF.get_all_medicamente().size() == 0);

    repoF.store(med4);
    repoF.modificare_pret_repo(med4);
    assert(repoF.get_all_medicamente().size() == 1);
    assert(repoF.get_all_medicamente()[0].get_producator() == "delta");

}

void test_load_fisier() {
    RepoFile repoF{"cmake-build-debug-coverage/test_med1.txt"};
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"theraflu","theta","calciu",8.6};
    Medicament med4{"borenar","delta","sodiu",9};
    Medicament med5{ "xyzal","alfa","zinc",27 };
    Medicament med6{"acutan","omega","fier",55};

    repoF.store(med1);
    repoF.store(med2);
    RepoFile repoF_load{ "cmake-build-debug-coverage/test_med1.txt" };
    assert(repoF_load.get_all_medicamente().size() == 2);

    repoF.modificare_pret_repo(med2);


}

void test_sterge_fisier(){
    RepoFile repoF{"test_med1.txt"};
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"theraflu","theta","calciu",8.6};
    Medicament med4{"borenar","delta","sodiu",9};
    Medicament med5{ "xyzal","alfa","zinc",27 };
    Medicament med6{"acutan","omega","fier",55};

    repoF.store(med1);
    repoF.store(med2);
    repoF.stergere_repo(med2);
    assert(repoF.get_all_medicamente().size() == 1);
    try {
        repoF.stergere_repo(med2);
        assert(false);
    }
    catch (Repo_Exception& re) {
        assert(true);
    }
    assert(repoF.get_all_medicamente().size() == 1);
    repoF.stergere_repo(med1);
    assert(repoF.get_all_medicamente().size() == 0);
}

void test_all_fisiere(){
    test_adauga_fisier();
//    test_load_fisier();
//    test_sterge_fisier();
}