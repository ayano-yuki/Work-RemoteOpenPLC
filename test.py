from serial.tools import list_ports
from pymodbus.client import ModbusSerialClient as ModbusClient

device_port = []
check_list = ["Arduino", "Raspberry", "ESP32", "tty"]
for info in list_ports.comports():
    for item in check_list:
        if item in info.description:
            device_port.append(info.device)

print(f"COM port connected to microcontroller : {device_port[0]}")
client = ModbusClient(method = "rtu", port=device_port[0], baudrate= 115200, timeout=0.1)
client.connect()



rr = client.read_coils(address=0, slave=1)
print(rr.bits)
client.write_coils(address=0, values=1, slave=1)
rr = client.read_coils(address=0, slave=1)
print(rr.bits)