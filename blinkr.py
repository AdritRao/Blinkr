from scipy.spatial import distance
from gtts import gTTS
import playsound
import time
import dlib
import cv2
import sys
import os

## Blink count variable to count number of blinks
blink_count = 0

def speak(text: str):
    tts = gTTS(text=text, lang="en")
    filename = "sound.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear_aspect_ratio = (A+B)/(2.0*C)
	return ear_aspect_ratio

## This is if you are using a Web Cam. If 0 does not work change it to 1.
cam = cv2.VideoCapture(0)

## This is if you are using a Raspberry Pi Camera V2.
# cam = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

start = time.time()

## Timer while loop -- code will restart after time is up
while time.time() - start < 60:

    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = hog_face_detector(gray)
    for face in faces:

        face_landmarks = dlib_facelandmark(gray, face)
        leftEye = []
        rightEye = []
        ## Left eye detection
        for n in range(36,42):
        	x = face_landmarks.part(n).x
        	y = face_landmarks.part(n).y
        	leftEye.append((x,y))
        	next_point = n+1
        	if n == 41:
        		next_point = 36
        	x2 = face_landmarks.part(next_point).x
        	y2 = face_landmarks.part(next_point).y
        	cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        ## Right eye detection
        for n in range(42,48):
        	x = face_landmarks.part(n).x
        	y = face_landmarks.part(n).y
        	rightEye.append((x,y))
        	next_point = n+1
        	if n == 47:
        		next_point = 42
        	x2 = face_landmarks.part(next_point).x
        	y2 = face_landmarks.part(next_point).y
        	cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)

        EAR = (left_ear+right_ear)/2
        EAR = round(EAR,2)
        ## Check Eye Aspect Ratio for blink
        if EAR < 0.26:
            cv2.putText(frame, "Blink", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 4)
            blink_count = blink_count + 1
            print("Blinked " + str(blink_count))


    cv2.imshow("Blinkr", frame)

    key = cv2.waitKey(1)
    if key == 'q':
        break
## Check blink count after time is up
else:
    if blink_count >= 10:
        print("Good, keep blinking")
        blink_count = 0
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        speak("Blink more please")
        blink_count = 0
        os.execl(sys.executable, sys.executable, *sys.argv)

cam.release()
cv2.destroyAllWindows()
