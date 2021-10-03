import cv2
import dropbox
import time

startTime = time.time()

def takeImage():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

while(True):
    if(time.time()-startTime > 20):
        takeImage()
    
    


