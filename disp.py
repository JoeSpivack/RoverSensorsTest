import sys
import json
sys.path.insert(0, './comms-python/')

from Node import Node

node = Node("disp.json")

while True:
    msg = node.recv_simple("sensors-in")
    print (msg)
