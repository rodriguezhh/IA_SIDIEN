import sys
import cv2
import psutil
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

        self.level = psutil.sensors_battery().percent
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.ui.label.setText(str(self.level)+"%")

        self.ui.save_ph.clicked.connect(self.saveph)
        self.ui.take_ph.clicked.connect(self.takeph)
        self.ui.retake_ph.clicked.connect(self.start_video)
        self.ui.close.clicked.connect(self.salir)

    def paintEvent(self, event):
        pass
    def update(self):
        self.level = psutil.sensors_battery().percent
        self.ui.label.setText(str(self.level)+"%")

    def Imageupd_slot(self, Image):
        self.ui.cam.setPixmap(QPixmap.fromImage(Image))
        
    def start_video(self):

        self.ui.save_ph.hide()
        self.ui.save_ph_tex.hide()
        self.ui.retake_ph.hide()
        self.ui.retake_ph_text.hide()

        self.ui.take_ph.show()
        self.ui.take_ph_tex.show()

        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
        
    def takeph(self):
        self.ui.save_ph.show()
        self.ui.save_ph_tex.show()
        self.ui.retake_ph.show()
        self.ui.retake_ph_text.show()

        self.ui.take_ph.hide()
        self.ui.take_ph_tex.hide()

        global stop
        stop = True
        #self.ui.cam.clear()

    def saveph(self):
        global frame_cache
        name_fecha = "images/" + str(datetime.datetime.now()) + ".png"
        cv2.imwrite(name_fecha, frame_cache)
        self.start_video()

    def salir(self):
        sys.exit(app.exec_())

class Work(QThread):
    Imageupd = pyqtSignal(QImage)

    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)480, height=(int)480,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !  appsink")
        global stop
        stop = False
        while self.hilo_corriendo:
            ret, frame = cap.read()
            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            flip = cv2.flip(Image, 1)
            convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
            pic = convertir_QT.scaled(480, 480, Qt.KeepAspectRatio)
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
