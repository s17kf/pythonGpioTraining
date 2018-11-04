#!/usr/bin/python
#import Adafruit_CharLCD as AdafruitLCD
from modules import LCD
import signal, sys
#from time import sleep
import time

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 21
lcd_d7 = 22
lcd_backlight = 4

lcd_columns = 16
lcd_rows = 2

lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def sigintHandler(signal, frame):
    print 'ending clock.py by SIGINT'
    lcd.stop()
    print 'waiting for lcd will end'
    lcd.join()
    print 'end of program'
    sys.exit(0)

signal.signal(signal.SIGINT, sigintHandler)

lcd.start()
localtime = time.asctime(time.localtime(time.time()))
firstLine = localtime[:4] + localtime[8:11] + localtime[4:8] + localtime[20:]
secondLine = localtime[11:19]
lcd.set([firstLine, secondLine])

while True:
    localtime = time.asctime(time.localtime(time.time()))[11:19]
#    firstLine = localtime[:4] + localtime[8:11] + localtime[4:8] + localtime[20:]
#    secondLine = localtime[11:19]
    lcd.setAtPoint(0,1,localtime)    
    #lcd.clear()
#    lcd.set_cursor(0,0)
#    lcd.message(firstLine + '\n' + secondLine)
    time.sleep(0.33)























