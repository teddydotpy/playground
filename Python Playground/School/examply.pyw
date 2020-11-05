#! /usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
class demowind(QtWidgets.QWidget, QtGui.QWindow):
    def __init__(self,parent=None): 
        QtWidgets.QWidget.__init__(self, parent) 
        self.setGeometry(300, 300, 200, 200) 
        self.setWindowTitle('Demo window') 
        quit = QtWidgets.QPushButton('Close', self) 
        quit.setGeometry(10, 10, 70, 40)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtWidgets.qApp, QtCore.SLOT('quit()'))

app = QtWidgets.QApplication(sys.argv) 
dw = demowind()
dw.show()
sys.exit(app.exec_())