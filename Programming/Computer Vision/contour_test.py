import numpy as np
import cv2

img = cv2.imread("pi_pics/port_20cm.jpg")
output=img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.blur(gray, (2, 2), 0)


# For different lighting conditions change minimum thresh classification value parameter 2
ret,thresh = cv2.threshold(gray,100,255,1) #(grayimage,minPixelThreshValue,Max,style of thresholding)

kernel = np.ones((7,7),np.uint8)
dilation = cv2.dilate(thresh,kernel,iterations =7)
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(dilation,kernel,iterations = 7)

contours,h = cv2.findContours(erosion,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

height, width, depth = img.shape
print("Height: "+str(height)+" Width: "+str(width))
mx = int(width/2)
my = int(height/2)
x_length = 20
# ensure at least some circles were found
#circle_detect(img)
cv2.line(img,(mx,my-25),(mx,my+25),(0, 0, 255), 2)
cv2.line(img,(mx-25,my),(mx+25,my),(0, 0, 255), 2)
if len(contours) != 0:
    # Draw only the contour with the largest area
    for contour in contours:
        print('contour:')
        print(contour)
        (x,y,w,h) = cv2.boundingRect(contour)
        #if w*h>200000 and w*h<5000000:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        print("Area:{} pixels".format(w*h))

cv2.imshow("original", img)
cv2.imshow("filter", erosion)
key =cv2.waitKey(0)
if key == ord('q') or key == 27:
    cv2.destroyAllWindows()
