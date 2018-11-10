import RPi.GPIO as GPIO
import threading, Queue, time

direction = { 'left' : 0, 'right' : 1 }

class STEP_MOTOR(threading.Thread):
    def __init__(self, in1, in2, in3, in4):
        threading.Thread.__init__(self)
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(in3, GPIO.OUT)
        GPIO.setup(in4, GPIO.OUT)
        self.isStopped = threading.Event()

    def run(self):
        while not isStopped.is_set():
            isStopped.wait()

    def stop(self):
       self.isStopped.set()

    def setLeft(self, steps):
        for i in range(steps):
            self.__setPins(self.in1, self.in2)
            self.__setPins(self.in2, self.in3)
            self.__setPins(self.in3, self.in4)
            self.__setPins(self.in1, self.in4)

    def setRight(self, steps):
        for i in range(steps):
            self.__setPins(self.in1, self.in2)
            self.__setPins(self.in1, self.in4)
            self.__setPins(self.in3, self.in4)
            self.__setPins(self.in2, self.in3)
        

    def __setPins(self, pin1, pin2):
        GPIO.output(pin1, 1)
        GPIO.output(pin2, 1)
        time.sleep(0.005)
        GPIO.output(pin1, 0)
        GPIO.output(pin2, 0)
        time.sleep(0.003)
        
