#pragma once
#include <QtWidgets/QApplication>
#include <QWindow>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QWidget>
#include <QListWidget>
#include <QTableWidget>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QGroupBox>
#include <QFormLayout>
#include "Service.h"
#include <QMessageBox>
#include <string>
#include <set>
#include <vector>
#include <QDebug>
#include <QPainter>
#include <cstdlib>
using std::to_string;
using std::set;
using std::vector;



class RetetaGUI : public QWidget  {
private:
	Medicamente_Service& srv;

	QHBoxLayout* lyMain;
	QListWidget* medList;

	QLabel* lblDenumire;
	QLabel* lblProducator;
	QLineEdit* editDenumire;
	QLineEdit* editProducator;


	QPushButton* btnAdd;
	QPushButton* btnGenerate;
	QPushButton* btnEmpty;
	QPushButton* btnExport;

	QLineEdit* editNoSlider;
	QLabel* lblSlider;
	QSlider* sliderGenerate;

	void initGUI();
	void connectSignalsSlots();

	void reloadReteta();
	void addToReteta();

public:
	RetetaGUI(Medicamente_Service& medStore) : srv{ medStore } {
		initGUI();
		connectSignalsSlots();
	}


};