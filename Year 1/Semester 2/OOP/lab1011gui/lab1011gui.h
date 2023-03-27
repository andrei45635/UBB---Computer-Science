#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_lab1011gui.h"

class lab1011gui : public QMainWindow
{
    Q_OBJECT

public:
    lab1011gui(QWidget *parent = Q_NULLPTR);

private:
    Ui::lab1011guiClass ui;
};
