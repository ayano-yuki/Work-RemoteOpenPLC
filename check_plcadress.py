from pymodbus.client import ModbusTcpClient as ModbusClient
from time import sleep

# 接続するデバイスのIPアドレスとポート番号を指定します。
IP_ADDRESS = '127.0.0.1'
PORT = 502
client = ModbusClient(host=IP_ADDRESS, port=PORT, timeout=0.1)
client.connect()
sleep(1.6)

# レジスタの探索
for i in 300:
    value =  client.read_holding_registers(address=i, count=1, slave=1)[0]
    if value is not 0:
        print(f"{i:3d} : {value}")

# ボタンの探索
for i in 300:
    value =  client.read_coils(address=i, count=1, slave=1)[0]
    if value is not 0:
        print(f"{i:3d} : {value}")