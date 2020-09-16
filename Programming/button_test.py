import time
import RPi.GPIO as GPIO

button_port = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_port,GPIO.IN)

prev_input = 0

while True:
    b_input = GPIO.input(button_port)
    if ((not prev_input) and b_input):
        print('Button Pressed')
    prev_input = b_input
    time.sleep(0.05)
