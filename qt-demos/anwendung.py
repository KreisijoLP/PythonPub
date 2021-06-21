import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5.QtWidgets import QLabel, QDateEdit, QTableView, QPushButton, QMainWindow, QWidget, QPlainTextEdit, QDialog, QFileDialog, QAction, QFrame, QGroupBox, QVBoxLayout, QGraphicsView, QToolBar, QStatusBar, QMenuBar
from PyQt5.QtCore import QSize, pyqtSlot, Qt, QDate
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets, uic





class App(QApplication):
    
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.build_ui()

    def build_ui(self):
        # Das Fenster an sich ...
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle('App')
        self.main_window.show()
        # ... hat schon eine Einteilung:

        # 1. ------------------------------------------  Werkzeug-Leiste 
        action = QAction('Toolbar action', self)
        tool_bar = QToolBar()
        tool_bar.addAction(action)
        self.main_window.addToolBar(tool_bar)

        # 2. ------------------------------------------  Status-Leiste
        status_bar = QStatusBar()
        status_bar.showMessage('Status bar')
        self.main_window.setStatusBar(status_bar)

        # 3. ------------------------------------------  Menu-Leiste
        menu_bar = self.menuBar()

        fileMenu = menu_bar.addMenu('File')
        exitButton = QAction(QIcon('exit24.png'), '&Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit Application')
        exitButton.triggered.connect(qApp.quit)
        fileMenu.addAction(exitButton)

        self.main_window.setMainMenu(menu_bar)

        
        # add a label to the main window
        label = QLabel('Label')
        self.main_window.setCentralWidget(label)



if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
