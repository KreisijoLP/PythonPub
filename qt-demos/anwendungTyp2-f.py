import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QLabel, QDateEdit, QTableView, QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction, QFrame, QGroupBox, QVBoxLayout, QGridLayout, QGraphicsView, QToolBar, QStatusBar, QMenuBar, qApp
#from PyQt5.QtWidgets import QToolBar, QStatusBar, QMenuBar, qApp
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QDate, QThread
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


# Die Version2 HAT ein Hauptfenster (und ist eine QApplication)
# => aus self.  wird nun self.main_window.

# In dieser Version kann man gut beobachten, dass
# - sowohl im Label als auch in der StatusBar -
# die 'calculating ...'-Ausgaben nicht erscheinen,
# sehr wohl aber die 'ready'-Ausgaben.
# Das liegt daran, dass die Haupt-Routine von Qt
# erst am Ende wieder zum Zuge kommt.

class Berechnung(QThread):
    def berechnePiThready(n):
        pi_halbe=1
        zaehler, nenner = 2.0, 1.0

        for i in range(n):
            pi_halbe *= zaehler/nenner
            if i % 2:
                zaehler+=2
            else:
                nenner*=2
        return 2*pi_halbe        

        
class App(QApplication):
    
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.build_ui()

    def berechnePi(self,n):
        self.label.setText('calcuating ... Pi')                
        self.status_bar.showMessage('calcuating ... Pi')        
        pi_halbe=1
        zaehler, nenner = 2.0, 1.0

        for i in range(n):
            pi_halbe *= zaehler/nenner
            if i % 2:
                zaehler+=2
            else:
                nenner+=2
        return 2*pi_halbe                

    def starteRechnung(self):
        self.label.setText('calcuating ...')        
        self.status_bar.showMessage('calcuating ...')        
        self.yWert = self.berechnePi(100000000)
        self.label.setText('ready :)')        
        self.status_bar.showMessage('ready :)')        
        self.label.setText(str(self.yWert))
        print(self.yWert)
        
    def build_ui(self):
        # Das Fenster an sich ...
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle('Anwendung Typ2 HAT Fenster')
        self.main_window.setGeometry(300,300,300,200)
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
        actButton.triggered.connect(self.starteRechnung)
        actMenu.addAction(actButton)

        self.main_window.setMenuBar(menu_bar)

        # 4. ------------------------------------------  Das Zentrum
        
        #label = QLabel("erst einmal primitiv")
        #label.setAlignment(Qt.AlignCenter)        
        #self.main_window.setCentralWidget(label)

        # Label für die Ausgabe
        self.label = QLabel()
        self.label.setText("Lable")

        
        layout = QGridLayout()
        #layout = QStackedLayout()
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 6, 2)
        layout.addWidget(self.label, 5, 0)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.main_window.setCentralWidget(widget)


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
