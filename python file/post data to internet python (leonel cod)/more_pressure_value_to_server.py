#read data from arduino python cod
import serial
import time
import requests
import urllib3, urllib
import urllib.request as urllib2

headers = {"Content-Type": "application/json; charset=utf-8"}

ser = serial.Serial('COM5',9600, timeout=0.1)
ser.close()
ser.open()

#arduino = serial.Serial('COM3',115200, timeout=0.1)

def read_sensor_data():
    data = ser.readline()
    return data
    #return data.decode('utf-8')#convert reciving data by in string

while True:
    #value = read_sensor_data
    data = ser.readline()
    if data:#verifi si la ligne n'est pas vide si c'est vide sa ne fait rien au cas contraire sa enregistre et sa break
        value = data.decode('utf-8')
        rows = [x for x in value.split(',')] #prend les valeur et l'enregistre dans une liste et les converti en float
        #separe la liste en differente valeur donnée par le sensor
        temperature = rows[0] 
        pressure = rows[1]
        altitude = rows[2]
        ReadSealevelPressure = rows[3]
        Real_altitude = rows[4]

        temp =temperature
        press =pressure
        alt =altitude
        rsp =ReadSealevelPressure
        ra =Real_altitude
        #urllib2.urlopen.read()
        #res = urllib.request.urlopen("https://datamakinafleo.000webhostapp.com/add_data.php?temperature="+temp+"&pressure="+press+"&altitude="+alt+"&ReadSealevelPressure"+rsp+"&Real_altitude"+ra)

        #res = requests.post('https://datamakinafleo.000webhostapp.com/add_data.php', data={'temperature': temperature,'pressure':pressure,'altitude': altitude,'ReadSealevelPressure':ReadSealevelPressure,'Real_altitude':Real_altitude})
        res = requests.post('https://datamakinafleo.000webhostapp.com/add_data.php', data={'temperature': temperature})
        print(res.text)
        print("Status Code", res.status_code)

        print(value) #affiche les valeur brute
        print(rows) #affiche les valeur enregistrer dans la liste
        print("trmperature : " +  str(temperature)) #affiche la valeur temperature enregistrer comme 1er element de la liste
        print("Pressure : " +  str(pressure))
        print("Altitude : " +  str(altitude))
        print("ReadSealevelPressure : " +  str(ReadSealevelPressure))
        print("Real_altitude : " +  str(Real_altitude))