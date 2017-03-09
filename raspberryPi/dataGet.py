#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports
import time
import subprocess
from operator import attrgetter

def __main():

    # wait arduino bootup
    time.sleep(3.0)

    # serial setting
    ser = serial.Serial(
        baudrate = 9600,
        bytesize = serial.EIGHTBITS,
        parity = serial.PARITY_EVEN,
        stopbits = serial.STOPBITS_ONE,
        timeout = 1
    )

    # get a list of ports
    ser_ls = [i for i in serial.tools.list_ports.comports() if i.location is not None]

    # sort by port location
    ser_ls.sort(key=attrgetter('location'))

    while True:
        for i in ser_ls:
            ser.port = i.device
            ser.open()

            # wait data
            while(ser.inWaiting() < 1):
                time.sleep(0.1)

            # read line
            while True:
                num = ser.readline().decode('utf-8').strip()
                if num:
                    break

            print(i.device)
            print(num)

            ser.close()

    # suspend
    # subprocess.call(["rtcwake", "-m", "mem", "-s", "900"])

if __name__ =='__main__':
    __main()

