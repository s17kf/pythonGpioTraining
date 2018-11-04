import Adafruit_CharLCD as AdafruitLCD
import threading
import Queue
import time

class LCD(threading.Thread):
    def __init__(self, rs, en, d4, d5, d6, d7, columns, rows, backlight = None, invert_polarity = True, enable_pwm = False, gpio = AdafruitLCD.GPIO.get_platform_gpio(), pwm = AdafruitLCD.PWM.get_platform_pwm(), initial_backlight = 1.0):
        threading.Thread.__init__(self)
        self.lcd = AdafruitLCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, columns, rows, backlight, invert_polarity, enable_pwm, gpio, pwm, initial_backlight)
        self.rows = rows
        self.cols = columns
        self.queue = Queue.Queue()
        self.isWorking = threading.Event()
        self.isWorking.set()
        localtime = time.asctime(time.localtime(time.time()))
        self.lines = []
        self.scroll = 0
        self.lastScrollTime = time.time()
        self.max_size = 0
        self.__autoscroll = True
        for i in range(self.rows):
            self.lines.append("")

    def run(self):
        while self.isWorking.is_set():
            try:
                new_item = self.queue.get(True, 0.9)
            except Queue.Empty:
                self.__scroll()
            except:
                print 'other error'
            else:
                if new_item[0] == self.rows:
                    if new_item[3] == True:
                        self.lcd.clear()
                    else:
                        for i in range(self.scroll):
                            self.lcd.move_left
                    self.max_size = 0
                    for i in range(self.rows):
                        self.lines[i] = new_item[i+1]
                        self.lcd.set_cursor(0, i)
                        self.lcd.message(self.lines[i])
                        if len(self.lines[i]) > self.max_size:
                            self.max_size = len(self.lines[i])
                    self.scroll = 0
                    self.__setLastScrollTime(time.time() + 1)
                elif new_item[0] >= 0 and new_item[0] < self.rows:
                    self.lines[new_item[0]] = new_item[1]
                    if new_item[2] == True:
                        self.lcd.clear()
                        for i in range(self.rows):
                            self.lcd.set_cursor(0, i)
                            self.lcd.message(self.lines(i))
                    else:
                        for i in range(self.scroll):
                            self.lcd.move_left
                        for line in self.lines:
                            if len(line) > self.max_size:
                                self.max_size = len(line)
                        self.lcd.set_cursor(0, new_item[0])
                        self.lcd.message(new_item[1])
                    self.scroll = 0
                    self.__setLastScrollTime(time.time() + 1)
                elif new_item[0] == -1:
                    if new_item[4] == True:
                        self.lcd.clear()
                    self.lcd.set_cursor(new_item[1], new_item[2])
                    self.lcd.message(new_item[3])
                    self.__scroll()
                #TODO obsluga linii
            
    def __scroll(self):
        if self.__autoscroll and self.max_size > self.cols and time.time() - self.lastScrollTime > 0.8:
            if self.scroll < self.max_size - self.cols:
                self.lcd.move_left()
                self.scroll += 1
                self.__setLastScrollTime(time.time())
            else:
                for i in range(self.scroll):
                    self.lcd.move_right()
                self.scroll = 0
                self.__setLastScrollTime(time.time() + 1)

    def __setLastScrollTime(self, scrollTime = time.time()):
        self.lastScrollTime = scrollTime

    def stop(self):
        self.isWorking.clear()

    def set(self, text, clear = True):
        new_item = [self.rows]
        for i in range(self.rows):
            new_item.append(text[i])
        new_item.append(clear)
        self.queue.put(new_item)

    def setLine(self, line, text, clear = True):
        if line < 0 or line >= self.rows:
            raise IndexError, 'only 0-1 lines available'
            return
        self.queue.put([line, text, clear])
    
    def setAtPoint(self, col, row, text, clear = False):
        self.queue.put([-1, col, row, text, clear])

    def turnOn(self, backlight = 1):
        self.lcd.set_backlight(backlight)
    def turnOff(self):
        self.lcd.set_backlight(0)

    def setAutoscroll(self, autoscroll):
        self.__autoscroll = autoscroll

    def moveLeft(self):
        self.lcd.move_left()

    def moveRight(self):
        self.lcd.move_right()



















