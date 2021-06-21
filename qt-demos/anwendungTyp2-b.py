import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QLabel, QDateEdit, QTableView, QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction, QFrame, QGroupBox, QVBoxLayout, QGridLayout, QGraphicsView, QToolBar, QStatusBar, QMenuBar, qApp
#from PyQt5.QtWidgets import QToolBar, QStatusBar, QMenuBar, qApp
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QDate
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



class App(QApplication):
    
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.build_ui()

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
        status_bar = QStatusBar()
        status_bar.showMessage('Ready')
        self.main_window.setStatusBar(status_bar)

        # 3. ------------------------------------------  Menu-Leiste
        menu_bar = QMenuBar()

        fileMenu = menu_bar.addMenu('File')
        exitButton = QAction(QIcon('exit24.png'), '&Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(qApp.quit)
        fileMenu.addAction(exitButton)

        self.main_window.setMenuBar(menu_bar)

        # 4. ------------------------------------------  Das Zentrum
        
        #label = QLabel("erst einmal primitiv")
        #label.setAlignment(Qt.AlignCenter)        
        #self.main_window.setCentralWidget(label)

        layout = QGridLayout()
        #layout = QStackedLayout()
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 6, 2)
        widget = QWidget()
        widget.setLayout(layout)
        self.main_window.setCentralWidget(widget)


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
