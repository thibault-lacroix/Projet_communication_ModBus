#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import minimalmodbus

minimalmodbus.BAUDRATE = 19200
minimalmodbus.TIMEOUT = 10

#slave_addr = 1
port = '/dev/ttyUSB0'

REG_DEBIT = 0
REG_TEMP = 1
REG_VANNE_STATE = 2
REG_DEBIT_STATE = 3