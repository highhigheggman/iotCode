#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports
import time

if __name__ =='__main__':

    # wait arduino bootup
    time.sleep(2.0)

    ser = serial.Serial()
    ser.baudrate = 9600

    # get a list of ports
    #ser_ls = serial.tools.list_ports.comports()

    ser.port = '/dev/tty.usbmodem14341'
    ser.open()

    while True:
        num=ser.read
        print(num)

    """
    for i in ser_ls:
        print (i)
        ser.port = i
        ser.open()

        num=ser.read(5)

        print(num)
"""
