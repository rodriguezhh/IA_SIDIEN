import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import numpy as np
import datetime

import GUI

#Clase de la interfaz
class app_VRU(QtWidgets.QMainWindow):
    def __init__(self):
        #Cargando interfaz
        super().__init__()
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TOLD2 IA")
        self.start_video()
        self.counter = 0

        self.ui.save_ph.clicked.connect(self.saveph)
        self.ui.take_ph.clicked.connect(self.takeph)
        self.ui.retake_ph.clicked.connect(self.start_video)
        self.ui.close.clicked.connect(self.salir)

    def Imageupd_slot(self, Image):
        self.ui.cam.setPixmap(QPixmap.fromImage(Image))
        
    def start_video(self):
        
        self.ui.save_ph.setEnabled(False)
        self.ui.save_ph_tex.setEnabled(False)
        self.ui.retake_ph.setEnabled(False)
        self.ui.retake_ph_text.setEnabled(False)

        self.ui.take_ph.setEnabled(True)
        self.ui.take_ph_tex.setEnabled(True)

        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
        
    def takeph(self):
        self.ui.save_ph.setEnabled(True)
        self.ui.save_ph_tex.setEnabled(True)
        self.ui.retake_ph.setEnabled(True)
        self.ui.retake_ph_text.setEnabled(True)

        self.ui.take_ph.setEnabled(False)
        self.ui.take_ph_tex.setEnabled(False)

        global stop
        stop = True
        #self.ui.cam.clear()

    def saveph(self):
        self.counter +=1
        self.ui.cont.setStyleSheet("color: white;")
        self.ui.cont.setText(f"Muestra #: {self.counter}")

        global frame_cache
        frame_cache = cv2.resize(frame_cache, (256, 256))
        name_fecha = "images/" + str(datetime.datetime.now()) + ".JPG"
        cv2.imwrite(name_fecha, frame_cache)
        self.start_video()

    def salir(self):
        sys.exit(app.exec_())

class Work(QThread):
    Imageupd = pyqtSignal(QImage)

    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(0)
        global stop
        stop = False
        while self.hilo_corriendo:
            ret, frame = cap.read()
            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            flip = cv2.flip(Image, 1)
            convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(640, 512, Qt.KeepAspectRatio)
            self.Imageupd.emit(pic)

            if stop:
                global frame_cache
                frame_cache = frame
                #cv2.imwrite("foto.png", frame)
                break

        cap.release()

#Inicio de la interfaz
if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = app_VRU()
    mainWindow.show()
    sys.exit(app.exec_())