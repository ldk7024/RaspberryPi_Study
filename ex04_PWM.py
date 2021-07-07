# PWM (Pulse Width Modulation): 펄스폭 변조
import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(18,gp.OUT)

p = gp.PWM(18,500)
p.start(0)

while True:
  for i in range(101):
      p.ChangeDutyCycle(i)
      time.sleep(0.05)
  for i in range(100,-1,-1):
      p.ChangeDutyCycle(i)
      time.sleep(0.05)
    
