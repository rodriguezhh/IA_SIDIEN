import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import numpy as np
import datetime
import os
import GUI
#import Jetson.GPIO as GPIO

# Clase de la interfaz de usuario
class app_VRU(QtWidgets.QMainWindow):
    def __init__(self):
        # Cargar la interfaz de usuario
        super().__init__()
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TOLD2 IA")     # Establecer el título de la ventana principal
        self.start_video()                  # Iniciar la transmisión de video
        self.counter = 0                    # Contador de imágenes guardadas

        # Conectar los botones de la interfaz de usuario a sus funciones correspondientes
        self.ui.save_ph.clicked.connect(self.saveph)
        self.ui.take_ph.clicked.connect(self.takeph)
        self.ui.retake_ph.clicked.connect(self.start_video)
        self.ui.close.clicked.connect(self.salir)

    # Función para actualizar la imagen mostrada en la interfaz de usuario
    def Imageupd_slot(self, Image):
        self.ui.cam.setPixmap(QPixmap.fromImage(Image))

        carpeta = self.ui.cb.currentText() + "/"        # Incrementar el contador de imágenes guardadas
        elementos = os.listdir(carpeta)
        count = len(elementos)
        self.ui.cont.setStyleSheet("color: white;")     # Actualizar el texto de la etiqueta que muestra el número de imágenes guardadas
        self.ui.cont.setText(f"Muestras tomadas: {count}")
    
    # Función para iniciar la transmisión de video
    def start_video(self):

        self.ui.cb.setEnabled(True)
        
        # Ocultar los botones de guardar y volver a tomar la foto
        self.ui.save_ph.hide()
        self.ui.save_ph_tex.hide()
        self.ui.retake_ph.hide()
        self.ui.retake_ph_tex.hide()

        # Mostrar el botón de tomar la foto
        self.ui.take_ph.show()
        self.ui.take_ph_tex.show()

        self.Work = Work()                              # Crear un objeto de trabajo y comenzar su ejecución en un hilo separado
        self.Work.start()                               
        self.Work.Imageupd.connect(self.Imageupd_slot)  # Conectar la señal de actualización de imagen del objeto de trabajo a la función Imageupd_slot de la clase de interfaz

    # Función para tomar una foto
    def takeph(self):

        # Mostrar los botones de guardar y volver a tomar la foto
        self.ui.cb.setEnabled(False)
        self.ui.save_ph.show()
        self.ui.save_ph_tex.show()
        self.ui.retake_ph.show()
        self.ui.retake_ph_tex.show()

        # Ocultar el botón de tomar la foto
        self.ui.take_ph.hide()
        self.ui.take_ph_tex.hide()

        # Detener la transmisión de video estableciendo la variable stop a True
        global stop
        stop = True

    # Función para guardar una foto
    def saveph(self):

        self.ui.cb.setEnabled(False)
        global frame_cache                                             # Redimensionar la imagen guardada a 256x256 píxeles
        frame_cache = cv2.resize(frame_cache, (256, 256))
        dir = self.ui.cb.currentText()
        name_fecha = dir + "/" + str(datetime.datetime.now()) + ".JPG" # Crear un nombre de archivo único basado en la fecha y hora actual
        cv2.imwrite(name_fecha, frame_cache)                           # Guardar la imagen en el disco
        
        self.start_video()                                             # Reiniciar la transmisión de video

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