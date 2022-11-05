import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()

while True:
	success,img = cap.read()
	imgout = segmentor.removeBG(img,(255,0,0),threshold=0.95)





	cv2.imshow('img', img)
	cv2.imshow('imgout', imgout)
	if cv2.waitKey(5) & 0xFF == 27:
		break
cap.release()