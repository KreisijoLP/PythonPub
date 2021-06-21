# Erweiterung meines statischen Beispiel2
# um Threads und Signalen aus Beispiel3b
# -> vgl beispiel3c.py

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


# Form, Window = uic.loadUiType("dialog.ui")
# Form, Window = uic.loadUiType("test01.ui")
Form, Fenster = uic.loadUiType("test01.ui")

app = QApplication([])
fenster = Fenster()
form = Form()
form.setupUi(fenster)
fenster.show()
app.exec_()
