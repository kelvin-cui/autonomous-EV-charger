from time import sleep
import RPi.GPIO as GPIO
DIR1 = 29  # Direction GPIO PIN
STEP1 = 31 # Step GPIO Pin
DIR2 = 33
STEP2 = 35 # Step GPIO Pin
DIR3 = 36
STEP3 = 38 # Step GPIO Pin
DIR4 = 37
STEP4 = 40   # Step GPIO Pin

CW = 1    # Clockwise Direction
CCW = 0   # CCW rotation
SPR = 384  # Steps per revolution 200 from Anton's test arduino code 360/200 = 9/5 degrees
step_count = SPR

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(STEP1,GPIO.OUT)
GPIO.setup(DIR2,GPIO.OUT)
GPIO.setup(STEP2,GPIO.OUT)
GPIO.setup(DIR3,GPIO.OUT)
GPIO.setup(STEP3,GPIO.OUT)
GPIO.setup(DIR4,GPIO.OUT)
GPIO.setup(STEP4,GPIO.OUT)

delay = 0.03

GPIO.output(DIR1,CW)
GPIO.output(DIR3,CCW)

for x in range(77):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP3,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
GPIO.output(DIR1,CCW)
GPIO.output(DIR3,CW)
for x in range(77):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP3,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
val = input("advance to port 2? enter 1")
print(val)
#Traverse along
GPIO.output(DIR2,CW)
GPIO.output(DIR4,CCW)

for x in range(384):
    GPIO.output(STEP2, GPIO.HIGH)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP2,GPIO.LOW)
    GPIO.output(STEP4,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
# Move into port
GPIO.output(DIR1,CW)
GPIO.output(DIR3,CCW)

for x in range(77):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP3,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
#move out of port
GPIO.output(DIR1,CCW)
GPIO.output(DIR3,CW)
for x in range(77):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP3,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
val = input("advance to port 1? enter 1")
print(val)
#Traverse along
GPIO.output(DIR2,CW)
GPIO.output(DIR4,CCW)

for x in range(384):
    GPIO.output(STEP2, GPIO.HIGH)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP2,GPIO.LOW)
    GPIO.output(STEP4,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
# Move into port
GPIO.output(DIR1,CW)
GPIO.output(DIR3,CCW)

for x in range(77):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP3,GPIO.HIGH)
    sleep(delay)
sleep(0.5)
#move out of port
GPIO.output(DIR1,CCW)
GPIO.output(DIR3,CW)
for x in range(77):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP3, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP3,GPIO.HIGH)
    sleep(delay)
