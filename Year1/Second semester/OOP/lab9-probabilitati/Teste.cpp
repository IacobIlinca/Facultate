//
// Created by Ilinca on 30-Mar-22.
//

#include "Teste.h"
#include "Service.h"
#include <assert.h>


void test_get_set(){
    Medicament med1{"algocalmin", "beta", "antianalgezic",10.0};
    assert(med1.get_denumire() == "algocalmin");
    assert(med1.get_producator() == "beta");
    assert(med1.get_substanta_activa() == "antianalgezic");
    assert(med1.get_pret() == 10.0);

    Medicament med2{"parasinus", "alfa","paracetamol", 2.5};
    assert(med2.get_denumire() == "parasinus");
    assert(med2.get_producator() == "alfa");
    assert(med2.get_substanta_activa() == "paracetamol");
    assert(med2.get_pret() == 2.5);

    med2.set_denumire("ibuprofen");
    med2.set_producator("theta");
    med2.set_substanta_activa("fervex");
    med2.set_pret(3.8);

    assert(med2.get_denumire() == "ibuprofen");
    assert(med2.get_producator() == "theta");
    assert(med2.get_substanta_activa() == "fervex");
    assert(med2.get_pret() == 3.8);
}

void test_add_repo(){
    Medicament_Repository test_repo;
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    test_repo.store(med1);
    assert(test_repo.get_all_medicamente().size() == 1);

    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"fervex","beta","calciu",8.6};

    try{
        test_repo.store(med3);
        assert(false);
    }
    catch(Repo_Exception){
        assert(true);
    }
}

void test_find_repo(){
    Medicament_Repository test_repo;
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"theraflu","theta","calciu",8.6};
    test_repo.store(med1);
    test_repo.store(med2);

    assert(test_repo.exists(med1));
    assert(!test_repo.exists(med3));

    auto found_med = test_repo.find("fervex", "beta");
    assert(found_med.get_denumire() == "fervex");
    assert(found_med.get_producator() == "beta");
    assert(found_med.get_substanta_activa() == "ibuprofen");

    try{
        test_repo.find("parasinus","omega");
        assert(false);
    }
    catch (Repo_Exception& ve){
        assert(ve.get_error_message()=="Medicamentul pe care il cautati nu exista.");
    }


}

void test_find_service(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","ibuprofen",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9.5);
    test_service.add_medicament("theraflu","omega","calciu",3.8);

    assert(test_service.get_all_medicamente().size() == 3);
    Medicament med;
    med = test_service.find_service("fervex", "beta");
    assert(med.get_substanta_activa() == "ibuprofen");

}

void test_find_denumire_repo(){
    Medicament_Repository test_repo;
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"theraflu","theta","calciu",8.6};
    test_repo.store(med1);
    test_repo.store(med2);

    assert(test_repo.exists(med1));
    assert(!test_repo.exists(med3));

    auto found_med = test_repo.find_denumire("fervex");
    assert(found_med.get_denumire() == "fervex");
    assert(found_med.get_producator() == "beta");
    assert(found_med.get_substanta_activa() == "ibuprofen");

    try{
        test_repo.find_denumire("nurofen");
        assert(false);
    }
    catch (Repo_Exception& ve){
        assert(ve.get_error_message()=="Medicamentul cu denumirea nurofen nu este in lista");
    }

}

void test_add_medicament_service(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","ibuprofen",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9.5);
    test_service.add_medicament("theraflu","omega","calciu",3.8);

    assert(test_service.get_all_medicamente().size() == 3);
    try{
        test_service.add_medicament("fervex","beta","ibuprofen",89.7);
        assert(false);
    }
    catch(Repo_Exception&){
        assert(true);
    }

    try{
        test_service.add_medicament("emetix","kapa","algocalmin",12.8);
        assert(true);
    }
    catch(Validation_Exception&) {
        assert(false);
    }

    try{
        test_service.add_medicament("","beta","ibuprofen",89.7);
        assert(false);
    }
    catch(Validation_Exception& ){
        assert(true);
    }

    try{
        test_service.add_medicament("acc","","ibuprofen",89.7);
        assert(false);
    }
    catch (Validation_Exception&){
        assert(true);
    }

    try{
        test_service.add_medicament("acc","beta","",89.7);
        assert(false);
    }
    catch (Validation_Exception&){
        assert(true);
    }

    try{
        test_service.add_medicament("acc","beta","ibuprofen",-89.7);
        assert(false);
    }
    catch (Validation_Exception&){
        assert(true);
    }

}

void test_modificare_repo(){
    Medicament_Repository test_repo;
    Medicament med1{"fervex", "alfa", "calciu",23.7};
    test_repo.store(med1);
    assert(test_repo.get_all_medicamente().size()==1);
    Medicament med2{"fervex","alfa", "calciu",21};
    test_repo.modificare_pret_repo(med2);
    assert(test_repo.find("fervex","alfa").get_pret() == 21);
    Medicament med3{"coldrex","beta","sodiu",13};
    try{
        test_repo.modificare_pret_repo(med3);
        assert(false);
    }
    catch (Repo_Exception& re) {
        assert(true);
    }
}

void test_modificare_service(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","ibuprofen",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9.5);
    test_service.add_medicament("theraflu","omega","calciu",3.8);

    test_service.modifica_pret_service("fervex","beta","ibuprofen", 7);
    assert(test_service.get_all_medicamente()[0].get_pret() == 7);

}

void test_stergere_repo(){
    Medicament_Repository test_repo;
    Medicament med1{"coldrex", "alfa","calciu",34.8};
    test_repo.store(med1);
    assert(test_repo.get_all_medicamente().size() == 1);

    Medicament med2{"fervex", "beta","sodiu",13};
    test_repo.store(med2);
    assert(test_repo.get_all_medicamente().size()==2);
    test_repo.stergere_repo(med2);
    assert(test_repo.get_all_medicamente().size() == 1);

    try{
        test_repo.stergere_repo(med2);
        assert(false);
    }
    catch (Repo_Exception& re){
        assert(true);
    }

}

void test_stergere_service() {
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","ibuprofen",7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9.5);
    test_service.add_medicament("theraflu","omega","calciu",3.8);

    assert(test_service.get_all_medicamente().size() == 3);
    test_service.stergere_service("fervex","beta","ibuprofen", 7);
    assert(test_service.get_all_medicamente().size() == 2);

}

void test_filtrare_service(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","calciu",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9);
    test_service.add_medicament("theraflu","omega","calciu",9);


    vector<Medicament> rezultat;
    rezultat = test_service.filtrare_substanta_activa("calciu");
    assert(rezultat.size() == 2);

    vector<Medicament> rezultat2;
    rezultat2 = test_service.filtrare_pret(9);
    assert(rezultat.size() == 2);

}

void test_sort_service(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","calciu",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9);
    test_service.add_medicament("theraflu","omega","calciu",9);

    auto first = test_service.sortdenumire(0)[0];
    assert(first.get_producator() == "alfa");

    first = test_service.sortdenumire(1)[1];
    assert(first.get_substanta_activa() == "calciu");

    first = test_service.sortproducator(0)[0];
    assert(first.get_denumire() == "coldrex");

    first = test_service.sortproducator(1)[0];
    assert(first.get_substanta_activa() == "calciu");

    first = test_service.sortdsubstpret(0)[0];
    assert(first.get_denumire() == "theraflu");

    first = test_service.sortdsubstpret(1)[0];
    assert(first.get_denumire() == "coldrex");

}

void test_all_of(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    test_service.add_medicament("fervex","beta","calciu",89.7);
    test_service.add_medicament("fervex","alfa","paracetamol",9);
    test_service.add_medicament("fervex","omega","calciu",9);

    int rez = test_service.all_of_denumire_incepe_cu_a("fervex");
    assert(rez == 1);

    test_service.add_medicament("coldrex","omega","calciu",9);
    int rez2 = test_service.all_of_denumire_incepe_cu_a("fervex");
    assert(rez2 == 0);
}

void test_undo(){
    Medicament_Repository test_repo;
    Medicament_Validator test_val;
    Medicamente_Service test_service{test_repo, test_val};

    try {
        test_service.undo();
        assert(false);
    }
    catch (UndoException& ue) {
        assert(true);
        assert(ue.get_msg() == "Nu se poate da undo!\n");
    }

    test_service.add_medicament("fervex","beta","calciu",89.7);
    test_service.add_medicament("coldrex","alfa","paracetamol",9);
    test_service.add_medicament("theraflu","omega","calciu",9);

    assert(test_service.get_all_medicamente().size() == 3);
    test_service.undo();
    assert(test_service.get_all_medicamente().size() == 2);

    test_service.add_medicament("alg","theta","zinc",12);
    test_service.stergere_service("alg","theta","zinc",12);
    test_service.undo();
    assert(test_service.get_all_medicamente().size() == 3);
    assert(test_service.get_dim_undo() == 3);

    test_service.modifica_pret_service("fervex","beta","calciu",50);
    test_service.undo();

}

void teste_fisier(){
    RepoFile repoF{"teste.txt"};
    Medicament med1{"fervex","beta","ibuprofen",5.9};
    Medicament med2{ "coldrex","alfa","paracetamol",2.7 };
    Medicament med3{"theraflu","theta","calciu",8.6};
    Medicament med4{"borenar","delta","sodiu",9};
    Medicament med5{ "xyzal","alfa","zinc",27 };
    Medicament med6{"acutan","omega","fier",55};

    //test adauga
    repoF.store(med1);
    assert(repoF.get_all_medicamente().size() == 1);
    try {
        repoF.store(med1);
        assert(false);
    }
    catch (Repo_Exception& re) {
        //std::cout<<re.get_error_message();
        assert(true);
    }
    assert(repoF.get_all_medicamente().size() == 1);
    repoF.store(med2);
    assert(repoF.get_all_medicamente().size() == 2);


    //teste load
    RepoFile repoF_load{ "test.txt" };
    assert(repoF_load.get_all_medicamente().size() == 2);


}

void test_all(){

    test_get_set();

    test_find_repo();
    test_find_denumire_repo();
    test_find_service();

    test_add_repo();
    test_add_medicament_service();

    test_modificare_repo();
    test_modificare_service();

    test_stergere_repo();
    test_stergere_service();

    test_filtrare_service();
    test_sort_service();

    test_undo();

    //teste_fisier();

    test_all_of();

}