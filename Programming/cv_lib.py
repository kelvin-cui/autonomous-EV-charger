import datetime

from threading import Thread
from picamera import PiCamera
from picamera.array import PiRGBArray
class FPS:
    def __init__(self):
        self._start=None
        self._end=None
        self._numFrames=0

    def start(self):
        '''
        Start the timer
        '''
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        self._end = datetime.datetime.now()

    def update(self):
        '''
        Increment the total number of frames examined during the start and 
        end intervals
        '''
        self._numFrames += 1

    def elapsed(self):
        '''
        return the total number of seconds between the start and end intervall
        '''
        return (self._end-self._start).total_seconds()

    def fps(self):
        '''
        compute approx fps
        '''
        return self._numFrames/self.elapsed()


class PiVideoStream:
    def __init__(self,resolution=(320,240),framerate=32):
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture,format="bgr", use_video_port=True)

        '''
        init the frame and the variable used to indicate if the thread should
        be stopped
        '''
        self.frame = None
        self.stopped = False

    def start(self):
        '''
        start the thread to read frames from video stream
        '''
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        '''
        keep looping infinitely until the thread is stopped
        '''
        for f in self.stream:
            '''
            grab the frame from the stream and clear the stream in prep 
            for next frame
            '''
            self.frame = f.array
            self.rawCapture.truncate(0)

            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
