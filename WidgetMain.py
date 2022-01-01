# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_design import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
