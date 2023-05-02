import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0) 

def analog_read(channel):

    if channel > 3 or channel < 0:
        return -1
   
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out

if __name__ == '__main__':
    while True:
        x = analog_read(0)
        if x < 500:
            print(x)
        time.sleep(0.1)
