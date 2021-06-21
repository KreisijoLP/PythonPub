#import sys, time 
#from PyQt4 import QtCore, QtGui 
import sys,time
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QLabel, QDateEdit, QTableView, QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction, QFrame, QGroupBox, QVBoxLayout, QGridLayout, QStackedLayout, QGraphicsView, QToolBar, QStatusBar, QMenuBar, qApp
#from PyQt5.QtWidgets import QToolBar, QStatusBar, QMenuBar, qApp
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QDate, SIGNAL
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5 import QtCore, QtWidgets, uic



class MyApp(QWidget): 
    def __init__(self, parent=None): 
        QWidget.__init__(self, parent) 

        self.setGeometry(300, 300, 280, 600) 
        self.setWindowTitle('threads') 

        self.layout = QVBoxLayout(self) 

        self.testButton = QPushButton("test") 
        self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test) 
        self.listwidget = QtGui.QListWidget(self) 

        self.layout.addWidget(self.testButton) 
        self.layout.addWidget(self.listwidget) 

    def add(self, text): 
        """ Add item to list widget """ 
        print ("Add: " + text) 
        self.listwidget.addItem(text) 
        self.listwidget.sortItems() 

    def addBatch(self,text="test",iters=6,delay=0.3): 
        """ Add several items to list widget """ 
        for i in range(iters): 
            time.sleep(delay) # artificial time delay 
            self.add(text+" "+str(i)) 

    def test(self): 
        self.listwidget.clear() 
        # adding entries just from main application: locks ui 
        self.addBatch("_non_thread",iters=6,delay=0.3) 
