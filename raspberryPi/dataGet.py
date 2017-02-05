#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports

if __name__ =='__main__':
    ser = serial.Serial()
    ser.baudrate = 9600

    # get a list of ports
    ser_ls = serial.tools.list_ports.comports()

    for i in ser_ls:
        print (i)
        ser.port = i
        ser.open()

        num=ser.read(5)

        print(num)

