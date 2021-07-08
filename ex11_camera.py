import picamera as pc
import time

camera = pc.PiCamera()

camera.start_preview()
time.sleep(5)
# camera.capture('../Downloads/test.jpg')

for i in range(3):
    camera.capture(f'test{i}.jpg')
    time.sleep(2)
    
camera.stop_preview()
camera.close()