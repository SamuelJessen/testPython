from tkinter import *
import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1015()
root = Tk()
root.geometry("800x480")



for x in range(0,10): 
    data = adc.read_adc(1,gain=1)
    print(data)
    time.sleep(0.5)


root.mainloop()






