# 5: Dateidialog+ Textbearbeitung
# 6: Menu + Textbearbeitung

import sys

from PyQt5.Qt import QApplication, QClipboard
from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction
from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets, uic



# ---------------------------------------------

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Menu')
        self.setGeometry(0, 0, 420, 500)
        # --- Menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        openButton = QAction(QIcon('open24.png'), 'Open', self)
        openButton.setShortcut('Ctrl+O')
        openButton.setStatusTip('open Datei')
        openButton.triggered.connect(self.onButtonLoadClick)
        fileMenu.addAction(openButton)
        saveButton = QAction(QIcon('save24.png'), 'Save', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.setStatusTip('save Datei')
        saveButton.triggered.connect(self.onButtonSaveClick)
        fileMenu.addAction(saveButton)
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        helpButton = QAction(QIcon('help24.png'), 'Help', self)
        helpButton.setShortcut('F1')
        #exitButton.setStatusTip('Exit application')
        #exitButton.triggered.connect(self.close)
        helpMenu.addAction(helpButton)
        aboutButton = QAction(QIcon('about24.png'), 'About', self)
        #exitButton.setShortcut('Ctrl+Q')
        #exitButton.setStatusTip('Exit application')
        #exitButton.triggered.connect(self.close)
        helpMenu.addAction(aboutButton)
        # --- Add text field
        self.b = QPlainTextEdit(self)
        self.b.setBackgroundVisible(False)
        self.b.insertPlainText("You can write text here.\n")
        self.b.move(10,30)
        self.b.resize(400,460)
        # --- feddich :)
        self.show()
        
# ---------------------------------------------
        
    # SaveButton
    def onButtonSaveClick(self):
        print("Save-Button\n")
        inhalt = self.b.toPlainText()
        print(inhalt)
        self.saveFileDialog()
        self.schreibTextdatei(inhalt)
        
    # Textdatei speichern
    def schreibTextdatei(self, inhaltP):
        print("Schreib Textdatei\n")
        fobj_out = open(self.datName2,"w")
        # i = 1
        # for line in fobj_in:
        #    print(line.rstrip())
        #    fobj_out.write(str(i) + ": " + line)
        #    i = i + 1
        #fobj_in.close()
        fobj_out.write(inhaltP)
        fobj_out.close()

    # LoadButton
    def onButtonLoadClick(self):
        print("Open-Button\n")
        self.openFileNameDialog()
        self.liesTextdateiV3(self.datName1)        
        self.b.insertPlainText(self.datInhalt)
        
    # Textdatei zeilenweise lesen    
    def liesTextdateiV1(self,datNameP):
        fobj = open(datNameP, "r")
        for line in fobj:
            print(line.rstrip())
        fobj.close()

    # Textdatei in eine Liste    
    def liesTextdateiV2(self,datNameP):        
        self.datInhalt = open(datNameP).readlines()
        print(self.datInhalt)

    # Textdatei in einen String    
    def liesTextdateiV3(self,datNameP):        
        self.datInhalt = open(datNameP).read()
        print(self.datInhalt)
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.datName1=fileName
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            self.datName2=fileName

        
# ---------------------------------------------
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
