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
        exitButton = QAction(QIcon('exit24.png'), 'E&xit', self)
        exitButton.setShortcut('Ctrl+X')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(qApp.quit)
        fileMenu.addAction(exitButton)

        viewMenu = menu_bar.addMenu('View')
        changeButton = QAction(QIcon('view24.png'), '&view', self)
        changeButton.setShortcut('Ctrl+V')
        changeButton.setStatusTip('change view')
        changeButton.triggered.connect(self.changeIt)
        viewMenu.addAction(changeButton)


        # 4. ------------------------------------------  Das Zentrum

        layout1 = QGridLayout()
        layout1.addWidget(Color('red'), 0, 0)
        layout1.addWidget(Color('green'), 1, 0)
        layout1.addWidget(Color('blue'), 1, 1)
        layout1.addWidget(Color('purple'), 6, 2)
        self.widget1 = QWidget()
        self.widget1.setLayout(layout1)

        layout2 = QGridLayout()
        layout2.addWidget(Color('red'), 1, 0)
        layout2.addWidget(Color('green'), 3, 0)
        layout2.addWidget(Color('blue'), 0, 1)
        layout2.addWidget(Color('purple'), 5, 2)
        layout2.addWidget(Color('red'), 1, 4)
        layout2.addWidget(Color('green'), 2, 5)
        self.widget2 = QWidget()
        self.widget2.setLayout(layout2)
        
        self.layout = QStackedLayout()
        self.layout.addWidget(self.widget1)        
        self.layout.addWidget(self.widget2)        
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        #time.sleep(2)

        self.layout.setCurrentIndex(0)
        print (str(int(self.layout.currentIndex())))

        



        
        # ----------------------------------------------  Hauptfenster

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Anwendung Typ1 IST Fenster")
        self.show()


    def changeIt(self):
        i = self.layout.currentIndex() + 1
        if i>1:
            i=0
        self.layout.setCurrentIndex(i)

        
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

