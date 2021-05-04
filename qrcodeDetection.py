import cv2 as cv
from pyzbar.pyzbar import decode
import pyzbar.pyzbar as pyzbar
import numpy as np

import time

# path = "ESPCN_x4.pb"

# sr = cv.dnn_superres.DnnSuperResImpl_create()
# sr.readModel(path)
# sr.setModel("espcn",4)

cap = cv.VideoCapture(-1)

prev_frame_time = 0

new_frame_time = 0
#print("Default Resolution : " + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)) + "*" + str(cap.get(cv.CV_CAP_PROP_FRAME_WIDTH)))

#easycv.trackbar(20,255,0,255)
i=0
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        frm = frame.copy()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        equalized = clahe.apply(gray)
        
        edge = cv.Laplacian(equalized, ddepth= cv.CV_8U, ksize = 3, scale = 1, delta = 0)
        #lower, upper = easycv.trackbarPos()
        #grad = easycv.sobelGrad(gray)
        #lateralBlur = cv.bilateralFilter(edge, 17, 50, 50)
        #blur = cv.medianBlur(lateralBlur, 1)
        #mean = cv.adaptiveThreshold(lateralBlur, 255, cv.ADAPTIVE_THRESH_MEAN_C, 1, 51,21)
        #gauss = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 1, (2*lower)+1,(2*upper)+1)
        ret, clearthresh = cv.threshold(edge, 140, 255, 0) 
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (15,15))
        thresh = cv.morphologyEx(clearthresh, cv.MORPH_CLOSE, kernel)
        thresh = cv.erode(thresh, None, iterations = 8)
        thresh = cv.dilate(thresh, None, iterations = 6)

        cnts,_ = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        bbox = []
        if len(cnts)>0:
            
            for cnt in cnts:
                area = cv.contourArea(cnt)
                x,y,w,h = cv.boundingRect(cnt)
                extent = area/(w*h)
            #cnt = sorted(cnts, key=cv.contourArea, reverse=True)[0]
            #print(cv.contourArea(cnt))
                if (extent>np.pi/5) and (area > 100):
                    # print("area- ", area)
                    rect = cv.minAreaRect(cnt)
                    box = np.int0(cv.boxPoints(rect))
                    #print("box", box)
                    bbox.append(box)
            bbox = sorted(bbox, key= cv.contourArea, reverse=True)[:1]
            for boxes in bbox:
                cv.drawContours(frm, [boxes], -1, (255,0,0), 2)
                if boxes[1][0]>boxes[3][0]:
                    barframe = equalized[boxes[1][1]-5:boxes[3][1]+5, boxes[3][0]-5: boxes[1][0]+5]
                elif boxes[3][1]<boxes[1][1]:
                    barframe = equalized[boxes[3][1]-5:boxes[1][1]+5, boxes[1][0]-5: boxes[3][0]+5]
                else:
                    barframe = equalized[boxes[1][1]-5:boxes[3][1]+5, boxes[1][0]-5: boxes[3][0]+5]
                
                
                if barframe.size>0:
                    
                    closed = cv.morphologyEx(barframe, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT, (1,1)))
                    
                    _, thresh2 = cv.threshold(closed, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)        
                        #resizedBarC = cv.resize(closed, (720,480))
                        #resizedBar = cv.resize(barframe, (720,480))
                    #cv.imshow("normal code", barframe)
                        
                    #cv.imshow("barcodeClosed", barframe)
                        #cv.imshow("barcodemean", threshnew)
                    
                    #finalbar = cv.resize(thresh2, (480,480), interpolation= cv.INTER_CUBIC)
                    # superResult = sr.upsample(thresh2)
                    # cv.imshow("Super", superResult)
                    cv.imshow("cubic", thresh2)

                    detections = pyzbar.decode(thresh2, symbols=[pyzbar.ZBarSymbol.QRCODE])
                    for barcode in detections:
                        code = barcode.data.decode('utf-8')
                        if code!="":
                            i+=1
                            print(code, " ---> Read -", i)
                            if i==1:
                                timer = time.time()
                else:
                    print(boxes)
                            

                            
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        fps = str(fps)

        cv.putText(frm, fps, (7,70), cv.FONT_HERSHEY_SIMPLEX, 3, (200,100,50), 3, cv.LINE_AA)

        cv.imshow("frame", frm)
        #cv.imshow("thresh", thresh)
        #cv.imshow("adaptg", gauss)
        #cv.imshow("afterfilterthresh", clearthresh)
        #cv.imshow("laplace", edge)
        #cv.imshow("bilateral", blur)
        if cv.waitKey(1) & 0xFF == ord('q'):
            finaltimer = time.time()
            rate = i/(finaltimer-timer)
            print(rate)
            break

cap.release()
cv.destroyAllWindows()
