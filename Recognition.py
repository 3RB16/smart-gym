#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
from cv2 import *
from PIL import Image
import numpy as np
import cv2
import PIL
import ctypes
import time


# In[15]:


def createDataset ():
    count = 0
    count_id = 0
    size = 4
    i=1
    #haarcascade model
    fn_haar = "D:\\ana\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    #Full screen mode
    WINDOW_NAME = 'Full Integration'
    cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    #get screen size
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    fn_num = input("Enter the number of trainees: ")
    (im_width, im_height) = (112, 92)
    # creating the classier based on the haarcascade file
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    #clear dataset folder
    clearImgFile()
    
    s="Taking pictures for person:"
    while i <= int(fn_num):
        fn_id = input("Enter the Person's Id: ")
        #intialize video capture object to read video from built-in camera
        webcam = cv2.VideoCapture(0)
        #take 45 photo for each person
        while count_id < 45:
            (rval, im) = webcam.read()
            if rval == False:
                break
            if rval == True:
                #get image scale
                frame_height, frame_width, _ = im.shape

                scaleWidth = float(screen_width)/float(frame_width)
                scaleHeight = float(screen_height)/float(frame_height)

                if scaleHeight>scaleWidth:
                    imgScale = scaleWidth

                else:
                    imgScale = scaleHeight

                newX,newY = im.shape[1]*imgScale, im.shape[0]*imgScale
            #resize frame to fit full screen
            im = cv2.resize(im,(int(newX),int(newY)))
            cv2.putText(im,s+fn_id , (100, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
            #use haar_cascade to save the grayscale image with only the detected face
            #converting the image into grayscale as most of the processing is done in gray scale format
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            mini = cv2.resize(gray,(gray.shape[1]//size, gray.shape[0]//size))
            # It converts the images in different sizes
            #(decreases by 1.3 times) and 5 specifies the number of times scaling happens
            faces = haar_cascade.detectMultiScale(mini,1.3,5)
            faces = sorted(faces, key=lambda x: x[3])
            if faces:
                face_i = faces[0]
                (x, y, w, h) = [v * size for v in face_i]
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (im_width, im_height))
                # save images in the dataset folder
                cv2.imwrite("C:\\Users\\hp\\Pictures\\image3\\"+str(count)+"."+fn_id+'.jpg',face_resize)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(im, fn_id, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
                    1,(0, 255, 0))
                time.sleep(0.38)
                count += 1
                count_id +=1
                if count_id == 30:
                    s="Give some expressions person:"
            cv2.imshow(WINDOW_NAME, im)
            k = cv2.waitKey(10)
            if k == ord(' '):
                break
        webcam.release()
        cv2.destroyAllWindows()
        print(str(count) + " images taken and saved to " + fn_id +" folder in database ")
        count_id=0
        i +=1
        if k == ord(' '):
                break
    webcam.release()
    cv2.destroyAllWindows()


# In[16]:



def clearImgFile(): 
    path = "C:\\Users\\hp\\Pictures\\image3\\"
    filePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for filePath in filePaths:
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            print("The system cannot find the file specified")


# In[17]:


def getImageAndLabels(path):

    facesSamples=[]
    # creating empty ID list
    ids=[]
    # get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]

    face_detector = cv2.CascadeClassifier("D:\\ana\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        PIL_img = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        img_numpy = np.array(PIL_img,'uint8')
        
        faces = face_detector.detectMultiScale(img_numpy)
        # getting the Id from the image
        id = int(os.path.split(imagePath)[1].split('.')[0])

        for x,y,w,h in faces:
            ids.append(id)
            # extract the face from the training image sample
            facesSamples.append(img_numpy[y:y+h,x:x+w])

    print('id',id)
    print('fs:',facesSamples)
    return facesSamples,ids


# In[18]:


def TrainImages():
    # algorithm inside OpenCV module used for training the image dataset
    recognizer = cv2.cv2.face.LBPHFaceRecognizer_create() 
    # extract facial features
    faces, Id = getImageAndLabels("C:\\Users\\hp\\Pictures\\image3\\")
    #train model
    recognizer.train(faces, np.array(Id))
    # Save the model into trainer/trainer.yml
    recognizer.save("C:\\Users\\hp\\Pictures\\image3\\Trainer.yml")


# In[19]:


def face_detect(img,names,tts):
    global voice_g
    #dic -> key:id,value:circle centre
    idx={}
    rec={}
    rec1=()
    rec2=()
    
    recogizer = cv2.face.LBPHFaceRecognizer_create()
    # Reading the trained model
    recogizer.read("C:\\Users\\hp\\Pictures\\image3\\Trainer.yml")
    #converting the image into grayscale 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Creating the classier based on the haarcascade file.
    face_detector=cv2.CascadeClassifier("D:\\ana\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
    face=face_detector.detectMultiScale(gray,1.3,5)
    for x,y,w,h in face:
        print("len"+str(len(face)))
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)

        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        # If confidence is less them 100 ==> "0" : perfect match 
        if confidence < 100:
            idx.update({(x+w//2):int(names[str(ids)])})
            rec1=(x,y)
            rec2=(x+w,y+h)
            rec.update({int(names[str(ids)]):[rec1,rec2]})
            cv2.putText(img,str(names[str(ids)]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            s="welcome "+str(names[str(ids)])
            try:
                if  voice_g != s and tts != 2:
                    tts.SetVolume(50)
                    tts.Speak(s,1)
                    voice_g=s
            except NameError:voice_g=""
           
        else:
            cv2.putText(img, 'unknown', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)

    return idx,rec


# In[31]:


def test(names,tts):
    tts.SetVolume(50)
    tts.SetVoice(1)
    global voice_g
    idx={}
    
    recogizer = cv2.face.LBPHFaceRecognizer_create()
    # Reading the trained model
    recogizer.read("C:\\Users\\hp\\Pictures\\image3\\Trainer.yml")
    #full screen mode
    WINDOW_NAME = 'Full Integration'
    cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    # Creating the classier based on the haarcascade file.
    face_detector = cv2.CascadeClassifier("D:\\ana\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
    
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret_flag,frame = cap.read()
        if ret_flag == False:
            break
        if ret_flag == True:
            frame_height, frame_width, _ = frame.shape

            scaleWidth = float(screen_width)/float(frame_width)
            scaleHeight = float(screen_height)/float(frame_height)

            if scaleHeight>scaleWidth:
                imgScale = scaleWidth

            else:
                imgScale = scaleHeight

            newX,newY = frame.shape[1]*imgScale, frame.shape[0]*imgScale

            frame = cv2.resize(frame,(int(newX),int(newY)))
            #converting the image into grayscale 
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face=face_detector.detectMultiScale(gray,1.3,5)
            for x,y,w,h in face:
                cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
                cv2.circle(frame,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
                ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
                # If confidence is less them 100 ==> "0" : perfect match 
                if confidence < 100:
                    idx.update({(x+w//2):int(names[str(ids)])})
                    cv2.putText(frame,str(names[str(ids)]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
                    s="welcome "+str(names[str(ids)])
                    try:
                        if  voice_g != s:
                            tts.Speak(s,1)
                            voice_g=s
                    except NameError:voice_g=""
                    
                else:
                    cv2.putText(frame, 'unknown', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
                
            cv2.imshow(WINDOW_NAME, frame)
            if (cv2.waitKey(1) == ord('q')):
                tts.Stop()
                break
    cap.release()
    cv2.destroyAllWindows()


# In[21]:


def name():
    
    path ="C:\\Users\\hp\\Pictures\\image3\\"
    names = {}
    # get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('.',2)[0])
        # getting the Id from the image
        id = str(os.path.split(imagePath)[1].split('.',2)[1])
        names.update({name:id})
    return names


 




