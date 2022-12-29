import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSlot, pyqtSignal
import numpy as np

import GUI

#Clase de la interfaz
class app_VRU(QtWidgets.QMainWindow):
    def __init__(self):
        #Cargando interfaz
        super().__init__()
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.iniciar.clicked.connect(self.initUI)
        self.ui.terminar.clicked.connect(self.cancel)
        #self.ui.iniciar.clicked.connect(self.print)

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.ui.cam.setPixmap(QPixmap.fromImage(image))
        
    def initUI(self):
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()
        
    def cancel(self):
        self.ui.cam.clear()
        th = Thread(self)
        th.stop()

    def takefo(self):
        capt = cv2.VideoCapture(0)
        leido, frame = capt.read()
        
        if leido == True:
            cv2.imwrite("foto.png", frame)
            
            capt.release()

    def salir(self):
        sys.exit(app.exec_())

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(0)
        while self.hilo_corriendo:
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                
    def stop(self):
        self.hilo_corriendo = False
        self.quit()

#Inicio de la interfaz
if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = app_VRU()
    mainWindow.show()
    sys.exit(app.exec_())
