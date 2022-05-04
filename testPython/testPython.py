from tkinter import *
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1015()
root = Tk()
root.geometry("800x480")
T = Text(root,height = 5, width = 5)


for x in range(0,500): 
    data = adc.read_adc(1,gain=GAIN)
    T.insert(tk.END, data)


root.mainloop()






