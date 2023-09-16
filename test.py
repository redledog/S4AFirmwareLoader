from avr_multiloader.avr_multiloader import avrdude

# a = avrdude(partno='ATmega328P', programmer_id='arduino', baud_rate='115200',
#             port='/dev/ttyUSB0')


a = avrdude(partno='ATmega328P', programmer_id='arduino', baud_rate='115200',
            port='COM5')

HEX_FILE = "Blink.ino.standard.hex"

output, error_out = a.testConnection()
output, error_out = a.flashFirmware(f'./hex/{HEX_FILE}', ['-vv'])
print(output)

