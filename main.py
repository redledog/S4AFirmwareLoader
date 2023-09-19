import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from arduinolib import arduino
from resourece_path import init_resource_path
from path import Path

def refresh_comport(cbbox : ttk.Combobox):
    comport_list = arduino.get_ports()
    cbbox['values'] = comport_list
    if len(comport_list) > 0:
        cbbox.set(comport_list[0])
    else:
        cbbox.set("")

def check_comport(comport):
    if comport == "":
        messagebox.showwarning("경고!","COM 포트가 비어있습니다.")
        return False
    return True

def test_connect(comport, baudrate):
    if not check_comport(comport):
        return
    print(comport, baudrate)
    res = arduino.connect_test(arduino.get_avrdude(comport, baudrate))
    set_log_text(res)
    messagebox.showinfo("알림","작업 완료!")

def upload_file(comport, baudrate):
    if not check_comport(comport):
        return
    res = arduino.upload_hex_file(arduino.get_avrdude(comport, baudrate))
    set_log_text(res)
    messagebox.showinfo("알림","작업 완료!")

def set_log_text(text):
    log_txt.config(state=tk.NORMAL)
    log_txt.delete("1.0", tk.END)
    for t in text:
        log_txt.insert(tk.END, f"{t.decode('cp949')}\n")
        print(f"{t.decode('cp949')}\n")
    log_txt.config(state=tk.DISABLED)
    
init_resource_path()

win = tk.Tk()
win.title("S4A 펌웨어 로더")
win_w = win.winfo_screenwidth()
win_h = win.winfo_screenheight()
win.geometry(f"+{win_w//3}+{win_h//3}")
win.resizable(False, False)

# icon 적용
icon_path = Path("./imgs/logo.png").abspath()
icon_img = tk.PhotoImage(file = icon_path)
win.iconphoto(False, icon_img)

comport_list = []

com_port_frame = ttk.Frame(win)
com_port_frame.pack()
upload_frame = ttk.Frame(win)
upload_frame.pack()
log_frame = ttk.Frame(win)
log_frame.pack()

lbl1 = ttk.Label(com_port_frame, text="COM 선택 ")
com_cbbox = ttk.Combobox(com_port_frame, values=comport_list)
refresh_btn = ttk.Button(com_port_frame, text="새로고침", command= lambda : refresh_comport(com_cbbox))

refresh_comport(com_cbbox)

lbl1.pack(side="left")
com_cbbox.pack(side="left")
refresh_btn.pack(side="left")

lbl2 = ttk.Label(upload_frame, text="보드레이트 선택 ") 
lbl2.pack(side="left")

baud_cbbox = ttk.Combobox(upload_frame, values=arduino.BAUD_RATE)
baud_cbbox.set(115200)
baud_cbbox.pack(side="left")

test_btn = ttk.Button(upload_frame, text="연결 테스트",
                    command = lambda: test_connect(com_cbbox.get(), baud_cbbox.get()))
test_btn.pack()

upload_btn = ttk.Button(upload_frame, text="업로드",
                        command = lambda: upload_file(com_cbbox.get(), baud_cbbox.get()))
upload_btn.pack()

log_label = ttk.Label(log_frame, text='Log')
log_label.pack()
log_txt = tk.Text(log_frame, state=tk.DISABLED)
log_txt.pack()

win.mainloop()