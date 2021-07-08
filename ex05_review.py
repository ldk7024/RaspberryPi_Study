import RPi.GPIO as gp

gp.setmode (gp.BCM)

gp.setup (20, gp.IN)
gp.setup (21, gp.IN)
gp.setup (18, gp.OUT)

p = gp.PWM(18,500)
p.start(0)

while True:
    buttonState1 = gp.input(20)
    buttonState2 = gp.input(21)
    print(buttonState1, buttonState2)
    
    if buttonState1 ==1:
        p.ChangeDutyCycle(50)
    if buttonState2 ==1:
        p.ChangeDutyCycle(100)
        
    