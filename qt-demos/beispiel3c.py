# https://riptutorial.com/de/pyqt5/example/29500/grundlegende-pyqt-fortschrittsleiste
# 3c: Erweiterung um eine variable Schrittweite


import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic

TIME_LIMIT = 100

# ---------------------------------------------

class External(QThread):
    """
    Runs a counter thread.

    countChanged ist der aktuelle Fortschritt, und 
    pyqtSignal(int) teilt dem Worker-Thread mit, 
    dass das gesendete Signal vom Typ int ist. 
    self.countChanged.emit(count) sendet das Signal einfach an 
    alle Verbindungen im Haupt-Thread (normalerweise kann es auch 
    mit anderen Worker-Threads kommunizieren). 
    """
    countChanged = pyqtSignal(int)  # Output
    stepChanged = pyqtSignal(int)   # Input
    schrittweite = -3
    
    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += self.schrittweite
            time.sleep(1)
            self.countChanged.emit(count)

    def beschleunige(self):
        self.schrittweite += 1

    def brems(self):
        self.schrittweite += -1

    def setSchrittweite(self, k):
        self.schrittweite = k
        
    def getSchrittweite(self):
        return self.schrittweite
        
# ---------------------------------------------
            
class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    In Version 3c kommt noch die variable Schrittweite hinzu.

    Wenn Sie auf die Schaltfläche self.onButtonClick klicken,
    wird self.onButtonClick ausgeführt und der Thread gestartet. 
    Der Thread wird mit .start() gestartet. Es sollte auch beachtet werden, 
    dass wir das self.calc.countChanged erstellte Signal self.calc.countChanged 
    mit der zum Aktualisieren des Fortschrittsbalkenwerts verwendeten Methode 
    verbunden haben. 
    Bei jeder Aktualisierung von External::run::count wird der int Wert 
    auch an onCountChanged gesendet. 
    """

    wichtigerCheckIndex = -1
    
    def __init__(self):
        super().__init__()
        self.wichtigerCheckIndex=0
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Progress Bar c')
        self.setGeometry(0, 0, 400, 250)       
        # Label
        self.label = QLabel('Schrittweite: ', self)
        self.label.move(100, 30+4)
        # Fortschrittsbalken
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 400, 25)
        self.progress.setMaximum(100)
        # Buttons
        self.buttonStart = QPushButton('Start', self)
        self.buttonStart.move(0, 30)
        self.buttonPlus = QPushButton('+', self)
        self.buttonPlus.move(200, 30)
        self.buttonMinus = QPushButton('-', self)
        self.buttonMinus.move(300, 30)
        self.buttonStart.clicked.connect(self.onButtonStartClick)
        self.buttonPlus.clicked.connect(self.onButtonPlusClick)
        self.buttonMinus.clicked.connect(self.onButtonMinusClick)
        # Checkbox & Label: indirekt über globale Variable
        self.checkbocks = QComboBox(self)
        self.checkbocks.addItems(["A", "B", "C", "D"])
        self.checkbocks.move(0,70)
        self.checkbocks.currentIndexChanged.connect(self.onIndexChanged)
        self.labelErgCheckbocks = QLabel('Wahl: '+str(self.wichtigerCheckIndex), self)
        self.labelErgCheckbocks.move(00, 100)
        # Textfeld & Label
        self.textfeld = QLineEdit(self)
        self.textfeld.setMaxLength(10)
        self.textfeld.setPlaceholderText("Enter your text")
        self.textfeld.move(0,140)
        self.textfeld.returnPressed.connect(self.onReturnPressed)
        self.textfeld.selectionChanged.connect(self.onSelectionChanged)
        self.textfeld.textChanged.connect(self.onTextChanged)
        self.textfeld.textEdited.connect(self.onTextEdited)
        self.textfeld.editingFinished.connect(self.onEditingFinished)
        #self.textfeld.setCentralWidget(self.textfeld)
        # Regler
        self.regler = QDial(self)
        self.regler.setNotchesVisible(1)
        self.regler.setMinimum(-5)
        self.regler.setMaximum(5)
        self.regler.setSliderPosition(self.calc.getSchrittweite())
        self.regler.move(235,66)
        self.regler.valueChanged.connect(self.onReglerChanged)
        # feddich :)
        self.show()               

    def onReglerChanged(self):
        print("Reglieren beendet! ")
        self.calc.setSchrittweite(self.regler.value())
        print(self.regler.value())
        
    def onEditingFinished(self):
        print("Editieren beendet!")
        #self.centralWidget().setText("BOOM!")

    def onReturnPressed(self):
        print("Return pressed!")
        #self.centralWidget().setText("BOOM!")

    def onSelectionChanged(self):
        print("Selection changed")
        #print(self.centralWidget().selectedText())
        
    def onTextChanged(self, s):
        print("Text changed...")
        print(s)
            
    def onTextEdited(self, s):
        print("Text edited...")
        print(s)        

    def onIndexChanged(self, k):
        self.wichtigerCheckIndex=k
        self.labelErgCheckbocks.setText(str(k+1))
        self.textfeld.setText(self.textfeld.text()+str(k+1))       
                
    def onButtonStartClick(self):
        self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)

    def onButtonPlusClick(self):
        if self.calc.getSchrittweite()<self.regler.maximum():
            self.calc.beschleunige()
            self.regler.setSliderPosition(self.calc.getSchrittweite())
        
    def onButtonMinusClick(self):
        if self.calc.getSchrittweite()>self.regler.minimum():       
            self.calc.brems()
            self.regler.setSliderPosition(self.calc.getSchrittweite())
        
# ---------------------------------------------
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())
