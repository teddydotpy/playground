#! /usr/bin/env python3

#I prefere using the shebang because it's more conveniant and more cool
# It makes me feel like a real hacker.
import CountryCharacter, sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv) 
CountryC = CountryCharacter.CountryCharacterGui()
CountryC.show()
sys.exit(app.exec_())