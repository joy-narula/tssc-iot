import cv2 as cv
import numpy as np

def trackbar(ll,lh,hl,hh):
    def nothing(x):
        return None

    cv.namedWindow('tuning')

    cv.createTrackbar('lower', 'tuning', ll , lh, nothing)
    cv.createTrackbar('upper', 'tuning', hl , hh, nothing)


def trackbarPos():
    lower = cv.getTrackbarPos('lower', "tuning")
    upper = cv.getTrackbarPos('upper', "tuning")
    
    return lower, upper

def sobelGrad(image, show="ok"):
    gradx = cv.Sobel(image, ddepth=cv.CV_64F, dx = 1, dy = 0, ksize = -1)
    
    grady = cv.Sobel(image, ddepth=cv.CV_64F, dx = 0, dy = 1, ksize = -1)
    
    if show=="all":
        cv.imshow("vertical", gradx)
        cv.imshow("horizontal", grady)

    grad = cv.subtract(gradx, grady)
    grad = cv.convertScaleAbs(grad)
    cv.imshow("Grad", grad)

    return grad
    
def camTest(id):
    cap = cv.VideoCapture(id)

    while cap.isOpened:
        ret, frame = cap.read()
        
        if ret:
            cv.imshow("webcam", frame)
            if cv.waitKey(1) & ord('q')==0xFF:
                break
        else:
            break

    cap.release()
    cv.destroyAllWindows()

