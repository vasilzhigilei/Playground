from threading import Thread
import cv2

class VideoGet:
    """
    Class that gets frames from a cv2 VideoCapture object
    Allows to be run as a seperate thread, increasing performance
    """

    def __init__(self):
        self.stream = cv2.VideoCapture()
        self.grabbed, self.frame = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while not self.stopped:
            if not self.grabbed:
                self.stopped = True
            else:
                self.grabbed, self.frame = self.stream.read()

    def stop(self):
        self.stopped = True