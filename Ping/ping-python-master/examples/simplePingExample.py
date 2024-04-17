#!/usr/bin/env python

#simplePingExample.py
from brping import Ping1D
import time
import argparse

from builtins import input

##Parse Command line options
############################


# Make a new Ping
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)


if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

print("------------------------------------")
print("Starting Ping..")
print("Press CTRL+C to exit")
print("------------------------------------")

input("Press Enter to continue...")

# Read and print distance measurements with confidence
while True:
    data = myPing.get_distance()
    if data:
        print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))
    else:
        print("Failed to get distance data")
    time.sleep(0.1)
