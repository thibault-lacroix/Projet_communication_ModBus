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


if sys.argv[1] :
    print "erreur il manque le debit"
    exit
    
else:
    val_debit=int(sys.argv[1])

print val_debit

print "Adresse de l'esclave: ", slave_addr

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', slave_addr,mode='rtu')
while True:


    debit=instrument.read_register(REG_DEBIT, 0)
    print "1.Débit: ", debit

    temperature=instrument.read_register(REG_TEMP, 2)
    print "2.Température: ", temperature,"°C"

    val_debit = val_debit + 1
    instrument.write_register(REG_VANNE_STATE, val_debit)
    print "3.Controle de l'electrovanne: ", val_debit,"L/min"
    

    # db = MySQLdb.connect("localhost","root","btsir123","ormeaux") # Query de connexion

    # cursor = db.cursor()
    # curseur = db.cursor()
    # idcurs = db.cursor()

    # query = ("SELECT valeurs FROM settings")
    
    # sql = ("""INSERT INTO mesure(temp, debit, id_bassin) VALUES (%s, %s, %s)""") # Query SQL
    # data = (temperature, debit, slave_addr)
    # iD = ("SELECT id_mesure FROM mesure WHERE id_bassin=1 ORDER BY datetime DESC LIMIT 1")

    # print "Query ok"
    # try:
    #     cursor.execute(sql, data) # Execution de la query
    #     print "Connexion à la db"

    #     curseur.execute(query) 
    #     row = curseur.fetchone() # Resultat de la query 
    #     valeur = row[0] # Affichage de la première valeur du tableau

    #     idcurs.execute(iD)
    #     val = idcurs.fetchone()
    #     id_mes = val[0]        

    #     db.commit() 
    #     print "Envoi"

    # except:
    #     db.rollback() # En cas d'erreur
    #     print "Erreur"

    # db.close() # Fermeture de la connexion avec la base de donnees
    # print "ID", id_mes
    # print "sleep: ",valeur
    # print "Déconnexion de la db"
    # print "--------------------"
    # print "                    "
    # time.sleep(valeur-3)