import cv2
import numpy as np
import os
import imutils
import keyboard
import RPi.GPIO as GPIO
import I2C_LCD_driver
from time import *
import RPi.GPIO as GPIO
import time

cap= cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#nombre=""
######################
pin_btn = 24
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode( GPIO.BCM )
GPIO.setup( pin_btn , GPIO.IN , pull_up_down=GPIO.PUD_UP )
######################
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()
def fotos():
    mylcd.lcd_clear()
    print("0")
    counts=0
    while True:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Nombre",1)
        mylcd.lcd_display_string("usuarios",2) 
        name=""
        print("")
        nombre=input()
        if counts==1:
            nombre="u"+nombre
        #time.sleep(1)
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Es correcto s/n",1)
        print("")
        mylcd.lcd_display_string("",2)
        mylcd.lcd_display_string(nombre,2)
        #time.sleep(2)
        print("")
        clave=input()
        if clave=='s':
            break
        if clave=='n':
            counts=1
    data= '/home/jmgarcia19/Desktop/Nuevo/Data'
    personPath= data+'/'+ nombre
    if not os.path.exists(personPath):
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Usuario creado",1)
        mylcd.lcd_display_string(nombre,2)
        time.sleep(2)
        os.makedirs(personPath)
    print("2")
    #cap= cv2.VideoCapture(0)
    #faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0
    while True:
        print("3")
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)
        k =  cv2.waitKey(1)
        print(count)
        if k == 27 or count >= 300:
            
            break
    cap.release()
    cv2.destroyAllWindows()
    dataPath = '/home/jmgarcia19/Desktop/Nuevo/Data'
    peopleList= os.listdir(data)
    mylcd.lcd_clear()
    #mylcd.lcd_display_string("Lista de personas",1)
    #mylcd.lcd_display_string(peopleList,2)
    labels= []
    faceData= []
    label=0
    for nameDir in peopleList:
        personPath= data+'/'+nameDir
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Leyendo las imagenes",1)
        
        for fileName in os.listdir(personPath):
            labels.append(label)
            faceData.append(cv2.imread(personPath+'/'+fileName,0))
        label= label+1
    face_recognizer= cv2.face.EigenFaceRecognizer_create()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Registrando...",1)
    
    face_recognizer.train(faceData, np.array(labels))
    face_recognizer.write('modeloEigenFace.xml')
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Registrado...",1)
    

def rec():
    dataPath='/home/jmgarcia19/Desktop/Nuevo/Data'
    imagePaths= os.listdir(dataPath)
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Listas...",1)
    mylcd.lcd_display_string(imagePaths,2)
    
    face_recognizer= cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read('modeloEigenFace.xml')
    cap=cv2.VideoCapture(0)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    while True:
        ret, frame= cap.read()
        if ret== False: break
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        auxFrame= gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            rostro= auxFrame[y:y+h,x:x+w]
            rostro=cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result= face_recognizer.predict(rostro)
            if result[1] < 5700:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            else:
                cv2.putText(frame,'Acceso denegado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                break
    cap.release()
    cv2-destroyAllWindows()



mylcd.lcd_clear()
while True:
    
    mylcd.lcd_display_string("Registrar u",1)
    mylcd.lcd_display_string("Boton login",2)
    #keyboard.wait('r')    
    if keyboard.is_pressed('u'):
        print("\n")
        os.system("clear")
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Registro",1)
        #time.sleep(1)
        fotos()
    elif GPIO.input( pin_btn ) == GPIO.LOW:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Verificar",1)
        time.sleep(1)
        rec()
    
