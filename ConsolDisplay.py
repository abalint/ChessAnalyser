
from PySide.QtCore import *
from PySide.QtGui import *
from datetime import datetime
import socket
import sys
import PySide.QtGui
from UI_consoleDisplay import Ui_ResultsDisplay

class ConsolDisplay(QMainWindow):

    def __init__(self, displayList, parent=None):
        super(ConsolDisplay, self).__init__(parent)

        # set up ui
        self.ui = Ui_ResultsDisplay()
        self.ui.setupUi(self)
        self.ui.textEdit.setReadOnly(1)

        self.displayList = displayList


    def output(self):
        self.ui.textEdit.setFontPointSize(15)
        #self.ui.textEdit.setTextColor("#0033CC") can set the text color
        index = 0;
        for value in self.displayList:
            print(value[0])
            if value[0] == 'B':
                print("got bad move")
                self.ui.textEdit.setTextColor("#CC0000")
            if value[0] == 'G':
                self.ui.textEdit.setTextColor("#004016")
            if value[0] == 'N':
                self.ui.textEdit.setTextColor("#000000")

            self.ui.textEdit.append(value)
            index = index + 1

            QCoreApplication.processEvents()
