import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(18,gp.OUT)

def led18on():
    gp.output(18,gp.HIGH)

def led18off():
    gp.output(18,gp.LOW)
    