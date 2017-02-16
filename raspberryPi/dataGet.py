#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports
import time
import subprocess

if __name__ =='__main__':

    # wait arduino bootup
    time.sleep(3.0)

    # serial setting
    ser = serial.Serial()
    ser.baudrate = 9600

    num = 0

    # get a list of ports
    # ser_ls = serial.tools.list_ports.grep(pattern)

"""
    ser.port = '/dev/cu.wchusbserial14110'
    ser.open()

    while True:
        if (ser.inWaiting() > 0):
            num = int(ser.readline())
            print(num)

    """
    for i in ser_ls:
        print (i)
        ser.port = i
        ser.open()

        #num=ser.readline()

        #print(num)

    # suspend
    # subprocess.call(["rtcwake", "-m", "mem", "-s", "900"])

