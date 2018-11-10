import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class BUTTON():
    def __init__(self, pin):
        self.__pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.last_state = self.getState()

    def getState(self): #returns actual state - True if button is pressed
        self.last_state = GPIO.input(self.__pin)
        return self.last_state

    def getChange(self):    #returns actual state and state when last checked state [actualState, lastCheckedState]
        last_state = self.last_state
        self.getState()
        return (self.last_state, last_state)

    def isPressed(self):
        actual_state, last_state = self.getChange()
        if actual_state:
            if not last_state:
                return True
        return False
