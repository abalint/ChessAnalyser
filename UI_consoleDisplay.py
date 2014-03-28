# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_consoleDisplay.ui'
#
# Created: Mon Mar 17 15:06:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResultsDisplay(object):
    def setupUi(self, ResultsDisplay):
        ResultsDisplay.setObjectName("ResultsDisplay")
        ResultsDisplay.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ResultsDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet(".QLineEdit, .QTextEdit\n"
"{\n"
"background-color: #F2FFFF;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        ResultsDisplay.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ResultsDisplay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ResultsDisplay.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ResultsDisplay)
        self.statusbar.setObjectName("statusbar")
        ResultsDisplay.setStatusBar(self.statusbar)

        self.retranslateUi(ResultsDisplay)
        QtCore.QMetaObject.connectSlotsByName(ResultsDisplay)

    def retranslateUi(self, ResultsDisplay):
        ResultsDisplay.setWindowTitle(QtGui.QApplication.translate("ResultsDisplay", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

