from PySide.QtCore import *
from PySide.QtGui import *
from MainWindow import MainWindow
import sys


class App(QApplication):

    def __init__(self, argv):
        super(App, self).__init__(argv)
        self.mainwindow = MainWindow()

    def exec_(self, *args, **kwargs):
        self.mainwindow.show()
        super(App, self).exec_()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())