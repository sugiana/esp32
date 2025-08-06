from machine import Pin


led = Pin(22, Pin.OUT)


def is_on():
    return led.value() == 0


def on():
    led.value(0)


def off():
    led.value(1)


off()
