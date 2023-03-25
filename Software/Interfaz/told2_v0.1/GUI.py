# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'told2_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 331, 771))
        self.frame.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"border-color: rgba(191, 64, 64, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 10, 271, 109))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("image: url(:/logos/icons/told2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 120, 269, 126))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.take = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.take.setContentsMargins(0, 0, 0, 0)
        self.take.setObjectName("take")
        self.take_ph = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.take_ph.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.take_ph.setIcon(icon)
        self.take_ph.setIconSize(QtCore.QSize(80, 80))
        self.take_ph.setObjectName("take_ph")
        self.take.addWidget(self.take_ph)
        self.take_ph_tex = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.take_ph_tex.setFont(font)
        self.take_ph_tex.setObjectName("take_ph_tex")
        self.take.addWidget(self.take_ph_tex)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(30, 240, 271, 131))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.retake = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.retake.setContentsMargins(0, 0, 0, 0)
        self.retake.setObjectName("retake")
        self.retake_ph = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.retake_ph.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/retake.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retake_ph.setIcon(icon1)
        self.retake_ph.setIconSize(QtCore.QSize(80, 80))
        self.retake_ph.setObjectName("retake_ph")
        self.retake.addWidget(self.retake_ph)
        self.retake_ph_tex = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.retake_ph_tex.setObjectName("retake_ph_tex")
        self.retake.addWidget(self.retake_ph_tex)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 630, 271, 86))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.close = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.close.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon2)
        self.close.setIconSize(QtCore.QSize(30, 40))
        self.close.setObjectName("close")
        self.verticalLayout.addWidget(self.close)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 370, 271, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.detec = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.detec.setContentsMargins(0, 0, 0, 0)
        self.detec.setObjectName("detec")
        self.detec_ic = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.detec_ic.setEnabled(True)
        self.detec_ic.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/detection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detec_ic.setIcon(icon3)
        self.detec_ic.setIconSize(QtCore.QSize(80, 80))
        self.detec_ic.setObjectName("detec_ic")
        self.detec.addWidget(self.detec_ic)
        self.detec_tex = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.detec_tex.setObjectName("detec_tex")
        self.detec.addWidget(self.detec_tex)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(30, 500, 271, 131))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.redetec = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.redetec.setContentsMargins(0, 0, 0, 0)
        self.redetec.setObjectName("redetec")
        self.redetec_ic = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.redetec_ic.setEnabled(True)
        self.redetec_ic.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/redetec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redetec_ic.setIcon(icon4)
        self.redetec_ic.setIconSize(QtCore.QSize(80, 80))
        self.redetec_ic.setObjectName("redetec_ic")
        self.redetec.addWidget(self.redetec_ic)
        self.redetec_tex = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.redetec_tex.setObjectName("redetec_tex")
        self.redetec.addWidget(self.redetec_tex)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 130, 631, 581))
        self.frame_2.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"border-color: rgba(191, 64, 64, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.cam = QtWidgets.QLabel(self.frame_2)
        self.cam.setGeometry(QtCore.QRect(20, 10, 600, 450))
        self.cam.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cam.setText("")
        self.cam.setObjectName("cam")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 469, 601, 101))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(40, 40, 40);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 581, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.result = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout_2.addWidget(self.result)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comment = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.comment.setObjectName("comment")
        self.verticalLayout_4.addWidget(self.comment)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.cont = QtWidgets.QLabel(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(750, 0, 211, 31))
        self.cont.setStyleSheet("background-color: rgba(191, 64, 64, 0);")
        self.cont.setObjectName("cont")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 0, 621, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("image: url(:/logos/icons/uis.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setStyleSheet("image: url(:/logos/icons/CEMOS.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setStyleSheet("image: url(:/logos/icons/DICBoT.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.take_ph_tex.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TOMAR FOTO</span></p></body></html>"))
        self.retake_ph_tex.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">NUEVA FOTO</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">SALIR</span></p></body></html>"))
        self.detec_tex.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">DETECCION</span></p></body></html>"))
        self.redetec_tex.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">NUEVA DETECCION</span></p></body></html>"))
        self.comment.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.cont.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
import recursos_rc
