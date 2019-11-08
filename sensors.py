import sys
import json
import serial
sys.path.insert(0, './comms-python/')

from Node import Node

# ser device names:
# Co2 ppm
# TVOC
# MQ-7 PPM

baud = 115200
node = Node("sensors.json")
ser = serial.Serial(sys.argv[1], baud)
while True:
    # parse the ser data to a json
    msg = ser.readline()
    msg = str(msg)
    node.send("sensors-out", msg)

