import Adafruit_CharLCD as AdafruitLCD
import threading
import Queue

#from time import sleep
import time

class LCD(threading.Thread):
    def __init__(self, rs, en, d4, d5, d6, d7, columns, rows, backlight = None, invert_polarity = True, enable_pwm = False, gpio = AdafruitLCD.GPIO.get_platform_gpio(), pwm = AdafruitLCD.PWM.get_platform_pwm(), initial_backlight = 1.0):
        #AdafruitLCD.Adafruit_CharLCD.__init__(self, rs, en, d4, d5, d6, d7, columns, rows, backlight, invert_polarity, enable_pwm, gpio, pwm, initial_backlight)
        threading.Thread.__init__(self)
        self.lcd = AdafruitLCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, columns, rows, backlight, invert_polarity, enable_pwm, gpio, pwm, initial_backlight)
        self.rows = rows
        self.cols = columns
        self.queue = Queue.Queue()
        self.isWorking = threading.Event()
        self.isWorking.set()
        localtime = time.asctime(time.localtime(time.time()))
        self.lines = []
        self.scroll = []
        self.sizes = []
        self.isScrollNeed = threading.Event()
        for i in range(self.rows):
            self.lines.append("")
            self.scroll.append(0)
            self.sizes.append(0)

    def run(self):
        while self.isWorking.is_set():
            try:
                new_item = self.queue.get(True, 1)
            except Queue.Empty:
#                if isScrollNeed.is_set():
#                    for i in range(self.rows):
#                        if self.sizes[i] > self.cols:
#                            if self.sizes[i] - self.cols > self.scroll[i]:
                pass                              
            except:
                print 'other error'
            else:
                if new_item[0] == self.rows:
                    if new_item[3] == True:
                        self.lcd.clear()
                    self.isScrollNeed.clear()
                    for i in range(self.rows):
                        self.lines[i] = new_item[i+1]
                        self.lcd.set_cursor(0, i)
                        self.lcd.message(self.lines[i])
                        self.sizes[i] = len(self.lines[i])
                        if self.sizes[i] > self.cols:
                            self.isScrollNeed.set()
                        self.scroll[i] = 0
                elif new_item[0] >= 0 and new_item[0] < self.rows:
                    self.lines[new_item[0]] = new_item[1]
                    if new_item[2] == True:
                        self.lcd.clear()
                        for i in range(self.rows):
                            self.lcd.set_cursor(0, i)
                            self.lcd.message(self.lines(i))
                    else:
                        self.lcd.set_cursor(0, new_item[0])
                        self.lcd.message(new_item[1])
                elif new_item[0] == -1:
                    if new_item[4] == True:
                        self.lcd.clear()
                    self.lcd.set_cursor(new_item[1], new_item[2])
                    self.lcd.message(new_item[3])
                #TODO obsluga linii
                #TODO scroll too long text
            
            


    def stop(self):
        self.isWorking.clear()

    def set(self, text0, text1, clear = True):
        self.queue.put([self.rows, text0, text1, clear])

    def setLine(self, line, text, clear = True):
        if line < 0 or line >= self.rows:
            raise IndexError, 'only 0-1 lines available'
            return
        self.queue.put([line, text, clear])
    
    def setAtPoint(self, col, row, text, clear = False):
        self.queue.put([-1, col, row, text, clear])

    def moveLeft(self):
        self.lcd.move_left()

    def moveRight(self):
        self.lcd.move_right()



















