#!/usr/bin/python

import sys
import serial

PORT_NAME = '/dev/ttyUSB0'

def main(input_number):
  ser = serial.Serial(PORT_NAME, 19200, timeout=1)   # Open serial port
  print ser.name
  cmd = 'sw i0%s\r\n' % input_number
  print cmd
  ser.write(cmd)
  ser.close()


if __name__ == '__main__':
  main(sys.argv[1]) # We only care about the first argument
