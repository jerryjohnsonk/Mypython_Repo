from cgitb import text
from struct import pack
import tkinter as tki
def fne():
    print("Jerry")
m = tki.Tk()  # main window
m.title("Currency Converter")  #title of main window
gt = tki.Label(text="Python Rocks!!",bg='purple',fg='yellow',width=30,height=10)
bt = tki.Button(m,text='Start',bg='red',width=30,height=10,command=fne)
gt.pack()
bt.pack()
m.mainloop()
