import Adafruit_GPIO.SPI as SPI
from time import sleep
import Adafruit_MCP3008
CLK = 11
MISO = 9
MOSI = 10
CS = 8
delay = 0.5
'''
delay for IR in seconds
'''
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7


# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def left_dist():
    v=(mcp.read_adc(0)/1023.0)*3.3
    l_dist = 43.543*((v+0.30221)**(-1.5281))
    return l_dist

def right_dist():
    vr=(mcp.read_adc(2)/1023.0)*3.3
    r_dist = 43.543*((vr+0.30221)**(-1.5281))
    return r_dist

while True:
    print('------------------')
   # print('Left sensor distance: {} cm'.format(left_dist()))
    print('Left sensor voltage: {} V'.format((mcp.read_adc(0)/1023.0)*3.3))
   # print('Right sensor distance: {} cm'.format(right_dist()))
    print('Right sensor voltage: {} V'.format((mcp.read_adc(2)/1023.0)*3.3))
    sleep(delay)

