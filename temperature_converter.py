from cgitb import text
import tkinter as tki
def fah_cels():
    
        fah = ent_frm.get()
        cel = (5/9)*(float(fah) - 32)
        lbl_result["text"] = float(round(cel,2)),"C"
    
    

win = tki.Tk()
win.resizable(width=0,height=0)
win.title("Temperature Converter")
frame_entry=tki.Frame(win)
ent_frm = tki.Entry(frame_entry,width=10)
lbl_temp = tki.Label(frame_entry,text ="F")
ent_frm.grid(row=0,column=0,sticky="e")
lbl_temp.grid(row=0,column=1,sticky="w")
btn_convert = tki.Button(win,text="-->",command=fah_cels)
lbl_result = tki.Label(win,text="C")
frame_entry.grid(row=0,column=0,padx=10)
btn_convert.grid(row=0,column=1,pady=10)
lbl_result.grid(row=0,column=2,padx=10)


win.mainloop()
