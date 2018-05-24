#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import minimalmodbus
import MySQLdb


minimalmodbus.BAUDRATE = 19200
minimalmodbus.TIMEOUT = 60
slave_addr = 1
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_addr)

temperature = instrument.read_register(1, 2) # Donnée dans le tableau, nombre de décimales
debit = instrument.read_register(0, 0)