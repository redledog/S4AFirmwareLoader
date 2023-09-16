import os
import serial.tools.list_ports

HEX_FILE = "Blink.ino.standard.hex"
BAUD_RATE = [
    300, 600, 1200, 2400,
    4800, 9600, 14400,
    19200, 28800, 31250,
    38400, 57600, 115200
    ]

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