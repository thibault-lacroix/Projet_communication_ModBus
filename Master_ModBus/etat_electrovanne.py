#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import sys
import minimalmodbus
import time
from settings import *

#minimalmodbus.BAUDRATE = 19200
#minimalmodbus.TIMEOUT = 10

#REG_DEBIT = 0
#REG_TEMP = 1
#REG_VANNE_STATE = 2
#REG_DEBIT_STATE = 3

off=0
on=1

slave_addr = sys.argv[1]
slave_addr = int(slave_addr)
print "L'adresse est: ", slave_addr


etat_vanne = sys.argv[2]
print "La valeur est: ", etat_vanne

instrument = minimalmodbus.Instrument(port, slave_addr,mode='rtu')
while True:
    if etat_vanne=='stop':
        instrument.write_register(REG_VANNE_STATE, off)
        print "Electrovanne OFF"
    elif etat_vanne=='start':
        instrument.write_register(REG_VANNE_STATE, on)
        print "Electrovanne ON"
    else:
        print "Erreur argument"
        break