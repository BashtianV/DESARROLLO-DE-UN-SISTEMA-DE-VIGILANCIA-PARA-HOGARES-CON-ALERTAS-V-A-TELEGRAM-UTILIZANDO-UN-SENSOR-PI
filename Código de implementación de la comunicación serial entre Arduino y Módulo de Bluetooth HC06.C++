import serial
 
Dispositivo= 'COM9'
baudios = 9600
 
# Connect to the device
s = serial.Serial(Dispositivo, baudios)
s.write(b'a')
s.close
