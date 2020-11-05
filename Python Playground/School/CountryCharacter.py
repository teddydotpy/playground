from PyQt5 import QtCore, QtWidgets, QtGui

#I apologize to my lecturers Qt5 was the only one i could set up in
#the alotted time so i did my best with what i had.

#Basically had to write the entire applications myself based on prior experience
#and some practice... anyway sorry.
class CountryCharacterGui(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300,300, 600, 300)
        self.setWindowTitle("Character Counter")
        self.CountryFieldtext = QtWidgets.QLineEdit(self)
        self.CharFieldtext = QtWidgets.QLineEdit(self)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        buttonLayout = QtWidgets.QHBoxLayout(self)
        CountryLayout = QtWidgets.QHBoxLayout(self)
        CharLayout = QtWidgets.QHBoxLayout(self)
        DetailsLayout = QtWidgets.QVBoxLayout(self)

        enterLabel = QtWidgets.QLabel('Enter a country name')
        CharLabel = QtWidgets.QLabel('Enter any Character')
        exitButt = QtWidgets.QPushButton("Exit")
        Tryagn = QtWidgets.QPushButton("Try Again")
        EnterBtn = QtWidgets.QPushButton("Enter")

        StudName = QtWidgets.QLabel('Name: Siphesihle Musa Ntombela' )
        StudNO = QtWidgets.QLabel('Student Number: 62360639' )

        buttonLayout.addWidget(EnterBtn)
        buttonLayout.addWidget(Tryagn)
        buttonLayout.addWidget(exitButt)

        CountryLayout.addWidget(enterLabel)
        CountryLayout.addWidget(self.CountryFieldtext)

        CharLayout.addWidget(CharLabel)
        CharLayout.addWidget(self.CharFieldtext)

        DetailsLayout.addWidget(StudName)
        DetailsLayout.addWidget(StudNO)

        DetailsLayout.setAlignment(QtCore.Qt.AlignRight)

        self.mainLayout.addLayout(CountryLayout)
        self.mainLayout.addLayout(CharLayout)
        self.mainLayout.addLayout(buttonLayout)
        self.mainLayout.addLayout(DetailsLayout)

        exitButt.clicked.connect(self.LeaveOk)
        Tryagn.clicked.connect(self.tryAngia)
        EnterBtn.clicked.connect(self.ProcessData)

#These are out event handlers :)
        
    def LeaveOk(self):
        exit()

    def tryAngia(self):
        self.CountryFieldtext.clear()
        self.CharFieldtext.clear()


#This function processes the word i.e counts the amount of times the character appears in the word.
    def ProcessData(self):
        messgBox = QtWidgets.QMessageBox()
        if len(self.CharFieldtext.text()) > 1:
            messgBox.setWindowTitle('Warning!')
            messgBox.setIcon(QtWidgets.QMessageBox.Warning)
            messgBox.setText('You messed up bruh... one letter, ok!')
            messgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            messgBox.exec()
            self.tryAngia()
        else:
            numMatch = 0
            for letter in range(len(self.CountryFieldtext.text())):
                if self.CountryFieldtext.text()[letter].lower() == self.CharFieldtext.text().lower():
                    numMatch += 1

            messgBox.setWindowTitle('Result!')
            messgBox.setIcon(QtWidgets.QMessageBox.Information)
            messgBox.setText( self.CharFieldtext.text().upper() + ' appears ' + str(numMatch) + ' times in ' + self.CountryFieldtext.text() + '.')
            messgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            messgBox.exec()


        