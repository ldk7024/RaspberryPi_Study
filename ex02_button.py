import RPi.GPIO as gp

gp.setmode(gp.BCM)

gp.setup(21,gp.IN)  # 21번 핀에 연결된 모듈은 Sensor다.
gp.setup(18,gp.OUT) 
while True:
    buttonState = gp.input(21)
    print('buttonState: {}'.format(buttonState))
    
    gp.output (18,buttonState)
#    if buttonState ==1:
#        gp.output(21, 1)
#    else:
#        gp.output(21,gp.0)
        