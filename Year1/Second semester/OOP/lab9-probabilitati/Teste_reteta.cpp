//
// Created by Ilinca on 25-Apr-22.
//

#include "Teste_reteta.h"
#include <assert.h>
#include "Service.h"
#include "Reteta.h"


void test_reteta(){
    List teste;
    Medicament med1{"coldrex","alfa","calciu", 90};
    Medicament med2{"fervex","beta","sodiu", 16};
    teste.addList(med1);
    teste.addList(med2);
    assert(teste.getallfromList().size() == 2);
    teste.emptyList();
    assert(teste.getallfromList().size() == 0);
}

void teste_reteta_service(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{ test_repo,test_val };

    test_service.add_medicament("fervex","beta","ibuprofen",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9.5);
    test_service.add_medicament("theraflu","omega","calciu",3.8);
    test_service.add_medicament("borenar","oli","mg",7);

    test_service.add_random_service(4);
    assert(test_service.get_all_from_list_service().size() == 4);
    test_service.empty_list_service();
    assert(test_service.get_all_from_list_service().size() == 0);

    test_service.add_random_service(20);
    //putem adauga doar 4 produse (fara sa se repete)
    assert(test_service.get_all_from_list_service().size() == 4);

    test_service.empty_list_service();
    test_service.add_list_service("fervex");
    assert(test_service.get_all_from_list_service().size() == 1);

    try{
        test_service.add_list_service("algc");
        assert(false);
    }
    catch (Repo_Exception&) {
        assert(true);
    }


}

void test_all_reteta(){
    test_reteta();
    teste_reteta_service();
}