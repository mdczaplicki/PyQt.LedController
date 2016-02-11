# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LedController.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import linecache
import serial
import sys
import time

PORT = "COM3"
BAUDRATE = 57600
BYTESIZE = serial.EIGHTBITS

RED = 0
GREEN = 0
BLUE = 0


def __except__():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    __show_warning__("Error", "Exception in file:\n%s\nLine number: %i\n%s\nException type: %s" %
                     (filename, lineno, line.strip(), exc_obj))


def __show_warning__(title, text):
    message_box = QtWidgets.QMessageBox()
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.exec_()


# noinspection PyAttributeOutsideInit
class UiLEDController(object):
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.port = PORT
        self.ser.baudrate = BAUDRATE
        self.ser.bytesize = BYTESIZE
        # self.worker = AThread()

    def setup_ui(self, led_controller):
        led_controller.setObjectName("led_controller")
        led_controller.resize(230, 160)
        led_controller.setWindowIcon(QtGui.QIcon("icon.png"))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(led_controller.sizePolicy().hasHeightForWidth())
        led_controller.setSizePolicy(size_policy)
        led_controller.setMinimumSize(QtCore.QSize(230, 160))
        led_controller.setMaximumSize(QtCore.QSize(230, 160))
        self.central_widget = QtWidgets.QWidget(led_controller)
        self.central_widget.setObjectName("central_widget")
        self.mode_box = QtWidgets.QComboBox(self.central_widget)
        self.mode_box.setGeometry(QtCore.QRect(10, 10, 211, 22))
        self.mode_box.setObjectName("mode_box")
        self.mode_box.addItem("")
        self.mode_box.addItem("")
        self.mode_box.addItem("")
# region Sliders
        self.bright_slider = QtWidgets.QSlider(self.central_widget)
        self.bright_slider.setGeometry(QtCore.QRect(70, 40, 150, 20))
        self.bright_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bright_slider.setMaximum(255)
        self.bright_slider.setObjectName("bright_slider")
        self.red_slider = QtWidgets.QSlider(self.central_widget)
        self.red_slider.setGeometry(QtCore.QRect(70, 70, 150, 20))
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setMaximum(254)
        self.red_slider.setObjectName("red_slider")
        self.green_slider = QtWidgets.QSlider(self.central_widget)
        self.green_slider.setGeometry(QtCore.QRect(70, 100, 150, 20))
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setMaximum(254)
        self.green_slider.setObjectName("green_slider")
        self.blue_slider = QtWidgets.QSlider(self.central_widget)
        self.blue_slider.setGeometry(QtCore.QRect(70, 130, 150, 20))
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setMaximum(254)
        self.blue_slider.setObjectName("blue_slider")
# endregion
# region Labels
        self.bright_label = QtWidgets.QLabel(self.central_widget)
        self.bright_label.setGeometry(QtCore.QRect(10, 40, 55, 20))
        self.bright_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bright_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bright_label.setObjectName("bright_label")
        self.red_label = QtWidgets.QLabel(self.central_widget)
        self.red_label.setGeometry(QtCore.QRect(10, 70, 55, 20))
        self.red_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.red_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.red_label.setObjectName("red_label")
        self.green_label = QtWidgets.QLabel(self.central_widget)
        self.green_label.setGeometry(QtCore.QRect(10, 100, 55, 20))
        self.green_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.green_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.green_label.setObjectName("green_label")
        self.blue_label = QtWidgets.QLabel(self.central_widget)
        self.blue_label.setGeometry(QtCore.QRect(10, 130, 55, 20))
        self.blue_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blue_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.blue_label.setObjectName("blue_label")
# endregion
        self.pick_button = QtWidgets.QPushButton(self.central_widget)
        self.pick_button.setGeometry(QtCore.QRect(10, 130, 20, 20))
        self.pick_button.setText("")
        self.pick_button.setIcon(QtGui.QIcon("picker.png"))
        self.pick_button.setObjectName("pick_button")
        led_controller.setCentralWidget(self.central_widget)

        self.retranslate_ui(led_controller)
        self.mode_box.setCurrentIndex(0)
        self.mode_box.currentIndexChanged['int'].connect(self.connect_ino)
        self.blue_slider.valueChanged.connect(self.change_color)
        self.green_slider.valueChanged.connect(self.change_color)
        self.bright_slider.valueChanged.connect(self.change_color)
        self.red_slider.valueChanged.connect(self.change_color)
        self.pick_button.released.connect(self.test)
        QtCore.QMetaObject.connectSlotsByName(led_controller)

        self.tray = QtWidgets.QSystemTrayIcon(self.central_widget)
        self.tray.setIcon(QtGui.QIcon("icon.png"))
        self.tray.show()

    # noinspection PyTypeChecker,PyArgumentList
    def retranslate_ui(self, led_controller):
        _translate = QtCore.QCoreApplication.translate
        led_controller.setWindowTitle(_translate("led_controller", "Controller"))
        self.bright_label.setText(_translate("led_controller", "Brightness"))
        self.red_label.setText(_translate("led_controller", "Red"))
        self.green_label.setText(_translate("led_controller", "Green"))
        self.mode_box.setItemText(0, _translate("led_controller", "Off"))
        self.mode_box.setItemText(1, _translate("led_controller", "Manual"))
        self.mode_box.setItemText(2, _translate("led_controller", "Automatic"))
        self.blue_label.setText(_translate("led_controller", "Blue"))

    def connect_ino(self, selected):
        # TODO: clean this function
        try:
            # self.worker.start()
            if not selected:
                # OFF
                if self.ser.isOpen():
                    self.ser.write([0xff, 0, 0, 0])
                    self.ser.close()
            elif selected == 1:
                # MANUAL
                if not self.ser.isOpen():
                    self.ser.open()
                time.sleep(1.7)
                self.change_color(None)
            elif selected == 2:
                # AUTO
                if not self.ser.isOpen():
                    self.ser.open()
        except:
            __except__()

    def change_color(self, _):
        try:
            brightness = self.bright_slider.value()
            red = int(self.red_slider.value() * brightness / 255)
            green = int(self.green_slider.value() * brightness / 255)
            blue = int(self.blue_slider.value() * brightness / 255)
            print([0xff, red, green, blue])
            if self.ser.isOpen():
                self.ser.write([0xff, red, green, blue])
        except:
            __except__()

    def test(self):
        print("test")

