import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class DCMOTOR:

    def __init__(self, pinA, pinB, inverse = False):
        GPIO.setup(pinA, GPIO.OUT)
        GPIO.setup(pinB, GPIO.OUT)
        self.__mode = pinA
        self.__speed = GPIO.PWM(pinB, 50)
        self.__inverse = inverse
        self.__is_left = True
        self.__speed.start(0)
        self.stop()
    
    def startLeft(self, speed):
        self.__is_left = True
        if not self.__inverse:
            self.__setSpeedMode(speed, 0)
#            GPIO.output(self.__mode, 0)
#            self.__speed.ChangeDutyCycle(speed)
        else:
            self.__setSpeedMode(100 - speed, 1)
#            GPIO.output(self.__mode, 1)
#            self.__speed.ChangeDutyCycle(100 - speed)

    def startRight(self, speed):
        self.__is_left = False
        if not self.__inverse:
            self.__setSpeedMode(100 - speed, 1)
        else:
            self.__setSpeedMode(speed, 0)

    def stop(self):
        if self.__is_left:
            if not self.__inverse:
                self.__setSpeedMode(0, 0)
            else:
                self.__setSpeedMode(100, 1)
        else:
            if not self.__inverse:
                self.__setSpeedMode(100, 1)
            else:
                self.__setSpeedMode(0, 0)

    def __setSpeedMode(self, speed, mode):
        GPIO.output(self.__mode, mode)
        self.__speed.ChangeDutyCycle(speed)

        
