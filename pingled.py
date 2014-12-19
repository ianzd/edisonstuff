#!/usr/bin/python

import mraa
import socket

ledpin = 4

def toggleled(led):
  currentval = led.read()
  led.write(not currentval)


def pingloop():
  sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
  sock.bind(('', 0))
  led  = mraa.Gpio(ledpin)
  while True :
    data = sock.recv(2)
    toggleled(led)

if __name__ == '__main__':
  pingloop()
