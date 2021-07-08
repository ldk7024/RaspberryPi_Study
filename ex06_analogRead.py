import spidevRead as sr
import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)
while True:
    readData = sr.analog_read(0)
    print('readData : {}'.format(readData))
    
    if readData < 800:
        gp.output(18, gp.HIGH)
    else:
        gp.output(18, gp.LOW)
    