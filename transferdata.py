import serial
import time


while 1:
    ser = serial.Serial(port="COM5", baudrate=9600)
    ser.write("1".encode('utf-8'))
    time.sleep(5)
    print("舵机已启动")
    time.sleep(10)
    ser.close()






