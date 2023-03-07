#include <iostream>
#include "UI.h"
#include "Teste.h"
//#include "Pet.h"
//#include "teste_vector.h"
#include "Teste_reteta.h"
#include "Teste_fisiere.h"
using std::cout;
using std::endl;

//void test_all(){
//    teste_domain();
//    cout << "Finished domain tests." << endl;
//    teste_repo();
//    cout << "Finished repo tests." << endl;
//    teste_service();
//    cout << "Finished service tests." << endl;
//}

void start_app(){
//    cout << "Alegeti modul de afisare: 1-consola    2-fisier.\n";
//    cout << "Optiunea dumneavoastra este: ";
//    int cmd;
//    std::cin >> cmd;
//    if (cmd == 1)
//    {
//        Medicament_Repository repo;
//        Medicament_Validator val;
//        Medicamente_Service srv{repo, val};
//        Console ui{srv};
//        ui.run();
//    }
//
//    else {
//        RepoFile repo{ "med2.txt"};
//        Medicament_Validator val;
//        Medicamente_Service srv{repo, val};
//        Console ui{srv};
//        ui.run();
//    }
    //Medicament_Repository repo;
    //RepoFile repo{ "med2.txt"};
    RepositoryLaborator repo;
    Medicament_Validator val;
    Medicamente_Service srv{repo, val};
    Console ui{srv};
    ui.run();
}

int main() {
    test_all();
    //testAll<VectorDinamic<Pet>>();
    test_all_reteta();
    test_all_fisiere();
    start_app();


    return 0;
}
