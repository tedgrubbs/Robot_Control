#!/usr/bin/env python
"""
    This will get the robot command list from my website and then send them to the arduino
    microcontroller. Also this command is beautiful: stty -F /dev/ttyUSB0 -hupcl.
    It turns off hardware flow control off so the arduino won't reset when you echo to it.
    SFTP calls are to let server know that the arduino has finished it's current command list
    or has none.
"""

import numpy as np
import time
from subprocess import call
import os

#initialize arduino to not reset with every echo connection
call(["stty","-F","/dev/ttyACM0","-hupcl"])

#Let's server know that the bot has finished it's current queue of commands
def callServer():
    call(["sftp","-b","sendFlag.txt","hyperdrifter@tegrubbs.me"])

#Sends command to arduino via serial port. Must send a string. Will always have to change ttyACM0 to the correct serial port. Sleep time is currently the same as Arduino's delay time, 200ms.
def sendCMD(cmd):
    if cmd in ('f','b','l','r'):
        commandString = ["echo"," \"",cmd,"\" ","> ", "/dev/ttyACM0"]
        os.system(''.join(commandString))
        time.sleep(0.2)

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
