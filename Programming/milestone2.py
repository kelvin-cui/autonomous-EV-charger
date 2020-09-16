class VideoStream:
	def __init__(self, src=0, resolution=(320, 240),
		framerate=32):
		# check to see if the picamera module should be used
		# only import the picamera packages unless we are
		# explicity told to do so -- this helps remove the
		# requirement of `picamera[array]` from desktops or
		# laptops that still want to use the `imutils` package
		from cv_lib import PiVideoStream
		# initialize the picamera stream and allow the camera
		# sensor to warmup
		self.stream = PiVideoStream(resolution=resolution,
				framerate=framerate)
    def start(self):
		# start the threaded video stream
		return self.stream.start()
	def update(self):
		# grab the next frame from the stream
		self.stream.update()
	def read(self):
		# return the current frame
		return self.stream.read()
	def stop(self):
		# stop the thread and release any resources
		self.stream.stop()

import imutils
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
DIR1 = 29  # Direction GPIO PIN
STEP1 = 31 # Step GPIO Pin
DIR2 = 33
STEP2 = 35 # Step GPIO Pin
DIR3 = 36
STEP3 = 38 # Step GPIO Pin
DIR4 = 37
STEP4 = 40   # Step GPIO Pin
#ZSTEP =
#ZDIR =
CW = 1    # Clockwise Direction
CCW = 0   # CCW rotation
wheel_delay = 0.003
z_delay = 0.001
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(STEP1,GPIO.OUT)
GPIO.setup(DIR2,GPIO.OUT)
GPIO.setup(STEP2,GPIO.OUT)
GPIO.setup(DIR3,GPIO.OUT)
GPIO.setup(STEP3,GPIO.OUT)
GPIO.setup(DIR4,GPIO.OUT)
GPIO.setup(STEP4,GPIO.OUT)
# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream().start()
time.sleep(2.0)
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
# loop over the frames from the video stream
def move_insert(dist_to_steps):
	v = (mcp.read_adc(0) / 1023.0) * 3.3
	dist = 43.543*((v+0.30221)**(-1.5281))
	in_steps = dist*dist_to_steps
    GPIO.output(DIR2,CW)
    GPIO.output(DIR4,CCW)
	for go in range(in_steps):
		GPIO.output(STEP2, GPIO.HIGH)
		GPIO.output(STEP4, GPIO.LOW)
		sleep(wheel_delay)
		GPIO.output(STEP2,GPIO.LOW)
		GPIO.output(STEP4,GPIO.HIGH)
		sleep(wheel_delay)

	if (GPIO.input(7)):
		return True
	else:
		GPIO.output(DIR2,CCW)
	    GPIO.output(DIR4,CW)
		for go in range(in_steps):
			GPIO.output(STEP2, GPIO.HIGH)
			GPIO.output(STEP4, GPIO.LOW)
			sleep(wheel_delay)
			GPIO.output(STEP2,GPIO.LOW)
			GPIO.output(STEP4,GPIO.HIGH)
			sleep(wheel_delay)
		return False
    '''
    IR Sensor reading distance -> Steps -> move motor for x steps

    then if limit switch is pressed, we good
    if not, reset and exit function
    '''
    return 0

def move_align(lateral,vertical,conversion,step_dist_convert):
    if lateral < 0:
        '''
        TENTATIVE: Adjust CW and CCW if needed
        '''
        GPIO.output(DIR1,CW)
        GPIO.output(DIR3,CCW)
    elif lateral > 0:
        GPIO.output(DIR1,CCW)
        GPIO.output(DIR3,CW)

    if vertical > 0:
        GPIO.output(ZDIR,CW)
    elif vertical < 0:
        GPIO.output(ZDIR,CCW)

    if lateral != 0:
        dist = conversion*abs(lateral)
        steps = step_dist_convert*dist
        for i in range(steps):
            GPIO.output(STEP1, GPIO.HIGH)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(wheel_delay)
            GPIO.output(STEP1,GPIO.LOW)
            GPIO.output(STEP3,GPIO.HIGH)
            sleep(wheel_delay)
	return True
    '''
    UNDER CONSTRUCTION FOR VERTICAL
    NEED MORE TRIG AND MATH
    if vertical != 0:
    '''
def vision():
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([170,25,0])
    upper = np.array([255,255,255])
    mask = cv2.inRange(image, lower, upper)
    height, width, depth = frame.shape
    mx = int(width/2)
    my = int(height/2)
    contours,h = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # Draw only the contour with the largest area
        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            #if w*h>200000 and w*h<5000000:
            if w/h < 5.6 and w/h>5.4 and w*h>780 and w*h<800:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1)
                cv2.line(frame,(x+int(w/2),y-length),(x+int(w/2),y+h+length),(0, 0, 255), 1)
				print("Area:{} pixels".format(w*h))
                print('Conversion: 11/{}={} cm/pix'.format(w,11/w))
				return True,x+int(w/2)-mx,my-y+int(h/2),11/w,frame


GPIO.output(DIR1,CW) #Change Direction if needed
GPIO.output(DIR3,CCW)
stop = False
max_setup_width_in_steps = 00000
step_dist_convert = 0000000
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	for k in range(max_setup_width_in_steps):
		stop, x_dist,y_dist,convert,Frame = vision()
		if stop:
			break
		GPIO.output(STEP1, GPIO.HIGH)
		GPIO.output(STEP3, GPIO.LOW)
		sleep(wheel_delay)
		GPIO.output(STEP1,GPIO.LOW)
		GPIO.output(STEP3,GPIO.HIGH)
		sleep(wheel_delay)

    if x_dist > threshold and y_dist > zthreshold:    #if bot is not aligned
        move_align(x_dist,0,convert) #lateral distance, vertical distance, conversion factor
    else:
        insert_complete = move_insert()
	if insert_complete:
		break

	# show the frame
	cv2.imshow("Frame", Frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
