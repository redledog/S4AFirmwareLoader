import os
import serial.tools.list_ports


# Get list available comport
def get_ports():
    ports = serial.tools.list_ports.comports()

    available_port = []

    for p in ports:
        available_port.append(p.device)
        
    print(available_port)
    return available_port

# upload hex file to arduino
def upload_hex_file(comport, hex_file):
    hex_path = os.path.abspath(f"./hex/{hex_file}")
    



a = get_ports()

HEX_FILE = "Blink.ino.standard.hex"

upload_hex_file(a[0], HEX_FILE)
