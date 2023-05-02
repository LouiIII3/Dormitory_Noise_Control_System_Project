import time
import spidev
import RPi.GPIO as GPIO

BASE = 200
SPI_CHAN = 0

spi = spidev.SpiDev()
spi.open(0, SPI_CHAN)
spi.max_speed_hz = 1000000

GPIO.setmode(GPIO.BCM)
GPIO.setup(BASE, GPIO.IN)


def analog_read(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


while True:
    x = analog_read(BASE)
    if x < 500:
        print(x)
    time.sleep(0.1)
