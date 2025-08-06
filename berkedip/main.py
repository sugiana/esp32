from time import sleep
import led

while True:
    sleep(1)
    led.on()
    sleep(2)
    led.off()
