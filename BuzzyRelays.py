#!/usr/bin/Python
import serial
import sys
from time import sleep
import os
import random

ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 2            #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write
ser.port = "/dev/ttyUSB0"
random.seed()
ser.open()

relayTriggers = [
    bytearray.fromhex("3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A"),
    bytearray.fromhex("3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A")]
    


if len(sys.argv) != 2:
    print ("Usage: python BuzzyRelays.py <relay #>")
    sys.exit()

if sys.argv[1] == "TEST":
    for i in range(1, 8):
        os.system("python BuzzyRelays.py "+str(i))


if sys.argv[1] == "1":
    
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A"))

if sys.argv[1] == "2":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A"))

if sys.argv[1] == "3":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A"))

if sys.argv[1] == "4":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A"))

if sys.argv[1] == "5":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A"))

if sys.argv[1] == "6":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A"))

if sys.argv[1] == "7":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A"))

if sys.argv[1] == "8":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A"))


if sys.arg[1] == "RANDOM":
    for i in range(1, 20):
        ser.write(relayTriggers[random.randint(1,16)])
        sleep(10)
