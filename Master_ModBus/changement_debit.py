#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import sys
import minimalmodbus
import time
from settings import *


slave_addr = sys.argv[1]
slave_addr = int(slave_addr)
print "L'adresse est: ", slave_addr

debit = sys.argv[2]
debit = int(debit)
print "La valeur est: ", debit

instrument = minimalmodbus.Instrument(port, slave_addr,mode='rtu')

while True:
    if debit>=0:
        instrument.write_register(REG_DEBIT_STATE, debit)
        print "Debit: ", debit
    else:
        instrument.write_register(REG_DEBIT_STATE, 0)
        print "ERREUR"