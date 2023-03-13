
#include "Lab10visual.h"
#include <QtWidgets/QApplication>
#include "GUI.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    //Medicament_Repository repo;
    RepoFile repo{ "med2.txt" };
    Medicament_Validator val;
    Medicamente_Service srv{ repo };
    GUI gui{ srv };
    gui.show();
    return a.exec();
}
