import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Test")
        self.label = QLabel(self)
        self.setCentralWidget(self.label)

        # Inicializar la cámara
        self.cap = cv2.VideoCapture(0)
        self.timer = self.startTimer(1) # 1000ms = 1s
    
    def timerEvent(self, event):
        # Leer el frame de la cámara
        ret, frame = self.cap.read()
        # Convertir el frame a RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Crear una imagen a partir del frame
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # Mostrar la imagen en el label
        self.label.setPixmap(QPixmap.fromImage(qImg))
    def closeEvent(self, event):
        self.cap.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())