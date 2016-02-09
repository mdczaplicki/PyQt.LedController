#include "ledcontroller.h"
#include "ui_ledcontroller.h"

LEDController::LEDController(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::LEDController)
{
    ui->setupUi(this);
    tray = new QSystemTrayIcon(this);
    tray->setIcon(QIcon(":/Other files/icon.png"));
    tray->show();

//    ui->horizontalSlider->setStyleSheet("QSlider::handle:horizontal {"
//                                            "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);"
//                                            "border: 1px solid #5c5c5c;"
//                                            "width: 18px;"
//                                            "margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */"
//                                            "border-radius: 3px;"
//                                            "}QSlider::add-page:horizontal {    background: white;}QSlider::sub-page:horizontal {    background: pink;}");
}

LEDController::~LEDController()
{
    delete ui;
}
