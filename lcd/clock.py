#!/usr/bin/python
#import Adafruit_CharLCD as AdafruitLCD
from modules import LCD, CLOCK, BUTTON
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
wakeupButton = BUTTON(19)

def sigintHandler(signal, frame):
    print 'ending clock.py by SIGINT'
    lcd.stop()
    print 'waiting for lcd will end'
    lcd.join()
    print 'end of program'
    sys.exit(0)

signal.signal(signal.SIGINT, sigintHandler)

last_update = 0.0
lcd.start()
localtime = time.asctime(time.localtime(time.time()))
firstLine = localtime[:4] + localtime[8:11] + localtime[4:8] + localtime[20:]
secondLine = localtime[11:19]
#lcd.set([firstLine, secondLine])
lcd.set([CLOCK.getDate(), CLOCK.getTime()])

def timeUpdate():
    global last_update
    if time.time() - last_update < 0.3:
        return
    last_update = time.time()
    lcd.setAtPoint(0, 1, time.asctime(time.localtime(last_update))[11:19])

data_set_time = 0
def setDate(line = 0):
    global data_set_time
    data_set_time = time.time()
    localtime = time.asctime(time.localtime(data_set_time))
    lcd.setLine(line, localtime[:4] + localtime[8:11] + localtime[4:8] + localtime[20:])

last_action_time = time.time()
button_presses = 0
sleep_time = 6
while True:
    button_state, button_last = wakeupButton.getChange()
    if button_state:
        last_action_time = time.time()
        if not button_last:
            lcd.turnOn()
#            button_presses += 1
#            lcd.setLine(0, 'button pressed: ' + str(button_presses) + 'times')
    timeUpdate()
    if time.localtime(time.time()).tm_mday != time.localtime(data_set_time).tm_mday:
        setDate()
    if time.time() - last_action_time > sleep_time:
       lcd.turnOff() 
    time.sleep(0.05)
    






















