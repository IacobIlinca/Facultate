#pragma once
#include <vector>
#include <string>
#include <set>
#include <cstdlib>
#include <QtWidgets/QApplication>
#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QFormLayout>
#include <QLineEdit>
#include <QTableWidget>
#include <QMessageBox>
#include <QHeaderView>
#include <QGroupBox>
#include <QListWidget>
#include <QComboBox>
#include <QRadioButton>
#include "Service.h"

using std::set;
using std::vector;
using std::string;
using std::to_string;

class GUI : public QWidget {
private:

	Medicamente_Service& srv;
	
	QLabel* lblDenumire = new QLabel{ "Denumire:" };
	QLabel* lblProducator = new QLabel{ "Producator:" };
	QLabel* lblSubstActiv = new QLabel{ "Substanta activa:" };
	QLabel* lblPret = new QLabel{ "Pret:" };

	QLineEdit* editDenumire;
	QLineEdit* editProducator;
	QLineEdit* editSubstActiv;
	QLineEdit* editPret;

	QPushButton* btnAddMedicament;
	QPushButton* btnModificare;

	QLabel* lblStergere = new QLabel{ "Denumire: " };
	QLineEdit* editStergere;
	QPushButton* btnStergere;

	QGroupBox* groupBox = new QGroupBox(tr("Sortare"));

	QRadioButton* radioSrtDenumire = new QRadioButton(QString::fromStdString("Nume"));
	QRadioButton* radioSrtProducator = new QRadioButton(QString::fromStdString("Producator"));
	QRadioButton* radioSrtSubstPret = new QRadioButton(QString::fromStdString("Substanta activa+Pret"));
	QPushButton* btnSortMedicamente;

	QLabel* lblFilterCriteria = new QLabel{ "Dupa ce se va face filtrarea:" };
	QLabel* lblFilterCriteriaPret = new QLabel{ "Dupa ce pret se va face filtrarea:" };
	QLineEdit* editFilterSubstActiv;
	QLineEdit* editFilterPret;
	QPushButton* btnFilterMedicamente;
	QPushButton* btnFilterMedicamentePret;
	QPushButton* btnUndo;
	QPushButton* btnReloadData;

	QTableWidget* tableMedicamente;

	QWidget* widgetDynamic;
	QVBoxLayout* lyBtnDynamic;

	//QTableWidget* tableMeds;
	//QPushButton* btnReteta;

	QWidget* wndreteta, * random;
	QWidget* leftreteta, * rightreteta, * formreteta;
	QVBoxLayout* lyleftreteta, * lyrightreteta;
	QHBoxLayout* layoutreteta, * lyrandomreteta;
	QFormLayout *lyexportreteta;
	QFormLayout* lyformreteta;
	QLabel* lblnumereteta, * lblprodreteta;
	QLineEdit* txtnumereteta;
	QPushButton* btnadd, * btnrandom, * btnempty, * btnexport;
	QComboBox* randombox;
	QListWidget* prodlist;
	QPushButton* meniureteta, * btnFindProd;


	QWidget* formfilter, * formexport, * butoane;
	QFormLayout* lyformfilter, * lyformexport;
	QLabel* lblfilter, * lblexport;
	QLineEdit* txtfilter, * txtexport;

	void reloadDynamicButtons();

	void initializeGUIComponents();

	void connectSignalsSlots();


	void reloadMedicamenteList(vector<Medicament> medicamente);
	set<string> getProducatori(const vector<Medicament>& all_medicamente);
	

public:
	GUI(Medicamente_Service& Medsrv) : srv{ Medsrv } {
		initializeGUIComponents();
		connectSignalsSlots();
		reloadMedicamenteList(srv.get_all_medicamente());

	}

	void guiAddMedicament();
	void guiStergereMedicament();
	void guiModificareMedicament();

	void reloaddata();

};