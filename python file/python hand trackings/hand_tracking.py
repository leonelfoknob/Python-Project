import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
	success, img = cap.read()
	imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			for id, lm in enumerate(handLms.landmark):
				#print(id,lm)
				h,w,c = img.shape
				cx, cy = int(lm.x*w), int(lm.y*h)
				#print(cx,cy)
				#cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
				if id == 2:#id max is 20 point of your hand
					cv2.circle(img,(cx+1,cy+1),10,(255,0,255),cv2.FILLED)
					cv2.putText(img,str(int(id)), (cx,cy),cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)

			mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)

	cTime = time.time()
	fps = 1/(cTime-pTime)
	pTime = cTime

	cv2.putText(img,str(int(fps)), (10,50),cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)
	cv2.imshow("video",img)
	#cv2.imshow("result",results)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()