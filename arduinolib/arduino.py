from path import Path
import serial.tools.list_ports
from avr_multiloader import avr_multiloader 

#HEX_FILE = "Blink.ino.standard.hex"
HEX_FILE = "S4AFirmware16.ino.standard.hex"

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

def get_avrdude(comport, baud_rate):
    avrd = avr_multiloader.avrdude(partno='ATmega328P', programmer_id='arduino', baud_rate=baud_rate,
            port=comport, confpath='./avrdude/avrdude.conf')
    avrd.avrdudePath = Path('./avrdude/avrdude.exe').abspath()
    print(avrd.avrdudePath)
    print(avrd.avrconf)
    return avrd

def connect_test(avrdude_obj : avr_multiloader.avrdude):
    output, error_out = avrdude_obj.testConnection()
    return output, error_out

# upload hex file to arduino
def upload_hex_file(avrdude_obj : avr_multiloader.avrdude):
    hex_path = Path(f"./hex/{HEX_FILE}").abspath()
    output, error_out = avrdude_obj.flashFirmware(hex_path, ['-vv'])
    return output, error_out