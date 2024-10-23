import cv2
from PIL import Image,ImageTk
import numpy as np
import os

def train():
    data_dir=("Data")
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    #print(path)

    faces=[]
    ids=[]

    for image in path:
        img=Image.open(image).convert('L')   #gray scale image
        imagenp=np.array(img,'uint8')
        id=int(os.path.split(image)[1].split('.')[1])

        faces.append(imagenp)
        ids.append(id)
    #print(ids)
        cv2.imshow("Training",imagenp)
        cv2.waitKey(1)==13
        cv2.destroyAllWindows()
    ids=np.array(ids)

    #traing the clasifier
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("clasifier.xml")
    cv2.destroyAllWindows()

