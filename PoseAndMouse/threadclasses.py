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
        """
        Initializes the VideoGet class
        Creates the cv2.VideoCapture stream using the default camera, and grabs initial frame
        """
        self.stream = cv2.VideoCapture(0)
        self.grabbed, self.frame = self.stream.read()
        self.stopped = False

    def start(self):
        """
        Starts the thread, running update as the target
        To be called externally to start the VideoGet thread
        :return: self
        """
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        """
        Target function for the VideoGet thread
        Repeatedly grabs next frame if stop conditions do not arise
        :return: None
        """
        while not self.stopped:
            if not self.grabbed:
                self.stopped = True
            else:
                self.grabbed, self.frame = self.stream.read()

    def read(self):
        """
        Function to be called externally to retrieve current frame
        :return: self.frame
        """
        return self.frame;

    def stop(self):
        """
        Function to be called to stop the VideoGet thread
        :return: None
        """
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
                pyautogui.moveTo(self.x, self.y, duration=self.distance/2000)
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