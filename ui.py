# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(280, 80)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.browseLine = QtWidgets.QLineEdit(self.centralwidget)
        self.browseLine.setGeometry(QtCore.QRect(10, 10, 160, 25))
        self.browseLine.setObjectName("browseLine")
        self.browseLine.setEnabled(False)

        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(180, 10, 90, 25))
        self.browseButton.setObjectName("browseButton")

        self.extractButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractButton.setGeometry(QtCore.QRect(10, 45, 260, 25))
        self.extractButton.setObjectName("extractButton")
        self.extractButton.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XSIG Extractor"))
        self.browseButton.setText(_translate("MainWindow", "Browse .XSIG"))
        self.extractButton.setText(_translate("MainWindow", "Extract .XSIG"))
