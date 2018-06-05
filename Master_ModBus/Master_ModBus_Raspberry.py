#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import minimalmodbus
import MySQLdb
import time
from settings import *
import sys

slave_addr = 1

instrument = minimalmodbus.Instrument(port, slave_addr,mode='rtu')

while True:

    debit=instrument.read_register(REG_DEBIT, 0)

    temperature=instrument.read_register(REG_TEMP, 2)


    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") # Query de connexion

    cursor = db.cursor()
    cursDebBass = db.cursor()
    
    queryInsertMes = ("""INSERT INTO mesure(temp, debit, id_bassin) VALUES (%s, %s, %s)""") # Query SQL
    data = (temperature, debit, slave_addr)


    try:
        cursor.execute(queryInsertMes, data) # Insertion de la base dans données

        db.commit() 

    except:
        db.rollback() # En cas d'erreur

    db.close() # Fermeture de la connexion avec la base de donnees
    time.sleep(58)