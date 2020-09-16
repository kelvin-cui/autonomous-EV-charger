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
SPR = 48  # Steps per revolution 200 from Anton's test arduino code 360/200 = 9/5 degrees
step_count = SPR

def motorXY(x_or_y,distance,direction):
    '''
    TENTATIVE!
    Verify Direction and step pin numbers when design is finalized
    Assuming Step per revolution is 200 MAY CHANGE
    distance in units of CM
    '''
    wheel_diameter = 0
    step_count = 200
    len_per_step = 0 / 200

    if x_or_y == 'X':
        if direction == 1:
            GPIO.output(DIR1,1)
            GPIO.output(DIR2,0)
        elif direction == 0:
            GPIO.output(DIR1,0)
            GPIO.output(DIR2,1)
    elif x_or_y == 'Y':
        if direction == 1:
            GPIO.output(DIR3,1)
            GPIO.output(DIR4,0)
        elif direction == 0:
            GPIO.output(DIR3,0)
            GPIO.output(DIR4,1)


    return 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(STEP1,GPIO.OUT)

GPIO.setup(DIR2,GPIO.OUT)
GPIO.setup(STEP2,GPIO.OUT)
GPIO.setup(DIR3,GPIO.OUT)
GPIO.setup(STEP3,GPIO.OUT)
GPIO.setup(DIR4,GPIO.OUT)
GPIO.setup(STEP4,GPIO.OUT)

delay = 0.001

GPIO.output(DIR1,CW)
#GPIO.output(DIR2,0)

for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    #GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    #GPIO.output(STEP2,GPIO.HIGH)
    sleep(delay)

sleep(1)
GPIO.output(DIR1,CCW)
for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    #GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    #GPIO.output(STEP2,GPIO.HIGH)
    sleep(delay)

GPIO.output(DIR3,1)
GPIO.output(DIR4,0)

for x in range(2*step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP3,GPIO.LOW)
    GPIO.output(STEP4,GPIO.HIGH)
    sleep(delay)

sleep(1)

GPIO.output(DIR1,0)
GPIO.output(DIR2,1)

for x in range(2*step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP2,GPIO.HIGH)
    sleep(delay)

sleep(1)

GPIO.output(DIR3,0)
GPIO.output(DIR4,1)

for x in range(2*step_count):
    GPIO.output(STEP3, GPIO.HIGH)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(delay)
    GPIO.output(STEP3,GPIO.LOW)
    GPIO.output(STEP4,GPIO.HIGH)
    sleep(delay)

sleep(1)

print('ROTATING')
GPIO.output(DIR1,1)
GPIO.output(DIR2,0)
GPIO.output(DIR3,1)
GPIO.output(DIR4,0)

for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.LOW)
    GPIO.output(STEP3, GPIO.HIGH)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(0.01)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP2,GPIO.HIGH)
    GPIO.output(STEP3,GPIO.LOW)
    GPIO.output(STEP4,GPIO.HIGH)
    sleep(0.01)

sleep(2)

GPIO.output(DIR1,0)
GPIO.output(DIR2,1)
GPIO.output(DIR3,0)
GPIO.output(DIR4,1)

for x in range(step_count):
    GPIO.output(STEP1, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.LOW)
    GPIO.output(STEP3, GPIO.HIGH)
    GPIO.output(STEP4, GPIO.LOW)
    sleep(0.01)
    GPIO.output(STEP1,GPIO.LOW)
    GPIO.output(STEP2,GPIO.HIGH)
    GPIO.output(STEP3,GPIO.LOW)
    GPIO.output(STEP4,GPIO.HIGH)
    sleep(0.01)

print('DONE')
