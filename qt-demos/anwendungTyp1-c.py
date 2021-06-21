import sys,time
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QLabel, QDateEdit, QTableView, QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction, QFrame, QGroupBox, QVBoxLayout, QGridLayout, QStackedLayout, QGraphicsView, QToolBar, QStatusBar, QMenuBar, qApp
#from PyQt5.QtWidgets import QToolBar, QStatusBar, QMenuBar, qApp
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QDate
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5 import QtCore, QtWidgets, uic


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        
# Die Version1 IST ein Hauptfenster

# Da ich das Hauptfenster bin, habe ich schon von Hause aus
#  - statusBar  --> self.statusBar().showMessage('Ready')
#  - menuBar
#  - toolBar

class Hauptfenster(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 1. ------------------------------------------  Werkzeug-Leiste

        # leider nicht einheitlich zu 2 und 3
        action = QAction('Toolbar action', self)

        toolbar = QToolBar("My tolle toolbar")
        self.addToolBar(toolbar)
  
        
        #tool_bar = self.toolBar()
        #tool_bar.addAction(action)
        #self.main_window.addToolBar(tool_bar)

        #action = QAction('Toolbar action', self)        

        # 2. ------------------------------------------  Status-Leiste
        status_bar = self.statusBar()
        
        status_bar.showMessage('Ready')

        # 3. ------------------------------------------  Menu-Leiste
        menu_bar = self.menuBar()

        fileMenu = menu_bar.addMenu('File')
        exitButton = QAction(QIcon('exit24.png'), '&Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(qApp.quit)
        fileMenu.addAction(exitButton)

        # 4. ------------------------------------------  Das Zentrum
        #das_zentrum = self.centralWidget()

        #layout = QGridLayout()
        self.layout = QStackedLayout()
        self.layout.addWidget(Color('red'))
        self.layout.addWidget(Color('green'))
        self.layout.addWidget(Color('yellow'))
        self.layout.addWidget(Color('purple'))
        self.layout.setCurrentIndex(1)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        for i in range(4):
            self.layout.setCurrentIndex(i%4)
            time.sleep(2)
        self.layout.setCurrentIndex(2)


         
        #label = QLabel("erst einmal primitiv")
        #label.setAlignment(Qt.AlignCenter)        

        #self.setCentralWidget(label)

        
        # ----------------------------------------------  Hauptfenster

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Anwendung Typ1 IST Fenster")
        self.show()
        
def main():
        app = QApplication(sys.argv)
        ex = Hauptfenster()
        #for i in range(19):
        #    ex.layout.setCurrentIndex(i%4)
        #    #ex.layout.reload()
        #    time.sleep(0.5)
        #print("fertig")    
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()

