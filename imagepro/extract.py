import sys

import cv2 as c
import numpy as np
from PySide2.QtWidgets import *
from pathlib import Path
import os
import json

i = 0
imax = 0
class extractImages():

    progress = 0
    progressMAX = 0

    def ext(self, path, extra, extrause):

        if extrause == True:

            path = path[0]

            print(str(path))
            cap = c.VideoCapture(str(path))
            ps = str(path)
            name = ps.split("/")[len(ps.split("/"))-1].split(".")[0]
            os.mkdir(path=extra)
            self.progressMAX = cap.get(c.CAP_PROP_FPS)
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == False:
                    break
                c.imwrite(extra+"/img_"+str(name)+str(self.progress)+'.jpg', frame)
                self.progress=self.progress+1

            cap.release()
            c.destroyAllWindows()

        else:

            path = path[0]

            print(str(path))
            cap = c.VideoCapture(str(path))
            ps = str(path)
            name = ps.split("/")[len(ps.split("/")) - 1].split(".")[0]
            os.mkdir(path="imgs_" + name)
            self.progressMAX = cap.get(c.CAP_PROP_FPS)
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == False:
                    break
                c.imwrite("imgs_" + str(name) + "/img_" + str(name) + str(self.progress) + '.jpg', frame)
                self.progress = self.progress + 1

            cap.release()
            c.destroyAllWindows()

class Manager():

    def __init__(self):
        self.load()

    def load(self):
        try:

            with open("./dataset/settings.json", "r") as jsonFile:
                self.jsonObject = json.load(jsonFile)
                jsonFile.close()

            test = self.jsonObject['test']

            print("yes")
            self.dirs = []
            self.dirs = self.jsonObject['dirs']
            print(self.dirs)

        except IOError:

            try:
                os.makedirs("./dataset")
            except FileExistsError:
                pass

            with open("./dataset/settings.json", "w") as jsonFile:

                ar = []

                jsonData = {

                    "test": "yes",
                    "dirs": ar

                }

                json.dump(jsonData, jsonFile)
                jsonFile.close()

            with open("./dataset/settings.json", "r") as jsonFile:
                self.jsonObject = json.load(jsonFile)
                jsonFile.close()

            self.dirs = self.jsonObject['dirs']



    def addData(self, args):

        self.dirs.add(args.name)
        jsonObject = json.loads(self.jsonObject)
        jsonObject


    def extFile(self, args):
        name = args.name
        text = args.text

        if self.dirs.contains(text):
            pass

        ei = extractImages()
        ei.ext(path=name, extra=text, extrause=True)




class QT(QWidget):

    def __init__(self, args):
        super(QT, self).__init__()
        self.load()
        self.manager = args.manager

    def extFile(self):

        allowedFiles = "Text Files (*.mp4)"#Add if needed: ;;Any File (*.*)
        name = QFileDialog.getOpenFileName(self, 'Open File any Text File', str(Path.home()), allowedFiles)

        text = self.showDialog()
        print(text)

        manager.extFile(text, name)

    def showDialog(self):
        text, result = QInputDialog().getText(self, 'Input', 'Enter Type of Video:')
        if result == True:
            return text

    def load(self):

        outlayout = QVBoxLayout()
        formlayout = QFormLayout()

        button = QPushButton()
        button.setFixedSize(50, 50)
        button.setText("Video Auswählen")
        button.clicked.connect(lambda: self.extFile())

        formlayout.addRow("Bitte das Video auswählen: ", button)

        outlayout.addLayout(formlayout)
        self.setLayout(outlayout)


if __name__ == "__main__":
    manager = Manager()
    #app = QApplication()
    #gui = QT()
    #gui.__init__(manager)
    #gui.show()
    #sys.exit(app.exec_())