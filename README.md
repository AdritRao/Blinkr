# Blinkr
Jetson Nano AI Blink Detection and Reminder Project ⭐️ Awared the Jetson AI Specialist Award ⭐️

![ScreenShot](https://i.ibb.co/pQpCdX8/Are-tch-2.png)

## Inspiration for building Blinkr
As many studies show, while looking at a computer screen our blink rate reduces. We usually do not realize this. Not blinking can lead to unwanted side affects that we want to avoid. I wanted to find a way to make ourselves blink more while using the computer.

![ScreenShot](https://i.ibb.co/f2XzGk2/Are-tch-3.png)

## How Blinkr aims to solve this problem
Blinkr is a device that utlizes [AI (Artifical Intellegence)](https://en.wikipedia.org/wiki/Artificial_intelligence) to detect blinks. Blinkr uses a camera that faces the user. Blinkr counts the number of times a user blinks and warns them if they are not blinking enough. An average adult blinks 10-20 times a minute. Blinkr looks at how much you are blinking per minute and informs you on whether you should blink or not.

![ScreenShot](https://i.ibb.co/DCbsY5Z/Are-tch-5.png)

## How does Blinkr work
The Blinkr devices utilizes the [NVIDIA Jetson Nano AI Computer](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/). The NVIDIA Jetson Nano is a fast single board computer meant for AI. My code runs on this computer. Additionally Blinkr uses a camera, speaker, as well as screen.

![ScreenShot](https://i.ibb.co/r6ZHpgQ/Are-tch-6.png)

## Make your own Blinkr
Recreating your own Blinkr device is easy! Using the code repository and the instructions below you can make your own Blinkr and blink more. Follow the steps belowed carefully and you'll be on your way. Below is a picture of a research paper that explains how to detect blinks:

![ScreenShot](https://i.ibb.co/4RY4cRH/Screen-Shot-2020-11-23-at-5-35-36-PM.png)
###### Real-Time Eye Blink Detection using Facial Landmarks-Tereza Soukupova and Jan Cech-Center for Machine Perception, Department of Cybernetics-Faculty of Electrical Engineering, Czech Technical University in Prague

***Here we cam see how the EAR (Eye Aspect Ratio) changes when someone blinks. Using this we can detect blinks.***

## Materials needed to build Blinkr

1. [NVIDIA Jetson Nano 2GB Developer Kit](https://www.amazon.com/NVIDIA-Jetson-Nano-2GB-Developer/dp/B08J157LHH/ref=sr_1_3?dchild=1&keywords=nvidia+jetson+nano&qid=1606178473&sr=8-3) -- This is the Jetson Nano AI Computer that will be the core of the Blinkr device. This computer will be doing all of the AI and running the code. We will be connecting things such as a camera to this device.

2. [HDMI Display](https://www.amazon.com/Developer-Accessories-Powerful-Development-XYGStudy/dp/B08629Y5JR/ref=sr_1_1_sspa?dchild=1&keywords=nvidia%2Bjetson%2Bnano%2Bdisplay&qid=1606178640&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTkZDV1A2REZGVVhPJmVuY3J5cHRlZElkPUExMDM4NDgyMkdTS1dWSkNXWks0WSZlbmNyeXB0ZWRBZElkPUEwMzk0NjI2MzlVVUlZUzVFQkxVUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1) -- You can either use a large HDMI display or you can purchase a small HDMI display and make the device fully integrated. I have given the link for the small HDMI display compatible with the Jetson Nano. This link sends you to a product that contains the display as well as cables and more to get you started.

3. [Raspberry Pi Camera V2](https://www.amazon.com/gp/product/B07W5T3J5T/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1) -- This is the link to the Raspberry Pi Camera but you can also use a web cam if you choose to do so. The Raspberry Pi Camera is small and compact so I decided to use it. 

4. [5V Power Supply](https://www.amazon.com/gp/product/B07TYQRXTK/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) -- You will need a good 5V Power Supply to power the Jetson Nano. I have chosen a good one that prouduces a stable source of power.

5. [Micro SD Card](https://www.amazon.com/SanDisk-Ultra-microSDXC-Memory-Adapter/dp/B073JWXGNT/ref=sr_1_2?dchild=1&keywords=sandisk+32gb&qid=1606179035&sr=8-2) -- You will need a Micro SD Card to put the OS (Operating System) onto the Jetson Nano.

6. [HDMI Cable](https://www.amazon.com/AmazonBasics-High-Speed-HDMI-Cable-1-Pack/dp/B014I8T0YQ/ref=sr_1_1_sspa?crid=20LGUYKA7TEIC&dchild=1&keywords=hdmi+cable+amazonbasics&qid=1606179113&sprefix=HDMI+Cable+amazon%2Caps%2C227&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQTc5VDMxOFo0U0o3JmVuY3J5cHRlZElkPUEwNTIxMTExM0hGVURXN1ZaSzNHTyZlbmNyeXB0ZWRBZElkPUEwNzYzMTI2M0o3RFVOQ1NORVBJMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) -- You will need a HDMI cable to connect a moniter/display to the Jetson Nano.

7. [Speaker](https://www.amazon.com/HONKYOB-Speaker-Computer-Multimedia-Notebook/dp/B075M7FHM1/ref=sr_1_3?dchild=1&keywords=usb+mini+speaker&qid=1606240300&sr=8-3) -- You will need a USB Speaker for the audible blink reminder.

## Setting up the NVIDIA Jetson Nano 2GB Developer Kit
Go to this [link](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/education-projects/) and follow the steps to get your NVIDIA Jetson Nano working. After following all of these steps and flashing the OS onto your Nano continue on below.

## Connecting the Camera to the Jetson Nano

The web cam can be connect via USB. To connect the Raspberry Pi Camera V2 to the Jetson Nano, follow this [video](https://www.youtube.com/watch?v=dHvb225Pw1s). If you are using a Web Cam comment out this line:
```python
  cam = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+flip+' ! video/x-raw, width='+width+', height='+height+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
```
If you are using the Raspberry Pi Camera V2 then comment out this line:
```python
  cam = cv2.VideoCapture(0)
```
Also add a height, width and flip variable above. I reccomend the width and height to be (you will have to test the flip and see what works):
```
  width = 320
  height = 240
  flip = 1
```

## Installing packages

Before installing python packages you will need to download the "shape_predictor_68_face_landmarks.dat" file and modify this line with the path to the file:

```python
  dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
```

To download it visit this [link](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).

To start installing packages via pip you will have to run this line in the LX Terminal:
```python
  sudo apt-get install python3-pip
```
These are the packages used in the Python script:
```python
  from scipy.spatial import distance
  from gtts import gTTS
  import playsound
  import time
  import dlib
  import cv2
  import sys
  import os
```

You can download these packages via pip using the [requirements.txt](https://github.com/AdritRao/Blinkr/blob/main/requirements.txt) file:
```python
  pip3 install -r requirements.txt
```

## Time and Blink Count Modifications

You can modify the time on line 37. Change the number on this line to change the seconds until the next reminder:

```python
  while time.time() - start < 60:
```

You can modify the number of blinks needed over here:

```python
   if blink_count >= 10:
       print("Good, keep blinking")
       blink_count = 0
       os.execl(sys.executable, sys.executable, *sys.argv)
   else:
       speak("Blink more please")
       blink_count = 0
       os.execl(sys.executable, sys.executable, *sys.argv)
```

## Eye Line and Blink Color Modifications

You can change the color of the line around the left and right eye by changing this line of code on lines 58 and 70:

```python
    cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)
```

You can change the font color of "Blink" on line 78:

```python
    cv2.putText(frame, "Blink", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 4)
```

## Program Restart

Every one minute the program will restart via this line of code.

```python
    os.execl(sys.executable, sys.executable, *sys.argv)
```

## Final Step - Running the code on the Jetson Nano
Download the code from this Repo and save it onto your Jetson Nano. Navigate to the LX Terminal and then to the folder. Then write this to see the code in action:
```
  python3 blinkr.py
```
I hope you enjoy using Blinkr! 👁



