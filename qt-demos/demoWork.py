class WorkThread(QtCore.QThread):
    
    def __init__(self): 
        QtCore.QThread.__init__(self) 

    def __del__(self): 
        self.wait() 

    def run(self): 
        for i in range(6): 
            time.sleep(0.3) # artificial time delay 
            self.emit(QtCore.SIGNAL('update(QString)'), "from work thread " + str(i)) 
        self.terminate() 
