import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QLabel, QDateEdit, QTableView, QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction, QFrame, QGroupBox, QVBoxLayout, QGridLayout, QGraphicsView, QToolBar, QStatusBar, QMenuBar, qApp
#from PyQt5.QtWidgets import QToolBar, QStatusBar, QMenuBar, qApp
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QDate, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5 import QtCore, QtWidgets, uic

#QtWidgets.QMenu() 



class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

"""
Die Version2 HAT ein Hauptfenster (und ist eine QApplication)
=> aus self.  wird nun self.main_window.

In der Version f konnte man gut beobachten, dass
- sowohl im Label als auch in der StatusBar -
die 'calculating ...'-Ausgaben nicht erscheinen,
sehr wohl aber die 'ready'-Ausgaben.
Das liegt daran, dass die Haupt-Routine von Qt
erst am Ende wieder zum Zuge kommt.

In Version g  wird der vorbereitete Thread genutzt
Das klappt auch soweit, allerdings passiert durch den direkten Aufruf des Threads
trotzdem nix, da muss ich wohl ein paar Infos raus schicken...

In dieser Version h wird emittiert... Als Vorlage dient beispiel3c
Die einzelnen Elemente sind per Kommentar markiert:
        # -------------------------------------------------------------------------------<<<< THREAD
Im Einzelnen:

1) Die Thread-Klasse mit 
     a) pyqt-Signalen
     b) Methode run
     c) Variablen emittieren
   
2) Die normale Qt-Applikation mit 
     a) Thread initialisieren und 
     b) die emittierten Variablen an eine Funktion binden
     c) Thread starten
     d) die Funktion, die die Änderung per Qt-Element darstellt. 

"""

class Punkt:
    def __init__(self,xP,yP):
        self.x = xP
        self.y = yP
        
    def gibAlles(self):
        return self.x, self.y




# 1 -------------------------------------------------------------------------------------<<<< THREAD

class Berechnung(QThread):

    # 1a --------------------------------------------------------------------------------<<<< THREAD
    # wir steigern uns bei den DT: int, float, str , Punkt
    calcOutputSignal_k = pyqtSignal(int) 
    calcOutputSignal_y = pyqtSignal(float)
    calcOutputSignal_t = pyqtSignal(str)
    calcOutputSignal_p = pyqtSignal(Punkt)
    
    calcInputSignal_n  = pyqtSignal(int) # noch ungenutzt

    n = 1000000
    z = 0
    
    # 1b --------------------------------------------------------------------------------<<<< THREAD
    def run(self):
        print(self.berechnePiThready(self.n))

    def berechnePiThready(self,nP):
        pi_halbe=1
        zaehler, nenner = 2.0, 1.0

        for i in range(nP):
            pi_halbe *= zaehler/nenner
            if i % 2:
                zaehler+=2
            else:
                nenner+=2
            # 1c ------------------------------------------------------------------------<<<< THREAD
            self.calcOutputSignal_k.emit(i)
            self.calcOutputSignal_y.emit(pi_halbe*2)
            if self.z==0:
                self.z=1
                self.calcOutputSignal_t.emit("klein")
            elif self.z==1 and i>0.3*nP:
                self.z=2
                self.calcOutputSignal_t.emit("mittel")
            elif self.z==2 and i>0.7*nP:
                self.z=3
                self.calcOutputSignal_t.emit("groß")
            elif self.z==3 and i==nP-1:
                self.z=0
                self.calcOutputSignal_t.emit("")                
        return 2*pi_halbe        

        
class App(QApplication):
    
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Den Thread initialisieren (a) und an Funktion onOutputChanged binden (b) 
        # 2a ----------------------------------------------------------------------------<<<< THREAD
        self.calc = Berechnung()
        # 2b ----------------------------------------------------------------------------<<<< THREAD
        self.calc.calcOutputSignal_k.connect(self.onOutputChanged_k)
        self.calc.calcOutputSignal_y.connect(self.onOutputChanged_y)
        self.calc.calcOutputSignal_t.connect(self.onOutputChanged_t)
        # UserInterface
        self.build_ui()

        
    def build_ui(self):

        # Das Fenster an sich ...
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle('Anwendung Typ2 HAT Fenster')
        self.main_window.setGeometry(300,300,800,300)
        self.main_window.show()
        # ... hat schon eine Einteilung:

        # 1. ------------------------------------------  Werkzeug-Leiste 
        action = QAction('Toolbar action', self)
        tool_bar = QToolBar("My tolle Toolbar")
        tool_bar.addAction(action)
        self.main_window.addToolBar(tool_bar)

        # 2. ------------------------------------------  Status-Leiste
        # jetzt global 
        self.status_bar = QStatusBar()
        self.status_bar.showMessage('waiting for a job to do')
        self.main_window.setStatusBar(self.status_bar)

        # 3. ------------------------------------------  Menu-Leiste
        menu_bar = QMenuBar()

        fileMenu = menu_bar.addMenu('File')
        exitButton = QAction(QIcon('exit24.png'), 'E&xit', self)
        exitButton.setShortcut('Ctrl+X')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(qApp.quit)
        fileMenu.addAction(exitButton)
        actMenu = menu_bar.addMenu('Action')
        actButton = QAction(QIcon('act24.png'), '&Act', self)
        actButton.setShortcut('Ctrl+A')
        #actButton.setStatusTip('Act and calculate')
        # ohne thread
        # actButton.triggered.connect(self.starteRechnung)
        # mit thread - erst einmal direkt
        # 2c ----------------------------------------------------------------------------<<<< THREAD
        actButton.triggered.connect(self.calc.start)
        actMenu.addAction(actButton)

        self.main_window.setMenuBar(menu_bar)

        # 4. ------------------------------------------  Das Zentrum
        
        #label = QLabel("erst einmal primitiv")
        #label.setAlignment(Qt.AlignCenter)        
        #self.main_window.setCentralWidget(label)

        # Label für die Ausgabe
        self.label1 = QLabel()
        self.label1.setText("k")
        self.label2 = QLabel()
        self.label2.setText("y")
        self.label3 = QLabel()
        self.label3.setText("")

        
        layout = QGridLayout()
        #layout = QStackedLayout()
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 6, 2)
        layout.addWidget(self.label1, 2, 0)
        layout.addWidget(self.label2, 2, 1)        
        layout.addWidget(self.label3, 3, 1)        
        widget = QWidget()
        widget.setLayout(layout)
        self.main_window.setCentralWidget(widget)

    # 2d --------------------------------------------------------------------------------<<<< THREAD
        
    def onOutputChanged_k(self, value):
        #self.progress.setValue(value) # kopie aus beispiel3c
        self.label1.setText("k= "+str(value))

    def onOutputChanged_y(self, value):
        #self.progress.setValue(value) # kopie aus beispiel3c
        self.label2.setText("y= "+str(value))

    def onOutputChanged_t(self, value):
        #self.progress.setValue(value) # kopie aus beispiel3c
        self.label3.setText(value)



if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
