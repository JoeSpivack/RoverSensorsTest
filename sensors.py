import sys
import json
import serial
sys.path.insert(0, './coms-python/Node.py')

import Node from Node

# ser device names:
# Co2 ppm
# TVOC
# MQ-7 PPM

baud = 115200
node = Node("sensors.json")
ser = serial.Serial(sys.args[1])
while True:
    # parse the ser data to a json
    msg = ser.readLine()
    msg = msg.decode('ANSI')
    node.send("sensors", msg)

