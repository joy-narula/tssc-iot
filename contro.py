from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtCore import QThread, QTimer, Qt, pyqtSignal, QTime
from mainscreen import Ui_MainWindow
from pyzbar.pyzbar import decode
import time
import numpy as np
import sys
import cv2 as cv
import time

targetTime = 0
detected = 0
print("global- ",targetTime)
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btnSignals()
        
    def btnSignals(self):
        self.btnStart.clicked.connect(self.startCam)
        self.btnStop.clicked.connect(self.stopCam)
        self.btnProductSub.clicked.connect(self.updateProduct)
        self.btnTime.clicked.connect(self.timeSet)

    def timeSet(self):
        global targetTime
        
        targetTime = self.lineTime.text()
        print("setvalue ", targetTime)
        self.labelTargetTime.setText(
            "Target Time - " + str(targetTime) + " m")
        self.labelTargetTime.adjustSize()
        

    def updateProduct(self):
        self.productName = self.lineProductName.text()
        self.labelProductName.setText("Product: " + str(self.productName))
        self.labelProductName.adjustSize()

    def updateProgress(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 1
            self.progressBar.setValue(value)
        else:
            self.timer.stop()

    def increment(self, value):
        self.progressBar.setValue(value)

    def progressThread(self):
        self.thread = ProgressThread()
        self.thread.countSignal.connect(self.increment)
        self.thread.start()

    def timeThread(self):
        self.timeThr = TimeThread()
        self.timeThr.timeSignal.connect(self.timeVal)
        self.timeThr.remaintimeSignal.connect(self.remainTimeVal)
        self.timeThr.start()

    def remainTimeVal(self, remainti):
        self.remain = remainti
        self.numRemainTime.setText(remainti)
        self.numRemainTime.adjustSize()

    def timeVal(self, tim):
        self.numElapsedTime.setText(tim)
        self.numElapsedTime.adjustSize()
        self.elapsedTime = tim

    def startCam(self):
        print("clicked")
        global detected


        self.cap = cv.VideoCapture(-1)

        prev_frame_time = 0

        new_frame_time = 0

        codeList = []

        i = 0

        #print("Default Resolution : " + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)) + "*" + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)))
        # easycv.trackbar(1,255,0,255)

        while self.cap.isOpened():
            ret, frame = self.cap.read()

            if ret == True:
                frm = frame.copy()
                frm2 = frame.copy()
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                equalized = clahe.apply(gray)

                edge = cv.Laplacian(equalized, ddepth=cv.CV_8U,
                                    ksize=3, scale=1, delta=0)
                #lower, upper = easycv.trackbarPos()

                lateralBlur = cv.bilateralFilter(edge, 13, 50, 50)

                # qrcode - 120 -- barcode - 100
                ret, clearthresh = cv.threshold(lateralBlur, 120, 255, 0)
                # qrcode - 21,21 -- barcode - 25,1
                kernel = cv.getStructuringElement(cv.MORPH_RECT, (21, 21))
                thresh = cv.morphologyEx(clearthresh, cv.MORPH_CLOSE, kernel)
                # qrcode-9 -- barcode - 10
                thresh = cv.erode(thresh, None, iterations=8)
                # qrcode-6 -- barcode - 8
                thresh = cv.dilate(thresh, None, iterations=6)

                cnts, _ = cv.findContours(
                    thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                if len(cnts) > 0:
                    for j in range(len(cnts)):
                        cnt = sorted(cnts, key=cv.contourArea, reverse=True)[j]
                        if (cv.contourArea(cnt)) > 4000:

                            rect = cv.minAreaRect(cnt)
                            box = np.int0(cv.boxPoints(rect))
                            cv.drawContours(frm, [box], -1, (255, 0, 0), 3)
                            barframe = equalized[box[1][1]:box[3]
                                                 [1]+10, box[1][0]: box[3][0]+10]
                            if np.sum(barframe) == 0:
                                continue
                            else:
                                closed = cv.morphologyEx(barframe, cv.MORPH_CLOSE, cv.getStructuringElement(
                                    cv.MORPH_RECT, (1, 1)))  # qrcode - 1,1 barcode - 1,3
                                _, thresh2 = cv.threshold(
                                    closed, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
                                if thresh2 is not None:
                                    resizedBar = cv.resize(
                                        thresh2, (180, 180), interpolation=cv.INTER_AREA)
                                #cv.imshow("barcodeClosed", closed)
                                    cv.imshow("corrected", resizedBar)

                                    flag = 0
                                    for barcode in decode(thresh2):
                                        code = barcode.data.decode('utf-8')
                                        if code != "":
                                            codes = code.split()
                                            self.mainCode = codes[0]
                                        if len(codes) > 1:
                                            self.unit = codes[3]

                                        if self.mainCode[:2] == "TS":
                                            if codeList == []:
                                                codeList.append(self.mainCode)
                                                detected = 1
                                                self.updateJob()
                                                self.progressThread()
                                                self.timeThread()
                                                print(codeList)
                                            else:
                                                for co in codeList:
                                                    if self.mainCode == co:
                                                        flag = flag + 1
                                                if flag < 1:
                                                    codeList.append(
                                                        self.mainCode)
                                                    self.updateJob()
                                                    print(codeList)

            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            fps = int(fps)
            fps = str(fps)

            cv.putText(frm, fps, (7, 70), cv.FONT_HERSHEY_SIMPLEX,
                       3, (200, 100, 50), 3, cv.LINE_AA)
            small = cv.resize(frm, None, fx=0.5, fy=0.5,
                              interpolation=cv.INTER_AREA)
            smallNormal = cv.resize(
                frm2, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

            threshSmall = cv.resize(thresh, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
            cv.imshow("frame", small)
            cv.imshow("Normal Frame", smallNormal)
            cv.imshow("theash", threshSmall)

            cv.waitKey(1)
            

    def stopCam(self):
        self.cap.release()
        cv.destroyAllWindows()

    def updateJob(self):
        self.labelBarcode.setText(self.mainCode)
        self.labelJobNum.setText("Job No. - " + str(self.mainCode))
        self.labelJobNum.adjustSize()


class ProgressThread(QThread):

    countSignal = pyqtSignal(int)
    count = 0
    secs = 0
    mins = 0
    print("global-", count)
    def __init__(self):
        global count
        global interval
        secs = 0
        mins = 0
        super(ProgressThread, self).__init__()
        interval = int(((int(targetTime)*60)/100)*1000)
        print("interval-", interval)
        if int(targetTime)>0:
            count = int((secs + (mins*60))/(interval/1000))
            print("init-", count)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(interval)

    # def run(self):
    #     print("inside progress thread-  ", targetTime)
    #     if int(targetTime)>0:
    #         interval = (int(targetTime)*60)/100
    #         count = int((secs + (mins*60))/interval)
    #         while count < 101:
    #             self.countSignal.emit(count)
    #             time.sleep(interval)
    #             count=count+1
    
    def progress(self):
        global count
        global interval
        if int(targetTime)>0 and detected == 1:
            interval = int(((int(targetTime)*60)/100)*1000)
            count = int((secs + (mins*60))/(interval/1000))
            print("init-", count)

            if count>99:
                self.timer.stop()
            self.countSignal.emit(count)
            count=count+1
            print("inc-", count)



class TimeThread(QThread):
    timeSignal = pyqtSignal(str)
    remaintimeSignal = pyqtSignal(str)

    def __init__(self):
        super(TimeThread, self).__init__()
        self.currentTime = QtCore.QTime(00, 00, 00)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        

    def showTime(self):
        global mins
        global secs
        self.currentTime = self.currentTime.addSecs(1)
        timeStr = self.currentTime.toString("hh:mm:ss")
        self.timeSignal.emit(timeStr)

        
        mins = int(timeStr[3:5])
        secs = int(timeStr[6:])
        print("inside timer thread-  ", targetTime)
        if int(targetTime) > 0 and mins >=int(targetTime):
            remainTimeStr = "00:00:00"
            self.remaintimeSignal.emit(remainTimeStr)
        elif int(targetTime) > 0 and (mins > 0 or secs > 0):
            remainTimeSecs = 60 - secs
            remainTimeMins = (int(targetTime)-1) - mins
            if remainTimeMins<10 and remainTimeSecs<10:
                remainTimeStr = "00:" + "0"+str(remainTimeMins) + ":" + "0" + str(remainTimeSecs)
            elif remainTimeSecs<10:
                remainTimeStr = "00:" + str(remainTimeMins) + ":" + "0" + str(remainTimeSecs)
            elif remainTimeMins<10:
                remainTimeStr = "00:" + "0"+str(remainTimeMins) + ":" + str(remainTimeSecs)
            else:
                remainTimeStr = "00:" + str(remainTimeMins) + ":" + str(remainTimeSecs)
            self.remaintimeSignal.emit(remainTimeStr)
        
        # self.upTime.setTime(self.curr_time))

    def stop(self):
        self.terminate()
        print("time thread terminated")

    # def __del__(self):
    #     self.wait()
    # def handleTimer(self):
    #     if self.count <100:
    #         self.count += 1
    #         print(self.count)
    #         self.countSignal.emit(self.count)
    #     else:
    #         self.timer.stop()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
