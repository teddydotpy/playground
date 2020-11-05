from PyQt5 import QtCore, QtWidgets, QtGui

#I am able to reuse my gui code because it's simple and with a bit more tweaks.
class CountryListGui(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300,300, 600, 300)
        self.setWindowTitle("Character Counter")

        self.CountryFieldtext = QtWidgets.QLineEdit(self)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setAlignment(QtCore.Qt.AlignRight)
        self.CountryListView = QtWidgets.QListWidget(self)
        self.setLayout(self.mainLayout)

        buttonLayout = QtWidgets.QHBoxLayout(self)
        CountryLayout = QtWidgets.QHBoxLayout(self)
        DetailsLayout = QtWidgets.QVBoxLayout(self)

        enterLabel = QtWidgets.QLabel('Enter the country name: ')
        self.ListSizeLabel = QtWidgets.QLabel('There are ' + str(self.CountryListView.count()) + ' items in the list, currently.')
    
        StudName = QtWidgets.QLabel('Name: Siphesihle Musa Ntombela' )
        StudNO = QtWidgets.QLabel('Student Number: 62360639' )
        
        exitButt = QtWidgets.QPushButton("Exit")
        DeleteBut = QtWidgets.QPushButton("Delete")
        AdddBtn = QtWidgets.QPushButton("Add New")

        buttonLayout.addWidget(AdddBtn)
        buttonLayout.addWidget(DeleteBut)
        buttonLayout.addWidget(exitButt)

        CountryLayout.addWidget(enterLabel)
        CountryLayout.addWidget(self.CountryFieldtext)

        DetailsLayout.addWidget(StudName)
        DetailsLayout.addWidget(StudNO)

        DetailsLayout.setAlignment(QtCore.Qt.AlignRight)

        self.mainLayout.addLayout(CountryLayout)
        self.mainLayout.addWidget(self.CountryListView)
        self.mainLayout.addWidget(self.ListSizeLabel)
        self.mainLayout.addLayout(buttonLayout)
        self.mainLayout.addLayout(DetailsLayout)

        exitButt.clicked.connect(self.LeaveOk)
        DeleteBut.clicked.connect(self.DelteCountry)
        AdddBtn.clicked.connect(self.addCountry)
        


    def updateUi(self):
        #I broke my head trying to make the UI update each time but i am incapable. i am no sufficiently smart enough.
        #Once i learn more i will be able to solve this problem but for now i am too stupid.
        self.ListSizeLabel.destroy()
        self.ListSizeLabel = QtWidgets.QLabel('There are ' + str(self.CountryListView.count()) + ' items in the list, currently.')


# Our beautiful event handliers.
    def LeaveOk(self):
        exit()

    def DelteCountry(self):
        messgBox = QtWidgets.QMessageBox()
        if len(self.CountryListView.selectedItems()) < 1:
            messgBox.setWindowTitle('Warning!')
            messgBox.setIcon(QtWidgets.QMessageBox.Warning)
            messgBox.setText('You messed up bruh... please select an item to delete, ok!')
            messgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            messgBox.exec()
        else:
            self.CountryListView.takeItem(self.CountryListView.row(self.CountryListView.currentItem()))
            self.updateUi()


    def addCountry(self):
        messgBox = QtWidgets.QMessageBox()
        if  self.CountryFieldtext.text() == '':
            messgBox.setWindowTitle('Warning!')
            messgBox.setIcon(QtWidgets.QMessageBox.Warning)
            messgBox.setText('You messed up bruh... please actually type something, ok!')
            messgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            messgBox.exec()
        elif len(self.CountryListView.findItems(self.CountryFieldtext.text(), QtCore.Qt.MatchExactly)) > 0:
            messgBox.setWindowTitle('Warning!')
            messgBox.setIcon(QtWidgets.QMessageBox.Warning)
            messgBox.setText('You messed up bruh... the item you added already exists in the list!')
            messgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            messgBox.exec() 
        else:   
            self.CountryListView.addItem(self.CountryFieldtext.text())
            self.CountryFieldtext.clear()
            self.updateUi()
