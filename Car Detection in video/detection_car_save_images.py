# -*- coding: utf-8 -*-

import cv2
print('Project Topic : Vehicle Classification')
print('Research Internship on Machine learning using Images')
print('By Aditya Yogish Pai and Aditya Baliga B')
i=0
cascade_src = 'cars.xml'

video_src = 'videoplayback.mp4'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, img = cap.read()
   
    if (type(img) == type(None)):
        break
    else:
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
      cars = car_cascade.detectMultiScale(gray, 1.1, 2)


      for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        filename=str(i)+'.png'
        cv2.imwrite(filename, img)
        #cv2.imshow('video', img)
        print(filename)
      i=i+1
    
   
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
