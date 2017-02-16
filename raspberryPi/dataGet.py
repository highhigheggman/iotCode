#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports
import time
import subprocess
from operator import itemgetter, attrgetter

if __name__ =='__main__':

    # wait arduino bootup
    time.sleep(3.0)

    # serial setting
    ser = serial.Serial()
    ser.baudrate = 9600

    num = 0

    # get a list of ports
    ser_ls = [i for i in serial.tools.list_ports.comports() if i.location is not None]

    # sort by port location
    ser_ls.sort(key=attrgetter('location'))


    for i in ser_ls:
        ser.port = i.device
        ser.open()

        # wait data
        while(ser.inWaiting() < 0):
            time.sleep(0.1)

        # read data
        num = int(ser.readline())

        print(i.device)
        print(num)

        ser.close()


    # suspend
    # subprocess.call(["rtcwake", "-m", "mem", "-s", "900"])
