#from tkinter import *

#Regarding sensors from ADC:
import time
import Adafruit_ADS1x15
adcforce = Adafruit_ADS1x15.ADS1015(address=0x48)
adctemplight = Adafruit_ADS1x15.ADS1015(address=0x49)

#Regarding temp sensor:
import os
import glob
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Readtemp raw method
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
#readtempincelcius
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def read_adc():
    data1 = adcforce.read_adc(1,gain=2/3)
    data2 = adctemplight.read_adc(2,gain=2/3)
    print("data læst fra adc 1:" + data1)
    print("data læst fra adc 2:" + data2)

while True:
    print("Temperatur: " + str(read_temp()))
    read_adc()
    time.sleep(3)
