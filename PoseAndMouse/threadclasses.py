from threading import Thread
import pyautogui
import cv2
import math

class VideoGet:
    """
    Class that gets frames from a cv2 VideoCapture object
    Allows to be run as a seperate thread, increasing performance
    """

    def __init__(self):
        self.stream = cv2.VideoCapture(0)
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

    def read(self):
        return self.frame;

    def stop(self):
        self.stopped = True



class Mouse():
    """
    Mouse class, runs all mouse movement operations in separate thread from main
    """

    def __init__(self):
        """
        Initialize Mouse class
        """
        pyautogui.PAUSE = 0  # default safety 0.1 delay, huge fps loss if not 0
        self.stopped = False
        self.x, self.y = 960, 540 # default initial positions assuming 1920x1080p monitor

    def start(self):
        """
        Start the thread with target function self.move
        :return: self
        """
        Thread(target=self.move, args=()).start()
        return self

    def move(self):
        """
        Called repeatedly to move the mouse until exit logic
        :return: None
        """
        while not self.stopped:
            self.distance = math.sqrt((self.x - pyautogui.position()[0])**2 + (self.y - pyautogui.position()[1])**2)
            if(self.distance >= 200):
                pyautogui.moveTo(self.x, self.y, duration=self.distance/1000)
            else:
                pyautogui.moveTo((self.x+pyautogui.position()[0]*4)/5, (self.y+pyautogui.position()[1]*4)/5)

    def setPos(self, x, y):
        """
        Called from main thread to set the new calculated position for the mouse
        :param x: new x position
        :param y: new y position
        :return: None
        """
        self.x = x
        self.y = y

    def stop(self):
        """
        Stop function that stops the thread loop of function moveTo
        :return: None
        """
        self.stopped = True