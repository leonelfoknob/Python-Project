import serial
import time

ser = serial.Serial('COM3',115200, timeout=0.1)

#arduino = serial.Serial('COM3',115200, timeout=0.1)

def read_sensor_data():
    data = arduino.readline()
    return data
while True:
    value = read_sensor_data
    Myfile = open('leo_file.txt','a+')
    Myfile.write('Temperature Sensor  Value : ')
    Myfile.write('\n'+'Data:'+ str(value))
    Myfile.close()