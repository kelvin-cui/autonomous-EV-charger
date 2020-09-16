import cv2
import numpy as np
import imutils
image = cv2.imread('50cm_h_stripe.jpg')
#image = imutils.resize(image, width=400)
result = image.copy()
#result = imutils.resize(result, width=400)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([170,25,0])
upper = np.array([255,255,255])
mask = cv2.inRange(image, lower, upper)
result2 = cv2.bitwise_and(result, result, mask=mask)
height, width, depth = result.shape
mx = int(width/2)
my = int(height/2)
length = 10

# ensure at least some circles were found
#circle_detect(img)
cv2.line(result,(mx,my-length),(mx,my+length),(0, 0, 255), 1)
cv2.line(result,(mx-length,my),(mx+length,my),(0, 0, 255), 1)

contours,h = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    # Draw only the contour with the largest area
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        #if w*h>200000 and w*h<5000000:
        if w/h < 5.6 and w/h>5.4 and w*h>780 and w*h<800:
            cv2.rectangle(result, (x,y), (x+w,y+h), (0,255,0), 1)
            cv2.line(result,(x+int(w/2),y-length),(x+int(w/2),y+h+length),(0, 0, 255), 1)
            print('Distance x:{}, Distance y:{}'.format(x+int(w/2)-mx,my-y+int(h/2)))
            print("Area:{} pixels".format(w*h))
            print('Conversion: 11/{}={} cm/pix'.format(w,11/w))
            print('Ratio: {}'.format(w/h))

cv2.imshow('img', result)
cv2.imshow('mask', mask)
cv2.imshow('result', result2)

key =cv2.waitKey(0)
if key == ord('q') or key == 27:
    cv2.destroyAllWindows()
