from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


# Form, Window = uic.loadUiType("dialog.ui")
Form, Window = uic.loadUiType("test01.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()
