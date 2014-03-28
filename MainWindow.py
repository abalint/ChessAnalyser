__author__ = 'Andrew'

import pgn
from Analyser import Analyser
from PySide.QtGui import *
from PySide.QtCore import *
from UI_MainWindow import Ui_MainWindow
from ConsolDisplay import ConsolDisplay

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # set up ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Chess Analyser')

        # connect signals
        self.ui.findButton.clicked.connect(self._onFindClicked)
        self.ui.AnalyseButton.clicked.connect(self._onAnalyseClicked)

    def _onFindClicked(self):
        '''do stuff '''

    def _onAnalyseClicked(self):
        filePath = self.ui.filePath.text()
        analyser = Analyser(filePath)
        list = analyser.analyse()
        print(list)
        display = ConsolDisplay(list, self)
        display.show()
        display.update()
        display.output()