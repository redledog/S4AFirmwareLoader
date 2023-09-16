import tkinter as tk
import tkinter.ttk as ttk
from arduinolib import arduino

def refresh_comport(cbbox : ttk.Combobox):
    comport_list = arduino.get_ports()
    cbbox['values'] = comport_list
    if len(comport_list) > 0:
        cbbox.set(comport_list[0])
    else:
        cbbox.set("")
    

win = tk.Tk()
win.title("S4A 펌웨어 로더")
win.geometry("300x300+500+500")
win.resizable(False, False)

comport_list = arduino.get_ports()

com_port_frame = ttk.Frame(win)
com_port_frame.pack()
upload_frame = ttk.Frame(win)
upload_frame.pack()

lbl1 = ttk.Label(com_port_frame, text="COM 선택 ")
com_cbbox = ttk.Combobox(com_port_frame, values=comport_list)
refresh_btn = ttk.Button(com_port_frame, text="새로고침", command= lambda : refresh_comport(com_cbbox))

refresh_comport(com_cbbox)

lbl1.pack(side="left")
com_cbbox.pack(side="left")
refresh_btn.pack(side="left")

#baud_cbbox = ttk.Combobox(upload_frame, values=comport_list)

win.mainloop()