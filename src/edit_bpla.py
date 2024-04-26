# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_bpla.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Edit(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(500, 430)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(245, 245, 245)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_EDIT_BPLA = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_EDIT_BPLA.setGeometry(QtCore.QRect(10, 10, 471, 331))
        self.groupBox_EDIT_BPLA.setMaximumSize(QtCore.QSize(16777215, 700))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.groupBox_EDIT_BPLA.setFont(font)
        self.groupBox_EDIT_BPLA.setObjectName("groupBox_EDIT_BPLA")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_EDIT_BPLA)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 451, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_MAX_TIME_FLIGHT = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_MAX_TIME_FLIGHT.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_MAX_TIME_FLIGHT.setObjectName("lineEdit_MAX_TIME_FLIGHT")
        self.gridLayout.addWidget(self.lineEdit_MAX_TIME_FLIGHT, 5, 1, 1, 1)
        self.lineEdit_MAX_DIST_POLET = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_MAX_DIST_POLET.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_MAX_DIST_POLET.setObjectName("lineEdit_MAX_DIST_POLET")
        self.gridLayout.addWidget(self.lineEdit_MAX_DIST_POLET, 6, 1, 1, 1)
        self.label_MAX_TIME_FLIGHT = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_MAX_TIME_FLIGHT.setFont(font)
        self.label_MAX_TIME_FLIGHT.setObjectName("label_MAX_TIME_FLIGHT")
        self.gridLayout.addWidget(self.label_MAX_TIME_FLIGHT, 5, 0, 1, 1)
        self.lineEdit_NAME = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_NAME.sizePolicy().hasHeightForWidth())
        self.lineEdit_NAME.setSizePolicy(sizePolicy)
        self.lineEdit_NAME.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_NAME.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_NAME.setText("")
        self.lineEdit_NAME.setObjectName("lineEdit_NAME")
        self.gridLayout.addWidget(self.lineEdit_NAME, 0, 1, 1, 1)
        self.lineEdit_MAX_SPEED = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_MAX_SPEED.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_MAX_SPEED.setObjectName("lineEdit_MAX_SPEED")
        self.gridLayout.addWidget(self.lineEdit_MAX_SPEED, 4, 1, 1, 1)
        self.lineEdit_VES = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_VES.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_VES.setObjectName("lineEdit_VES")
        self.gridLayout.addWidget(self.lineEdit_VES, 3, 1, 1, 1)
        self.lineEdit_ZAVODCKOY_NOMER = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ZAVODCKOY_NOMER.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_ZAVODCKOY_NOMER.setText("")
        self.lineEdit_ZAVODCKOY_NOMER.setObjectName("lineEdit_ZAVODCKOY_NOMER")
        self.gridLayout.addWidget(self.lineEdit_ZAVODCKOY_NOMER, 2, 1, 1, 1)
        self.label_2_MODEL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2_MODEL.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2_MODEL.setFont(font)
        self.label_2_MODEL.setObjectName("label_2_MODEL")
        self.gridLayout.addWidget(self.label_2_MODEL, 1, 0, 1, 1)
        self.label_ZAVODSKOY_NOMER = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ZAVODSKOY_NOMER.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_ZAVODSKOY_NOMER.setFont(font)
        self.label_ZAVODSKOY_NOMER.setObjectName("label_ZAVODSKOY_NOMER")
        self.gridLayout.addWidget(self.label_ZAVODSKOY_NOMER, 2, 0, 1, 1)
        self.label_VES = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_VES.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_VES.setFont(font)
        self.label_VES.setObjectName("label_VES")
        self.gridLayout.addWidget(self.label_VES, 3, 0, 1, 1)
        self.label_MAX_SPEED = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_MAX_SPEED.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_MAX_SPEED.setFont(font)
        self.label_MAX_SPEED.setObjectName("label_MAX_SPEED")
        self.gridLayout.addWidget(self.label_MAX_SPEED, 4, 0, 1, 1)
        self.label_MAX_DIST_POLET = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_MAX_DIST_POLET.setFont(font)
        self.label_MAX_DIST_POLET.setObjectName("label_MAX_DIST_POLET")
        self.gridLayout.addWidget(self.label_MAX_DIST_POLET, 6, 0, 1, 1)
        self.label_NAME = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_NAME.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_NAME.setFont(font)
        self.label_NAME.setObjectName("label_NAME")
        self.gridLayout.addWidget(self.label_NAME, 0, 0, 1, 1)
        self.lineEdit_MODEL = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_MODEL.setStyleSheet("QLineEdit{\n"
"    background-color:white;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(5,142,215);\n"
"}\n"
"QLineEdit:pressed{\n"
"    border:1px solid rgb(5,142,215);\n"
"}")
        self.lineEdit_MODEL.setText("")
        self.lineEdit_MODEL.setObjectName("lineEdit_MODEL")
        self.gridLayout.addWidget(self.lineEdit_MODEL, 1, 1, 1, 1)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 350, 471, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_EDIT_BPLA_IN_BD = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_EDIT_BPLA_IN_BD.setFont(font)
        self.pushButton_EDIT_BPLA_IN_BD.setStyleSheet("QPushButton{\n"
"background-color: rgb(215, 215, 215);\n"
"border: 1px solid gray;\n"
"}\n"
"QPushButton:hover {border:2px solid  rgb(0, 120, 215);}\n"
"QPushButton:pressed {border:2px solid  rgb(0, 120, 215);}")
        self.pushButton_EDIT_BPLA_IN_BD.setObjectName("pushButton_EDIT_BPLA_IN_BD")
        self.horizontalLayout.addWidget(self.pushButton_EDIT_BPLA_IN_BD)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактировать БПЛА"))
        self.groupBox_EDIT_BPLA.setTitle(_translate("MainWindow", "БПЛА"))
        self.label_MAX_TIME_FLIGHT.setText(_translate("MainWindow", "Максимальное времая полета, мин"))
        self.label_2_MODEL.setText(_translate("MainWindow", "Модель"))
        self.label_ZAVODSKOY_NOMER.setText(_translate("MainWindow", "Заводской номер"))
        self.label_VES.setText(_translate("MainWindow", "Вес, кг"))
        self.label_MAX_SPEED.setText(_translate("MainWindow", "<html><head/><body><p>Максимальная скорость, км\\ч</p></body></html>"))
        self.label_MAX_DIST_POLET.setText(_translate("MainWindow", "Максимальная дальность полет, м"))
        self.label_NAME.setText(_translate("MainWindow", "Наименование"))
        self.pushButton_EDIT_BPLA_IN_BD.setText(_translate("MainWindow", "Редактировать"))
        self.menu.setTitle(_translate("MainWindow", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())