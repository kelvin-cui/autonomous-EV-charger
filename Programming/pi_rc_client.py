import socket
from time import sleep
import RPi.GPIO as GPIO
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = 'LAPTOP-4CCTQVLJ'
port = 8080
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
SPR = 200  # Steps per revolution 200 from Anton's test arduino code 360/200 = 9/5 degrees
step_count = SPR
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(STEP1,GPIO.OUT)
GPIO.setup(DIR2,GPIO.OUT)
GPIO.setup(STEP2,GPIO.OUT)
GPIO.setup(DIR3,GPIO.OUT)
GPIO.setup(STEP3,GPIO.OUT)
GPIO.setup(DIR4,GPIO.OUT)
GPIO.setup(STEP4,GPIO.OUT)
delay = 0.03
s.connect((hostname,port))
try:
    while True:
        msg = s.recv(1)
        print(msg.decode("utf-8"))
        if msg.decode("utf-8") == "W":
            print('moving motors w')
            GPIO.output(DIR1,CCW)
            GPIO.output(DIR3,CW)
            while True:
                GPIO.output(STEP1, GPIO.HIGH)
                GPIO.output(STEP3, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP1,GPIO.LOW)
                GPIO.output(STEP3,GPIO.HIGH)
                sleep(delay)
                msg = s.recv(1)
                print(msg.decode('utf-8'))
                if msg.decode("utf-8") != "W":
                    break
        elif msg.decode("utf-8") == "S":
            print('moving motors S')
            GPIO.output(DIR1,CW)
            GPIO.output(DIR3,CCW)
            while True:
                GPIO.output(STEP1, GPIO.HIGH)
                GPIO.output(STEP3, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP1,GPIO.LOW)
                GPIO.output(STEP3,GPIO.HIGH)
                sleep(delay)
                msg = s.recv(1)
                print(msg.decode('utf-8'))
                if msg.decode("utf-8") != "S":
                    break
        elif msg.decode("utf-8") == "A":
            print('moving motors A')
            GPIO.output(DIR2,CW)
            GPIO.output(DIR4,CCW)
            while True:
                GPIO.output(STEP2, GPIO.HIGH)
                GPIO.output(STEP4, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP2,GPIO.LOW)
                GPIO.output(STEP4,GPIO.HIGH)
                sleep(delay)
                msg = s.recv(1)
                print(msg.decode('utf-8'))
                if msg.decode("utf-8") != "A":
                    break
        elif msg.decode("utf-8") == "D":
            print('moving motors D')
            GPIO.output(DIR2,CCW)
            GPIO.output(DIR4,CW)
            while True:
                GPIO.output(STEP2, GPIO.HIGH)
                GPIO.output(STEP4, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP2,GPIO.LOW)
                GPIO.output(STEP4,GPIO.HIGH)
                sleep(delay)
                msg = s.recv(1)
                print(msg.decode('utf-8'))
                if msg.decode("utf-8") != "D":
                    break
        elif msg.decode("utf-8") == "Q":
            print('rot left')
            GPIO.output(DIR1,CCW)
            GPIO.output(DIR3,CCW)
            GPIO.output(DIR2,CCW)
            GPIO.output(DIR4,CCW)
            while True:
                GPIO.output(STEP1,GPIO.HIGH)
                GPIO.output(STEP2, GPIO.LOW)
                GPIO.output(STEP3,GPIO.HIGH)
                GPIO.output(STEP4, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP1,GPIO.LOW)
                GPIO.output(STEP2, GPIO.HIGH)
                GPIO.output(STEP3,GPIO.LOW)
                GPIO.output(STEP4, GPIO.HIGH)
                sleep(delay)
                msg = s.recv(1)
                print('Q')
                if msg.decode("utf-8") != "Q":
                    break
        elif msg.decode("utf-8") == "E":
            print('rot right')
            GPIO.output(DIR1,CW)
            GPIO.output(DIR3,CW)
            GPIO.output(DIR2,CW)
            GPIO.output(DIR4,CW)
            while True:
                GPIO.output(STEP1,GPIO.HIGH)
                GPIO.output(STEP2, GPIO.LOW)
                GPIO.output(STEP3,GPIO.HIGH)
                GPIO.output(STEP4, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP1,GPIO.LOW)
                GPIO.output(STEP2, GPIO.HIGH)
                GPIO.output(STEP3,GPIO.LOW)
                GPIO.output(STEP4, GPIO.HIGH)
                sleep(delay)
                msg = s.recv(1)
                print('E')
                if msg.decode("utf-8") != "E":
                    break
        elif msg.decode("utf-8") == "Z":
            while True:
                print('stopping')
                msg = s.recv(1)
                if msg.decode('utf-8') != "Z":
                    break
        elif msg.decode("utf-8") == "M":
            break
except:
    print("ERROR: Try Failed")
finally:
    print('cleaning up')
    print('DONE')
