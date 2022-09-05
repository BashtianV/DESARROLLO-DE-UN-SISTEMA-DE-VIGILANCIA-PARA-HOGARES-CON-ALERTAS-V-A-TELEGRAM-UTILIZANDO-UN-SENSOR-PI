from gpiozero import MotionSensor
from picamera import PiCamera
import time
 
pir=MotionSensor(4)
camera=PiCamera()
contador=0
while True:
        pir.wait_for_motion()
        camera.start_preview()
        contador=contador+1
        camera.capture('/home/augusto124/Desktop/foto%s.jpg' % contador)
        print('Intruso')
        pir.wait_for_no_motion()
        camera.stop_preview()
        time.sleep (3)
