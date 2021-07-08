import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.start_preview()
    camera.start_recording('test222.h264')
    camera.wait_recording(12)
    camera.stop_recording()
    camrea.stop_preview()