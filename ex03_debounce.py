import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setup(21,gp.IN)
gp.output(18,gp.OUT)

cnt = 0
check = True
while True:
    buttonState = gp.input(21)
    if buttonState ==1:
      if check == True:
          cnt +=1
          check = False
          
    else:
        check = True
    print(cnt)    
    
    if cnt % 2 ==1:
        gp.output(18,gp.HIGH)
    else:
        gp.output(18,gp.LOW)
        