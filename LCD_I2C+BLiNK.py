import machine

from machine import Pin, I2C 
from lcd_api import LcdApi
from i2c_lcd import LcdI2c
from time import sleep

    I2C_ADDR = 0x27
    totalRows = 2
    totalColumns = 16

    i2c = I2C(slc=Pin(22)), sda=Pin(21), freq=10000
    lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

    while True:
        lcd.putstr("Texto1")
        sleep(4)
        lcd.clear()
        lcd.putstr("Texto2")
        sleep (4)
        lcd.clear()
        
        from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep (0.5)
