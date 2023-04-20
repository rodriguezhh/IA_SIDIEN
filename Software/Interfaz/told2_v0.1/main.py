import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QIcon, QImage, QPixmap, QFont
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import numpy as np
import datetime
import tensorflow as tf
from tensorflow import keras

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
        self.predictions = []

        self.ui.detec_ic.clicked.connect(self.predict)
        self.ui.take_ph.clicked.connect(self.takeph)
        self.ui.retake_ph.clicked.connect(self.start_video)
        self.ui.close.clicked.connect(self.salir)
        self.ui.redetec_ic.clicked.connect(self.start_video)

    def Imageupd_slot(self, Image):
        self.ui.cam.setPixmap(QPixmap.fromImage(Image))
        
    def start_video(self):
        
        self.ui.detec_ic.hide()
        self.ui.detec_tex.hide()
        self.ui.retake_ph.hide()
        self.ui.retake_ph_tex.hide()
        self.ui.redetec_ic.hide()
        self.ui.redetec_tex.hide()

        self.ui.take_ph.show()
        self.ui.take_ph_tex.show()

        self.ui.result.clear()
        self.ui.comment.clear()

        self.Work = Work()
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
        
    def takeph(self):
        self.ui.detec_ic.show()
        self.ui.detec_tex.show()
        self.ui.retake_ph.show()
        self.ui.retake_ph_tex.show()

        self.ui.take_ph.hide()
        self.ui.take_ph_tex.hide()

        global stop
        stop = True
        #self.ui.cam.clear()

    def predict(self):

        self.ui.retake_ph.hide()
        self.ui.retake_ph_tex.hide()
        self.ui.detec_ic.hide()
        self.ui.detec_tex.hide()
        self.ui.redetec_ic.show()
        self.ui.redetec_tex.show()

        global frame_cache
        frame_cache = cv2.resize(frame_cache, (224, 224))

        model_1 = keras.models.load_model('modelo_ResNet50.h5')
        img = frame_cache.astype(np.uint8)
        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
        self.predictions = model_1.predict(img)

        result = np.argmax(self.predictions)
        percent = round(self.predictions[0,result]*100)

        if result == 0:
            res = str(percent) + '% Tizón Temprano'
            comment = 'Se recomienda que consulte a su agronomo asesor de confianza'

        elif result == 1:
            res = str(percent) + '% Tizón tardío'
            comment = 'Se recomienda que consulte a su agronomo asesor de confianza'

        elif result == 2:
            res = str(percent) + '% Hoja sana'
            comment = 'Felicidades su planta está sana'

        else:
            res = str(percent) + '% Virus del mosaico'
            comment = 'Se recomienda que consulte a su agronomo asesor de confianza'

        self.ui.result.setStyleSheet("color: white;")
        self.ui.result.setText(res)

        font = QFont()
        font.setPointSize(20)
        self.ui.result.setFont(font)

        self.ui.comment.setStyleSheet("color: white;")
        self.ui.comment.setText(comment)
        self.ui.comment.setWordWrap(True)

        font1 = QFont()
        font1.setPointSize(15)
        self.ui.comment.setFont(font1)

        name_fecha_img = "detections/" + str(datetime.datetime.now()) + ".JPG"
        name_fecha_tex = "detections/" + str(datetime.datetime.now()) + ".txt"
        with open(name_fecha_tex, "w") as file:
            file.write(res)
        cv2.imwrite(name_fecha_img, frame_cache)

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
            pic = convertir_QT.scaled(600, 450, Qt.KeepAspectRatio)
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