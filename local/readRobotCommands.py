#!/usr/bin/env python
"""
    This will get the robot command list from my website and then send them to the arduino
    microcontroller. Also this command is beautiful: stty -F /dev/ttyUSB0 -hupcl.
    It turns off hardware flow control off so the arduino won't reset when you echo to it.
"""

import numpy as np
import time
from subprocess import call
from rrb3 import *

#creates rrb3 object using 9V supply and 3V motors
rr = RRB3(9,3)

#Let's server know that the bot has finished it's current queue of commands
def callServer():
    call(["sftp","-b","sendFlag.txt","hyperdrifter@tegrubbs.me"])

#Sends command to arduino via serial port. Must send a string. Will always have to change ttyACM0 to the correct serial port. Sleep time is currently the same as Arduino's delay time, 200ms.
def sendCMD(cmd):
    if cmd in ('f','b','l','r'):
	if cmd == 'f':
		rr.forward(1,.5)
	elif cmd == 'b':
		rr.reverse(1,.5)
	elif cmd == 'l':
		rr.left(1,.5)
	elif cmd == 'r':
		rr.right(1,.5)

def clearCommandList():
    call(["rm","output.txt"])



#begins main control loop
while True:
    #gets command list. If empty keeps trying
    while True:
        try:
            call(["wget","https://tegrubbs.me/Robot/output.txt"])
            cmdarr = np.loadtxt("output.txt", dtype="string", skiprows=1, usecols=(2,))
            break
        except:
            print("Error! Probably an empty list of commands! Sending GO_FLAG")
            clearCommandList()
            callServer()
            time.sleep(1)

    #trys to iterate through command list. If only one command present then it catches the 0-D error
    try:
        for i in cmdarr:
            sendCMD(i)
        callServer()
    except:
        sendCMD(str(cmdarr))
        callServer()

    clearCommandList()
