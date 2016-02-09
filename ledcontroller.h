#ifndef LEDCONTROLLER_H
#define LEDCONTROLLER_H

#include <QMainWindow>
#include <QSystemTrayIcon>

namespace Ui {
class LEDController;
}

class LEDController : public QMainWindow
{
    Q_OBJECT

public:
    explicit LEDController(QWidget *parent = 0);
    ~LEDController();
    QSystemTrayIcon * tray;

private:
    Ui::LEDController *ui;
};

#endif // LEDCONTROLLER_H
