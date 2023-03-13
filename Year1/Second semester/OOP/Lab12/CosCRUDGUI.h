#include "Reteta.h"

#include "Observer.h"
#include "Service.h"
#include <qwidget.h>
#include <qpushbutton.h>
#include <qtablewidget.h>
#include <qslider.h>
#include <qlayout>
#include <vector>

using std::vector;

class CosCRUDGUI : public QWidget, public Observer {
private:
    List& cos;
    Medicamente_Service& srv;
    QWidget* wndcos;
    QHBoxLayout* layout;
    QTableWidget* table;
    QSlider* slider;
    QPushButton* btnadd;
    QPushButton* btnempty;


    void initComponents();
    void connectSignals();

    //void populateTable(QTableWidget* table, const vector<Produs>& all);
    void populateTable(QTableView* table, const vector<Medicament>& all);
public:
    explicit CosCRUDGUI(List& cos, Medicamente_Service& srv) :cos{ cos }, srv{ srv }{
        wndcos = new QWidget;
        layout = new QHBoxLayout;
        btnadd = new QPushButton("GENERARE MEDICAMENTE RANDOM");
        btnempty = new QPushButton("GOLESTE RETETA");
        slider = new QSlider;
        table=new QTableWidget(0,4);
        

    };
    //CosCRUDGUI(List& cos,ProdService& srv);
    void run();

    void update() override;

    ~CosCRUDGUI() {
        this->cos.removeObserver(this);
    }
};