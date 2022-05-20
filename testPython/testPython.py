#from tkinter import *

#Regarding sensors from ADC:
import time
import Adafruit_ADS1x15
adcforce = Adafruit_ADS1x15.ADS1015(address=0x48)
adctemplight = Adafruit_ADS1x15.ADS1015(address=0x49)

#Regarding temp sensor:
import os #Miscellaneous operating system interfaces
import glob #Unix style pathname pattern expansion
os.system('modprobe w1-gpio') #takes a command and runs it. 
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/' # gives a path to our base directory
device_folder = glob.glob(base_dir + '28*')[0] #modul, lægger 28* til i filen. 
device_file = device_folder + '/w1_slave'

#Readtemp raw method
def read_temp_raw():
    f = open(device_file, 'r') #åbner fil og giver rettigheder til at skrive i den 
    lines = f.readlines() #lægger dem i en liste
    f.close() #lukker
    return lines #returnere listen
 
#readtempincelcius
def read_temp():
    lines = read_temp_raw() #henter linjerne fra metoden over. 
    while lines[0].strip()[-3:] != 'YES': # fjerner alt uden de tre sidste digits i linjen, når YES ikke er i linjen. 
        time.sleep(0.2)
        lines = read_temp_raw() #laver en ny liste
    equals_pos = lines[1].find('t=') #Look for the position of the '=' in the second line of the device file.
    if equals_pos != -1: #hvis der er et "=", så skal resten converteres til celsius
        temp_string = lines[1][equals_pos+2:] 
        temp_c = float(temp_string) / 1000.0
        return temp_c #nu er det lavet om til celsius.

def read_adc():
    data1 = adcforce.read_adc(1,gain=2/3)
    data2 = adctemplight.read_adc(2,gain=2/3)
    print("data læst fra adc 1:" + str(data1))
    print("data læst fra adc 2:" + str(data2))

while True: #printer temperaturen indtil programmet stoppes. 
    print("Temperatur: " + str(read_temp()))
    read_adc()
    time.sleep(3)
