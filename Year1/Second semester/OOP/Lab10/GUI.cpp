#include "GUI.h"

void GUI::initializeGUIComponents() {
	//impartim fereastra in 2: in stanga, butoane+labels+qlineedits
	//iar in dreapta: tabelul cu melodii

	//"stanga" si "dreapta" pentru ca este QHBoxLayout
	//se adauga componente incepand din stanga, pe orizontala
	//aici: "left" component, then "right" component
	//care la randul lor contin alte componente

	//main layout
	QHBoxLayout* lyMain = new QHBoxLayout;
	this->setLayout(lyMain);

	//left part of the window
	//pentru aceasta parte setam layout vertical
	QWidget* left = new QWidget;
	QVBoxLayout* lyLeft = new QVBoxLayout;
	left->setLayout(lyLeft);

	//componente pentru functionalitatea de adaugare a unei melodii
	//folosim un QFormLayout pentru detaliile de adaugare a unei melodii
	QWidget* form = new QWidget;
	QFormLayout* lyForm = new QFormLayout;
	form->setLayout(lyForm);
	editDenumire = new QLineEdit;
	editProducator = new QLineEdit;
	editSubstActiv = new QLineEdit;
	editPret = new QLineEdit;

	lyForm->addRow(lblDenumire, editDenumire);
	lyForm->addRow(lblProducator, editProducator);
	lyForm->addRow(lblSubstActiv, editSubstActiv);
	lyForm->addRow(lblPret, editPret);
	btnAddMedicament = new QPushButton("Adauga medicament");
	lyForm->addWidget(btnAddMedicament);
	btnModificare = new QPushButton("Modifica medicament");
	lyForm->addWidget(btnModificare);



	//adaugam toate componentele legate de adaugare medicament
	//in layout-ul care corespunde partii din stanga a ferestrei

	lyLeft->addWidget(form);

	QWidget* formStergere = new QWidget;
	QFormLayout* lyFormStergere = new QFormLayout;
	formStergere->setLayout(lyFormStergere);
	editStergere = new QLineEdit();
	btnStergere = new QPushButton("Sterge medicament");
	lyFormStergere->addRow(lblStergere, editStergere);
	lyFormStergere->addWidget(btnStergere);
	lyLeft->addWidget(formStergere);

	//Radio Buttons: ne ajuta cand trebuie sa selectam doar o 
	//optiune din mai multe (doar un RadioButton poate fi selectat
	//la un moment dat)


	//vs. CheckBox (see documentation)
	//also see documentation on QGroupBox, QRadioButton pentru detalii

	//cream un GroupBox pentru radiobuttons care corespund 
	//criteriilor de sortare pe care le avem (dupadenumire/producator/substanta activa+pret.) 
	//+ butonul de sortare

	QVBoxLayout* lyRadioBox = new QVBoxLayout;
	this->groupBox->setLayout(lyRadioBox);
	lyRadioBox->addWidget(radioSrtDenumire);
	lyRadioBox->addWidget(radioSrtProducator);
	lyRadioBox->addWidget(radioSrtSubstPret);

	btnSortMedicamente = new QPushButton("Sorteaza medicamente");
	lyRadioBox->addWidget(btnSortMedicamente);


	//adaugam acest grup in partea stanga, 
	//dupa componentele pentru adaugare in layout-ul vertical
	lyLeft->addWidget(groupBox);

	//cream un form pentru filtrarea dupa substanta_activa
	QWidget* formFilter = new QWidget;
	QFormLayout* lyFormFilter = new QFormLayout;
	formFilter->setLayout(lyFormFilter);
	editFilterSubstActiv = new QLineEdit();
	editFilterPret = new QLineEdit();
	lyFormFilter->addRow(lblFilterCriteria, editFilterSubstActiv);
	btnFilterMedicamente = new QPushButton("Filtreaza medicamentele dupa substanta activa");
	lyFormFilter->addWidget(btnFilterMedicamente);
	lyFormFilter->addRow(lblFilterCriteriaPret, editFilterPret);
	btnFilterMedicamentePret = new QPushButton("Filtreaza medicamentele dupa pret");
	lyFormFilter->addWidget(btnFilterMedicamentePret);



	lyLeft->addWidget(formFilter);
	btnUndo = new QPushButton("Undo");
	lyLeft->addWidget(btnUndo);
	//Buton folosit pentru a reincarca datele
	//i.e. afisam toate melodiile in tabel, in ordinea initiala din fisier
	btnReloadData = new QPushButton("Reload data");
	lyLeft->addWidget(btnReloadData);

	//componenta right - contine doar tabelul cu medicamente
	QWidget* right = new QWidget;
	QVBoxLayout* lyRight = new QVBoxLayout;
	right->setLayout(lyRight);


	int noLines = 10;
	int noColumns = 4;
	this->tableMedicamente = new QTableWidget{ noLines, noColumns };

	//setam header-ul tabelului
	QStringList tblHeaderList;
	tblHeaderList << "Denumire" << "Producator" << "Substanta activa" << "Pret";
	this->tableMedicamente->setHorizontalHeaderLabels(tblHeaderList);

	//optiune pentru a se redimensiona celulele din tabel in functie de continut
	this->tableMedicamente->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);

	lyRight->addWidget(tableMedicamente);

	
	widgetDynamic = new QWidget{};
	lyBtnDynamic = new QVBoxLayout{};
	widgetDynamic->setLayout(lyBtnDynamic);
	reloadDynamicButtons();


	int noLines2 = 10;
	int noColumns2 = 4;
	this->tableMeds = new QTableWidget{ noLines2, noColumns2 };


	//setam header-ul tabelului
	QStringList tblHeaderList2;
	tblHeaderList2 << "Denumire" << "Producator" << "Substanta activa" << "Pret";
	this->tableMeds->setHorizontalHeaderLabels(tblHeaderList2);

	//optiune pentru a se redimensiona celulele din tabel in functie de continut
	this->tableMeds->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
	btnReteta = new QPushButton{ "Open reteta" };
	lyLeft->addWidget(btnReteta);
	lyRight->addWidget(tableMeds);

	lyMain->addWidget(left);
	lyMain->addWidget(widgetDynamic);
	lyMain->addWidget(right);
	lyMain->addWidget(widgetDynamic);
	


}

set<string> GUI::getProducatori(const vector<Medicament>& all_medicamente) {
	set<string> producatori;

	for (const auto& med : all_medicamente) {
		producatori.insert(med.get_producator());
	}
	return producatori;
}

void clearLayout(QLayout* layout) {
	if (layout == NULL)
		return;
	QLayoutItem* item;
	while ((item = layout->takeAt(0))) {
		if (item->layout()) {
			clearLayout(item->layout());
			delete item->layout();
		}
		if (item->widget()) {
			delete item->widget();
		}
		delete item;
	}
}

int howManyWithProducator(const vector<Medicament>& all_medicamente, string producator) {
	int noProd = count_if(all_medicamente.begin(), all_medicamente.end(), [&](Medicament med) {
		return med.get_producator() == producator;
		});
	return noProd;
}

void GUI::reloadDynamicButtons() {
	clearLayout(this->lyBtnDynamic);
	const vector<Medicament>& all_medicamente = this->srv.get_all_medicamente();
	set<string> producatori = this->getProducatori(all_medicamente);

	for (string prod : producatori) {
		QPushButton* btn = new QPushButton{ QString::fromStdString(prod) };
		lyBtnDynamic->addWidget(btn);
		int howMany = howManyWithProducator(all_medicamente, prod);
		QObject::connect(btn, &QPushButton::clicked, [prod, howMany]() {
			QMessageBox::information(nullptr, "Info", QString::fromStdString("Medicamente cu producatorul " + prod + " : " + to_string(howMany)));
			});
	}
}


void GUI::reloadMedicamenteList(vector<Medicament> medicamente) {
	this->tableMedicamente->clearContents();
	this->tableMedicamente->setRowCount(medicamente.size());

	int lineNumber = 0;
	for (auto& med : medicamente) {
		this->tableMedicamente->setItem(lineNumber, 0, new QTableWidgetItem(QString::fromStdString(med.get_denumire())));
		this->tableMedicamente->setItem(lineNumber, 1, new QTableWidgetItem(QString::fromStdString(med.get_producator())));
		this->tableMedicamente->setItem(lineNumber, 2, new QTableWidgetItem(QString::fromStdString(med.get_substanta_activa())));
		this->tableMedicamente->setItem(lineNumber, 3, new QTableWidgetItem(QString::number(med.get_pret())));
		lineNumber++;
	}
}


void GUI::connectSignalsSlots() {
	QObject::connect(btnAddMedicament, &QPushButton::clicked, this, &GUI::guiAddMedicament);
	QObject::connect(btnStergere, &QPushButton::clicked, this, &GUI::guiStergereMedicament);
	QObject::connect(btnModificare, &QPushButton::clicked, this, &GUI::guiModificareMedicament);
	QObject::connect(btnSortMedicamente, &QPushButton::clicked, [&]() {
		if (this->radioSrtDenumire->isChecked())
			this->reloadMedicamenteList(srv.sortdenumire(0));
		else if (this->radioSrtProducator->isChecked())
			this->reloadMedicamenteList(srv.sortproducator(0));
		else if (this->radioSrtSubstPret->isChecked())
			this->reloadMedicamenteList(srv.sortdsubstpret(0));
		});

	QObject::connect(btnFilterMedicamente, &QPushButton::clicked, [&]() {
		string filterC = this->editFilterSubstActiv->text().toStdString();
		this->reloadMedicamenteList(srv.filtrare_substanta_activa(filterC));

		}
	);
	QObject::connect(btnFilterMedicamentePret, &QPushButton::clicked, [&]() {
		double filterC = this->editFilterPret->text().toDouble();
		this->reloadMedicamenteList(srv.filtrare_pret(filterC));

		}
	);
	

	QObject::connect(btnReloadData, &QPushButton::clicked, [&]() {
		this->reloadMedicamenteList(srv.get_all_medicamente());
		});

	QObject::connect(btnUndo, &QPushButton::clicked, [&]() {
		srv.undo();
		this->reloadMedicamenteList(srv.get_all_medicamente());
		});

	
}

void GUI::guiAddMedicament() {
	try {
		//preluare detalii din QLineEdit-uri
		string denumire = editDenumire->text().toStdString();
		string producator = editProducator->text().toStdString();
		string substanta_activa = editSubstActiv->text().toStdString();
		double pret = editPret->text().toDouble();

		//golim QLineEdit-urile dupa apasarea butonului
		editDenumire->clear();
		editProducator->clear();
		editSubstActiv->clear();
		editPret->clear();

		this->srv.add_medicament(denumire, producator, substanta_activa, pret);
		this->reloadMedicamenteList(this->srv.get_all_medicamente());

		//afisam un mesaj pentru a anunta utilizatorul ca melodia s-a adaugat
		QMessageBox::information(this, "Info", QString::fromStdString("Medicament adaugat cu succes."));

	}
	catch (Repo_Exception& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.get_error_message()));
	}
	reloadDynamicButtons();
}


void GUI::guiStergereMedicament() {
		string denumire = editStergere->text().toStdString();
		//string producator = editProducator->text().toStdString();
		//string substanta_activa = editSubstActiv->text().toStdString();
		//double pret = editPret->text().toDouble();

		//golim QLineEdit-urile dupa apasarea butonului
		editStergere->clear();

		this->srv.stergere_dupa_denumire(denumire);
		this->reloadMedicamenteList(this->srv.get_all_medicamente());

		//afisam un mesaj pentru a anunta utilizatorul ca melodia s-a adaugat
		QMessageBox::information(this, "Info", QString::fromStdString("Medicament sters cu succes."));
	
		reloadDynamicButtons();

}

void GUI::guiModificareMedicament() {
	try {
		//preluare detalii din QLineEdit-uri
		string denumire = editDenumire->text().toStdString();
		string producator = editProducator->text().toStdString();
		string substanta_activa = editSubstActiv->text().toStdString();
		double pret_nou = editPret->text().toDouble();

		//golim QLineEdit-urile dupa apasarea butonului
		editDenumire->clear();
		editProducator->clear();
		editSubstActiv->clear();
		editPret->clear();

		this->srv.modifica_pret_service(denumire, producator, substanta_activa, pret_nou);
		this->reloadMedicamenteList(this->srv.get_all_medicamente());

		//afisam un mesaj pentru a anunta utilizatorul ca melodia s-a adaugat
		QMessageBox::information(this, "Info", QString::fromStdString("Medicament modificat cu succes."));

	}
	catch (Repo_Exception& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.get_error_message()));
	}
	reloadDynamicButtons();
}