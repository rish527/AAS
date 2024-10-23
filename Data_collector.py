import cv2
import numpy as np



fc=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def face_croped(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting into black & white photo
    faces=fc.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        f_crop=img[y:y+h,x:x+w]  #croping out face
        return f_crop


def capture(id):
    cap=cv2.VideoCapture(0)
    img_id=0
    while True:
        ret,fr=cap.read()
        if face_croped(fr) is not None:
            img_id+=1
            face=cv2.resize(face_croped(fr),(450,450))  #resizing the croped faces into passpord size photo
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),0,2,(0,255,0),2)
            cv2.imshow("Croped",face)

        if (cv2.waitKey(1)==13) or (int(img_id)==200):
            break

    cap.release()
    cv2.destroyAllWindows()

   