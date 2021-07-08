import spidevRead as sr
import led18

while True:
    readData = sr.analog_read(0)
    print('readData : {}'.format(readData))
    
    if readData <=700:
        led18.led18on()
    else:
        led18.led18off()