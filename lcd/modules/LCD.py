import Adafruit_CharLCD as AdafruitLCD
import threading

#from time import sleep
#import time

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 21
lcd_d7 = 22
lcd_backlight = 4

lcd_columns = 16
lcd_rows = 2

class LCD(AdafruitLCD.Adafruit_CharLCD, threading.Thread):
    def __init__(self, rs, en, d4, d5, d6, d7, columns, rows, backlight = None, invert_polarity = True, enable_pwm = False, gpio = AdafruitLCD.GPIO.get_platform_gpio(), pwm = AdafruitLCD.PWM.get_platform_pwm(), initial_backlight = 1.0):
#        super(LCD, self).__init__(rs, en, d4, d5, d6, d7, columns, rows, backlight, invert_polarity, enable_pwm, gpio, pwm, initial_backlight)
        AdafruitLCD.Adafruit_CharLCD.__init__(self, rs, en, d4, d5, d6, d7, columns, rows, backlight, invert_polarity, enable_pwm, gpio, pwm, initial_backlight)
#        super(AdafruitLCD.Adafruit_CharLCD, self).__init__(rs, en, d4, d5, d6, d7, columns, rows, backlight, invert_polarity, enable_pwm, gpio, pwm, initial_backlight)
           


#lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
#lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight, True, True)
#lcd = AdafruitLCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
#lcd = AdafruitLCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight, True, True)

#localtime = time.localtime(time.time())
#localtime = time.asctime(localtime)
#print localtime

#lcd.message(localtime)
#time.sleep(0.5)

#lcd.set_backlight(0)

#for i in range(11):
#    lcd.set_backlight(i/10.0)
#    time.sleep(0.7)






















