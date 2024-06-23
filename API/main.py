# -----import--------------------------------------------------------------------------------------------
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import random
import time
import json
from time import sleep
from serial.tools import list_ports
from pymodbus.client import ModbusSerialClient as ModbusClient
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

# -----Running-------------------------------------------------------------------------------------------
camera_index = 0
state        = "waiting"
result       = []

# Establishing modbus RTU communication
device_port = []
check_list = ["Arduino", "Raspberry", "ESP32", "tty"]
for info in list_ports.comports():
    for item in check_list:
        if item in info.description:
            device_port.append(info.device)

print(f"COM port connected to microcontroller : {device_port[0]}")
client = ModbusClient(method = "rtu", port=device_port[0], baudrate= 115200, timeout=0.1)
client.connect()
sleep(1.6)

# Launching the API server
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# -----Function------------------------------------------------------------------------------------------
def process_in_background():
        global client
        global result

        rr = client.read_coils(address=0, slave=1)
        print(rr.bits)
        client.write_coils(address=0, values=1, slave=1)
        rr = client.read_coils(address=0, slave=1)
        print(rr.bits)

        while True:
            if state == "processing":
                rr = client.read_holding_registers(address=0, count=20, slave=1)
                result = rr.registers
                sleep( 10 / 1000 )

            else:
                rr = client.read_coils(address=1, slave=1)
                print(rr.bits)
                client.write_coils(address=1, values=1, slave=1)
                rr = client.read_coils(address=1, slave=1)
                print(rr.bits)
                break

# -----POST data format----------------------------------------------------------------------------------
class Setting(BaseModel):
    Name:           str
    Address:        int
    Max:            int
    Min:            int
    Unit:           str
    Division:       int
    Multiplication: int
    Graph:          str

class Result(BaseModel):
    Name:  str
    Data:  list
    Graph: str

# -----API-----------------------------------------------------------------------------------------------
@app.post("/save_setting", response_description='response', tags=['Setting'])
def save_setting(datas:list[Setting]):
    """
    Save the received information in json format
    - **datas** post data  
    """
    save_data = []
    for data in datas:
        save_data.append({
            "Name":            data.Name,
            "Address":         data.Address,
            "Max":             data.Max,
            "Min":             data.Min,
            "Unit":            data.Unit,
            "Division":        data.Division,
            "Multiplication":  data.Multiplication,
            "Graph":           data.Graph,
        })

    with open('../Front/public/json/setting.json', 'w') as f:
        json.dump(save_data, f, indent=4)

    return {
        "message": "success",
    }

@app.post("/save_result", response_description='response', tags=['Setting'])
def save_result(datas:list[Result]):
    """
    Save the received information in json format
    - **datas** post data  
    """
    print(datas)
    save_data = []
    for data in datas:
        save_data.append({
            "Name":  data.Name,
            "Data":  data.Data,
            "Graph": data.Graph,
        })

    with open('../Front/public/json/result.json', 'w') as f:
        json.dump(save_data, f, indent=4)

    return {
        "message": "success",
    }

@app.post("/start_experiment", response_description='response', tags=['Running'])
async def start_processing(background_tasks: BackgroundTasks):
    """
    Start of experiment (start of measurement)
    """
    global state
    state = "processing"

    background_tasks.add_task(process_in_background)
    return (
        {
            "message": "Processing started"
        }
    )

@app.post("/stop_experiment", response_description='response', tags=['Running'])
async def stop_processing():
    """
    Stopping the experiment (stopping the measurement)
    """
    global state
    state = "waiting"
    return (
        {
            "message": "Processing stopped"
        }
    )

@app.get("/get_experiment_result", response_description='response', tags=['Running'])
def get_result():
    """
    Obtaining experimental measurements
    """
    global result
    return (
        {
            "result": result
        }
    )