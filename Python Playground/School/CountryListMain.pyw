#! /usr/bin/env python3

import CountryListTracker, sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv) 
CountryC = CountryListTracker.CountryListGui()
CountryC.show()
sys.exit(app.exec_())