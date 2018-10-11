from DataTransferFromMeter.PcDataTransferModule import *
from tkinter import*




class MeterReadingWindow ():

    def __init__(self,master):

        self.label=Label(master)
        self.label.grid(row=0,column=0,sticky=W)
        self.button=Button(master,text="Meter Reading",command=self.showNum)
        self.button.grid(row=1,column=0)
        self.clearButton=Button(master,text="Clear",command=self.clear)
        self.clearButton.grid(row=1,column=1)
        master.winfo_toplevel().title("Meter Reading")

    def clear(self):
        self.label.config(text="")

    def showNum(self):
        self.label.config(text="data is {0}".format(getDataFromMeter()))
    






root=Tk()

meterFrame=Frame(root)
dataBaseFrame=Frame(root)

root.geometry("950x55")


MeterReadingWindow(meterFrame)

meterFrame.pack(side=LEFT)


root.mainloop()



