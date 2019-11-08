import sys
import json
sys.path.insert(0, './coms-python/Node.py')

import Node from Node

node = Node("disp.json")

while True:
    msg = node.recv_simple("sensors-out")
    print (msg)
