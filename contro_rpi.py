from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtCore import QThread, QTimer, Qt, pyqtSignal, QTime
from mainscreen import Ui_MainWindow
from pyzbar.pyzbar import decode
import pyzbar.pyzbar as pyzbar
import time
import numpy as np
import sys
import cv2 as cv
import time

targetTime = 0
detected = 0



def my_excepthook(type, value, tback):
    # log the exception here

    # then call the default handler
    sys.__excepthook__(type, value, tback)
    
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
        self.btnUnitsSub.clicked.connect(self.updateCount)
        self.btnHold.clicked.connect(self.holdTimers)
        self.btnCon.clicked.connect(self.resumeTimers)

    def startCam(self):
        self.detect = DetectionThread()
        self.detect.codeSignal.connect(self.updateJob)
        self.detect.productSignal.connect(self.products)
        self.detect.progressThreadSig.connect(self.progressThread)
        self.detect.timeThreadSig.connect(self.timeThread)
        self.detect.startCam()
    
    def products(self, prductScanned):
        self.numCount.setText(str(productScanned))
        self.labelCount.setText("Units Count - " + str(productScanned))

    def holdTimers(self):
        if timer.isActive():

            timer.stop()
        if progressTimer.isActive():
            progressTimer.stop()
        
    def resumeTimers(self):
        if not timer.isActive():
            timer.start(1000)

        if not progressTimer.isActive():
            progressTimer.start(interval)

    def updateCount(self):
        global targetUnits
        targetUnits = self.lineUnits.text()
        self.numTarget.setText(targetUnits)

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

    def increment(self, value):
        self.progressBar.setValue(value)

    def progressThread(self, sig):
        
        self.thread = ProgressThread()
        self.thread.countSignal.connect(self.increment)
        self.thread.start()

    def timeThread(self, sig):
    
        self.timeThr = TimeThread()
        self.timeThr.timeSignal.connect(self.timeVal)
        self.timeThr.remaintimeSignal.connect(self.remainTimeVal)
        self.timeThr.extraTimeSignal.connect(self.extraTime)
        self.timeThr.start()

    def remainTimeVal(self, remainti):
        self.remain = remainti
        self.numRemainTime.setText(remainti)
        self.numRemainTime.adjustSize()

    def extraTime(self, extrati):
        self.extra = extrati
        self.numExtraTime.setText(extrati)
        self.numExtraTime.adjustSize()

    def timeVal(self, tim):
        self.elapsedTime = tim
        self.numElapsedTime.setText(tim)
        self.numElapsedTime.adjustSize()

    def stopCam(self):
        try:
            if self.thread.isRunning == True:
                self.thread.stop()
                
        except Exception:
            print("Progress bar is not Running")
        try:
            if self.timeThr.isRunning == True:
            
                self.timeThr.stop()
        except Exception:
            print("Timer is not Running")
        try:    
            if self.detect.isRunning == True:
                self.detect.stop()
        except Exception:
            print("Camera is not Running")

    def updateJob(self, code):
        self.labelBarcode.setText(code)
        self.labelJobNum.setText("Job No. - " + str(code))
        self.labelJobNum.adjustSize()


class DetectionThread(QThread):
    
    productSignal = pyqtSignal(int)
    codeSignal = pyqtSignal(str)
    progressThreadSig = pyqtSignal(int)
    timeThreadSig = pyqtSignal(int)
    camOn = 0
    check = 0
    def __init__(self):
        super(DetectionThread, self).__init__()
        self.isRunning = True
        global detectTimer
        detectTimer = QTimer(self)
        detectTimer.timeout.connect(self.runDetect)
        detectTimer.start(1000/24)

    def stop(self):
        
        self.codeList = []
        if detectTimer.isActive():
            detectTimer.stop()
        self.cap.release()
        cv.destroyAllWindows()
        self.camOn = 0
        self.isRunning = False
        
        self.terminate()
        print("vision thread termina")
    def startCam(self):
        self.cap = cv.VideoCapture(-1)
        if not detectTimer.isActive():
            print("yes")
            detectTimer.start(1000/24)
        if self.cap.isOpened():
            self.camOn = 1
        
    def runDetect(self):

        global detected
        global productScanned
        

        prev_frame_time = 0

        new_frame_time = 0

        self.codeList = []

        i = 0
              
        #print("Default Resolution : " + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)) + "*" + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)))
        # easycv.trackbar(1,255,0,255)

        if self.camOn == 1:
            
            ret, frame = self.cap.read()

            if ret == True:
                frm = frame.copy()
                frm2 = frame.copy()
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                equalized = clahe.apply(gray)

                edge = cv.Laplacian(equalized, ddepth=cv.CV_8U,
                                    ksize=3, scale=1, delta=0)

                #grad = easycv.sobelGrad(gray)
                #lateralBlur = cv.bilateralFilter(edge, 17, 50, 50)
                #blur = cv.medianBlur(lateralBlur, 1)
                #mean = cv.adaptiveThreshold(lateralBlur, 255, cv.ADAPTIVE_THRESH_MEAN_C, 1, 51,21)
                #gauss = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 1, (2*lower)+1,(2*upper)+1)
                ret, clearthresh = cv.threshold(edge, 140, 255, 0)
                kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
                thresh = cv.morphologyEx(clearthresh, cv.MORPH_CLOSE, kernel)
                thresh = cv.erode(thresh, None, iterations=8)
                thresh = cv.dilate(thresh, None, iterations=6)
 
                cnts, _ = cv.findContours(
                    thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                bbox = []
                if len(cnts) > 0:

                    for cnt in cnts:
                        area = cv.contourArea(cnt)
                        x, y, w, h = cv.boundingRect(cnt)
                        extent = area/(w*h)
                    #cnt = sorted(cnts, key=cv.contourArea, reverse=True)[0]
                    # print(cv.contourArea(cnt))
                        if (extent > np.pi/5) and (area > 100):
                            # print("area- ", area)
                            rect = cv.minAreaRect(cnt)
                            box = np.int0(cv.boxPoints(rect))
                            #print("box", box)
                            bbox.append(box)
                    bbox = sorted(bbox, key=cv.contourArea, reverse=True)[:1]
                    for boxes in bbox:
                        cv.drawContours(frm, [boxes], -1, (255, 0, 0), 2)
                        if boxes[1][0]>boxes[3][0]:
                            barframe = equalized[boxes[1][1]-7:boxes[3][1]+7, boxes[3][0]-7: boxes[1][0]+7]
                        elif boxes[3][1]<boxes[1][1]:
                            barframe = equalized[boxes[3][1]-7:boxes[1][1]+7, boxes[1][0]-7: boxes[3][0]+7]
                        else:
                            barframe = equalized[boxes[1][1]-7:boxes[3][1]+7, boxes[1][0]-7: boxes[3][0]+7]
                
                        # print(boxes)
                        if barframe.size > 0:

                            closed = cv.morphologyEx(
                                barframe, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT, (1, 1)))

                            _, thresh2 = cv.threshold(
                                closed, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

                            #finalbar = cv.resize(
                            #    thresh2, (480, 480), interpolation=cv.INTER_CUBIC)
                            # superResult = sr.upsample(thresh2)
                            # cv.imshow("Super", superResult)
                            cv.imshow("cubic", thresh2)
                            flag = 0
                            detections = pyzbar.decode(
                                thresh2, symbols=[pyzbar.ZBarSymbol.QRCODE])
                            for barcode in detections:
                                code = barcode.data.decode('utf-8')
                                codes = code.split()
                                self.mainCode = codes[0]
                                if len(codes) > 1:
                                    self.unit = codes[3]

                                if self.mainCode[:2] == "TS":
                                    if self.codeList == []:
                                        self.codeList.append(self.mainCode)
                                        #print(self.mainCode)
                                        self.codeSignal.emit(self.mainCode)
                                        detected = 1
                                        if self.check<1:
                                            self.progressThreadSig.emit(1)
                                            self.timeThreadSig.emit(1)
                                        self.check = 1
                                        #print(codeList)
                                        productScanned = len(self.codeList)
                                        self.productSignal.emit(productScanned)
                                    else:
                                        for co in self.codeList:
                                            if self.mainCode == co:
                                                flag = flag + 1
                                        if flag < 1:
                                            self.codeList.append(
                                                self.mainCode)
                                            self.codeSignal.emit(self.mainCode)
                                            #print(codeList)

            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            fps = int(fps)
            fps = str(fps)

            cv.putText(frm, fps, (7, 70), cv.FONT_HERSHEY_SIMPLEX,
                       3, (200, 100, 50), 3, cv.LINE_AA)
            small = cv.resize(frm, (240, 240),
                              interpolation=cv.INTER_AREA)
            smallNormal = cv.resize(
                frm2, (240, 240), interpolation=cv.INTER_AREA)

            threshSmall = cv.resize(
                thresh, (240, 240), interpolation=cv.INTER_AREA)
            cv.imshow("frame", small)
            cv.imshow("Normal Frame", smallNormal)
            #cv.imshow("theash", threshSmall)
            cv.waitKey(1)

class ProgressThread(QThread):

    countSignal = pyqtSignal(int)
    global secs
    global mins
    secs = 0
    mins = 0
    flag = 0
    count = 0
    def __init__(self):
        
        super(ProgressThread, self).__init__()
        self.isRunning = True
        global progressTimer
        interval = int(((int(targetTime)*60)/100)*1000)
        print("interval-", interval)
        
        progressTimer = QTimer(self)
        progressTimer.timeout.connect(self.progress)
        progressTimer.start(interval)

    def progress(self):
        
        global interval
        if int(targetTime) > 0 and self.flag == 0:
            interval = int(((int(targetTime)*60)/100)*1000)
            progressTimer.start(interval)
            self.count = int((secs + (mins*60))/(interval/1000))
            self.countSignal.emit(self.count)
            self.flag = 1
            if self.count > 99:
                progressTimer.stop()

        elif int(targetTime) > 0 and self.flag != 0:
            interval = int(((int(targetTime)*60)/100)*1000)
            self.count = self.count+1
            self.countSignal.emit(self.count)
            print("inc progress thread-", self.count)
            if self.count > 99:
                progressTimer.stop()

    def stop(self):
        if progressTimer.isActive():
            progressTimer.stop()
        self.isRunning = False
        self.count = 0
        
        #self.terminate()
        print("progress terminated")

class TimeThread(QThread):
    timeSignal = pyqtSignal(str)
    remaintimeSignal = pyqtSignal(str)
    extraTimeSignal = pyqtSignal(str)
    flag = 0

    def __init__(self):
        super(TimeThread, self).__init__()
        self.extraTime = QtCore.QTime(00, 00, 00)
        self.currentTime = QtCore.QTime(00, 00, 00)
        print("hellllll")
        global timer
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.isRunning = True

    def showTime(self):
        global mins
        global secs
        self.currentTime = self.currentTime.addSecs(1)
        self.timeStr = self.currentTime.toString("hh:mm:ss")
        self.timeSignal.emit(self.timeStr)
        mins = int(self.timeStr[3:5])
        secs = int(self.timeStr[6:])
        hours = int(self.timeStr[0:2])
        #print("inside timer thread-")
        if int(targetTime) > 0 and mins >= int(targetTime):
            remainTimeStr = "00:00:00"
            self.remaintimeSignal.emit(remainTimeStr)
            if self.flag > 0:
                self.extraTime = self.extraTime.addSecs(1)
                extraTimeStr = self.extraTime.toString("hh:mm:ss")
                self.extraTimeSignal.emit(extraTimeStr)
            self.flag = self.flag + 1
        elif int(targetTime) > 0 and (mins > 0 or secs > 0):
            remainTimeSecs = 60 - secs
            remainTimeMins = (int(targetTime)-1) - mins
            if remainTimeMins < 10 and remainTimeSecs < 10:
                remainTimeStr = "00:" + "0" + \
                    str(remainTimeMins) + ":" + "0" + str(remainTimeSecs)
            elif remainTimeSecs < 10:
                remainTimeStr = "00:" + \
                    str(remainTimeMins) + ":" + "0" + str(remainTimeSecs)
            elif remainTimeMins < 10:
                remainTimeStr = "00:" + "0" + \
                    str(remainTimeMins) + ":" + str(remainTimeSecs)
            else:
                remainTimeStr = "00:" + \
                    str(remainTimeMins) + ":" + str(remainTimeSecs)
            self.remaintimeSignal.emit(remainTimeStr)

    def stop(self):
        if timer.isActive():
            timer.stop()
        self.isRunning = False
        timeStr[3:5] = "00"
        timeStr[6:] = "00"
        timeStr[0:2] = "00"
        #self.terminate()

        print("time thread terminated")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #sys.excepthook = my_excepthook
    win = Main()
    win.show()
    sys.exit(app.exec_())
