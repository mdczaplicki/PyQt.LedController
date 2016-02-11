from LEDController import UiLEDController, __except__
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, a=None):
        try:
            super().__init__(a)
            self.ui = UiLEDController()
            self.ui.setup_ui(self)
            self.ui.tray.activated.connect(self.__show__)
        except:
            __except__()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(None, "Quit?", "Are you sure you want to quit?",
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if self.ui.ser.isOpen():
                self.ui.ser.close()
            self.ui.tray.hide()
            event.accept()
        else:
            event.ignore()

    def hideEvent(self, event):
        self.hide()

    def __show__(self):
        self.show()
        self.showNormal()
        self.activateWindow()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = QtWidgets.QWidget(None, QtCore.Qt.Tool)
    LEDController = MyWindow(test)
    LEDController.show()
    sys.exit(app.exec_())
