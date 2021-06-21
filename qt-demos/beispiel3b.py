# https://riptutorial.com/de/pyqt5/example/29500/grundlegende-pyqt-fortschrittsleiste

import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

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
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count +=1
            time.sleep(1)
            self.countChanged.emit(count)

# ---------------------------------------------
            
class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.

    Wenn Sie auf die Schaltfläche self.onButtonClick klicken,
    wird self.onButtonClick ausgeführt und der Thread gestartet. 
    Der Thread wird mit .start() gestartet. Es sollte auch beachtet werden, 
    dass wir das self.calc.countChanged erstellte Signal self.calc.countChanged 
    mit der zum Aktualisieren des Fortschrittsbalkenwerts verwendeten Methode 
    verbunden haben. 
    Bei jeder Aktualisierung von External::run::count wird der int Wert 
    auch an onCountChanged gesendet. 
    """
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.button = QPushButton('Start', self)
        self.button.move(0, 30)
        self.show()

        self.button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)

# ---------------------------------------------
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())
