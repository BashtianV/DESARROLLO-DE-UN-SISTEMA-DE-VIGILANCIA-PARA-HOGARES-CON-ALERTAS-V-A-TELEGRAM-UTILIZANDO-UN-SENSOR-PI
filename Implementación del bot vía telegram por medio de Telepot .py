import telepot
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
from telepot.loop import MessageLoop
from subprocess import call 
import serial

Dispositivo= '/dev/ttyAMA0'
baudios = '9600'
s = serial.Serial(Dispositivo,baudios)

PIR    = 4
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

motion = 0
motionNew = 0
 
def handle(msg):
    global telegramText
    global chat_id
  
    chat_id = msg['chat']['id']
    telegramText = msg['text']
  
    print('Mensaje recibido de ' + str(chat_id))
  
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'SIN DETECCIÓN.')
        

    while True:
        main()
    
bot = telepot.Bot('5406541478:AAH5twKnQz8aXWvHmydJAL4NKXz-qJktBQw')
bot.message_loop(handle)       
     
def main():
        
    global chat_id
    global motion 
    global motionNew
    
    if GPIO.input(PIR) == 1:
        
        print("INTRUSO DETECTADO")
        motion = 1
        if motionNew != motion:
            motionNew = motion
            sendNotification(motion)
               
    elif GPIO.input(PIR) == 0:
        print("DESPEJADO")
        motion = 0
        if motionNew != motion:
            motionNew = motion

def sendNotification(motion):   

    global chat_id
    
    if motion == 1:
        filename = "/home/augusto124/Desktop/v/video" + (time.strftime("%y%b%d_%H%M%S"))
        camera.start_recording(filename + ".h264")
        sleep(10)
        camera.stop_recording()
        command = "MP4Box -add " + filename + '.h264' + " " + filename + '.mp4'
        print(command)
        call([command], shell=True)
        bot.sendVideo(chat_id, video = open(filename + '.mp4', 'rb'))
        bot.sendMessage(chat_id, 'MOVIMIENTO DETECTADO')

while 1:
    time.sleep(5)