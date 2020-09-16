All code in the old testing folder were prototypes for old CV stratergies we tried to implement that we are no longer planning on using.
This includes:
	- Detecting the square profile of the cutout
	- Detecting the circular shape of the open port 
We scrapped these ideas because there is too much noise to filter out and too prone to error. In addition, alot of noise filtering would slow down the algorithm
alot as the Pi Zero is not as powerful as a laptop.

Instead our main stratergy was to apply a red filter (red_detect.py). This approach will be explained in more detail in the review and report but in short,
it is a method that will filter out all colours in the photo except for a certain shade of red, then we use that mask to do contour matching to draw rectangles.
We were planning on using a rectangular piece of red electrical tape on the top horizontal edge of the port. This algorithm is not only less 
computationally expensive versus other filters that use built in cv2 noise filtering functions, but also is alot more reliable and less conditions need
to be checked to ensure we are detecting exactly what we wanted to through rectangle ratios and areas. 
