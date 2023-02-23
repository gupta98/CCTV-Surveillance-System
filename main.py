from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import os
import cv2
import threading
import getpass
import shutil

import functions as fn
from datetime import datetime as dt


class CamThread(threading.Thread):
    def __init__(self, guiOBJ):
        threading.Thread.__init__(self)
        self.guiOBJ = guiOBJ

    def run(self):
        cam1 = cv2.VideoCapture(self.guiOBJ.CAMERA1_PORT)
        cam2 = cv2.VideoCapture(self.guiOBJ.CAMERA2_PORT)
        cam3 = cv2.VideoCapture(self.guiOBJ.CAMERA3_PORT)
        cam4 = cv2.VideoCapture(self.guiOBJ.CAMERA4_PORT)

        while True:
            if self.guiOBJ.camera1_on:
                ret, frame1 = cam1.read()

                if self.guiOBJ.camera1_recording_on:
                    self.guiOBJ.camera1_video_writer.write(
                        fn.imageStretchAndBlurBigCamera(cv2.resize(frame1, (709, 403), interpolation=cv2.INTER_LINEAR)))
                    self.guiOBJ.lblCamera1RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                                            f"<html><head/><body><p><span style=\" color:#ff0004;\">{fn.secondToDay((self.guiOBJ.camera1_recording_started_at_time - dt.now()).total_seconds())}</span></p></body></html>",
                                                                                            None))

                frame1 = cv2.resize(frame1, (350, 197), interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(".\\__Images\\frame1.jpg", fn.imageStretchAndBlurNormalCamera(frame1, "Camera 1"))
                pix1 = QPixmap(".\\__Images\\frame1.jpg")
            else:
                pix1 = QPixmap(".\\__Images\\CameraOff.jpg")
            self.guiOBJ.lblCamera1.setPixmap(pix1)

            if self.guiOBJ.camera2_on:
                ret, frame2 = cam2.read()

                if self.guiOBJ.camera2_recording_on:
                    self.guiOBJ.camera2_video_writer.write(
                        fn.imageStretchAndBlurBigCamera(cv2.resize(frame2, (709, 403), interpolation=cv2.INTER_LINEAR)))
                    self.guiOBJ.lblCamera2RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                                            f"<html><head/><body><p><span style=\" color:#ff0004;\">{fn.secondToDay((self.guiOBJ.camera2_recording_started_at_time - dt.now()).total_seconds())}</span></p></body></html>",
                                                                                            None))

                frame2 = cv2.resize(frame2, (350, 197), interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(".\\__Images\\frame2.jpg", fn.imageStretchAndBlurNormalCamera(frame2, "Camera 2"))
                pix2 = QPixmap(".\\__Images\\frame2.jpg")
            else:
                pix2 = QPixmap(".\\__Images\\CameraOff.jpg")
            self.guiOBJ.lblCamera2.setPixmap(pix2)

            if self.guiOBJ.camera3_on:
                ret, frame3 = cam3.read()

                if self.guiOBJ.camera3_recording_on:
                    self.guiOBJ.camera3_video_writer.write(
                        fn.imageStretchAndBlurBigCamera(cv2.resize(frame3, (709, 403), interpolation=cv2.INTER_LINEAR)))
                    self.guiOBJ.lblCamera3RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                                            f"<html><head/><body><p><span style=\" color:#ff0004;\">{fn.secondToDay((self.guiOBJ.camera3_recording_started_at_time - dt.now()).total_seconds())}</span></p></body></html>",
                                                                                            None))

                frame3 = cv2.resize(frame3, (350, 197), interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(".\\__Images\\frame3.jpg", fn.imageStretchAndBlurNormalCamera(frame3, "Camera 3"))
                pix3 = QPixmap(".\\__Images\\frame3.jpg")
            else:
                pix3 = QPixmap(".\\__Images\\CameraOff.jpg")
            self.guiOBJ.lblCamera3.setPixmap(pix3)

            if self.guiOBJ.camera4_on:
                ret, frame4 = cam4.read()

                if self.guiOBJ.camera4_recording_on:
                    self.guiOBJ.camera4_video_writer.write(
                        fn.imageStretchAndBlurBigCamera(cv2.resize(frame4, (709, 403), interpolation=cv2.INTER_LINEAR)))
                    self.guiOBJ.lblCamera4RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                                            f"<html><head/><body><p><span style=\" color:#ff0004;\">{fn.secondToDay((self.guiOBJ.camera4_recording_started_at_time - dt.now()).total_seconds())}</span></p></body></html>",
                                                                                            None))

                frame4 = cv2.resize(frame4, (350, 197), interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(".\\__Images\\frame4.jpg", fn.imageStretchAndBlurNormalCamera(frame4, "Camera 4"))
                pix4 = QPixmap(".\\__Images\\frame4.jpg")
            else:
                pix4 = QPixmap(".\\__Images\\CameraOff.jpg")
            self.guiOBJ.lblCamera4.setPixmap(pix4)

            if self.guiOBJ.big_camera_on:
                if self.guiOBJ.big_camera_number == 1:
                    if self.guiOBJ.camera1_on:
                        ret, frame = cam1.read()
                        frame = cv2.resize(frame, (709, 403), interpolation=cv2.INTER_LINEAR)
                        cv2.imwrite(".\\__Images\\frame.jpg", fn.imageStretchAndBlurBigCamera(frame, "Camera 1"))
                        pix = QPixmap(".\\__Images\\frame.jpg")
                    else:
                        pix = QPixmap(".\\__Images\\BigCameraOff.jpg")
                elif self.guiOBJ.big_camera_number == 2:
                    if self.guiOBJ.camera2_on:
                        ret, frame = cam2.read()
                        frame = cv2.resize(frame, (709, 403), interpolation=cv2.INTER_LINEAR)
                        cv2.imwrite(".\\__Images\\frame.jpg", fn.imageStretchAndBlurBigCamera(frame, "Camera 2"))
                        pix = QPixmap(".\\__Images\\frame.jpg")
                    else:
                        pix = QPixmap(".\\__Images\\BigCameraOff.jpg")
                elif self.guiOBJ.big_camera_number == 3:
                    if self.guiOBJ.camera3_on:
                        ret, frame = cam3.read()
                        frame = cv2.resize(frame, (709, 403), interpolation=cv2.INTER_LINEAR)
                        cv2.imwrite(".\\__Images\\frame.jpg", fn.imageStretchAndBlurBigCamera(frame, "Camera 3"))
                        pix = QPixmap(".\\__Images\\frame.jpg")
                    else:
                        pix = QPixmap(".\\__Images\\BigCameraOff.jpg")
                else:
                    if self.guiOBJ.camera4_on:
                        ret, frame = cam4.read()
                        frame = cv2.resize(frame, (709, 403), interpolation=cv2.INTER_LINEAR)
                        cv2.imwrite(".\\__Images\\frame.jpg", fn.imageStretchAndBlurBigCamera(frame, "Camera 4"))
                        pix = QPixmap(".\\__Images\\frame.jpg")
                    else:
                        pix = QPixmap(".\\__Images\\BigCameraOff.jpg")
                self.guiOBJ.lblBigCamera.setPixmap(pix)


class ClickableQLabel(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ClickableQLabel, self).__init__(parent)
        self.ultimo = ""

    def mousePressEvent(self, event):
        self.ultimo = "Click"

    def mouseReleaseEvent(self, event):
        if self.ultimo == "Click":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(), self.performSingleClickAction)
        else:
            self.clicked.emit(self.ultimo)

    def mouseDoubleClickEvent(self, event):
        self.ultimo = "Double Click"

    def performSingleClickAction(self):
        if self.ultimo == "Click":
            self.clicked.emit(self.ultimo)


# noinspection PyUnresolvedReferences
class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self, parent)

        # Needed Data #
        self.CAMERA1_PORT = 0
        self.CAMERA2_PORT = 1
        self.CAMERA3_PORT = 2
        self.CAMERA4_PORT = 3

        self.camera1_image = None
        self.camera2_image = None
        self.camera3_image = None
        self.camera4_image = None
        self.big_camera_number = None

        self.camera1_on = True
        self.camera2_on = True
        self.camera3_on = True
        self.camera4_on = True
        self.big_camera_on = False

        # Recording #
        self.backup_path = f"C:\\Users\\{getpass.getuser()}\\Desktop\\"

        self.camera1_recording_on = False
        self.camera2_recording_on = False
        self.camera3_recording_on = False
        self.camera4_recording_on = False

        self.camera1_recording_time = 0
        self.camera2_recording_time = 0
        self.camera3_recording_time = 0
        self.camera4_recording_time = 0

        self.camera1_recording_started_at = ""
        self.camera2_recording_started_at = ""
        self.camera3_recording_started_at = ""
        self.camera4_recording_started_at = ""

        self.camera1_recording_started_at_time = None
        self.camera2_recording_started_at_time = None
        self.camera3_recording_started_at_time = None
        self.camera4_recording_started_at_time = None

        self.camera1_recording_ended_at = ""
        self.camera2_recording_ended_at = ""
        self.camera3_recording_ended_at = ""
        self.camera4_recording_ended_at = ""

        self.camera1_video_writer = None
        self.camera2_video_writer = None
        self.camera3_video_writer = None
        self.camera4_video_writer = None

        self.camera1_recording_path = ""
        self.camera2_recording_path = ""
        self.camera3_recording_path = ""
        self.camera4_recording_path = ""

        # Main Window Setup #
        self.setWindowTitle("CCTV Surveillance Control Box")
        self.setWindowIcon(QIcon(".\\__Images\\cctv_icon.png"))
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint)
        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(1001, 521)

        # Main Heading #
        self.lblCCTVSurveillanceController = QLabel(self)
        self.lblCCTVSurveillanceController.setGeometry(10, 10, 961, 71)
        lblCCTVSurveillanceController_font = QFont()
        lblCCTVSurveillanceController_font.setFamily("Rockwell")
        lblCCTVSurveillanceController_font.setPointSize(24)
        lblCCTVSurveillanceController_font.setBold(True)
        lblCCTVSurveillanceController_font.setWeight(75)
        self.lblCCTVSurveillanceController.setFont(lblCCTVSurveillanceController_font)
        self.lblCCTVSurveillanceController.setFrameShape(QFrame.Box)
        self.lblCCTVSurveillanceController.setScaledContents(True)
        self.lblCCTVSurveillanceController.setAlignment(Qt.AlignCenter)
        self.lblCCTVSurveillanceController.setText(
            QCoreApplication.translate("MainWindow", "CCTV Surveillance Control Box", None))

        # Cameras Frame #
        self.frmCameras = QFrame(self)
        self.frmCameras.setGeometry(QRect(10, 90, 728, 422))
        self.frmCameras.setFrameShape(QFrame.Box)
        self.frmCameras.setFrameShadow(QFrame.Raised)

        # Cameras & Button Inside CameraFrame #
        self.lblCamera1 = ClickableQLabel(self.frmCameras)
        self.lblCamera1.setGeometry(QRect(10, 10, 350, 197))
        self.lblCamera1.setFrameShape(QFrame.Box)
        self.lblCamera1.setTextFormat(Qt.RichText)
        self.lblCamera1.setScaledContents(True)
        self.lblCamera1.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.lblCamera2 = ClickableQLabel(self.frmCameras)
        self.lblCamera2.setGeometry(QRect(369, 10, 350, 197))
        self.lblCamera2.setFrameShape(QFrame.Box)
        self.lblCamera2.setTextFormat(Qt.RichText)
        self.lblCamera2.setScaledContents(True)
        self.lblCamera2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.lblCamera3 = ClickableQLabel(self.frmCameras)
        self.lblCamera3.setGeometry(QRect(10, 216, 350, 197))
        self.lblCamera3.setFrameShape(QFrame.Box)
        self.lblCamera3.setTextFormat(Qt.RichText)
        self.lblCamera3.setScaledContents(True)
        self.lblCamera3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.lblCamera4 = ClickableQLabel(self.frmCameras)
        self.lblCamera4.setGeometry(QRect(369, 216, 350, 197))
        self.lblCamera4.setFrameShape(QFrame.Box)
        self.lblCamera4.setTextFormat(Qt.RichText)
        self.lblCamera4.setScaledContents(True)
        self.lblCamera4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.lblBigCamera = ClickableQLabel(self.frmCameras)
        self.lblBigCamera.setGeometry(QRect(10, 10, 709, 403))
        self.lblBigCamera.setFrameShape(QFrame.Box)
        self.lblBigCamera.setTextFormat(Qt.RichText)
        self.lblBigCamera.setScaledContents(True)
        self.lblBigCamera.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lblBigCamera.setVisible(False)

        self.btnCloseBigCamera = QPushButton(self.frmCameras)
        self.btnCloseBigCamera.setObjectName(u"btnCloseBigCamera")
        self.btnCloseBigCamera.setGeometry(QRect(660, 360, 41, 41))
        btnCloseBigCamera_font = QFont()
        btnCloseBigCamera_font.setPointSize(30)
        btnCloseBigCamera_font.setBold(True)
        btnCloseBigCamera_font.setWeight(75)
        self.btnCloseBigCamera.setFont(btnCloseBigCamera_font)
        self.btnCloseBigCamera.setText(QCoreApplication.translate("MainWindow", u"\u2196", None))
        self.btnCloseBigCamera.setVisible(False)

        # Camera Controller Frame #
        self.frmOptions = QFrame(self)
        self.frmOptions.setGeometry(QRect(750, 90, 241, 422))
        self.frmOptions.setFrameShape(QFrame.Box)
        self.frmOptions.setFrameShadow(QFrame.Raised)

        # Group Boxes Inside Camera Controller Frame #
        # Group Box - Camera 1 #
        self.gbCamera1 = QGroupBox(self.frmOptions)
        self.gbCamera1.setGeometry(QRect(10, 20, 221, 81))
        gbCamera1_font = QFont()
        gbCamera1_font.setBold(True)
        gbCamera1_font.setWeight(75)
        self.gbCamera1.setFont(gbCamera1_font)
        self.gbCamera1.setFlat(False)
        self.gbCamera1.setCheckable(False)
        self.gbCamera1.setTitle(QCoreApplication.translate("MainWindow", "Camera 1", None))

        self.btnRecordOrStopRecordCamera1 = QPushButton(self.gbCamera1)
        self.btnRecordOrStopRecordCamera1.setGeometry(QRect(70, 50, 51, 23))
        btnRecordOrStopRecordCamera1_font = QFont()
        btnRecordOrStopRecordCamera1_font.setBold(False)
        btnRecordOrStopRecordCamera1_font.setWeight(50)
        self.btnRecordOrStopRecordCamera1.setFont(btnRecordOrStopRecordCamera1_font)
        self.btnRecordOrStopRecordCamera1.setText(QCoreApplication.translate("MainWindow", "Record", None))

        self.leCamera1RecordLocation = QLineEdit(self.gbCamera1)
        self.leCamera1RecordLocation.setGeometry(QRect(10, 21, 151, 20))
        self.leCamera1RecordLocation.setReadOnly(True)
        self.leCamera1RecordLocation.setEnabled(False)

        self.btnBrowseCamera1RecordLocation = QPushButton(self.gbCamera1)
        self.btnBrowseCamera1RecordLocation.setGeometry(QRect(170, 20, 21, 23))
        self.btnBrowseCamera1RecordLocation.setFont(btnRecordOrStopRecordCamera1_font)
        self.btnBrowseCamera1RecordLocation.setText(QCoreApplication.translate("MainWindow", "...", None))

        self.lblCamera1RecordingTimer = QLabel(self.gbCamera1)
        self.lblCamera1RecordingTimer.setGeometry(QRect(130, 51, 81, 20))
        lblCamera1RecordingTimer_font = QFont()
        lblCamera1RecordingTimer_font.setPointSize(10)
        lblCamera1RecordingTimer_font.setBold(False)
        lblCamera1RecordingTimer_font.setWeight(50)
        self.lblCamera1RecordingTimer.setFont(lblCamera1RecordingTimer_font)
        self.lblCamera1RecordingTimer.setTextFormat(Qt.RichText)
        self.lblCamera1RecordingTimer.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblCamera1RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                         "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                         None))
        self.lblCamera1RecordingTimer.setVisible(False)

        self.btnTurnOnOrOffCamera1 = QPushButton(self.gbCamera1)
        self.btnTurnOnOrOffCamera1.setGeometry(QRect(10, 50, 41, 23))
        self.btnTurnOnOrOffCamera1.setFont(btnRecordOrStopRecordCamera1_font)
        self.btnTurnOnOrOffCamera1.setText(QCoreApplication.translate("MainWindow", "Off", None))

        # Group Box - Camera 2 #
        self.gbCamera2 = QGroupBox(self.frmOptions)
        self.gbCamera2.setGeometry(QRect(10, 120, 221, 81))
        gbCamera2_font = QFont()
        gbCamera2_font.setBold(True)
        gbCamera2_font.setWeight(75)
        self.gbCamera2.setFont(gbCamera2_font)
        self.gbCamera2.setFlat(False)
        self.gbCamera2.setCheckable(False)
        self.gbCamera2.setTitle(QCoreApplication.translate("MainWindow", "Camera 2", None))

        self.btnRecordOrStopRecordCamera2 = QPushButton(self.gbCamera2)
        self.btnRecordOrStopRecordCamera2.setGeometry(QRect(70, 50, 51, 23))
        btnRecordOrStopRecordCamera2_font = QFont()
        btnRecordOrStopRecordCamera2_font.setBold(False)
        btnRecordOrStopRecordCamera2_font.setWeight(50)
        self.btnRecordOrStopRecordCamera2.setFont(btnRecordOrStopRecordCamera2_font)
        self.btnRecordOrStopRecordCamera2.setText(QCoreApplication.translate("MainWindow", "Record", None))

        self.leCamera2RecordLocation = QLineEdit(self.gbCamera2)
        self.leCamera2RecordLocation.setGeometry(QRect(10, 21, 151, 20))
        self.leCamera2RecordLocation.setReadOnly(True)
        self.leCamera2RecordLocation.setEnabled(False)

        self.btnBrowseCamera2RecordLocation = QPushButton(self.gbCamera2)
        self.btnBrowseCamera2RecordLocation.setGeometry(QRect(170, 20, 21, 23))
        self.btnBrowseCamera2RecordLocation.setFont(btnRecordOrStopRecordCamera2_font)
        self.btnBrowseCamera2RecordLocation.setText(QCoreApplication.translate("MainWindow", "...", None))

        self.lblCamera2RecordingTimer = QLabel(self.gbCamera2)
        self.lblCamera2RecordingTimer.setGeometry(QRect(130, 51, 81, 20))
        lblCamera2RecordingTimer_font = QFont()
        lblCamera2RecordingTimer_font.setPointSize(10)
        lblCamera2RecordingTimer_font.setBold(False)
        lblCamera2RecordingTimer_font.setWeight(50)
        self.lblCamera2RecordingTimer.setFont(lblCamera2RecordingTimer_font)
        self.lblCamera2RecordingTimer.setTextFormat(Qt.RichText)
        self.lblCamera2RecordingTimer.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblCamera2RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                         "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                         None))
        self.lblCamera2RecordingTimer.setVisible(False)

        self.btnTurnOnOrOffCamera2 = QPushButton(self.gbCamera2)
        self.btnTurnOnOrOffCamera2.setGeometry(QRect(10, 50, 41, 23))
        self.btnTurnOnOrOffCamera2.setFont(btnRecordOrStopRecordCamera2_font)
        self.btnTurnOnOrOffCamera2.setText(QCoreApplication.translate("MainWindow", "Off", None))

        # Group Box - Camera 3 #
        self.gbCamera3 = QGroupBox(self.frmOptions)
        self.gbCamera3.setGeometry(QRect(10, 220, 221, 81))
        gbCamera3_font = QFont()
        gbCamera3_font.setBold(True)
        gbCamera3_font.setWeight(75)
        self.gbCamera3.setFont(gbCamera3_font)
        self.gbCamera3.setFlat(False)
        self.gbCamera3.setCheckable(False)
        self.gbCamera3.setTitle(QCoreApplication.translate("MainWindow", "Camera 3", None))

        self.btnRecordOrStopRecordCamera3 = QPushButton(self.gbCamera3)
        self.btnRecordOrStopRecordCamera3.setGeometry(QRect(70, 50, 51, 23))
        btnRecordOrStopRecordCamera3_font = QFont()
        btnRecordOrStopRecordCamera3_font.setBold(False)
        btnRecordOrStopRecordCamera3_font.setWeight(50)
        self.btnRecordOrStopRecordCamera3.setFont(btnRecordOrStopRecordCamera3_font)
        self.btnRecordOrStopRecordCamera3.setText(QCoreApplication.translate("MainWindow", "Record", None))

        self.leCamera3RecordLocation = QLineEdit(self.gbCamera3)
        self.leCamera3RecordLocation.setGeometry(QRect(10, 21, 151, 20))
        self.leCamera3RecordLocation.setReadOnly(True)
        self.leCamera3RecordLocation.setEnabled(False)

        self.btnBrowseCamera3RecordLocation = QPushButton(self.gbCamera3)
        self.btnBrowseCamera3RecordLocation.setGeometry(QRect(170, 20, 21, 23))
        self.btnBrowseCamera3RecordLocation.setFont(btnRecordOrStopRecordCamera3_font)
        self.btnBrowseCamera3RecordLocation.setText(QCoreApplication.translate("MainWindow", "...", None))

        self.lblCamera3RecordingTimer = QLabel(self.gbCamera3)
        self.lblCamera3RecordingTimer.setGeometry(QRect(130, 51, 81, 20))
        lblCamera3RecordingTimer_font = QFont()
        lblCamera3RecordingTimer_font.setPointSize(10)
        lblCamera3RecordingTimer_font.setBold(False)
        lblCamera3RecordingTimer_font.setWeight(50)
        self.lblCamera3RecordingTimer.setFont(lblCamera3RecordingTimer_font)
        self.lblCamera3RecordingTimer.setTextFormat(Qt.RichText)
        self.lblCamera3RecordingTimer.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblCamera3RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                         "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                         None))
        self.lblCamera3RecordingTimer.setVisible(False)

        self.btnTurnOnOrOffCamera3 = QPushButton(self.gbCamera3)
        self.btnTurnOnOrOffCamera3.setGeometry(QRect(10, 50, 41, 23))
        self.btnTurnOnOrOffCamera3.setFont(btnRecordOrStopRecordCamera3_font)
        self.btnTurnOnOrOffCamera3.setText(QCoreApplication.translate("MainWindow", "Off", None))

        # Group Box - Camera 4 #
        self.gbCamera4 = QGroupBox(self.frmOptions)
        self.gbCamera4.setGeometry(QRect(10, 320, 221, 81))
        gbCamera4_font = QFont()
        gbCamera4_font.setBold(True)
        gbCamera4_font.setWeight(75)
        self.gbCamera4.setFont(gbCamera4_font)
        self.gbCamera4.setFlat(False)
        self.gbCamera4.setCheckable(False)
        self.gbCamera4.setTitle(QCoreApplication.translate("MainWindow", "Camera 4", None))

        self.btnRecordOrStopRecordCamera4 = QPushButton(self.gbCamera4)
        self.btnRecordOrStopRecordCamera4.setGeometry(QRect(70, 50, 51, 23))
        btnRecordOrStopRecordCamera4_font = QFont()
        btnRecordOrStopRecordCamera4_font.setBold(False)
        btnRecordOrStopRecordCamera4_font.setWeight(50)
        self.btnRecordOrStopRecordCamera4.setFont(btnRecordOrStopRecordCamera4_font)
        self.btnRecordOrStopRecordCamera4.setText(QCoreApplication.translate("MainWindow", "Record", None))

        self.leCamera4RecordLocation = QLineEdit(self.gbCamera4)
        self.leCamera4RecordLocation.setGeometry(QRect(10, 21, 151, 20))
        self.leCamera4RecordLocation.setReadOnly(True)
        self.leCamera4RecordLocation.setEnabled(False)

        self.btnBrowseCamera4RecordLocation = QPushButton(self.gbCamera4)
        self.btnBrowseCamera4RecordLocation.setGeometry(QRect(170, 20, 21, 23))
        self.btnBrowseCamera4RecordLocation.setFont(btnRecordOrStopRecordCamera4_font)
        self.btnBrowseCamera4RecordLocation.setText(QCoreApplication.translate("MainWindow", "...", None))

        self.lblCamera4RecordingTimer = QLabel(self.gbCamera4)
        self.lblCamera4RecordingTimer.setGeometry(QRect(130, 51, 81, 20))
        lblCamera4RecordingTimer_font = QFont()
        lblCamera4RecordingTimer_font.setPointSize(10)
        lblCamera4RecordingTimer_font.setBold(False)
        lblCamera4RecordingTimer_font.setWeight(50)
        self.lblCamera4RecordingTimer.setFont(lblCamera4RecordingTimer_font)
        self.lblCamera4RecordingTimer.setTextFormat(Qt.RichText)
        self.lblCamera4RecordingTimer.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lblCamera4RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                         "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                         None))
        self.lblCamera4RecordingTimer.setVisible(False)

        self.btnTurnOnOrOffCamera4 = QPushButton(self.gbCamera4)
        self.btnTurnOnOrOffCamera4.setGeometry(QRect(10, 50, 41, 23))
        self.btnTurnOnOrOffCamera4.setFont(btnRecordOrStopRecordCamera4_font)
        self.btnTurnOnOrOffCamera4.setText(QCoreApplication.translate("MainWindow", "Off", None))

        # Window is ready #

        self.leCamera1RecordLocation.setText(self.backup_path)
        self.leCamera1RecordLocation.setToolTip(self.backup_path)
        self.leCamera2RecordLocation.setText(self.backup_path)
        self.leCamera2RecordLocation.setToolTip(self.backup_path)
        self.leCamera3RecordLocation.setText(self.backup_path)
        self.leCamera3RecordLocation.setToolTip(self.backup_path)
        self.leCamera4RecordLocation.setText(self.backup_path)
        self.leCamera4RecordLocation.setToolTip(self.backup_path)

        self.handleButtons()
        self.startMonitoring()

    def handleButtons(self):
        self.lblCamera1.clicked.connect(self.lblCamera1Clicked)
        self.lblCamera2.clicked.connect(self.lblCamera2Clicked)
        self.lblCamera3.clicked.connect(self.lblCamera3Clicked)
        self.lblCamera4.clicked.connect(self.lblCamera4Clicked)
        self.lblBigCamera.clicked.connect(self.lblBigCameraClicked)
        self.btnCloseBigCamera.clicked.connect(self.btnCloseBigCameraClicked)

        self.btnTurnOnOrOffCamera1.clicked.connect(self.btnTurnOnOrOffCamera1Clicked)
        self.btnTurnOnOrOffCamera2.clicked.connect(self.btnTurnOnOrOffCamera2Clicked)
        self.btnTurnOnOrOffCamera3.clicked.connect(self.btnTurnOnOrOffCamera3Clicked)
        self.btnTurnOnOrOffCamera4.clicked.connect(self.btnTurnOnOrOffCamera4Clicked)

        self.btnBrowseCamera1RecordLocation.clicked.connect(self.btnBrowseCamera1RecordLocationClicked)
        self.btnBrowseCamera2RecordLocation.clicked.connect(self.btnBrowseCamera2RecordLocationClicked)
        self.btnBrowseCamera3RecordLocation.clicked.connect(self.btnBrowseCamera3RecordLocationClicked)
        self.btnBrowseCamera4RecordLocation.clicked.connect(self.btnBrowseCamera4RecordLocationClicked)

        self.btnRecordOrStopRecordCamera1.clicked.connect(self.btnRecordOrStopRecordCamera1Clicked)
        self.btnRecordOrStopRecordCamera2.clicked.connect(self.btnRecordOrStopRecordCamera2Clicked)
        self.btnRecordOrStopRecordCamera3.clicked.connect(self.btnRecordOrStopRecordCamera3Clicked)
        self.btnRecordOrStopRecordCamera4.clicked.connect(self.btnRecordOrStopRecordCamera4Clicked)

    def lblCamera1Clicked(self):
        self.lblCamera1.setVisible(False)
        self.lblCamera2.setVisible(False)
        self.lblCamera3.setVisible(False)
        self.lblCamera4.setVisible(False)

        self.big_camera_number = 1
        self.big_camera_on = True
        self.lblBigCamera.setVisible(True)

        self.btnCloseBigCamera.setVisible(True)

    def lblCamera2Clicked(self):
        self.lblCamera1.setVisible(False)
        self.lblCamera2.setVisible(False)
        self.lblCamera3.setVisible(False)
        self.lblCamera4.setVisible(False)

        self.big_camera_number = 2
        self.big_camera_on = True
        self.lblBigCamera.setVisible(True)

        self.btnCloseBigCamera.setVisible(True)

    def lblCamera3Clicked(self):
        self.lblCamera1.setVisible(False)
        self.lblCamera2.setVisible(False)
        self.lblCamera3.setVisible(False)
        self.lblCamera4.setVisible(False)

        self.big_camera_number = 3
        self.big_camera_on = True
        self.lblBigCamera.setVisible(True)

        self.btnCloseBigCamera.setVisible(True)

    def lblCamera4Clicked(self):
        self.lblCamera1.setVisible(False)
        self.lblCamera2.setVisible(False)
        self.lblCamera3.setVisible(False)
        self.lblCamera4.setVisible(False)

        self.big_camera_number = 4
        self.big_camera_on = True
        self.lblBigCamera.setVisible(True)

        self.btnCloseBigCamera.setVisible(True)

    def lblBigCameraClicked(self):
        self.lblCamera1.setVisible(True)
        self.lblCamera2.setVisible(True)
        self.lblCamera3.setVisible(True)
        self.lblCamera4.setVisible(True)

        self.lblBigCamera.setVisible(False)
        self.btnCloseBigCamera.setVisible(False)

    def btnCloseBigCameraClicked(self):
        self.lblCamera1.setVisible(True)
        self.lblCamera2.setVisible(True)
        self.lblCamera3.setVisible(True)
        self.lblCamera4.setVisible(True)

        self.lblBigCamera.setVisible(False)
        self.btnCloseBigCamera.setVisible(False)

    def btnTurnOnOrOffCamera1Clicked(self):
        if self.camera1_on:
            self.btnTurnOnOrOffCamera1.setText(QCoreApplication.translate("MainWindow", "On", None))
        else:
            self.btnTurnOnOrOffCamera1.setText(QCoreApplication.translate("MainWindow", "Off", None))
        self.camera1_on = not self.camera1_on

    def btnTurnOnOrOffCamera2Clicked(self):
        if self.camera2_on:
            self.btnTurnOnOrOffCamera2.setText(QCoreApplication.translate("MainWindow", "On", None))
        else:
            self.btnTurnOnOrOffCamera2.setText(QCoreApplication.translate("MainWindow", "Off", None))
        self.camera2_on = not self.camera2_on

    def btnTurnOnOrOffCamera3Clicked(self):
        if self.camera3_on:
            self.btnTurnOnOrOffCamera3.setText(QCoreApplication.translate("MainWindow", "On", None))
        else:
            self.btnTurnOnOrOffCamera3.setText(QCoreApplication.translate("MainWindow", "Off", None))
        self.camera3_on = not self.camera3_on

    def btnTurnOnOrOffCamera4Clicked(self):
        if self.camera4_on:
            self.btnTurnOnOrOffCamera4.setText(QCoreApplication.translate("MainWindow", "On", None))
        else:
            self.btnTurnOnOrOffCamera4.setText(QCoreApplication.translate("MainWindow", "Off", None))
        self.camera4_on = not self.camera4_on

    def btnBrowseCamera1RecordLocationClicked(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Folder To Save Recording From Camera 1')
        if path:
            path = path.replace('/', '\\') + '\\'
            self.leCamera1RecordLocation.setText(path)
            self.leCamera1RecordLocation.setToolTip(path)

    def btnBrowseCamera2RecordLocationClicked(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Folder To Save Recording From Camera 2')
        if path:
            path = path.replace('/', '\\') + '\\'
            self.leCamera2RecordLocation.setText(path)
            self.leCamera2RecordLocation.setToolTip(path)

    def btnBrowseCamera3RecordLocationClicked(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Folder To Save Recording From Camera 3')
        if path:
            path = path.replace('/', '\\') + '\\'
            self.leCamera3RecordLocation.setText(path)
            self.leCamera3RecordLocation.setToolTip(path)

    def btnBrowseCamera4RecordLocationClicked(self):
        path = QFileDialog.getExistingDirectory(self, 'Select Folder To Save Recording From Camera 4')
        if path:
            path = path.replace('/', '\\') + '\\'
            self.leCamera4RecordLocation.setText(path)
            self.leCamera4RecordLocation.setToolTip(path)

    def btnRecordOrStopRecordCamera1Clicked(self):
        if not self.camera1_recording_on:
            path = self.leCamera1RecordLocation.text()
            if not os.path.exists(path):
                QMessageBox.critical(self, "Invalid Path", "The path doesn't exist!", QMessageBox.Ok)
            else:
                self.camera1_recording_path = path
                self.camera1_video_writer = cv2.VideoWriter(f"{path}camera1.avi", cv2.VideoWriter_fourcc(*'MJPG'), 15,
                                                            (709, 403))
                self.camera1_recording_started_at = fn.nowToStr()
                self.camera1_recording_started_at_time = dt.now()
                self.btnRecordOrStopRecordCamera1.setText(QCoreApplication.translate("MainWindow", "Stop", None))
                self.lblCamera1RecordingTimer.setVisible(True)
                self.camera1_recording_on = True
        else:
            self.camera1_recording_on = False
            self.camera1_recording_ended_at = fn.nowToStr()
            self.btnRecordOrStopRecordCamera1.setText(QCoreApplication.translate("MainWindow", "Record", None))
            self.lblCamera1RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                             None))
            self.lblCamera1RecordingTimer.setVisible(False)

            self.camera1_video_writer.release()
            self.camera1_video_writer = None

            shutil.move(self.camera1_recording_path + "camera1.avi",
                        f"{self.camera1_recording_path}Camera 1 -- {self.camera1_recording_started_at} -- {self.camera1_recording_ended_at}.avi")
            QMessageBox.information(self, "Done!", "Recording saved successfully!", QMessageBox.Ok)

            self.camera1_recording_path = ""
            self.camera1_recording_started_at = ""
            self.camera1_recording_started_at_time = None
            self.camera1_recording_ended_at = ""

    def btnRecordOrStopRecordCamera2Clicked(self):
        if not self.camera2_recording_on:
            path = self.leCamera2RecordLocation.text()
            if not os.path.exists(path):
                QMessageBox.critical(self, "Invalid Path", "The path doesn't exist!", QMessageBox.Ok)
            else:
                self.camera2_recording_path = path
                self.camera2_video_writer = cv2.VideoWriter(f"{path}camera2.avi", cv2.VideoWriter_fourcc(*'MJPG'), 15,
                                                            (709, 403))
                self.camera2_recording_started_at = fn.nowToStr()
                self.camera2_recording_started_at_time = dt.now()
                self.btnRecordOrStopRecordCamera2.setText(QCoreApplication.translate("MainWindow", "Stop", None))
                self.lblCamera2RecordingTimer.setVisible(True)
                self.camera2_recording_on = True
        else:
            self.camera2_recording_on = False
            self.camera2_recording_ended_at = fn.nowToStr()
            self.btnRecordOrStopRecordCamera2.setText(QCoreApplication.translate("MainWindow", "Record", None))
            self.lblCamera2RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                             None))
            self.lblCamera2RecordingTimer.setVisible(False)

            self.camera2_video_writer.release()
            self.camera2_video_writer = None

            shutil.move(self.camera2_recording_path + "camera2.avi",
                        f"{self.camera2_recording_path}Camera 2 -- {self.camera2_recording_started_at} -- {self.camera2_recording_ended_at}.avi")
            QMessageBox.information(self, "Done!", "Recording saved successfully!", QMessageBox.Ok)

            self.camera2_recording_path = ""
            self.camera2_recording_started_at = ""
            self.camera2_recording_started_at_time = None
            self.camera2_recording_ended_at = ""

    def btnRecordOrStopRecordCamera3Clicked(self):
        if not self.camera3_recording_on:
            path = self.leCamera3RecordLocation.text()
            if not os.path.exists(path):
                QMessageBox.critical(self, "Invalid Path", "The path doesn't exist!", QMessageBox.Ok)
            else:
                self.camera3_recording_path = path
                self.camera3_video_writer = cv2.VideoWriter(f"{path}camera3.avi", cv2.VideoWriter_fourcc(*'MJPG'), 15,
                                                            (709, 403))
                self.camera3_recording_started_at = fn.nowToStr()
                self.camera3_recording_started_at_time = dt.now()
                self.btnRecordOrStopRecordCamera3.setText(QCoreApplication.translate("MainWindow", "Stop", None))
                self.lblCamera3RecordingTimer.setVisible(True)
                self.camera3_recording_on = True
        else:
            self.camera3_recording_on = False
            self.camera3_recording_ended_at = fn.nowToStr()
            self.btnRecordOrStopRecordCamera3.setText(QCoreApplication.translate("MainWindow", "Record", None))
            self.lblCamera3RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                             None))
            self.lblCamera3RecordingTimer.setVisible(False)

            self.camera3_video_writer.release()
            self.camera3_video_writer = None

            shutil.move(self.camera3_recording_path + "camera3.avi",
                        f"{self.camera3_recording_path}Camera 3 -- {self.camera3_recording_started_at} -- {self.camera3_recording_ended_at}.avi")
            QMessageBox.information(self, "Done!", "Recording saved successfully!", QMessageBox.Ok)

            self.camera3_recording_path = ""
            self.camera3_recording_started_at = ""
            self.camera3_recording_started_at_time = None
            self.camera3_recording_ended_at = ""

    def btnRecordOrStopRecordCamera4Clicked(self):
        if not self.camera4_recording_on:
            path = self.leCamera4RecordLocation.text()
            if not os.path.exists(path):
                QMessageBox.critical(self, "Invalid Path", "The path doesn't exist!", QMessageBox.Ok)
            else:
                self.camera4_recording_path = path
                self.camera4_video_writer = cv2.VideoWriter(f"{path}camera4.avi", cv2.VideoWriter_fourcc(*'MJPG'), 15,
                                                            (709, 403))
                self.camera4_recording_started_at = fn.nowToStr()
                self.camera4_recording_started_at_time = dt.now()
                self.btnRecordOrStopRecordCamera4.setText(QCoreApplication.translate("MainWindow", "Stop", None))
                self.lblCamera4RecordingTimer.setVisible(True)
                self.camera4_recording_on = True
        else:
            self.camera4_recording_on = False
            self.camera4_recording_ended_at = fn.nowToStr()
            self.btnRecordOrStopRecordCamera4.setText(QCoreApplication.translate("MainWindow", "Record", None))
            self.lblCamera4RecordingTimer.setText(QCoreApplication.translate("MainWindow",
                                                                             "<html><head/><body><p><span style=\" color:#ff0004;\">00:00:00:00</span></p></body></html>",
                                                                             None))
            self.lblCamera4RecordingTimer.setVisible(False)

            self.camera4_video_writer.release()
            self.camera4_video_writer = None

            shutil.move(self.camera4_recording_path + "camera4.avi",
                        f"{self.camera4_recording_path}Camera 4 -- {self.camera4_recording_started_at} -- {self.camera4_recording_ended_at}.avi")
            QMessageBox.information(self, "Done!", "Recording saved successfully!", QMessageBox.Ok)

            self.camera4_recording_path = ""
            self.camera4_recording_started_at = ""
            self.camera4_recording_started_at_time = None
            self.camera4_recording_ended_at = ""

    def startMonitoring(self):
        camThread = CamThread(self)
        camThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
