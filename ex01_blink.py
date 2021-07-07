import RPi.GPIO as gp   # python에서 GPIO를 사용하기 위해
import time            
gp.setmode(gp.BCM)      # index에서 NAME부분을 사용
for i in range(18,21):
    gp.setup(i, gp.OUT)    # 18번핀에 Actuator가 연결됨
    

try:
    while True:
        for i in range(18,21):
            gp.output(i,gp.HIGH)
            time.sleep(0.1)
            gp.output(i, gp.LOW)
            time.sleep(0.1)
except KeyboardInterrupt:          # Ctrl + C를 통해서 코드 종료
    gp.cleanup()