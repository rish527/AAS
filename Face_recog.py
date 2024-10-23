import cv2
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime

#id=2001
def nam(id):
    conn=mysql.connector.connect(host="localhost",user="root",password="2005",database="aas")
    my_cur=conn.cursor()
    my_cur.execute("select Name from students where Id="+str(id))
    name=my_cur.fetchone()
    if name:  # Check if the query returned a result
        name = "+".join(name)  # Join the tuple into a string
 
    return name

def mark_attendance(id,name):
    with open("Attandence.csv","r+",newline="\n") as f:
        mydata=f.readlines()
        n_l=[]
        for line in mydata:
            entry=line.split(",")
            n_l.append(entry[0])
            
        if((str(id) not in n_l) and (name not in n_l)):
            
            now=datetime.now()
            d1=now.strftime("%d/%m/%Y")
            dtString=now.strftime("%H:%M:%S")
            f.writelines(f"\n{id},{name},{dtString},{d1},Present")


def face_recog():
    def boundray(img,clasifier,scalefactor,minneighbors,color,text,clf):

        #converting to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features=clasifier.detectMultiScale(gray,scalefactor,minneighbors)

        cord=[]

        for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
            id,predict=clf.predict(gray[y:y+w,x:x+w])
            confidence=int((100*(1-predict/300)))
            
            name=nam(id) #getting name from database
            
            if confidence>77:
                cv2.putText(img,name,(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),1)
                mark_attendance(id,name)

            else:
                cv2.putText(img,"Chutiya",(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1)

            cord=[x,y,w,h]

        return cord
    
    def recognize(img,clf,facecascade):
        cord=boundray(img,facecascade,1.1,10,(255,25,255),"Face",clf)
        return img
    
    facecascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read("clasifier.xml")

    video_cap=cv2.VideoCapture(0)
    while True:
        ret,img=video_cap.read()
        img=recognize(img,clf,facecascade)
        cv2.imshow("Face Recognition",img)

        if cv2.waitKey(1)==13:
            break
    video_cap.release()
    cv2.destroyAllWindows()

# face_recog()

