from machine import Pin


led = Pin(2, Pin.OUT)


def is_on():
    return led.value() == 1


def on():
    led.value(1)


def off():
    led.value(0)
