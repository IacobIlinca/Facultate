#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Lab10visual.h"

class Lab10visual : public QMainWindow
{
    Q_OBJECT

public:
    Lab10visual(QWidget *parent = Q_NULLPTR);

private:
    Ui::Lab10visualClass ui;
};
