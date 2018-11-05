#!/usr/bin/python
from modules import LCD, CLOCK, BUTTON, DHT
import signal, sys
import time

#pinout
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 21
lcd_d7 = 22
lcd_backlight = 4
button_pin = 19
dht_pin = 26

lcd_columns = 16
lcd_rows = 2

activity_time = 10
time_update_freq = 0.3

lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
wakeupButton = BUTTON(button_pin)
dht = DHT(dht_pin)

def sigintHandler(signal, frame):
    print 'ending betterClock.py by SIGINT'
    lcd.stop()
    dht.stop()
    print 'waiting for lcd and dht will end'
    lcd.join()
    dht.join()
    print 'end of program'
    sys.exit(0)

dht.start()
lcd.start()
signal.signal(signal.SIGINT, sigintHandler)

states = { 'sleep' : 0, 'clock' : 1, 'dht' : 2 }
state = states['clock']
last_activity = time.time()
#button_pressed = False
last_time_update = 0

def toClock(lcdTurnOn = False):
    global state
    state = states['clock']
    lcd.turnOn()
    timeUpdate(True)

def timeUpdate(update_anyway = False):
    global last_time_update
    if time.time() - last_time_update < time_update_freq and not update_anyway:
        return
        #TODO analiza czy napewno dobry warunek
    lcd.set([CLOCK.getDate(), CLOCK.getTime()], update_anyway)
    last_time_update = time.time()

def dhtShow():
    temp, hum, read_time = dht.getReading()
    if temp is not None and hum is not None and read_time is not None:
        first_line = 'Temp. ' + str(temp) + '*C ' + 'Wilgotnosc ' + str(hum) + '%'
        second_line = 'Pomiar o ' + time.asctime(time.localtime(read_time))[11:19]
        lcd.set([first_line, second_line])
    else:
        lcd.set(['blad odczytu!', 'sprawdz polaczenia i sprobuj ponownie'])
#    print 'dhtShow()'

def sleep():
    global last_activity
    global state
    if time.time() - last_activity > activity_time:
        state = states['sleep']
        lcd.turnOff()



while True:
    button_state, button_last_state = wakeupButton.getChange()
    button_pressed = False
    if button_state:
        last_activity = time.time()
        if not button_last_state:
            button_pressed = True

    if state == states['sleep']:
        if button_pressed:
            toClock(True)
            continue
    elif state == states['clock']:
#        print 'state clock = ', state
        if button_pressed:
            state = states['dht']
            dhtShow()
            continue
        else:
            timeUpdate()
            sleep()
    elif state == states['dht']:
        if button_pressed:
            toClock()
            continue
        else:
            sleep()
    time.sleep(0.05)
