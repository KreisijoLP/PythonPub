import sys

from PySide2.QtWidgets import *
from text.password_hashing import getlines, iterFile
from pathlib import Path

class gui(QWidget):

    def __init__(self):
        super(gui, self).__init__()
        self.load_ui()
        self.setBaseSize(400, 400)
        self.setWindowTitle("Hallo")

    def test(self):
        print("Hallo")
        print("Content: "+str(self.user.text()))

    def load_ui(self):
        layout = QHBoxLayout()
        layoutinlayout = QFormLayout()
        button = QPushButton()
        button.setFixedSize(100, 100)
        button.setText("Hallo")
        button.clicked.connect(lambda: self.test())
        layout.addWidget(button)
        self.othertext = QLineEdit()

        self.othertext.setPlaceholderText("TEst")

        self.user = QLineEdit()

        self.user.setPlaceholderText("User")
        #self.user.setFixedSize(200, 20)
        self.user.setMinimumSize(200, 20)
        self.user.setMaximumWidth(400)
        self.user.setMaxLength(2000)
        layout.addWidget(self.user)
        layout.addWidget(self.othertext)

        self.setLayout(layout)

def test2():
    print("Das ist der 2. Test")

class othergui(QWidget):

    def __init__(self):
        super(othergui, self).__init__()
        self.setBaseSize(400, 400)
        self.setWindowTitle("Hallo")
        self.load_ui()

    def openfile(self):
        allowedFiles = "Text Files (*.txt);;Other Files (*.jar);;Other Files (*.*)"
        name = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', allowedFiles)
        print(name)

    def load_ui(self):

        outerlayout = QVBoxLayout()
        formLayout = QFormLayout()

        text = QTextEdit()
        text.setPlaceholderText("Ein Test oder so")
        text.setMinimumWidth(200)

        formLayout.addWidget(text)

        otherFormLayout = QFormLayout()

        user = QLineEdit()
        user.setPlaceholderText("Username")
        otherFormLayout.addRow("Usdername:", user)

        button = QPushButton()
        button.setText("Push me!")
        button.clicked.connect(lambda: self.openfile())
        otherFormLayout.addWidget(button)

        otherLayout = QVBoxLayout()

        for l in getlines(10):
            otherLayout.addWidget(QCheckBox(str(l).rstrip())) #Bitte immer rstrip machen (Machst du so oder so nicht außer es fällt dir auf :) )

        #outerlayout.addLayout(formLayout)
        outerlayout.addLayout(otherFormLayout)
        outerlayout.addLayout(otherLayout)

        self.setLayout(outerlayout)

class openFileWithGui(QWidget):
    
    def __init__(self):
        super(openFileWithGui, self).__init__()
        self.setBaseSize(400, 400)
        self.setWindowTitle("Hallo")
        #self.setWindowIcon()
        self.load_gui()

    def load_gui(self):

        #Outline
        outerlayout = QVBoxLayout()

        #First FormLayout
        formlayout = QFormLayout()

        button = QPushButton("Hallo")
        button.clicked.connect(lambda: self.openfile())
        formlayout.addRow("Bitte drücken: ", button)

        outerlayout.addLayout(formlayout)
        self.setLayout(outerlayout)

    def openfile(self):
        allowedFiles = "Text Files (*.txt);;Any File (*.*)"#Add if needed: ;;Any File (*.*)
        name = QFileDialog.getOpenFileName(self, 'Open File any Text File', str(Path.home()), allowedFiles)
        ns = str(name)
        print(name)
        print(len(ns.split("/")))
        name2 = ns.split("/")[len(ns.split("/"))-1].split(".")[0]
        print(name2)
        try:
            for z in name:
                if not str(z).__contains__(allowedFiles):
                    print(z)
                    print("\n#######################################\nCONTENT OF THE FILE: "+z+"\n#######################################\n")
                    iterFile(path=z)
                    print("\n#######################################\nEND CONTENT\n#######################################\n")
        except:
            print("Anything went wrong!")


if __name__ == "__main__":
    app = QApplication()
    gui = openFileWithGui()
    gui.show()
    sys.exit(app.exec_())