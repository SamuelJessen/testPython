from tkinter import *
import time
import Adafruit_ADS1x15
adcport1 = Adafruit_ADS1x15.ADS1015(address=0x48)
adcport2 = Adafruit_ADS1x15.ADS1015(address=0x49)


root = Tk()
#root.geometry("800x480")
#root.title('PythonTestProgram')

#temperatur felt
#frame = LabelFrame(root,padx=5,pady=5,bg="green",)
#frame.pack(padx=10,pady=10)
#frame.place(x=10,y=10)
#Label(frame,text="TEMPERATUR").pack(pady=20)
#lysfelt 
#frame = LabelFrame(root,padx=5,pady=5,bg="green",)
#frame.pack(padx=10,pady=10)
#frame.place(x=10,y=100)
#Label(frame,text="LYS").pack(pady=20)



for x in range(0,100): 
    data1 = adcport1.read_adc(1,gain=2/3)
    data2 = adcport2.read_adc(2,gain=2/3)
    print("data læst fra adc 1:" + data1)
    print("data læst fra adc 2:" + data1)
    time.sleep(4)


#class ForceControl:
    #def __init__(self, name):
        #self.name = name

    #def _update_widgets_(self,forceinput):



root.mainloop()






