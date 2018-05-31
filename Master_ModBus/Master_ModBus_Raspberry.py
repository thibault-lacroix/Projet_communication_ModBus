#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import minimalmodbus
import MySQLdb
import time
from settings import *
import sys

REG_DEBIT = 0
REG_TEMP = 1
REG_VANNE_STATE = 2
REG_DEBIT_STATE = 3

val_electro=1
val_debit=20

#if sys.argv[1] :
#    print "erreur il manque le debit"
#    exit
    
#else:
#    val_electro=int(sys.argv[1])


print "Adresse de l'esclave: ", slave_addr

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_addr,mode='rtu')

while True:

    debit=instrument.read_register(REG_DEBIT, 0)
    print "1.Débit: ", debit

    temperature=instrument.read_register(REG_TEMP, 2)
    print "2.Température: ", temperature,"°C"

    #val_electro = val_electro + 1
    instrument.write_register(REG_VANNE_STATE, val_electro)
    print "3.Etat de l'electrovanne:", val_electro

    instrument.write_register(REG_DEBIT_STATE, val_debit)
    print "4.Valeur du debit: ", val_debit


    db = MySQLdb.connect("localhost","root","btsir123","ormeaux") # Query de connexion

    cursor = db.cursor()
    cursDebBass = db.cursor()
    
    queryInsertMes = ("""INSERT INTO mesure(temp, debit, id_bassin) VALUES (%s, %s, %s)""") # Query SQL
    data = (temperature, debit, slave_addr)

    debitBassin = ("""SELECT debitentre FROM controldeb WHERE id_bassin=?""")

    print "Query ok"

    try:
        cursor.execute(queryInsertMes, data) # Execution de la query

        cursDebBass.execute("""SELECT debitentre FROM controldeb WHERE id_bassin=(%s)""", (slave_addr,))

        controlDeb = cursDebBass.fetchone()
        valControlDeb = controlDeb[0]
        print "Connexion à la db"
        db.commit() 
        print "Envoi"

    except:
        db.rollback() # En cas d'erreur
        print "Erreur"

    db.close() # Fermeture de la connexion avec la base de donnees
    print "control debit: ", valControlDeb
    print "Déconnexion de la db"
    print "--------------------"
    print "                    "