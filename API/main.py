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